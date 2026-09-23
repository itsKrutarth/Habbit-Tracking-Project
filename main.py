import requests

# created this project by following the "How to use API doc at https://pixe.la/"

#create my account
parametersPost = {"token": "krutarthpixelaapikey4567891230",
                  "username": "imgp004",
                  "agreeTermsOfService": "yes",
                  "notMinor": "yes",}

responePost = requests.post(url="https://pixe.la/v1/users", json=parametersPost)
# print(responePost.json())

#create my graph
USERNAME = "imgp004"
TOKEN = "krutarthpixelaapikey4567891230"
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
parametersGraph={
    "id": "graph1",
    "name": "My Learning Streak",
    "unit": "commit",
    "type": "int",
    "color": "sora",
    "startOnMonday": True,
}
headersGraph={
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=parametersGraph, headers=headersGraph)
# print(response.json())

# Our graph is now available at https://pixe.la/v1/users/imgp004/graphs/graph1.html
