#!/usr/local/bin/python3 python
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import urllib.parse
import webbrowser

FIRST_NAME = os.getenv('FIRST_NAME')
LAST_NAME = os.getenv('LAST_NAME')
CHROME = os.getenv('CHROME')
PROFILE = os.getenv('PROFILE')
TO_ADDR = os.getenv('TO_ADDR')
CC_ADDR = os.getenv('CC_ADDR')
WORK_TIME = os.getenv('WORK_TIME')
fileName = "mail.txt"


def main():
    with open(f"{fileName}", mode="r", encoding="UTF-8") as f:
        url = getUrl(f.read())
        openUrl(url)

def getUrl(template_body: str):
    url = "https://mail.google.com/mail/?view=cm"
    url += f"&to={TO_ADDR}"
    url += f"&cc={CC_ADDR}"
    today = datetime.now()
    mail_date = str(today.month)+"月"+str(today.day)+"日"
    subject_date = '{0:02d}{1:02d}'.format(today.month, today.day)
    url += f"&su=【日報】{subject_date}_{LAST_NAME}{FIRST_NAME}"
    body_data = [
        LAST_NAME,
        mail_date,
        WORK_TIME
    ]
    body = template_body.format(*body_data)
    url += f"&body={strenc(body)}"

    return url

def strenc(txt: str):
    lst = list("#'|^<>{};?@&$" + '"')
    for v in lst:
        txt = txt.replace(v, urllib.parse.quote(v))
    txt = urllib.parse.quote(txt)
    return txt

def openUrl(url: str):
    print(url)
    webbrowser.get(CHROME+' --profile-directory='+PROFILE+ ' %s')
    webbrowser.open(url)


if __name__ == "__main__":
    main()
