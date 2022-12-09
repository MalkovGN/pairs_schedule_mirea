import os
import requests

from bs4 import BeautifulSoup as Soup

from schedule_app.utils import read_xls_as_xlsx


def get_links():
    """
    Getting the link of the schedule to download it
    """
    url = 'https://www.mirea.ru/schedule/'
    page = requests.get(url)
    soup = Soup(page.text, "html.parser")
    schedule_link = soup.find_all("a", class_='uk-link-toggle')

    links_lst = []
    for elem in schedule_link:
        links_lst.append(elem.get('href'))
    return links_lst  # Return the list of the links of the Excel files


def get_files():
    """
    Download files for the next parsing
    Creating a list of the file names
    """
    file_names = []
    links_lst = get_links()
    for link in links_lst:
        url_to_download = link
        filename = url_to_download.split('/')[-1]  # Need to append a loop for checking all the files
        file_names.append(filename)
        file = requests.get(url_to_download, allow_redirects=True)
        open(f'{os.getcwd()}/schedule_app/static/schedule_app/{filename}', 'wb').write(file.content)

    read_xls_as_xlsx()

    directory = f'{os.getcwd()}/schedule_app/static/schedule_app/'
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return file_names  # Return the list of the filenames after parsing
