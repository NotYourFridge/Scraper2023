import requests
import os


if not os.path.exists("images"):
    os.makedirs("images")


with open("sneaker_images_BristolVER2.0.txt") as f:
    urls = f.read().splitlines()

for i, url in enumerate(urls):
    response = requests.get(url)
    with open(f"images/image_{i}.jpg", "wb") as f:
        f.write(response.content)