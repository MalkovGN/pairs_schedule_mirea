import os
import pyexcel
import shutil
import win32com.client as win32


def xls_as_xlsx():
    excel = win32.Dispatch('excel.application')
    for file in os.listdir(os.getcwd() + '/schedule_app/static/schedule_app/'):
        filename, fileextantion = os.path.splitext(file)
        wb = excel.Workbooks.Open(os.getcwd() + '/schedule_app/static/schedule_app/' + file)
        output_path = os.getcwd() + '/excel_files/' + filename
        if fileextantion[-1] == 's':
            wb.SaveAs(output_path + fileextantion + 'x', FileFormat=51)
            wb.Close()
        else:
            wb.SaveAs(output_path + fileextantion, FileFormat=51)
            wb.Close()
    excel.Quit()


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
