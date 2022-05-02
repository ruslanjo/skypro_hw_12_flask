from flask import Blueprint, render_template, request
from config import POST_PATH, UPLOAD_FOLDER
from functions import add_new_post_to_json, save_picture
from exceptions import ImgUploadError
import logging

logging.basicConfig(filename='logger.log', level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def upload_new_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_new_post():
    try:
        picture = request.files.get('picture')
    except ImgUploadError('Не получилось загрузить изображение'):
        logging.error('Image was not uploaded')
    else:
        content = request.form.get('content')
        if not content or not picture:
            return f'Загрузите и картинку, и текст <a href="/post"> Назад к загрузке</a>'
        else:

            picture_path = f'{UPLOAD_FOLDER}/{picture.filename}'
            save_picture(picture)
            new_post = {'pic': picture_path, 'content': content}
            add_new_post_to_json(POST_PATH, new_post)
            return render_template('post_uploaded.html', new_post=new_post)
