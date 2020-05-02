import json

def get_text_about_uk():
    with open("..\data\jawiki-country.json", mode="r", encoding="utf-8", errors='ignore') as f:
        for line in f.readlines():
            data = json.loads(line)

            if "イギリス" in data["text"]:
                yield data


if __name__ == "__main__":
    for data in get_text_about_uk():
        for line in data["text"].split("\n"):
            if "カテゴリ:" in line:
                print(line)