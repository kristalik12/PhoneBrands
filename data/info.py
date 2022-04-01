import requests

url="https://api-mobilespecs.azharimm.site/v2/brands"
response = requests.get(url).json()
brand_names = response["data"]

















# def get_brands(url="https://api-mobilespecs.azharimm.site/v2/brands"):
#   response = requests.get(url).json()
#   brand_slug = url + "/" + response["data"][0]['brand_slug']
#   return brand_slug

# # print(get_brands(url)[1])

