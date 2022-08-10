import discord
import requests
import datetime
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.content == "dhbw karlsruhe bot":
        await message.channel.send("`" + "possible commands, they only work in the chancel mensa-essen, but you can read it anywhere:" +"`"+ "\n" +
                                   "`" + "Mensa Erzbergerstraße-Heute" +"`"+ "\n" +
                                   "`" + "Mensa Erzbergerstraße-Morgen" +"`"+ "\n" +
                                   "`" + "Mensa Moltke-Heute" +"`"+ "\n" +
                                   "`" + "Mensa Moltke-Morgen" +"`"+ "\n" +
                                   "`" + "Mensa Adenauerring-Heute" +"`"+ "\n" +
                                   "`" + "Mensa Adenauerring-Morgen" +"`"+ "\n" )



    channels = ["mensa-essen"]
    if str(message.channel) in channels:
            if message.content =="Mensa Erzbergerstraße-Heute":
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
                     await message.channel.send("`" + food_data + "`")
                await message.channel.send("(☞ﾟヮﾟ)☞, das was!")






            if message.content =="Mensa Erzbergerstraße-Morgen":
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
                    await message.channel.send("`" +food_data+ "`")
                await message.channel.send("(☞ﾟヮﾟ)☞, das was!")







            if message.content =="Mensa Moltke-Heute":
                date = datetime.datetime.now()
                now = date.strftime("%A")
                url = "https://www.imensa.de/karlsruhe/mensa-moltke/"
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
                     await message.channel.send("`" + food_data + "`")
                await message.channel.send("(☞ﾟヮﾟ)☞, das was!")




            if message.content =="Mensa Moltke-Morgen":
                date = datetime.datetime.now()
                now = date.strftime("%A")
                url = "https://www.imensa.de/karlsruhe/mensa-moltke/"
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
                    await message.channel.send("`" +food_data+ "`")
                await message.channel.send("(☞ﾟヮﾟ)☞, das was!")





            if message.content =="Mensa Adenauerring-Heute":
                date = datetime.datetime.now()
                now = date.strftime("%A")
                url = "https://www.imensa.de/karlsruhe/mensa-am-adenauerring/"
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
                     await message.channel.send("`" + food_data + "`")
                await message.channel.send("(☞ﾟヮﾟ)☞, das was!")




            if message.content =="Mensa Adenauerring-Morgen":
                date = datetime.datetime.now()
                now = date.strftime("%A")
                url = "https://www.imensa.de/karlsruhe/mensa-am-adenauerring/"
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
                    await message.channel.send("`" +food_data+ "`")
                await message.channel.send("(☞ﾟヮﾟ)☞, das was!")


client.run(os.getenv("TOKEN"))



