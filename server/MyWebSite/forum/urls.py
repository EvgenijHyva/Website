from django.urls import path, include
from forum.views import QuestionViewSet, AnswerCreateAPIView, AnswerRUDAPIView, AnswerListAPIView, AnswerLikeAPIView
from rest_framework.routers import DefaultRouter

app_name = "forum_api"

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls), name="questions"),
    path("questions/<slug:slug>/answers/", AnswerListAPIView.as_view(), name="question_answers"),
    path("questions/<slug:slug>/answer/", AnswerCreateAPIView.as_view(), name="create_answer"),
    path("answers/<uuid:uuid>/", AnswerRUDAPIView.as_view(), name="answer_detail"),
    path("answers/<uuid:uuid>/like/", AnswerLikeAPIView.as_view(), name="answer_like"),
]
