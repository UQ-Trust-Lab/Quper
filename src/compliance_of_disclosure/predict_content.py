import csv
import re

import bs4
import joblib

# from bayesian import clf,tf
from bs4 import BeautifulSoup

mark_txt = {'0':"personal_information_type.txt",'1':"personal_information_type.txt",'2':"personal_information_type.txt",
            '3':"share_information.txt",'4':"protect_information.txt",
            '5':"advertising.txt",'6':"user_right.txt",'7':"special_group.txt",
            '8':"special_area.txt",'9':"update.txt",'10':"way_to_collect.txt",
            '11':"provider.txt",'12':"data_retention.txt",'13':"personal_information_type.txt",'14':"thrid_party.txt",'15':"personal_infoinformation_tyoe.txt"}
clf = joblib.load('bys_classifier.pkl')
tf = joblib.load('bys_tf.pkl')
def pre_title(title_list):
    type = 0
    cookie = 0
    share = 0
    security = 0
    right = 0
    children = 0
    specialArea = 0
    update = 0
    how = 0
    provide = 0
    retention = 0
    useData = 0
    clean_title_list = []
    for title in title_list:
        if title.text != "•":
            clean_title_list.append(title)
    order = []
    for title in clean_title_list:
        title_Str = re.sub(r'\s+', ' ', str(title))
        title_Str = re.sub(r'<[^<]+?>', '', title_Str).replace('\n', '').strip()
        title_Str = title_Str.lower()
        if title is None:
            continue
        try:
            mark = clf.predict(tf.transform([title_Str]))
            # print("---------")
            # print(title_Str)
            # print(mark)
            # print("---------")
            if mark[0] == "1":
                if "USE" in title_Str or "use" in title_Str:
                    how = 1
                type = 1
            elif mark[0] == "2":
                cookie = 1
            elif mark[0] == "3":
                share = 1
            elif mark[0] == "4":
                security = 1
            elif mark[0] == "6":
                right = 1
            elif mark[0] == "7":
                children = 1
            elif mark[0] == "8":
                specialArea = 1
            elif mark[0] == "9":
                update = 1
            elif mark[0] == "10":
                how = 1
                type = 1
            elif mark[0] == "11":
                provide = 1
            elif mark[0] == "12":
                retention = 1
            elif mark[0] == "13":
                useData = 1
            elif mark[0] == "15":
                how = 1
                type = 1
        except Exception as e:
            continue
        if mark[0] not in order:
            order.append(mark[0])

    return type , cookie , share , security , right , children , specialArea , update , how ,  provide , retention , useData, order


