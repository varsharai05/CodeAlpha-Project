import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
for page in range(1, 51):
  url = f"https://books.toscrape.com/catalogue/page-{page}.html"
  
  response = requests.get(url , timeout=10)
  
  print("Scraping page :" , page)
  
  soup = BeautifulSoup(response.text , "html.parser")
  
  for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text.strip()
    rating = book.select_one("p.star-rating")["class"][1]
    books.append({
      "Title":title,
      "Price":price,
      "Rating": rating
    })
print("Total books scraped :" ,len(books))

df = pd.DataFrame(books)
print(df.head())

df.to_csv("data/books.csv" , index=False)
print("Data saved successfully..")