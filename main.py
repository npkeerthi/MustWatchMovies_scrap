from bs4 import BeautifulSoup
import requests
# url="https://www.empireonline.com/movies/features/best-movies-2/"


url="http://web.archive.org/web/20200821234542/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(url)
webhtml=response.text

soup=BeautifulSoup(webhtml,"html.parser")
# print(soup.prettify())
al_muvs=soup.find_all(name="h3",class_="title" )
# print(al_muvs)

names=[muv.getText() for muv in al_muvs]
movie=names[::-1] #[start:stop:step]

with open("movies.txt",mode="w") as file:
  for muv in movie:
    file.write(f"{muv}\n")


