import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

now = datetime.now()
today_date = now.strftime("%Y%m%d")

PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
PIXELA_USERNAME = os.getenv('PIXELA_USERNAME')
PIXELA_GRAPH_ID = os.getenv('PIXELA_GRAPH_ID')

pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
put_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today_date}"
delete_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today_date}"

new_user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

new_graph_params = {
    "id": "graph1",
    "name": "running graph",
    "unit":"kms",
    "type":"float",
    "color":"shibafu"
}

pixel_params = {
    "date": today_date,
    "quantity": "10.01",
}

put_pixel_params = {
    "quantity": "14.01",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Following the 6 steps from here
# https://pixe.la/
# 3 done, 2 to go
# This one is next: Post value to the graph

# POST create a user
# response = requests.post(url=pixela_endpoint,json=new_user_params)
# print(response.text)
# output: https://pixe.la/@ashwinalexander

# POST https://docs.pixe.la/entry/post-graph
# response = requests.post(url=graphs_endpoint,json=new_graph_params, headers=headers)
# print(response.text)
# output: https://pixe.la/v1/users/ashwinalexander/graphs/graph1.html

# POST https://docs.pixe.la/entry/post-pixel
# response = requests.post(url=pixel_endpoint,json=pixel_params, headers=headers)
# output: new pixel at https://pixe.la/v1/users/ashwinalexander/graphs/graph1.html
# print(response.text)

# PUT https://docs.pixe.la/entry/put-pixel
# response = requests.put(url=put_endpoint, json=put_pixel_params, headers=headers)
# output: updated pixel at https://pixe.la/v1/users/ashwinalexander/graphs/graph1.html
# print(response.text)

# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# https://docs.pixe.la/entry/delete-pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)