'''
This example will use a class statically

Let's imagine that there is a class that represents the "core" of the social app

1. create module called core.py
2. create a class called App, inside it
3. add the attributes: name (name of the application), version (release version of the application), 
   author (author of the app name and email), year (the year the app was first published), rating (in the 5 star scale)
4. create a separate function called appInfo() in the same module which will print the information from the class using formatted string
5. test your module by importing it and using it in the main module called main.py'''

class App:
    name = "NewApp"
    version = "1.1.1"
    author = "John"
    year = 2002
    rating = 4.5

    def appInfo():
       print (f" app name: {App.name}\n version: {App.version}\n author: { App.author} \n year: {App.year}\n rating: {App.rating}")

