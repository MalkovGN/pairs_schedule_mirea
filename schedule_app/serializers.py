from rest_framework import serializers

from .models import GroupModel


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ['group_name', 'day_info']

# class OneGroupSerializer(serializers.ModelSerializer):
