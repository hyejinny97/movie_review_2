from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

# Create your views here.
def detail(request, movie_id):
    # TMDB API를 이용해 영화 정보 가져오기
    load_dotenv()
    key = os.environ.get('TMDB_API_key')
    base_url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}'
    parameters = {
        'api_key': key,
        'language': 'ko-kr',
    }

    movie = requests.get(base_url + path, params=parameters).json()
    
    context = {
        'movie': movie,
    }

    return render(request, 'movie/detail.html', context)