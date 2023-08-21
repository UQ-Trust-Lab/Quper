import csv
import os

from bs4 import BeautifulSoup
import pandas as pd
from beautifulSoupGetText import pre_title
from find_Title import findTitleLabel

def list_files(directory):
    files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            files.append(filepath)
    return files
def all_process(path):
    try:
        soup = BeautifulSoup(open(path),features="html.parser",)
    except Exception:
        print('Formatting issues')
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"N",1, 0
    label = findTitleLabel(path)
    if label == "TitleWrong":
        print("TitleWrong")
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"N",0, 1
    title_list = soup.find_all(label)
    # print(title_list)
    type, cookie, share, security, right, children, specialArea, update, how, provide, retention, useData, order = pre_title(title_list)
    return type, cookie, share, security, right, children, specialArea, update, how, provide, retention, useData, order , 0, 0
# print(all_process("./pp_example/69_Developer Privacy Policy.html"))

if __name__ == "__main__":
    folder_path = "./pp_example/"
    files_in_folder = list_files(folder_path)
    for file in files_in_folder:
        if file == "./pp_example/.DS_Store":
            continue
        print(all_process(file))
        print(file)

