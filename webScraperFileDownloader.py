import requests
import easygui
import os
import os.path
from urllib import request, response, error, parse
from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup

ListofTypes = ['mp3','wav','rar','zip','csv','exe','jpeg','jpg','png','svg','gif','bmp','html','ppt','mp4','doc','docx','pdf','txt','out']
while(True):
    url = input("Paste the url to extract files from (type 'exit' to close at any point): ") #change this url of course
    if(url == 'exit'):
        break
    while(True):
        while(True):
            fileType = input("Enter the type of file (ex: ppt, pdf): ")
            if(fileType in ListofTypes):
                break
            if(fileType=='exit'):
                break
            elif(len(fileType)>0):
                message = "Please enter a filename from the following types: "
                for i in ListofTypes:
                    message+=(i+", ")
                print(message)
        if(fileType=='exit'):
            break
        folder = input("Enter the name of the folder to be created (Files will be downloaded here): ")
        if folder=='exit':
            break
        path = 'C:/users/ntseg/desktop/'+folder
        if(not os.path.isdir(path)):
            os.mkdir(path)
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")
        titles = soup.findAll('a')
        filecount = 0
        for i in titles:
            if(i.get('href')[-3:]==fileType or i.get('href')[-2:]==fileType): #change filename depending on what you want to download
                filecount+=1
                urlToDownload = urljoin(url,i.get('href'))
                r = requests.get(urlToDownload, allow_redirects=True)
                open(path+'/'+i.get('href'),'wb').write(r.content) #change the directory to be saved
        if(filecount == 0):
            print("Filetype "+fileType+" not found on the webpage.")
            os.rmdir(path)
        else:
            print("Download complete!")
        response = input("Would you like to save another type of file from the same page? (y/n): ")
        if(response == 'n' or response == 'no' or response == 'exit'):
            break
    break
