from lxml import html
import requests
import json
import sys
from requests.auth import HTTPBasicAuth

def getfile(filename):
    try:
        with open(filename) as f:
            input_data= json.load(f)
        f.close()
    except FileNotFoundError:
            print('No such file')
            exit(1)
    return input_data

def main():
    # defaults
    INI_URL='https://yolaw-tokeep-hiring-env.herokuapp.com'
    USERNAME_AUTH = 'Thumb'
    PASSWORD_AUTH = 'Scraper'
    if(len(sys.argv)!=2):
        print('Error!')
        print('Usage: python thumbs.py distortedjsonfilename')
        exit()
    input_data=getfile(sys.argv[1])
    url = INI_URL
    key = next(iter(input_data))
    count = 0
    while True:
        page=requests.get(url, auth=HTTPBasicAuth(USERNAME_AUTH, PASSWORD_AUTH))
        if page.status_code != 200:
            raise Exception('Problem fetching page')
        page=page.content
        xmltree = html.fromstring(page)
        xpath_find,next_page_to_find=input_data[key]['xpath_test_query'],input_data[key]['xpath_button_to_click']
        #check validity
        if (xmltree.xpath(xpath_find) == input_data[key]['xpath_test_result']):
            print('Move to page',  (count + 1))
            #update URLs
            npageurl = xmltree.xpath(next_page_to_find + '/@href')[0]
            url = INI_URL + npageurl
            key = input_data[key]['next_page_expected']
            count += 1
        else:
            print('ALERT - Can’t move to page ',
                  count+1,
                  ': page ',
                  count,
                  ' link has been malevolently tampered with!!'
            )
            return



if __name__ == '__main__':
    main()
