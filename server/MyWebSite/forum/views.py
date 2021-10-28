from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from MyWebSite.site_permisions import ForumIsAuthorOrReadOnly
from forum.api.serializers import QuestionSerializer, AnswerSerializer
from forum.models import Question, Answer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(is_active=True)
    serializer_class = QuestionSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated, ForumIsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.filter(is_active=True)
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        _request_user = self.request.user
        _slug = self.kwargs.get("slug")
        _question = get_object_or_404(Question, slug=_slug)
        # if _question.answers.filter(author=_request_user, is_active=True).exists():
        if _question.answers.filter(is_active=True).order_by("-created_at").first().author == _request_user:
            raise ValidationError({
                "error": "You have already answered to this question, wait until other user answer's this"
            })
        serializer.save(author=_request_user, question=_question)


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ForumIsAuthorOrReadOnly]
    lookup_field = "uuid"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Answer.objects.all().order_by("-created_at")
        else:
            return Answer.objects.filter(is_active=True).order_by("-created_at")


    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        _slug = self.kwargs.get("slug")
        if self.request.user.is_staff:
            return Answer.objects.filter(question__slug=_slug).order_by("-created_at")
        else:
            return Answer.objects.filter(question__slug=_slug, is_active=True).order_by("-created_at")

class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, uuid):
        answer = get_object_or_404(Answer, uuid=uuid)
        answer.voters.add(request.user)
        answer.save()
        _serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=_serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, uuid):
        answer = get_object_or_404(Answer, uuid=uuid)
        answer.voters.remove(request.user)
        answer.save()
        _serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=_serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
