import requests

URL = "https://ummahapi.com/api/duas/random"


def fetch_dua():
    response = requests.get(URL).json()

    title = response["data"]["title"]
    category_name = response["data"]["category_info"]["name"]
    category_description = response["data"]["category_info"]["description"]
    arabic = response["data"]["arabic"]
    arabic_english = response["data"]["transliteration"]
    english = response["data"]["translation"]
    source = response["data"]["source"]

    return {
        "title": title,
        "category_name": category_name,
        "category_description": category_description,
        "arabic": arabic,
        "arabic_english": arabic_english,
        "english": english,
        "source": source,
    }


