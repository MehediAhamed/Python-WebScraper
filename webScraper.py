#Developed BY 
#Mehedi Ahamed 200041125
  
import os
from urllib import response
import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
import re

URL=input("Enter URL : ")
print("Given URL :",URL)
print("\n")
bol1=1
bol2=1
bol3=1
bol4=1
bol5=1
bol6=1

#checking protocols

bol1=URL.find('https://')
bol2=URL.find('http://')
bol3=URL.find('ftp://')

if  bol1<0 and bol2<0 and bol3<0:
    print("Wrong protocol. You didn't enter correct protocol like https://  http:// or ftp://" )
    exit(-1)

#checking domain

bol4=URL.find('.com')
bol5=URL.find('.net')
bol6=URL.find('.org')   

if (bol4<0 and bol5<0 and bol6<0):
    print("Wrong domain. You didn't enter correct domain like .com  .org or .net" )
    exit(-1)



#checking URL validity

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

if(re.match(regex,URL) is not None)==False:
       print("URL is not valid")
       exit(-1)



print("Data is loading...\n")
#getting html source
try:
    
    request_site = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    r = urlopen(request_site).read()
   
    print(r)

except Exception as e:
    print(str(e))





#writing in txt and html

open("D:\Mars_Rover_ID_200041125_source.txt", "wb").write(r)
open("D:\Mars_Rover_ID_200041125_source.html", "wb").write(r)



os.system('cls')

# CREATE FOLDER
try:
        folder_name = input("Enter Folder Name:- ")
        # folder creation
    
      

        folder_name= "D:\Mars_Rover_WebImage_ID_200041125_"+ folder_name  
        
        os.mkdir(folder_name)
 
    # if folder exists with that name, ask another name
except:
        print("\nFolder Exist with that name!")
      


# search img src

webcontent=r
webcontent=str(webcontent)

pattern='<img src="([^\s]+)"'
match=re.findall(pattern,webcontent)

c=0
i=1
for item in match:
    c+=1

if (c==0) :
    print("\nNo image found in the website.")

else:
    print("\nTotal ",c," Images Found")  

    for item in match:

        imageUrl=item
        res = Request(imageUrl, headers={"User-Agent": "Mozilla/5.0"})
        web = urlopen(res).read()  
        open(f"{folder_name}/images{i}.jpg", "wb+").write(web)          
        i += 1          
print("\nTotal ",i-1," images downloaded out of ",c,".")

