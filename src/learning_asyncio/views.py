from django.shortcuts import render
import asyncio
import requests
# import pandas
from bs4 import BeautifulSoup
import csv


def index(request):
    return render(request, 'learning_asyncio/asyncio_index.html')


async def get_web_data(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')
    data = soup.findAll("div", {"id": "mainPanel"})
    output = list(set(data[0].text.split('\n')))
    data_file = pandas.DataFrame(output)
    data_file.to_csv('asyncio_data.csv', mode='a', index=False)


def show_data_csv(request):
    loop = asyncio.get_event_loop()
    task = [
        get_web_data('https://www.tuenvio.cu/artemisa/Products?depPid=46095')
    ]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()

    data_file = csv.reader('asyncio_data.csv')
    context = {'data': data_file}
    return render(request, 'learning_asyncio/asyncio_show.html', context)
