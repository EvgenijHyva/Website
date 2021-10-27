from rest_framework import serializers
from forum.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["updated_at", "id"]

    author_is_admin = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()


    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_answers_count(self, instance):
        return instance.answers.filter(is_active=True).count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()

    def get_author_is_admin(self, instance):
        return instance.author.is_staff



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ["updated_at", "question", "voters", "id"]

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_liked_answer = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()
    is_active = serializers.ReadOnlyField()

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_liked_answer(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug

