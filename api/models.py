from django.db import models


class Poll(models.Model):

    """Polls Model"""

    POLL_STATUS = [
        ('WAITING', 'Waiting to start'),
        ('IN_PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField("URL", max_length=255, unique=True)
    description = models.TextField()
    starting = models.DateTimeField("Starting date",
                                    null=True,
                                    default=None)
    finished = models.DateTimeField("End date",
                                    null=True,
                                    default=None)
    status = models.CharField("Poll Status",
                              max_length=15,
                              choices=POLL_STATUS,
                              default='WAITING')

    def __str__(self):
        return self.name


class Question(models.Model):

    """Questions Model"""

    QUESTION_TYPES = [
        ('1', 'Text'),
        ('2', 'Choose one'),
        ('3', 'Choose many'),
    ]
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField("Question text", max_length=255)
    question_type = models.CharField(max_length=15,
                                     choices=QUESTION_TYPES,
                                     default='1')

    def __str__(self):
        return self.text


class Choice(models.Model):

    """Choices Model"""

    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='choices')
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text


class User(models.Model):

    """Users Model"""

    def __str__(self):
        return str(self.id)


class UserPoll(models.Model):

    """Finished Polls by User"""

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_polls')
    poll = models.ForeignKey(Poll,
                             on_delete=models.CASCADE,
                             null=True)
    questions = models.TextField(null=True)

    def __str__(self):
        return str(self.id)
