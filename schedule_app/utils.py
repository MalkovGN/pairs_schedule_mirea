import os
import pyexcel
import shutil


def read_xls_as_xlsx():
    for file in os.listdir(os.getcwd() + '/schedule_app/static/schedule_app/'):
        file_name, file_extension = os.path.splitext(file)

        if file_extension[-1] == 's':
            pyexcel.save_book_as(
                file_name=f'{os.getcwd()}/schedule_app/static/schedule_app/{file_name}.xls',
                dest_file_name=f'{os.getcwd()}/schedule_app/static/excel_files/{file_name}.xlsx',
            )
            print(f'Extension of file {file_name}.{file_extension} changed successfully')
        else:
            shutil.move(
                f'{os.getcwd()}/schedule_app/static/schedule_app/{file_name}{file_extension}',
                f'{os.getcwd()}//schedule_app/static/excel_files/{file_name}{file_extension}',
            )
