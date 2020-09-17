from flask import Blueprint, request, render_template
from flaskblog.models import Post

main = Blueprint('main', __name__)

# posts = [
#     {
#         'author': 'Micah',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': 'Sept 8, 2020'
#     },
#     {
#         'author': 'Bob',
#         'title': 'Blog Post 2',
#         'content': 'Second Post Content',
#         'date_posted': 'Sept 12, 2020'
#     }
# ]


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5)
    return render_template('home.html', posts=posts, page=page)


@main.route('/about')
def about():
    return render_template('about.html', title='About')