from flask import Blueprint, render_template, request
from config import POST_PATH, UPLOAD_FOLDER
from functions import add_new_post_to_json

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def upload_new_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_new_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture and not content:
        return 'Загрузите и картинку, и текст'
    else:
        picture_path = f'{UPLOAD_FOLDER}/{picture.filename}'
        picture.save(picture_path)
        new_post = {'pic': picture_path, 'content': content}
        add_new_post_to_json(POST_PATH, new_post)
        return render_template('post_uploaded.html')
