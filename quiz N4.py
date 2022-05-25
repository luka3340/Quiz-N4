import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

file = open('Phones.csv','w',encoding='utf-8_sig')
file.write('Name/Model/Color' + ',' + 'Price' + ',' + 'Picture URL' + '\n' )


for page in range(1,6):

    r = requests.get(f'https://alta.ge/smartphones-page-{page}.html?features_hash=17-1000-3500-USD.329-127-128')
    soup = BeautifulSoup(r.text,'html.parser')
    list = soup.find('div',class_='grid-list')
    phones = list.find_all('div',class_='ty-column3')

    for phone  in phones:
        item_name = phone.find('div',class_='ty-grid-list__item-name')
        model = item_name.a.text
        # print(model)

        item_price = phone.find('div',class_='ty-grid-list__price')
        price = item_price.span.text.strip()
        # print(price)

        pic_url = phone.img.attrs['src']
        # print(pic_url)

        file.write(model + ',' + price + ',' + pic_url + '\n')

    sleep(randint(15,20))




file.close()


