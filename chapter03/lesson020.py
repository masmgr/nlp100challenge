import json

if __name__ == "__main__":
    with open("..\data\jawiki-country.json", mode="r", encoding="utf-8", errors='ignore') as f:
        for line in f.readlines():
            data = json.loads(line)

            if "イギリス" in data["text"]:
                print(data["text"])
