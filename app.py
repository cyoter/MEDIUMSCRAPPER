import json
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)


def parse_medium_article(html):
    soup = BeautifulSoup(html, 'html.parser')

    script = soup.select_one('script[type="application/ld+json"]')
    data = json.loads(script.text)

    article = {}
    article['id'] = data.get('identifier')
    article['title'] = data.get('name')

    subtitle = re.findall('subtitle":"(.*?)",', html)
    article['subtitle'] = subtitle[0] if subtitle else ''

    article['published_date'] = data.get('datePublished')
    article['modified_date'] = data.get('dateModified')
    article['reading_time'] = soup.select_one('meta[name="twitter:data1"]').get('value')
    article['image'] = soup.select('img[role="presentation"]')[2].get('src')
    article['url'] = data.get('url')
    article['description'] = data.get('description')
    article['author'] = data.get('author', {}).get('name')
    article['author_url'] = data.get('author', {}).get('url')
    article['publisher'] = data.get('publisher', {}).get('name')
    article['publisher_url'] = data.get('publisher', {}).get('url')
    article['keywords'] = [keyword.replace('Tag:', '') for keyword in data.get('keywords', []) if
                           keyword.startswith('Tag:')]

    claps = re.findall('totalClapCount":(\d+)', html)
    if claps:
        article['claps'] = claps[0]
    return article


# in localhost 127.0.0.1:5000/medium?url=PASTE YOUR URL HERE
@app.route('/medium')
def medium():
    url = request.args.get('url')
    if not url:
        return jsonify({'Status': 'Error', 'Message': 'Please supply a valid medium article\'s url'})

    try:
        response = requests.get(url)
    except Exception as e:
        return jsonify({'Status': 'Error', 'Message': str(e)})

    if response.ok:
        article = parse_medium_article(response.text)
    else:
        article = {'Status': response.status_code, 'Message Type': 'Error'}
    return jsonify(article)


@app.route('/')
def index():
    url = urljoin(request.url_root,
                  "medium?url=PASTE YOUR URL HERE")
    return jsonify({
        'message': f'To use the API goto {url}'
    })


if __name__ == '__main__':
    app.run(debug=True)
