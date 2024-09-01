import requests
import os
from bs4 import BeautifulSoup

response  =requests.get("https://blog.education.nationalgeographic.org/2024/04/19/alex-schnell/")
file_path = os.path.join(os.getcwd(),'docs.txt')

try:
    if not os.path.exists(file_path):
        with open(file_path,'w') as file:
            print("file created succesfully")
    else:
        print("already existed")

except Exception as e:
    print(f'an error occured: {e}')


soup = BeautifulSoup(response.text,'html.parser')
try:
    if response.status_code == 200:
        with open(file_path,'w') as file:
            title = soup.find('h1', class_ = 'entry-title')
            file.write(title.string)
            
            entry_content = soup.find('div', class_='entry-content')
            paragraphs = entry_content.find_all('p')

            if(len(paragraphs) > 1):
                for p in paragraphs:
                    txt = p.get_text(strip = True) + '\n'
                    file.write(txt)

            print("file changed successfully")
    else:
        print(f"status code: {response.status_code}")

except Exception as e:
    print(f"error : {e}")

