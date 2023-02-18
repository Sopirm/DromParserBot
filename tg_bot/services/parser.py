from bs4 import BeautifulSoup
from aiogram import types, Dispatcher
import aiohttp
import asyncio


async def get_page_data(session, page,message):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36"}
    url = f"{message.text.split(' ')[1]}page{page}/"
    async with session.get(url=url, headers=headers) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, "html.parser")
        all_cars_info = soup.find_all(class_="css-xb5nz8 e1huvdhj1")
        item_car = soup.find_all(class_="css-13ocj84 e727yh30")
        for i in range(len(all_cars_info)):
            item_link = all_cars_info[i].get("href")
            item = all_cars_info[i]
            if item_link.split('.')[0] == "https://moscow":
                item_car = item.text.split(',')[0]
                item_year = int(item.text.split(',')[1][:5])
                await message.answer(f"{item_car} {item_year}: {item_link}")
            else:
                pass
async def gather_data(message: types.Message):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36"}
    url = message.text.split(' ')[1]
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), "html.parser")
        tasks = []
        pages_count = int(soup.find_all(class_="css-19tk3lt e15hqrm30")[-1].text)
        for page in range(1, pages_count + 1):
            task = asyncio.create_task(get_page_data(session, page,message))
            tasks.append(task)
        await asyncio.gather(*tasks)

def register_parser(dp: Dispatcher):
    dp.register_message_handler(gather_data,commands=['parser'])