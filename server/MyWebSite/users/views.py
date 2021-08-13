from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializer import UserDisplaySerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from users.models import CustomUser


class CurrentUserAPIView(RetrieveDestroyAPIView):
    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated, ]

    #def get(self, request):
     #   serializer = UserDisplaySerializer(request.user)
     #   return Response(serializer.data)

    def get_object(self):
        return CustomUser.objects.filter(pk=self.request.user.id, is_active=True).first()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()