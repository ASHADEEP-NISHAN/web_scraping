from bs4 import BeautifulSoup
import requests
response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page=response.text
soup=BeautifulSoup(movie_web_page,"html.parser")
movie_headings=soup.find_all(name="h3",class_="title")
movie_list=[movie.getText() for movie in movie_headings]
movie_list=movie_list[::-1]
print(movie_list)
with open("movies.txt",'w',encoding="utf-8") as file:
    for m in movie_list:
       file.write(f"{m}\n")