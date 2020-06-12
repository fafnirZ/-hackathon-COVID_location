'''
downloading the information
'''
import requests
from urllib import request
from bs4 import BeautifulSoup


def update_info():
    url = 'https://data.nsw.gov.au/data/dataset/covid-19-cases-by-location/resource/21304414-1ff1-4243-a5d2-f52778048b29?fbclid=IwAR3gSceCXp8zZY4-OBMJm9bwPI0cLRaHkKT880bUPUqqua8rKIT94OYHyEI'
    site = request.urlopen(url)


    '''
    bs4
    '''

    soup = BeautifulSoup(site, 'html.parser')

    for A in soup.find_all('a'):

        c = A.get('class')
        if(c == ['btn', 'btn-primary', 'resource-url-analytics', 'resource-type-None']):
            file = A.get('href')
            print(file)
            FILE = requests.get(file, allow_redirects=True)

            open('data.csv', 'wb').write(FILE.content)

