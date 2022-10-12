# -*- coding: utf-8 -*-
import httplib2
from urllib.request import urlopen
import re
import os

def get_file(file):
    h = httplib2.Http('.cache')
    response_code, data = h.request(file)
    if data != '':
        
        if re.findall('http://', file):
            rebuilt_file = re.sub('http://', '', file)
        elif re.findall('https://', file):
            rebuilt_file = re.sub('https://', '', file)
        else:
            rebuilt_file = file
        resource = rebuilt_file
        print('resource: ' + resource)
        with open(resource, 'wb') as new_file:
            new_file.write(data)
        status('done with getting')
    else:
        print('4False')
    
def get_files(file_set):
    
    for cloud_file in file_set:
        if re.findall('http://', cloud_file):
            file = re.sub('http://', '', cloud_file)
        elif re.findall('https://', cloud_file):
            file = re.sub('https://', '', cloud_file)
        else:
            file = cloud_file
        mkfolder(file)
        make_err_less_file(file)
        get_file(cloud_file)

def mkfolder(path):
    lists = re.split('/', path)
    lists.pop()
    list_str = ''
    for x in range(0, len(lists)):
        list_str += lists[x] + '/'
    if not os.path.exists(list_str):
        print(lists)
        os.makedirs(list_str)
 
def make_err_less_file(path):
    lists = re.split('/', path)
    list_make = ''
    for x in range(0, len(lists)):
        #check if index is not the last one
        if x != len(lists):
            if x + 1 != len(lists):
                if lists[x+1] == '..':
                    continue
                elif lists[x] == '..':
                    continue
                else:
                    list_make += lists[x] + '/'
    return list_make

def status(string):
    print(string)
