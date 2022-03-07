import feedparser
import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

rss_url = 'https://nv.ua/rss/2283.xml'
published_articles_filename = './parser/nv/published_articles'

def mark_processed(entry):
    with open(published_articles_filename, 'a') as f:
        f.write(entry['id'] + '\n')
        f.close()

def publish_page(data):
    template_env = Environment(loader=FileSystemLoader(searchpath='./parser/nv/templates/'))
    template = template_env.get_template('article_template.md')
    rendered_article = template.render(
        title=data['title'],
        article_date=data['published_date'],
        media_name='Новое Время',
        article_url=data['url'],
        paragraphs=data['paragraphs'],
    )

    filename = './site/content/posts/{0}.md'.format(data['title'][:30])
    with open(filename, 'w') as f:
        f.write(rendered_article)
        f.close()

def parse_nv_page(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
    content = soup.find('div', {'class': 'article-content-body'}).find('div', {'class': 'content_wrapper'})
    paragraphs = content.find_all('p', recursive=False)
    paragraphs_text = map(lambda p: p.text, paragraphs)

    title_img_block = content.find('div', {'class': 'article__content__head_img'})
    title_img = title_img_block.find('img') if title_img_block is not None else None

    return {
        'paragraphs': list(paragraphs_text),
        'title_image': title_img.attrs['src'] if title_img is not None else None,
    }

def parse_entry(entry):
    page_data = parse_nv_page(entry['link'])
    return {
        'id': entry['id'],
        'title': entry['title'],
        'summary': entry['summary'],
        'paragraphs': page_data['paragraphs'],
        'title_image': page_data['title_image'],
        'published_date': entry['published'],
        'url': entry['link'],
    }

def is_processed(entry):
    result = False
    with open(published_articles_filename, 'r') as f:
        ids = f.readlines()
        result = any(map(lambda id: id[:-1] == entry['id'], ids))
        f.close()

    return result

def update_news(url):
    feed = feedparser.parse(url)

    for entry in feed['entries']:
        if is_processed(entry):
            print('Page skipped {0}'.format(entry['id']))
            continue
        page_data = parse_entry(entry)
        publish_page(page_data)
        mark_processed(entry)

        print('Page generated {0}'.format(entry['id']))

if __name__ == '__main__':
    update_news(rss_url)
