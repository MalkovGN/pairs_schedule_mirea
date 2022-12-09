from rest_framework import generics

from .serializers import GroupSerializer
from .models import GroupModel


class GroupsScheduleView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return GroupModel.objects.all()


class GroupScheduleView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        group_name = self.kwargs['group_name']
        return GroupModel.objects.filter(group_name=group_name)
