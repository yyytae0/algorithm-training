import requests


movie_name = ''
for i in movies:
    movie_name = i.name
    release_date = i.date # '2019-01-09' 형식으로
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=5796ca45f3451bf2d68f3949e8f4c4de&language=ko&region=KR&query={movie_name}'
    response = requests.get(URL).json()
    results = response.get('results')
    tmdb_id = ''
    for i in results:
        if i.get('original_language') == 'ko' and i.get('release_date') == release_date:
            tmdb_id = i.get('id')
    if tmdb_id:
        # db에 저장
