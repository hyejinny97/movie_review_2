# 참고(템플릿 필터): https://daeunnniii.tistory.com/128
# 참고(정규 표현식): https://wikidocs.net/4308
from django import template
import re

register = template.Library()

@register.filter
def is_movie_detail(path):
    pattern = re.compile('/movie/[0-9]+')
    if pattern.match(path):
        return True
    else: 
        return False