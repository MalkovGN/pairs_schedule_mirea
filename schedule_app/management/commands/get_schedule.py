import os

from django.core.management.base import BaseCommand

from schedule_app.parser import get_schedule
from schedule_app.models import GroupModel
from schedule_app.downloader import get_files


def save_schedule_to_db():
    """
    Пока делаю только для одного файла
    потом сделать для всех файлов
    """
    get_files()

    directory = f'{os.getcwd()}/schedule_app/static/excel_files'
    for file in os.listdir(directory):
        file_schedule = get_schedule(directory + '/' + file)

        for list_schedule in file_schedule.values():
            for group_name in list_schedule.keys():
                group_schedule = list_schedule[group_name]
                group_info = GroupModel(
                    group_name=group_name,
                    day_info=group_schedule,
                )
                group_info.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        save_schedule_to_db()
