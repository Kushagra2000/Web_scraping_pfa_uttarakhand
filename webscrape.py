from bs4 import BeautifulSoup, SoupStrainer
import requests
import urllib3
import os
import urllib
from tqdm import tqdm
from bs4.element import Comment
import traceback

url= "https://web.archive.org/web/20150102141104/http://pfauttarakhand.org/"
root_path="/home/samsepi0l/Scraping/website/pfauttarakhand_org/"

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

dates=sorted(os.listdir(root_path))
dates
url_links=set()
for date in dates:
    # with open(root_path+date,'r') as f:
    #     contents=f.read()
    #     contents
    with open(root_path+date) as file:
        file_data=file.read()
        file_soup=BeautifulSoup(file_data,"lxml")
        relevant_data=str(file_soup.find("div",{"id":"the_body"}))
    for link in BeautifulSoup(relevant_data,"html.parser",parse_only=SoupStrainer('a')):
        if(link.has_attr('href')):
            url_links.add(link['href'])
len(url_links)

for url in tqdm(url_links,total=len(url_links)):
    #print(url)
    try:
        html=requests.get(url).text
        new_soup=BeautifulSoup(html,'lxml')
        archive_data=str(new_soup.find("div",{"id":"archive"}))
        if archive_data is None:
            print("No div with id ARCHIVE. Moving to next link")
            continue
        else:

            archive_soup=BeautifulSoup(archive_data,'lxml')
            desc_data=str(archive_soup.find("div",{"class":"description"}))
            if desc_data is None:
                print("No div with class DESCRIPTION. Moving to next link")
                continue
            else:
                desc_soup=BeautifulSoup(desc_data,'lxml')
                content_data=str(archive_soup.find("div",{"id":"content"}))
                if content_data is None:
                    print("No div with class CONTENT. Moving to next link")
                    continue
                else:
                    content_soup=BeautifulSoup(content_data,'lxml')

                    heading=desc_soup.findAll(text=True)
                    visible_heads=filter(tag_visible,heading)
                    with open('/home/samsepi0l/Code/scraped_text.txt','r+') as res_file:
                        already_there=res_file.read()
                        res_file.write(" ".join(t.upper() for t in visible_heads if t.upper() not in already_there))
                        res_file.write("\n")
                        res_file.write("\n")


                    art_text=content_soup.findAll(text=True)
                    visible_text=filter(tag_visible,art_text)
                    with open('/home/samsepi0l/Code/scraped_text.txt','r+') as res_file:
                        already_there=res_file.read()
                        res_file.write(" ".join(t for t in visible_text if t not in already_there))
                        res_file.write("\n")
                        res_file.write("\n")

    except Exception as e:
        print(url)
        print(e)
        print(traceback.format_exc())



















































# texts=new_soup.findAll(text=True)
# visible_texts=filter(tag_visible,texts)
# count=0
# # for x in visible_texts:
# #     print(x)
# #     count+=1
# #     print("COUNTS:{}".format(count))
# #print(" ".join(t for t in visible_texts))
#
# # with open('/home/samsepi0l/Code/scraped_text.txt','a') as res_file:
# #     res_file.write(" ".join(t for t in visible_texts))
