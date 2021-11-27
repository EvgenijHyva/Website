from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.api.serializer import UserDisplaySerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from users.models import CustomUser
from MyWebSite.site_permisions import IsUserOrReadOnly

class CurrentUserAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDisplaySerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly, ]

    def get_object(self):
        user = get_object_or_404(CustomUser, pk=self.request.user.id)
        return user

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
