#!/usr/bin/python3
import json
from urllib import parse
import requests
from bs4 import BeautifulSoup

import sys # For INPUT args

class Google:
    def __init__(self):
        self.GOOGLE_SEARCH_URL = 'https://www.google.co.jp/search'
        self.session = requests.session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})

    def Search(self, keyword, type='text', maximum=100):
        '''Google検索'''
        print('Google', type.capitalize(), 'Search :', keyword)
        result, total = [], 0
        query = self.query_gen(keyword, type)
        while True:
            # 検索
            html = self.session.get(next(query)).text
            links = self.get_links(html, type)

            # 検索結果の追加
            if not len(links):
                print('-> No more links')
                break
            elif len(links) > maximum - total:
                result += links[:maximum - total]
                break
            else:
                result += links
                total += len(links)

        print('-> Finally got', str(len(result)), 'links')
        return result

    def query_gen(self, keyword, type):
        '''検索クエリジェネレータ'''
        page = 0
        while True:
            if type == 'text':
                params = parse.urlencode({
                    'q': keyword,
                    'num': '100',
                    'filter': '0',
                    'start': str(page * 100)})
            elif type == 'image':
                params = parse.urlencode({
                    'q': keyword,
                    'tbm': 'isch',
                    'filter': '0',
                    'ijn': str(page)})

            yield self.GOOGLE_SEARCH_URL + '?' + params
            page += 1

    def get_links(self, html, type):
        '''リンク取得'''
        soup = BeautifulSoup(html, 'lxml')
        if type == 'text':
            elements = soup.select('.rc > .r > a')
            links = [e['href'] for e in elements]
        elif type == 'image':
            elements = soup.select('.rg_meta.notranslate')
            jsons = [json.loads(e.get_text()) for e in elements]
            links = [js['ou'] for js in jsons]
        return links

def main(input_filename, output_filename='output.txt'):
    print("mainstart")
    google = Google()
    # テキスト検索
    Words=[]
    with open(input_filename) as ifs:
        while True:
          s = ifs.readline()
          if not s:
              break
          Words.append(s)
    print("read finish")
    print(Words)
    with open(output_filename, mode='w') as ofs:
        for _,Word in enumerate(Words):
            ofs.write(Word)
            result = google.Search(Word, type='text', maximum=3)
            counter = 0
            for _, e in enumerate(result):
              ofs.write(e)
              ofs.write('\n')
            #    if counter == 3:
            #      break
            #    if e.find('.html') != -1:
            #      ofs.write(e)
            #      ofs.write('\n')
            #      #counter = counter+1
            #print(counter)

if __name__=='__main__':
    args = sys.argv
    print('file name:', args[1])
    try:
        if len(args) == 2:
            main(args[1])
        elif len(args) == 3:
            main(args[1], args[2])
        else:
            print("Error len(args) != 2 || 3")
    except(ValueError):
        print('ValuError happen')
