from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = ''

posts = [
    {
        'author': 'Micah',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Sept 8, 2020'
    },
    {
        'author': 'Bob',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Sept 12, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=posts, title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)