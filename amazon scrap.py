import csv
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

r = requests.get('https://www.amazon.in/s?k=laptops&ref=nb_sb_noss_2', headers = headers).text
htmlContent = r
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)


Name = []
Prices = []
Ratings= []

for i in soup.find_all('a', class_ = 'a-link-normal a-text-normal'):
    string = i.text
    Name.append(string.strip())

for i in soup.find_all('span', class_ = 'a-price-whole'):
    Prices.append(i.text)

for i in soup.find_all('a', class_ = 'a-popover-trigger a-declarative'):
    Ratings.append(i.text)

file_name = 'Amazon.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No','Laptop Name','Ratings','Prices'])

    for i in range(1,23):
        writer.writerow([i, Name[i], Ratings[i], Prices[i]])

