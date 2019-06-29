import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
import time
import timeit


def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


def time_spend():
    start = time.clock()
    main()
    end = time.clock()
    print('spend time {}'.format(end - start))

# time_spend()


timeit.timeit('main()', 'from __main__ import main', number=1)


# with  asyncio python


async def fetch_content(url):
    async with aiohttp.ClientSession(
        headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    moive_names, urls_to_fetch, moive_dates = [], [], []

    all_moives = init_soup.find('div', id="showing-soon")
    for each_moive in all_moives.find('div',class_ ="item"):
        all_a_tag = each_moive.find_all("a")
        all_li_tag = each_moive.find_all("li")

        moive_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        moive_names.append(all_li_tag[0].text)

        tasks = [fetch_content(url) for url in urls_to_fetch]
        pages = await asyncio.gather(*tasks)

        for moive_name,moive_date,page in zip(moive_names,moive_dates,pages):
            soup_item = BeautifulSoup(page,'lxml')
            img_tag = soup_item.find('img')

            print(' {} {} {}'.format(moive_name,moive_date,img_tag['src']))

