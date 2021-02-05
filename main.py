import os
import datetime
import pathlib
import shutil

PATH = "C:\\Users\\Ryuu\\downloads\\Test\\"
OUT_DIR = "E:\\Test\\"


def create_dir(dir_name):
    new_dir = os.path.isdir(dir_name)
    if not new_dir:
        os.mkdir(dir_name)


for file in os.listdir(PATH):
    if file.endswith(".pdf"):

        PDF_DIR = OUT_DIR + 'PDF'

        create_dir(PDF_DIR)

        full_filepath = pathlib.Path(PATH + file)
        file_time = full_filepath.stat().st_mtime
        file_date = str(datetime.datetime.fromtimestamp(file_time).date())

        date_dir = f'{PDF_DIR}\\{file_date}\\'

        create_dir(date_dir)

        shutil.move(PATH + file, date_dir + file)

    elif file.endswith(".pptx"):

        PPT_DIR = OUT_DIR + 'PPT'

        create_dir(PPT_DIR)

        full_filepath = pathlib.Path(PATH + file)
        file_time = full_filepath.stat().st_mtime
        file_date = str(datetime.datetime.fromtimestamp(file_time).date())

        date_dir = f'{PPT_DIR}\\{file_date}\\'

        create_dir(date_dir)

        shutil.move(PATH + file, date_dir + file)


