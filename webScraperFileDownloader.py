import requests
import easygui
import os
from urllib import request, response, error, parse
from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = easygui.enterbox("Paste the url to extract files from: ") #change this url of course
while(True):
    fileType = easygui.enterbox("Enter the type of file (ex: ppt, pdf): ")
    folder = easygui.enterbox("Enter the name of the folder to be created (Files will be downloaded here): ")
    os.mkdir('C:/users/ntseg/desktop/'+folder)
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    titles = soup.findAll('a')
    for i in titles:
        if(i.get('href')[-3:]==fileType): #change filename depending on what you want to download
            urlToDownload = urljoin(url,i.get('href'))
            r = requests.get(urlToDownload, allow_redirects=True)
            open('C:/users/ntseg/desktop/'+folder+'/'+i.get('href'),'wb').write(r.content) #change the directory to be saved
    easygui.msgbox("Download complete!")
    response = easygui.enterbox("Would you like to save another type of file from the same page? (y/n): ")
    if(response == 'n' or response == 'no'):
        break
