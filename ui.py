# -*- coding: utf-8 -*-
"""
Thank you Heavenly Father
"""

import sys
from PyQt6 import QtWidgets
import os
import re
import httplib2
from urllib.request import urlopen

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.crawled_files = set()
        self.queued_files = set()
        self.main_domain = ''
        self.domain = ''
        self.protocol = ''
        self.current = 0
        
        self.init_ui()
    
    def init_ui(self):
        
        # Declare Layouts
        h_box = QtWidgets.QHBoxLayout()
        h2_box = QtWidgets.QHBoxLayout()
        h3_box = QtWidgets.QHBoxLayout()
        h4_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        
        # Add Layout
        v_box.addLayout(h_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addLayout(h4_box)
        
        # Declare and add Widgets to Layouts
        self.lineEdit = QtWidgets.QLineEdit('http://')
        self.button = QtWidgets.QPushButton("Go")
        self.infobox = QtWidgets.QLabel(self)
        self.infobox1 = QtWidgets.QLabel()
        self.infobox2 = QtWidgets.QLabel()
        self.infobox3 = QtWidgets.QLabel()
        self.infobox4 = QtWidgets.QLabel(self)
        self.progress = QtWidgets.QProgressBar(self)
        
        h_box.addWidget(self.lineEdit)
        h_box.addWidget(self.button)
        h2_box.addWidget(self.infobox)
        h2_box.addSpacing(20)
        h2_box.addWidget(self.infobox1)
        h2_box.addWidget(self.infobox2)
        h2_box.addWidget(self.infobox4)
        h3_box.addWidget(self.progress)
        h4_box.addWidget(self.infobox3)
        
        # Set Layout to the app
        self.setLayout(v_box)
        
        # Set window Title
        self.setWindowTitle('Thank you Heavenly Father')
        
        # Set Geometry
        self.setGeometry(70, 70, 500, 300)
        
        # Add Actions
        self.button.clicked.connect(self.initialise)
        
        # Actually Show the Window
        self.show()
        
    def initialise(self):
        self.url_address = self.lineEdit.text()
        self.crawl(self.url_address)
        
    
    """                             ""
    " Externally Developed Functions "
    """                             ""
    
    """                                                ""
            
       FATHER, TO YOU BE ALL THE GLORY AND ADORATION
           FOR GUIDING ME AND BRINGING THIS FAR.
                   LOVE YOU ALMIGHTY FATHER
    
    """                                                ""
    
    def crawl(self, url_address):
        print(url_address)
        self.infobox.setText('Currently Crawling')
        if url_address in self.crawled_files:
            self.crawled_files.remove(url_address)
        else:
            ('Do nothing')
        print('here domain')
        
        # Set the main Domain of the website
        if self.main_domain == '':
            protocol, Domain = self.make_domain(url_address)
            self.main_domain = Domain
            self.domain = Domain
            self.protocol = protocol
        else:
            protocol, Domain = self.make_domain(url_address)
            self.domain = Domain
            self.protocol = protocol
        

        print(self.domain)
        print('self.domain up')
        if protocol == '':
            protocol = 'http://'
        else:
            ('do nothing')
        Domain = protocol + self.domain
        print(Domain)
        print('domain up')
        if re.findall('^http', url_address):
            url = url_address
        else:
            url = protocol + url_address
        ('Do nothing')
        data = self.connect(url)
        if data != False:
            self.find_href(Domain, data)
            self.find_src(Domain, data)
            if re.findall('.css', url_address):
                self.find_url(Domain, data)
        else:
            ('Do nothing')
        self.queued_files.add(url)
        for item in self.queued_files:
            self.crawled_files.discard(item)
        self.check_for_files(self.crawled_files)
        self.get_files(self.queued_files)
        self.infobox.setText('Download Completed')
        self.infobox3.setText('Thank you Jesus')
 

    def make_str(self, lists):
        print(lists)
        print('lists up')
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
        print(str_a)
        print('string up')
        return str_a
    
    def strip_sub_domain(self, url):
        print('inside strip sub domain')
        if re.findall('http://', url):
            new_url = re.sub('http://', '', url)
            protocol = 'http://'
        elif re.findall('https://', url):
            new_url = re.sub('https://', '', url)
            protocol = 'https://'
        else:
            new_url = url
            protocol = ''
        
        print('through here')
        print(new_url)
        print('new url up')
        newer_url = new_url
        #        #  Check if for the double slashes (//)
        #        if self.main_domain != '':
        #            if re.findall('/{2,4}', new_url):
        #                splits = re.split('/{2,4}', new_url)
        #                newer_url = self.main_domain + splits[-1]
        #        else:
        #            newer_url = new_url
        
        if re.findall('[?]', newer_url):
            results = newer_url.split('[?]')
            if re.findall('/', results[0]):
                new_results = results[0].split('/')
            else:
                new_results = results
            broken_url = self.make_str(new_results)
        elif re.findall('#', newer_url):
            results = newer_url.split('#')
            broken_url = self.make_str(results)
        else:
            broken_url = newer_url
            
        print(broken_url)
        print('broken url up')
        if re.findall('/.*?..*?', broken_url):
            print('here 1')
            results = re.split('/', broken_url)
            str_a = self.make_str(results)
            print(str_a)
            print('final')
            return protocol, str_a
        elif re.findall('..*?[?]', broken_url):
            print('here 2')
            results = newer_url.split('?')
            str_a = self.make_str(results)
            return protocol, str_a
        else:
            print('here t1')
            if re.findall('/$', broken_url):
                print('here 3')
                results = broken_url
                return protocol, results
            else:
                print('here 4')
                results = broken_url + '/'
                return protocol, results
    
    def make_domain(self, url):
        print('inside make domain')
        if re.findall('http://', url):
            prot, domain = self.strip_sub_domain(url)
            return prot, domain
            
        elif re.findall('https://', url):
            prot, domain = self.strip_sub_domain(url)
            return prot, domain
            
        elif re.findall('www', url):
            prot, domain = self.strip_sub_domain(url)
            return prot, domain
            
        elif re.findall('.*?.', url):
            prot, domain = self.strip_sub_domain(url)
            return prot, domain
            
        elif re.findall('.*?/', url):
            prot, domain = self.strip_sub_domain(url)
            return prot, domain
            
        else:
            prot, domain = self.strip_sub_domain(url)
            return prot, domain
    
    
    def set_file(self, filename):
        if filename not in self.queued_files:
            if not self.main_domain == '':
                # check if there is a double slash (//) here
                if re.findall('/{2,4}', filename):            
                    splited = re.split('/{2,4}', filename)
                    ok_resource = self.main_domain + splited[-1]
                else:
                    ok_resource = filename
                print(ok_resource)
                print('ok resource up')
            else:
                ok_resource = filename
            
            self.crawled_files.add(ok_resource)
        else:
            ('do nothing')
    
    
    def connect(self, url):
        
        try:
            http = httplib2.Http()
            request, response = http.request(url)
            data = response.decode('utf-8')
            return data
        except:
            return False
    
    
    def find_href(self, Domain, data):
        if re.findall('href', data):
            link1 = re.findall('href=\'.*?.*?.*?\'', data)
            link2 = re.findall('href=".*?.*?.*?"', data)
            
            for attr1 in link1:
                striped_quotes = re.sub('[\']','', attr1)
                striped_href1 = re.sub('href=', '', striped_quotes)
                self.check_if_ext(Domain, striped_href1)
            for attr2 in link2:
                striped_double_quotes = re.sub('["]', '', attr2)
                striped_href2 = re.sub('href=', '', striped_double_quotes)
                self.check_if_ext(Domain, striped_href2)
        else:
            ('Do nothing')
    
    def find_src(self, Domain, data):
        if re.findall('src', data):
            result1 = re.findall('src=\'.*?.*?.*?\'', data)
            result2 = re.findall('src=".*?.*?.*?"', data)
            
            for attr in result1:
                striped_quotes = re.sub('[\']', '', attr)
                striped_name1 = re.sub('src=', '', striped_quotes)
                self.check_if_ext(Domain, striped_name1)
            for attr2 in result2:
                striped_dobble_quotes = re.sub('["]', '', attr2)
                striped_name2 = re.sub('src=', '', striped_dobble_quotes)
                self.check_if_ext(Domain, striped_name2)
    
    def find_url(self, Domain, data):
        if re.findall('url', data):
            urls = re.findall('url[(?]\'.*?.*?.*?\'[)?]', data)
            urls2 = re.findall('url[(?]".*?.*?.*?"[)?]', data)
            for links in urls:
                strip_quotes = re.sub('[\']', '', links)
                strip_open_braces = re.sub('[(]', '', strip_quotes)
                strip_close_braces = re.sub('[)]', '', strip_open_braces)
                strip_attr = re.sub('url', '', strip_close_braces)
                self.check_if_ext(Domain, strip_attr)
            for links1 in urls2:
                strip_dbl_quotes = re.sub('"', '', links1)
                strip_open_braces1 = re.sub('[(]', '', strip_dbl_quotes)
                strip_close_braces2 = re.sub('[)]', '', strip_open_braces1)
                strip_attr1 = re.sub('url', '', strip_close_braces2)
                self.check_if_ext(Domain, strip_attr1)
        elif re.findall('URL', data):
            urls = re.findall('URL[(?]\'.*?.*?.*?\'[)?]', data)
            urls2 = re.findall('URL[(?]".*?.*?.*?"[)?]', data)
            for links in urls:
                strip_quotes = re.sub('[\']', '', links)
                strip_open_braces = re.sub('[(]', '', strip_quotes)
                strip_close_braces = re.sub('[)]', '', strip_open_braces)
                strip_attr = re.sub('URL', '', strip_close_braces)
                self.check_if_ext(Domain, strip_attr)
            for links1 in urls2:
                strip_dbl_quotes = re.sub('["]', '', links1)
                strip_open_braces1 = re.sub('[(]', '', strip_dbl_quotes)
                strip_close_braces2 = re.sub('[)]', '', strip_open_braces1)
                strip_attr1 = re.sub('URL', '', strip_close_braces2)
                self.check_if_ext(Domain, strip_attr1)
    
    def check_for_files(self, files_set):
        for items in self.queued_files:
            self.crawled_files.discard(items)
        for lists in self.crawled_files:
            if not lists in self.queued_files:
                self.crawl(lists)
            else:
                continue
    
    def check_if_ext(self, Domain, lnk):
        if re.findall('^http', lnk):
            self.queued_files.add(lnk)
        elif re.findall('^www', lnk):
            self.queued_files.add(lnk)
        else:
            final = Domain + lnk
            self.set_file(final)
    
    
    def get_file(self, file):
        print('here')
        h = httplib2.Http('.cache')
        
        # Get thte Data
        response_code, data = h.request(file)
        
        # If the file coming has a slash at the end of the file
        if not re.findall('/$', file):
            file_ok = file
        else:
            file_ok = file + '#'
        
        if data != '':
            print('data')
            self.infobox.setText('Downloading')
            self.current += 1;
            percent = (self.current / len(self.queued_files) ) * 100
            self.progress.setValue(percent)
            self.infobox1.setText(str(self.current))
            self.infobox4.setText(str(len(self.queued_files)))
            if re.findall('http://', file_ok):
                rebuilt_file = re.sub('http://', '', file_ok)
            elif re.findall('https://', file_ok):
                rebuilt_file = re.sub('https://', '', file_ok)
            else:
                rebuilt_file = file_ok
            resource = rebuilt_file
            
            #print('resource: ' + resource)
            try:
                with open(resource, 'wb') as new_file:
                    new_file.write(data)
                ('Do nothing')
                print('Done down')
            except:
                ('do nothing')
                return 0
        else:
            print('non da')
            ('do nothing')
        
    def get_files(self, file_set):
        self.infobox2.setText( '/' )
        for cloud_file in self.queued_files:
            if re.findall('http://', cloud_file):
                prtcl = 'http://'
                file = re.sub('http://', '', cloud_file)
            elif re.findall('https://', cloud_file):
                prtcl = 'https://'
                file = re.sub('https://', '', cloud_file)
            else:
                prtcl = ''
                file = cloud_file
            self.mkfolder(file)
            err_less_file = self.make_err_less_file(prtcl, file)
            ('Do nothing')
            print(err_less_file)
            self.get_file(err_less_file)
    
    def mkfolder(self, path):
        lists = re.split('/', path)
        lists.pop()
        list_str = ''
        for x in range(0, len(lists)):
            list_str += lists[x] + '/'
        if not os.path.exists(list_str):
            os.makedirs(list_str)
     
    def make_err_less_file(self, prtcl, path):
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
                else:
                    if re.findall('[?]', lists[x]):
                        splits = re.split('[?]', lists[x])
                        list_make += splits[0]
                    else:
                        list_make += lists[x]
        return prtcl + list_make
    
    def status(self, string):
        print(string)
    

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec())