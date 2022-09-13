from django.db import models


class GroupModel(models.Model):
    group_name = models.CharField(max_length=16)

    def __str__(self):
        return self.group_name
