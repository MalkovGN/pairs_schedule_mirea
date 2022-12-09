from django.db import models


class GroupModel(models.Model):
    group_name = models.CharField(max_length=16)
    day_info = models.JSONField()

    def __str__(self):
        return self.group_name





