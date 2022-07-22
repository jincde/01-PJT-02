import requests

speciesURL = '/movie/popular'
APIkey = 'NEED YOUR API_KEY!!'

URL = f'https://api.themoviedb.org/3{speciesURL}?api_key={APIkey}'

response = requests.get(URL)

data = response.json()


def popular_count():
    return len(data['results'])
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
