from rest_framework import serializers
from .models import Poll, Question, Choice, User, UserPoll


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'choice_text',
        )


class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            'text',
            'question_type',
            'choices',
        )


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = (
            'id',
            'name',
            'slug',
            'description',
        )


class PollDetailSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'questions',
        )


class UserPollSerializer(serializers.ModelSerializer):

    poll = PollSerializer(read_only=True)
    questions = serializers.SerializerMethodField()

    class Meta:
        model = UserPoll
        fields = (
            'poll',
            'questions',
        )

    def get_questions(self, obj):
        # Gets questions data in JSON view
        import json
        obj.questions = obj.questions.replace("\'", "\"")
        return json.loads(obj.questions)


class UserSerializer(serializers.ModelSerializer):

    user_polls = UserPollSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'user_polls',
        )
