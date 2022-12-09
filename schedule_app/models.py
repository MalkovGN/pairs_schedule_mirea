from django.db import models


# class PairModel(models.Model):
#     subject_name = models.TextField(null=True)
#     pair_time_start = models.CharField(max_length=8, null=True)
#     pair_time_end = models.CharField(max_length=8, null=True)
#     pair_number = models.SmallIntegerField(null=True)
#     pair_type = models.CharField(max_length=32, null=True)
#     teacher_name = models.CharField(max_length=32, null=True)
#     cabinet_number = models.CharField(max_length=16, null=True)
#     campus = models.CharField(max_length=16, null=True)
#     week_parity = models.CharField(max_length=8, null=True)
#
#
# class DayModel(models.Model):
#     week_day = models.CharField(max_length=16, null=True)
#     pair = models.ManyToManyField(PairModel)
#
#
# class GroupModel(models.Model):
#     group_name = models.CharField(max_length=16)
#     # week_day = models.CharField(max_length=16, null=True)
#     day = models.ForeignKey(DayModel, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.group_name


class GroupModel(models.Model):
    group_name = models.CharField(max_length=16)
    day_info = models.JSONField()

    def __str__(self):
        return self.group_name





