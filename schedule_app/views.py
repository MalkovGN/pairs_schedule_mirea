from django.shortcuts import render

from . import get_schedule_info


def look_results(request):
    names = get_schedule_info.get_files()
    group_names = get_schedule_info.read_file_info()
    return render(
        request,
        'schedule_app/test.html',
        # {'names': names},
        {'group_names': group_names},
    )
