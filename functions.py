import json
import logging
from config import UPLOAD_FOLDER
from exceptions import ImgTypeError


def read_posts_list(path):
    try:
        with open(path, 'r', encoding='utf-8') as json_posts:
            users_posts = json.load(json_posts)
        return users_posts
    except json.JSONDecodeError:
        return 'Файл не удаётся преобразовать'
    except FileNotFoundError:
        return 'Файл не найден'


def search_posts(substring, posts_list):
    selected_posts = []
    for post in posts_list:
        if substring.lower() in post.get('content').lower():
            selected_posts.append(post)
    return selected_posts


def add_new_post_to_json(json_file_path, new_post):
    posts = read_posts_list(json_file_path)
    posts.append(new_post)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(posts, json_file, ensure_ascii=False, indent=4)


def save_picture(picture):
    allowed_type = ['png', 'jpg', 'jpeg']
    picture_type = picture.filename.split('.')[-1]
    if picture_type not in allowed_type:
        logging.info('Uploaded file is not an image')
        raise ImgTypeError(f'Неверный формат файла. Допустимы только {", ".join(allowed_type)}')
    picture_path = f'{UPLOAD_FOLDER}/{picture.filename}'
    picture.save(picture_path)

