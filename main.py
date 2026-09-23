import requests

# created this project by following the "How to use API doc at https://pixe.la/"

parametersPost = {"token": "krutarthpixelaapikey4567891230",
                  "username": "imgp004",
                  "agreeTermsOfService": "yes",
                  "notMinor": "yes",}

responePost = requests.post(url="https://pixe.la/v1/users", json=parametersPost)
print(responePost.json())