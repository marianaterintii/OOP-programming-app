from core import *
from os import system
system ("cls")

def appInfo(App):
       print (f" app name: {App.name}\n version: {App.version}\n author: { App.author} \n year: {App.year}\n rating: {App.rating}")

print(appInfo(App))

print()
