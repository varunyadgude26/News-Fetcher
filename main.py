from dotenv import load_dotenv
import requests
import os

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

url = 'https://api.akta.pro/api/v1/news?limit=10'
header = {'x-api-key': NEWS_API_KEY}


def get_news():
    while True:
        genre_ops = [i for i in range(0,6)]
        genre_dict = {1:"Sports",
                    2:"Politics",
                    3:"Science",
                    4:"Bussiness",
                    5:"Tech"}
        genre = int(input("What Genre of news Do you want ? \n1.Sports\n2.Politics\n3.Science\n4.Bussiness\n5.Tech\n0:'Exit'"))
        if  genre not in genre_ops:
            print("Invalid Genre")
        elif genre == 0 :
            print('Thank you for reading, Bye')
            break
        else:
            topic = input(f"What would you like to know about {genre_dict[genre]}?")
            query = f'I want to know about {topic} from the genre {genre_dict[genre]}'
            params={
                "query": query,
                'limit':1
            }
            with requests.get(url,headers=header,params=params,stream=True) as r:
                if r.status_code == 200:

                    data = r.json()

                    print('\n'+data['data'][0]['full_text'])
                else:
                    print(f"API ERROR : {r.status_code}")
                    print(r.text)
        

if __name__ == '__main__':

    get_news()