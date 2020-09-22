import requests
import json
from pprint import pprint


#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()


resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)
#resp = requests.get('https://jsonplaceholder.typicode.com/comments')


#Converts response to JSON
data = resp.json()

pprint(data)