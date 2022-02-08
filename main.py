import json

import requests
from bs4 import BeautifulSoup


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.6.0.616 Yowser/2.5 Safari/537.36"
    }


    url = "https://www.lefigaro.fr/international"

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    articles_cards = soup.find_all("article", class_="fig-profile")


    news_dict = {}
    for article in articles_cards:
        article_title = article.find("h2", class_="fig-profile__headline").text.strip()
        article_desc = article.find("p").text.strip()


        news_dict[article_title] = {
            article_title: article_title,
            article_desc: article_desc
        }

        with open("news_dict.json", "w") as file:
            json.dump(news_dict, file, indent=4, ensure_ascii=False)

def main():
    get_first_news()

if __name__ == '__main__':
    main()





