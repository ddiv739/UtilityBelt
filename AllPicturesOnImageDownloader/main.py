# Imports
import requests
import urllib.request
from bs4 import BeautifulSoup 
import os 
import argparse
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=False,
	help="name of the folder")
ap.add_argument("-u","--url", required=True,
    help="Url to download from")
#Make an accumulator if you only want certain file types!
args = vars(ap.parse_args())
 
#Variable declaration
files = []
URL = args['url']
accepted_formats = ['.jpg','.png','.webm','.jpeg', '.gif']
parent_dir = os.path.dirname(os.path.realpath(__file__))

print("Starting download")
#Argument Interpretation
print("Interpreting arguments")
#URL (Required)
print("Downloading from " + URL)
site= URL
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib.request.Request(site, headers=hdr)
response = urllib.request.urlopen(req)
# print(response.read())
soup= BeautifulSoup(response.read(), 'html.parser')
print(soup.prettify())


#Find all a tags
for link in soup.find_all('a'):
    # print(link)
    potential = link.get('href')
    # print(potential)
    if(potential == None):
        potential = link.get('img')
        continue
    for form in accepted_formats:
        if(potential[-len(form):] == form):
            if(potential not in files):
                files.append(potential)
                print("Adding! : " + potential)

    
if (len(files) == 0):
    print("Couldn't find any files!")
else:
    #Pythonic equivalent of x= y || 1 from javascript. fallback value
    #.rsplit("/",1)[-1] conducts a only 1 split from the right and takes the second (everything after final /) string
    child_dir = args['name'] if args['name'] is not None else args['url'].rsplit("/",1)[-1]
    if not os.path.exists(parent_dir + "\\" + child_dir):
        print("creating file directory")  
        os.mkdir(parent_dir + "\\" +  child_dir)
#Download all 
for fileurl in files:
    filename = fileurl.rsplit("/",1)[-1]
    if(fileurl[:2] == "//"):
        # fileurl = fileurl[2:]
        fileurl = "https:" + fileurl
    print("Downloading: " + filename)
    urllib.request.urlretrieve(fileurl,  child_dir + "/" + filename)

print("All finished - all up " + str(len(files)) + " files downloaded! Enjoy!")
    
