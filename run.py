import json
import requests
import settings
import os

def print_ascii():
    print("""
  __                               
 / _|                              
| |_ __ _ _ __ _ __ ___   ___ _ __ 
|  _/ _` | '__| '_ ` _ \ / _ \ '__|
| || (_| | |  | | | | | |  __/ |   
|_| \__,_|_|  |_| |_| |_|\___|_|                   
    """)


print_ascii()

response = requests.get(os.getenv("RANCHER_API_URL"), auth=(os.getenv("RANCHER_API_USER"), os.getenv("RANCHER_API_TOKEN")))
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')

data = response.json()

ignored_stacks = ['network-services', 'healthcheck', "ipsec", "scheduler"]
for stack in data['data']:
    stack_name = stack['name']
    if stack_name not in ignored_stacks:
        print(stack['id'], ": ", stack['name'])

