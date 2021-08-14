import requests, re
import wget
import urllib
import time
from datetime import date
import os.path
import datetime

def get_url_images_in_text(html):
    urls = []
    all_urls = re.findall(r'((http\:|https\:)?\/\/[^"\' ]*?\.(png|jpg))', html, flags=re.IGNORECASE | re.MULTILINE | re.UNICODE)
    for url in all_urls:
            if url[0].startswith("https://mir-s3-cdn-cf.behance.net/project_modules"): 
                try:
                    if not os.path.isfile("./Downloads/" + str(url[0].split('/')[-1])): 
                        urllib.request.urlretrieve(url[0],"Downloads/" + str(url[0].split('/')[-1]) )
                        print("Image downloaded successfully: " + str(url[0].split('/')[-1]) )
                except :
                    continue
                urls.append(url[0])
    return urls

def main():
    
    
    while True:
        _input = input("Please enter link: ")
        try: 
            resp = requests.get(_input)
            get_url_images_in_text(resp.text)
        except : print("Given string is not a valid link, please enter link starts with www.behance.net/gallery")


main()
    
    
