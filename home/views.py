from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

# Create your views here.
# 홈페이지
def index(request):
    # TMDB API를 이용해 영화 정보 가져오기
    load_dotenv()
    key = os.environ.get('TMDB_API_key')
    base_url = 'https://api.themoviedb.org/3'

    # 지역별 인기 영화
    path_popular = '/movie/popular'
    parameters_popular = {
            'api_key': key,
            'language': 'ko-kr',
            'region': 'kr',
    }
    response_popular = requests.get(base_url + path_popular, params=parameters_popular).json()
    results_popular = response_popular.get("results")
    results_popular.sort(key=lambda result:result.get("release_date"), reverse=True)

    # 오늘 인기 영화
    path_trend = f'/trending/movie/day'
    parameters_trend = {
            'api_key': key,
    }
    response_trend = requests.get(base_url + path_trend, params=parameters_trend).json()
    results_trend = response_trend.get("results")

    context = {
        'results_popular': results_popular[:10],
        'results_trend': results_trend[:10]
    }

    return render(request, 'home/index.html', context)

# 검색
def search(request):
    q = request.GET.get('query')
    
    # TMDB API를 이용해 영화 정보 가져오기
    load_dotenv()
    key = os.environ.get('TMDB_API_key')
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    parameters = {
        'api_key': key,
        'query': q,
        'language': 'ko-kr',
    }

    response = requests.get(base_url + path, params=parameters).json()
    
    results = response.get('results')
    results.sort(key=lambda result:result.get("release_date"), reverse=True)

    tot_results = response.get('total_results')
    
    context = {
        'search': q,
        'results': results,
        'tot_results': tot_results,
    }

    return render(request, 'home/search.html', context)
