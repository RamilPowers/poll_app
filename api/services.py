from . import models
from .models import Poll, UserPoll

USER_ID = 'user-id'


class User:

    def __init__(self, request):
        self.session = request.session
        user_id = self.session.get(USER_ID)
        if user_id:
            user = models.User.objects.filter(id=user_id).first()
            if user is None:
                user = self._create_new_session()
        else:
            user = self._create_new_session()
        self.user = user

    def _create_new_session(self):
        user = models.User.objects.create()
        self.session[USER_ID] = user.id
        return user

    def _save_session(self):
        self.session.modified = True
        self.user.save()

    def add_poll(self, poll_obj, questions):
        """Add poll as finished"""
        poll = UserPoll.objects.filter(user=self.user, poll=poll_obj).first()
        if poll:
            return
        else:
            poll = UserPoll.objects.create(user=self.user,
                                           poll=poll_obj,
                                           questions=questions)
        self._save_session()
        return poll

    def get_passed_poll(self):
        """Get finished poll"""
        queryset = UserPoll.objects.filter(user=self.user)
        return queryset

