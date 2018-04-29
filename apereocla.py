# -*- coding: utf-8 -*-
'''
python-apereocla
================

This is a simple python library to parse and access the Apereo Foundation's
lists include those who have submitted Apereo Foundation CLAs, as well as those
who had previously submitted CLAs with Jasig or Sakai.

The data is retrieved from the official lists at:

> http://licensing.apereo.org/

This library offers access to the lists of ICLAs, CCLAs as well as the list of
Github user names associated with ICLAs.

:license: MIT
'''

from bs4 import BeautifulSoup
import requests


BASEURL = 'https://docs.google.com' \
          '/spreadsheets/d/1RoXOkTLsa2lAMOj0PoH4zDB7Rjz-gIJqH1aFYwZBcMU' \
          '/pubhtml/sheet?headers=false&gid='
GHURL = BASEURL + '2009020919'
CLAURL = BASEURL + '5'


def github_users():
    req = requests.get(GHURL)
    assert req.ok
    soup = BeautifulSoup(req.text, 'html.parser')
    for gh_username in soup.find_all('td', **{'class': 's1'}):
        if gh_username.string:
            yield gh_username.string


def _cla(field):
    req = requests.get(CLAURL)
    assert req.ok
    soup = BeautifulSoup(req.text, 'html.parser')
    for tr in soup.find_all('tr'):
        td = tr.find_all('td', **{'class': 's3'})
        if len(td) != 2:
            continue
        cla = td[field].string
        if cla:
            yield cla


def icla():
    return _cla(0)


def ccla():
    return _cla(1)
