import os
import win32com.client as win32


def xls_as_xlsx():
    excel = win32.Dispatch('excel.application')
    for file in os.listdir(os.getcwd() + '/schedule/schedule_app/static/schedule_app/'):
        filename, fileextantion = os.path.splitext(file)
        # print(filename, fileextantion, '14y37fueidfbbfn')
        wb = excel.Workbooks.Open(os.getcwd() + '/schedule/schedule_app/static/schedule_app/' + file)
        output_path = os.getcwd() + '/excel_files/' + filename
        if fileextantion[-1] == 's':
            wb.SaveAs(output_path + fileextantion + 'x', FileFormat=51)
            wb.Close()
        else:
            wb.SaveAs(output_path + fileextantion, FileFormat=51)
            wb.Close()
    excel.Quit()