from flask import Blueprint, render_template, request
from functions import read_posts_list, search_posts
from config import POST_PATH
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='logger.log', level=logging.INFO)


@main_blueprint.route('/')
def show_index_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    substring = request.args.get('search')
    logging.info('Search in progress')
    all_users_posts = read_posts_list(POST_PATH)
    selected_posts = search_posts(substring, all_users_posts)
    return render_template('post_list.html', posts=selected_posts, substring=substring)

