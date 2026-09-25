import requests

URL = "https://ummahapi.com/api/hadith/random?collection=bukhari"


def fetch_hadith():
    response = requests.get(URL).json()

    def clean_text(text):
        return (
            text.replace('\\"', '"').replace('"', "").replace("\\", "").replace("`", "")
        )

    english = clean_text(response["data"]["english"])
    arabic = response["data"]["arabic"]
    collection_name = response["data"]["collection_name"]
    hadithnumber = response["data"]["hadithnumber"]
    return {
        "english": english,
        "arabic": arabic,
        "collection_name": collection_name,
        "hadithnumber": hadithnumber,
    }
