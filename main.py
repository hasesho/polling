import requests
import os
import xml.etree.ElementTree as ET

URL1 = os.environ["URL1"]
URL2 = os.environ["URL2"]

def test(message: str):
    payload = {
        "text": message
    }
    response = requests.post(URL1, json=payload)
    response.raise_for_status()

def is_site_up():

    headers = {
        "Accept": "application/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(URL2, headers=headers, timeout=60)
    if response.status_code == 200:
        xml_data = response.content
        root = ET.fromstring(xml_data)

        for item in root.findall(".//pagination"):
            result = item.find("totalResults").text
            if result == "0":
                return False
            else:
                return True

def main():
    if is_site_up():
        test("hoge")
    else:
        pass

if __name__ == "__main__":
    main()
