from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Poll, UserPoll
from .serializers import PollSerializer, UserSerializer, PollDetailSerializer
from .services import User


class PollView(viewsets.ReadOnlyModelViewSet):

    """Get all in progress polls"""

    queryset = Poll.objects.filter(status='IN_PROGRESS')
    serializer_class = PollSerializer


@api_view(['GET', 'POST'])
def poll_detail(request, slug):

    """Get Poll Detail

    1. Getting User session data
    2. Getting Poll object by slug
    3. Checking if User has the same completed poll
    4. If not, He can to pass this poll
    5. POST-method takes questions object from request with answer fields on each question.

    """

    user = User(request)
    poll = get_object_or_404(Poll, slug=slug)

    if request.method == 'GET':
        user_poll = UserPoll.objects.filter(user=user.user, poll=poll).first()
        if user_poll:
            if poll.id == user_poll.poll.id:
                return Response('You`ve done this poll')

        serializer = PollDetailSerializer(poll)
        return Response(serializer.data)

    if request.method == 'POST':
        # Save JSON answers field from front-end
        try:
            questions = [i for i in request.data['questions']]
        except KeyError:
            return Response('No Questions Data')
        user.add_poll(poll, questions)
        return Response('Thanks! You`ve done this poll')


@api_view(['GET'])
def get_result(request):

    """Get completed poll results"""

    user = User(request)
    queryset = user.get_passed_poll()
    if queryset:
        serializer = UserSerializer(user.user)
        return Response(serializer.data)
    return Response('You have not any completed polls')




