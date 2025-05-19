import os
import sys
import urllib.request
import json
import random
import time

def search_naver_blog(query, display=10):
    """
    네이버 블로그 검색 API를 사용하여 특정 키워드에 대한 검색 결과를 반환합니다.

    Args:
        query (str): 검색할 키워드입니다.
        display (int): 가져올 검색 결과의 개수입니다 (최대 100).

    Returns:
        list: 검색 결과를 담고 있는 딕셔너리 리스트입니다. 각 딕셔너리는 'title', 'link', 'description',
              'bloggername', 'postdate' 키를 가집니다. 검색에 실패하면 None을 반환합니다.
    """
    client_id = "SwljxgBgdggGbgH3Zpqf"
    client_secret = "uhe_h6zAXK"
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}&display={display}" # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            json_data = response_body.decode('utf-8')
            data = json.loads(json_data)
            extracted_list = []
            for item in data['items']:
                extracted_item = {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "description": item.get("description", ""),
                    "bloggername": item.get("bloggername", ""),
                    "postdate": item.get("postdate", "")
                }
                extracted_list.append(extracted_item)
            return extracted_list
        else:
            print(f"Error Code: {rescode}")
            return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e}")
        return None
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None

def m100(query):
    print(f"[{query}] 검색 결과 100건을 가져옵니다.")
    results = search_naver_blog(query, display=100)
    if results:
        for item in results:
            print("제목:", item['title'])
            print("링크:", item['link'])
            print("-" * 30)
    else:
        print("검색 결과를 가져오지 못했습니다.")

def m50(query):
    print(f"[{query}] 검색 결과 50건을 가져옵니다.")
    results = search_naver_blog(query, display=50)
    if results:
        for item in results:
            print("제목:", item['title'])
            print("링크:", item['link'])
            print("-" * 30)
    else:
        print("검색 결과를 가져오지 못했습니다.")

def m10(query):
    print(f"[{query}] 검색 결과 10건을 가져옵니다.")
    results = search_naver_blog(query, display=10)
    if results:
        for item in results:
            print("제목:", item['title'])
            print("링크:", item['link'])
            print("-" * 30)
    else:
        print("검색 결과를 가져오지 못했습니다.")

def m_random(query):
    print(f"[{query}] 맛집을 추천합니다.")
    results = search_naver_blog(query, display=100) # 최대 100개 검색 후 랜덤 선택
    if results:
        if results:
            random_item = random.choice(results)
            print("\n[추천 맛집]")
            print("제목:", random_item['title'])
            print("링크:", random_item['link'])
            print("설명:", random_item['description'])
            print("블로거:", random_item['bloggername'])
            print("작성일:", random_item['postdate'])
    else:
        print("검색 결과를 가져오지 못했습니다.")