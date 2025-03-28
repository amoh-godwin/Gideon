# -*- coding: utf-8 -*-
"""
Functions for the tiny Download
"""
import os
import re
import httplib2
from urllib.request import urlopen

crawled_files = set()
queued_files = set()
Domain = ''

#def get_file(file):

def crawl(url_address):
    if url_address in crawled_files:
        crawled_files.remove(url_address)
    protocol, Domain = make_domain(url_address)
    if protocol == '':
        protocol = 'http://'
    Domain = protocol + Domain
    if re.findall('^http', url_address):
        url = url_address
    else:
        url = protocol + url_address
    print(url)
    data = connect(url)
    if data != False:
        find_href(Domain, data)
        find_src(Domain, data)
        if re.findall('.css', url_address):
            find_url(Domain, data)
    
    queued_files.add(url)
    check_for_files(crawled_files)
    status('Ready to set, Thank you Heavenly Father')
    get_files(queued_files)
    return 'Love'
 

def make_str(lists):
    if re.findall('[.|=]', lists[-1]) or lists[-1] == '':
        lists.pop()

    str_a = str()
    for x in range(0, len(lists)):
        if x == 0:
            if re.findall('/$', lists[x]):
                str_a += lists[0]
            else:
                str_a += lists[0] + '/'
        else:
            if re.findall('[.|=]', lists[x]):
                return str_a
            str_a += lists[x] + '/'
    return str_a

def strip_sub_domain(url):
    if re.findall('http://', url):
        new_url = re.sub('http://', '', url)
        protocol = 'http://'
    elif re.findall('https://', url):
        new_url = re.sub('https://', '', url)
        protocol = 'http://'
    else:
        new_url = url
        protocol = ''
        
    if re.findall('[?]', new_url):
        results = new_url.split('[?]')
        broken_url = make_str(results)
    elif re.findall('#', new_url):
        results = new_url.split('#')
        broken_url = make_str(results)
    else:
        broken_url = new_url
        
    if re.findall('/.*?..*?', broken_url):
        results = re.split('/', broken_url)
        str_a = make_str(results)
        return protocol, str_a
    elif re.findall('..*?[?]', broken_url):
        results = new_url.split('?')
        str_a = make_str(results)
        return protocol, str_a
    else:
        if re.findall('/$', broken_url):
            results = broken_url
            return protocol, results
        else:
            results = broken_url + '/'
            return protocol, results

def make_domain(url):
    if re.findall('http://', url):
        prot, domain = strip_sub_domain(url)
        return prot, domain
        
    elif re.findall('https://', url):
        prot, domain = strip_sub_domain(url)
        return prot, domain
        
    elif re.findall('www', url):
        prot, domain = strip_sub_domain(url)
        return prot, domain
        
    elif re.findall('.*?.', url):
        prot, domain = strip_sub_domain(url)
        return prot, domain
        
    elif re.findall('.*?/', url):
        domain = strip_sub_domain(url)
        return prot, domain
        
    else:
        prot, domain = strip_sub_domain(url)
        return prot, domain


def set_file(filename):
    crawled_files.add(filename)


def connect(url):
    try:
        request = urlopen(url)
        response = request.read()
        data = response.decode('utf-8')
        return data
    except:
        return False


def find_href(Domain, data):
    if re.findall('href', data):
        link1 = re.findall('href=\'.*?.*?.*?\'', data)
        link2 = re.findall('href=".*?.*?.*?"', data)
        
        for attr1 in link1:
            striped_quotes = re.sub('[\']','', attr1)
            striped_href1 = re.sub('href=', '', striped_quotes)
            check_if_ext(Domain, striped_href1)
        for attr2 in link2:
            striped_double_quotes = re.sub('["]', '', attr2)
            striped_href2 = re.sub('href=', '', striped_double_quotes)
            check_if_ext(Domain, striped_href2)

def find_src(Domain, data):
    if re.findall('src', data):
        result1 = re.findall('src=\'.*?.*?.*?\'', data)
        result2 = re.findall('src=".*?.*?.*?"', data)
        
        for attr in result1:
            striped_quotes = re.sub('[\']', '', attr)
            striped_name1 = re.sub('src=', '', striped_quotes)
            check_if_ext(Domain, striped_name1)
        for attr2 in result2:
            striped_dobble_quotes = re.sub('["]', '', attr2)
            striped_name2 = re.sub('src=', '', striped_dobble_quotes)
            check_if_ext(Domain, striped_name2)

def find_url(Domain, data):
    if re.findall('url', data):
        urls = re.findall('url[(?]\'.*?.*?.*?\'[)?]', data)
        urls2 = re.findall('url[(?]".*?.*?.*?"[)?]', data)
        for links in urls:
            strip_quotes = re.sub('[\']', '', links)
            strip_open_braces = re.sub('[(?]', '', strip_quotes)
            strip_close_braces = re.sub('[)?]', '', strip_open_braces)
            strip_attr = re.sub('url', '', strip_close_braces)
            check_if_ext(Domain, strip_attr)
        for links1 in urls2:
            strip_dbl_quotes = re.sub('"', '', links1)
            strip_open_braces1 = re.sub('[(?]', '', strip_dbl_quotes)
            strip_close_braces2 = re.sub('[)?]', '', strip_open_braces1)
            strip_attr1 = re.sub('url', '', strip_close_braces2)
            check_if_ext(Domain, strip_attr1)
    elif re.findall('URL', data):
        urls = re.findall('URL[(?]\'.*?.*?.*?\'[)?]', data)
        urls2 = re.findall('URL[(?]".*?.*?.*?"[)?]', data)
        for links in urls:
            strip_quotes = re.sub('[\']', '', links)
            strip_open_braces = re.sub('[(?]', '', strip_quotes)
            strip_close_braces = re.sub('[)?]', '', strip_open_braces)
            strip_attr = re.sub('URL', '', strip_close_braces)
            check_if_ext(Domain, strip_attr)
        for links1 in urls2:
            strip_dbl_quotes = re.sub('["]', '', links1)
            strip_open_braces1 = re.sub('[(?]', '', strip_dbl_quotes)
            strip_close_braces2 = re.sub('[)?]', '', strip_open_braces1)
            strip_attr1 = re.sub('URL', '', strip_close_braces2)
            check_if_ext(Domain, strip_attr1)

def check_for_files(files_set):
    for items in files_set:
        if items in queued_files:
            crawled_files.remove(items)
            return
        else:
            crawl(items)

def check_if_ext(Domain, lnk):
    if re.findall('^http', lnk):
        queued_files.add(lnk)
    elif re.findall('^www', lnk):
        queued_files.add(lnk)
    else:
        final = Domain + lnk
        set_file(final)


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
