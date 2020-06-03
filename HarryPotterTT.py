from flask import Flask, render_template, request # import flask
import sys
app = Flask(__name__) # create an app instance
import requests
import random
def random_HPcharacter():
    potter_number = random.randint(1, 151)
    url = "https://hp-api.herokuapp.com/api/characters".format(potter_number)
    response = requests.get(url)
    random_number = random.randint(0, len(response.json())-1)
    potter = response.json()[random_number]
    print(response.json)
    print(potter)
    return {
        "name": potter["name"],
        "species": potter["species"],
        "gender": potter["gender"],
        "house": potter["house"],
        "dateOfBirth": potter["dateOfBirth"],
        "yearOfBirth": potter["yearOfBirth"],
        "ancestry": potter["ancestry"],
        "eyeColour": potter["eyeColour"],
        "hairColour": potter["hairColour"],
        "wand": potter["wand"],
        "patronus": potter["patronus"],
    }
species = {'human': 1, 'werewolf' : 2, 'cat' : 0, 'half-giant' :2 }
house = {'Gryffindor': 4, 'Slytherin':0, 'Ravenclaw':3, 'Hufflepuff':2}
def patronus():
   return random.randint(0, 10)
def ancestry():
    return random.randint(0, 10)
def run():
    my_harrypotter = random_HPcharacter()
    print('You were given {}'.format(my_harrypotter['name']))
    stat_choice = input('Which stat do you want to use? (species, house, patronus, ancestry) ')
    opponent_potter = random_HPcharacter()
    print('The opponent chose {}'.format(opponent_potter['name']))
    my_stat = my_harrypotter[stat_choice]
    opponent_stat = opponent_potter[stat_choice]
    if stat_choice == 'species':
        if species[my_stat] > species[opponent_stat]:
            print('You Win!')
        elif species[my_stat] < species[opponent_stat]:
            print('You Lose!')
        else:
            print('Draw!')
    if stat_choice == 'house':
        if house[my_stat] > house[opponent_stat]:
            print('You Win!')
        elif house[my_stat] < house[opponent_stat]:
            print('You Lose!')
        else:
            print('Draw!')
    if stat_choice == ancestry:
        if house[my_stat] > house[opponent_stat]:
            print('You Win!')
        elif house[my_stat] < house[opponent_stat]:
            print('You Lose!')
        else:
            print('Draw!')
    if stat_choice == patronus:
        if house[my_stat] > house[opponent_stat]:
            print('You Win!')
        elif house[my_stat] < house[opponent_stat]:
            print('You Lose!')
        else:
            print('Draw!')
run()
