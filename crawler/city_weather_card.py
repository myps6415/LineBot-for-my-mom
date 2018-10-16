from crawler.weather_crawler import *

def hualien_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '花蓮' in img_url:
            hualien_img_url = img_url.split('  ')[1].replace('http', 'https')
            return hualien_img_url

def taipei_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '臺北' in img_url:
            taipei_img_url = img_url.split('  ')[1].replace('http', 'https')
            return taipei_img_url

def newtaipei_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '新北' in img_url:
            newtaipei_img_url = img_url.split('  ')[1].replace('http', 'https')
            return newtaipei_img_url

def taoyuan_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '桃園' in img_url:
            taoyuan_img_url = img_url.split('  ')[1].replace('http', 'https')
            return taoyuan_img_url

def kaohsiung_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '高雄' in img_url:
            kaohsiung_img_url = img_url.split('  ')[1].replace('http', 'https')
            return kaohsiung_img_url

def hsinchu_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '新竹' in img_url:
            hsinchu_img_url = img_url.split('  ')[1].replace('http', 'https')
            return hsinchu_img_url

def taichung_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '臺中' in img_url:
            taichung_img_url = img_url.split('  ')[1].replace('http', 'https')
            return taichung_img_url

def chiayi_crawler():
    soup = every_city()
    for images in soup.find_all(class_='col-sm-6 col-md-4'):
        img_url = images.find('div').find(class_='navbar-brand Brand-icon icon-line-sign').get('href')
        if '嘉義' in img_url:
            chiayi_img_url = img_url.split('  ')[1].replace('http', 'https')
            return chiayi_img_url