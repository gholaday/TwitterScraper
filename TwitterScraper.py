from bs4 import BeautifulSoup
from selenium import webdriver
import time

MAXPAGES = 5000
SLEEPTIME = 1.5

def GetNames():
  
    names = set()

    url = input('Enter the hashtag: ')
    numPages = int(input('How many pages do you want to scrape?\n(Enter 0 if you want it to check as many as possible) '))

    if numPages == 0:
        numPages = MAXPAGES;

    url = url.replace('#', '')

    wd = webdriver.Firefox()
    wd.get('https://twitter.com/search?q=%23' + url + '&src=typd')

    lastHeight =  0

    for i in range(numPages):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SLEEPTIME)

        newHeight = wd.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

        if i % 5 == 0 and i != 0:
            print('Scrolled through ' + str(i) + ' lines...')

    print('Finished scrolling....finding Twitter handles...')

    source = wd.find_element_by_id('timeline').get_attribute('outerHTML')

    soup = BeautifulSoup(source, 'xml')
    print('Begun name search...')
    for page in soup.findAll('span', {'class':'username js-action-profile-name'}):
        names.add('@' + page.b.getText())

    print('....Done!')
    print('Number of names found = ' + str(len(names)))

    fn = url + '-names.txt'

    SaveNames(fn, names)

    wd.quit()

def SaveNames(fileName, names):
    print('Saving to ' + fileName + '...')
    file = open(fileName, 'w')
    for name in names:
        file.write(name + '\n')

    print('File Saved!')
    file.close()

GetNames()
