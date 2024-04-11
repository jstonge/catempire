import requests
import json
import random
import re

def get_annotations():
    url = "https://app.heartex.com/api/projects/59149/export?exportType=JSON"
    headers = { "Authorization": f"Token d096de230cae0ff545503d3305a386b3bbd84e6f" }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        json_data = [_ for _ in json_data if len(_['annotations']) > 0]
        
        out = []
        for obj in json_data:
            for annot in obj['annotations'][0]['result']:
                if annot['value']['labels'][0] == 'Course':
                    course = annot['value']['text']
                    course = course.replace("-\\n", "").replace("\\n", " ")
                    # Remove or replace various non-printable characters, including '\xad'
                    course = re.sub(r'[^\x20-\x7E\n\r\t]', '', course)
                    # Replace multiple spaces (including tabs and newlines) with a single space
                    course = re.sub(r'\s+', ' ', course)
                    out.append(course)

        random.shuffle(out)

        with open("courses.txt", "w") as fout:
            [fout.write(f"{c}\n") for c in out]
        
        full_page = json_data[0]['data']['text']

        with open("single_full_page.txt", "w") as fout:
            fout.write(full_page)

if __name__ == "__main__":
    get_annotations()
