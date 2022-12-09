# from openpyxl import load_workbook
#
# from .downloader import get_files
#
# # def get_links():
# #     """
# #     Getting the link of the schedule to download it
# #     """
# #     url = 'https://www.mirea.ru/schedule/'
# #     page = requests.get(url)
# #     soup = Soup(page.text, "html.parser")
# #     schedule_link = soup.find_all("a", class_='uk-link-toggle')
# #
# #     links_lst = []
# #     for elem in schedule_link:
# #         links_lst.append(elem.get('href'))
# #
# #     return links_lst  # Return the list of the links of the Excel files
# #
# #
# # def get_files():
# #     """
# #     Download files for the next parsing
# #     Creating a list of the file names
# #     """
# #     file_names = []
# #     links_lst = get_links()
# #     url_to_download = links_lst[0]  # For test take the first link from the lst
# #     filename = url_to_download.split('/')[-1]  # Need to append a loop for checking all the files
# #     file_names.append(filename)
# #
# #     file = requests.get(url_to_download, allow_redirects=True)
# #     open(f'{os.getcwd()}/schedule_app/static/schedule_app/{filename}', 'wb').write(file.content)
# #
# #     return file_names  # Return the list of the filenames after parsing
#
#
# def read_file_info():
#     file_names = get_files()
#     wb = load_workbook(f'schedule_app/static/schedule_app/{file_names[0]}')
#     sheets_name_list = wb.sheetnames
#     # group_names = []
#     group_schedule = {}
#
#     for sheet_name in sheets_name_list:
#         sheet = wb[f'{sheet_name}']
#
#         columns_counter = 6
#         while columns_counter <= sheet.max_column:
#             subjects_lst = []
#             for row in range(2, 75):
#                 if sheet.cell(row=row, column=columns_counter).value in list(group_schedule.keys()):
#                     subject_name = sheet.cell(row=row, column=columns_counter).value
#                     subjects_lst.append(subject_name)
#             group_schedule[sheet.cell(row=row, column=columns_counter).value] = subjects_lst
#             columns_counter += 5
#         return group_schedule
