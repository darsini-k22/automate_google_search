from selenium import webdriver
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

def imgDownload(key_words):   
    browser = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    browser.get("https://www.google.com/")
    search = browser.find_element_by_name('q')
    search.send_keys(key_words,Keys.ENTER)

    elem = browser.find_element_by_link_text('Images')
    elem.get_attribute('href')
    elem.click()
    sub = browser.find_elements_by_tag_name("img") 
    try:
        os.mkdir('images')
    except FileExistsError:
        pass
    for i in sub[1:10]:
        src = i.get_attribute('src')
        try:
            if src != None:
                src = str(src)
                print(src)
                urllib.request.urlretrieve(src, os.path.join('images','image'+str(1)+'.jpg'))
                # rename img name to movies name
            else:
                raise TypeError
        except TypeError:
            print('Fail')

    # rename image to movies name
    # print(key_words.replace("poster",""))
    dst = "C:/Users/darsi/OneDrive/Documents/GitHub/images/"+key_words.replace("poster","").replace("\n","").replace(" ","").replace(":","")+".jpg"
    src = "C:/Users/darsi/OneDrive/Documents/GitHub/images/"+"image1.jpg"
    os.rename(src, dst)
    # close browser
    browser.close()


f=open("movies.txt","r")
img=[i+" poster" for i in f]


print("Done importing species names...")
for name in img:
    print(name)
    imgDownload(name)