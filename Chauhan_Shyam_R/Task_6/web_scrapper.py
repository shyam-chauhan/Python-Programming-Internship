import requests
from bs4 import BeautifulSoup as bs4
import csv



def request_maker():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    url = 'https://books.toscrape.com/index.html'
    res = requests.get(url, headers=headers) 
    soup = bs4(res.content, 'html5lib')
    return soup

def finder(soup):
    books=[]
    prices = [] 
    h3 = soup.find_all('h3')
    price_tags = soup.find_all('p', class_='price_color')

    for price_tag in price_tags:
        price = price_tag.text.strip() 
        prices.append(price)
    
    for book in h3:
        i = book.find('a').get('title')
        books.append(i)
    return books,prices

def csv_maker(data):
    books,prices = data
    file_name = 'book_data.csv'
    with open(file_name,'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Price'])
        for i in range(0,len(books)):
            writer.writerow([books[i],prices[i]])
    print("csv file generated successfully, saved as book_data.csv")
    

def main():
    soup = request_maker()
    data = finder(soup)
    csv_maker(data)

if __name__ == '__main__':
    main()