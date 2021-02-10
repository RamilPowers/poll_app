from django.contrib import admin, messages
from .models import Poll, Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionInline(admin.StackedInline):
    model = Question
    readonly_fields = ['question_type']
    extra = 0


class PollAdmin(admin.ModelAdmin):

    inlines = [QuestionInline]
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'status', 'description']}),
        ('DATE INFO', {'fields': [('starting', 'finished')]})
    ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = [
        'starting',
        'finished',
    ]

    def save_model(self, request, obj, form, change):
        """Save Model override for access control of the poll"""
        import datetime

        def get_message(msg, type):
            messages.add_message(
                request,
                type,
                f'{msg}!'
            )

        if not obj.starting and obj.status == 'IN_PROGRESS':
            obj.starting = datetime.datetime.now()
            get_message('Poll has started!', messages.SUCCESS)
            obj.save()

        if obj.starting and not obj.finished and obj.status == 'FINISHED':
            obj.finished = datetime.datetime.now()
            get_message('Poll has finished!', messages.SUCCESS)
            obj.save()

        if not (obj.starting or obj.finished) and obj.status != 'WAITING':
            obj.status = 'WAITING'
            get_message('Woo Wee Woo Waa! Error!', messages.ERROR)
            obj.save()

        if not obj.id:
            obj.save()


class QuestionAdmin(admin.ModelAdmin):

    inlines = [ChoiceInline]

    # def save_model(self, request, obj, form, change):
    # When Admin choose type of the question is text, answer choices are removing
    #    choices = Choice.objects.filter(question=obj)
    #    if obj.question_type == '1' and choices:
    #       choices.delete()
    #   obj.save()


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

