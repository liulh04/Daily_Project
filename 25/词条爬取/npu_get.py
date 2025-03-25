
import requests
from bs4 import BeautifulSoup
import urllib

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 百度词条URL
url = 'https://baike.baidu.com/item/%E8%A5%BF%E5%8C%97%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6?sefr=cr'

# 发送GET请求获取页面内容
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 提取词条内容
content = soup.find('div', class_='lemma-summary')
if content is not None:
    content = content.get_text().strip()
    print('词条内容：')
    print(content)
else:
    print('无法找到词条内容')

# 提取词条图片链接
image_div = soup.find('div', class_='summary-pic')
if image_div is not None:
    image_url = image_div.find('img')['src']

    # 下载图片
    urllib.request.urlretrieve(image_url, '词条图片.jpg')
    print('图片已下载')
else:
    print('无法找到词条图片')
