from django.shortcuts import render

from . import get_schedule_info
from .models import GroupModel


def look_results(request):
    # names = get_schedule_info.get_files()
    # # group_names = get_schedule_info.read_file_info()
    # group_names = GroupModel.objects.all()
    # for group_name in group_names:
    #     group = GroupModel(
    #         group_name=group_name,
    #     )
    #     group.save()
    groups_schedule = get_schedule_info.read_file_info()
    return render(
        request,
        'schedule_app/test.html',
        # {'names': names},
        {'group_names': groups_schedule},
    )
