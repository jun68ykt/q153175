from bs4 import BeautifulSoup
import re

pattern = r"privacy policy|個人情報|プライバシーポリシー"

with open('./test.html') as f:
    soup = BeautifulSoup(f.read(), 'lxml')

    for link in soup.findAll('a', text=re.compile(pattern, re.IGNORECASE)):
        print(link['href'])
