import discord
import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
        if message.author == client.user:
            return
        if message.content =="food-today":
            date = datetime.datetime.now()
            now = date.strftime("%A")
            url = "https://www.imensa.de/karlsruhe/mensa-erzbergerstrasse/"
            if (now == 'Monday'):
                url = url + "montag.html"
            elif (now == 'Tuesday'):
                url = url + "dienstag.html"
            elif (now == 'Wednesday'):
                url = url + "mittwoch.html"
            elif (now == 'Tuesday'):
                url = url + "donnerstag.html"
            elif (now == 'Friday'):
                url = url + "freitag.html"
            html_today = requests.get(url)
            soup_today = BeautifulSoup(html_today.text, "html.parser")
            food = soup_today.find_all('p', {"class": "aw-meal-description"})
            prices = soup_today.find_all('div', {"class": "col-sm-2 no-padding-xs aw-meal-price"})
            for f, p in zip(food, prices):
                 food_data =f.text+" für "+p.text
                 await message.channel.send(food_data)
        if message.content =="food-tomorrow":
            date = datetime.datetime.now()
            now = date.strftime("%A")
            url = "https://www.imensa.de/karlsruhe/mensa-erzbergerstrasse/"
            if (now == 'Monday'):
                url = url + "dienstag.html"
            elif (now == 'Tuesday'):
                url = url + "mittwoch.html"
            elif (now == 'Wednesday'):
                url = url + "donnerstag.html"
            elif (now == 'Tuesday'):
                url = url + "freitag.html"
            elif (now == 'Friday'):
                await message.channel.send("keine Ahnung,  heute ist freitag 🤞 ")
                return
            html_today = requests.get(url)
            soup_today = BeautifulSoup(html_today.text, "html.parser")
            food = soup_today.find_all('p', {"class": "aw-meal-description"})
            prices = soup_today.find_all('div', {"class": "col-sm-2 no-padding-xs aw-meal-price"})
            for f, p in zip(food, prices):
                food_data = f.text + " für " + p.text
                await message.channel.send(food_data)
client.run(os.getenv("TOKEN"))



