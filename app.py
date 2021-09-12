from werkzeug.exceptions import RequestURITooLarge
from server import find_all_products_data, find_product_data
from db_manager import save_to_db
from flask import Flask, url_for, request, redirect, render_template
import os
from talk import add_comment_to_db, get_all_posts

app = Flask(__name__)
key = os.environ.get('KEY')
app.config['SECRET_KEY'] = key

@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/api/find-all/<string:product>', methods=['GET'])
def api_find_all(product):
    product_to_search = product.replace(' ', '-')

    return find_all_products_data(product_to_search)

@app.route('/api/find/<string:product2>', methods=['GET'])
def api_find_product(product2):
    product_to_search2 = product2.replace(' ', '-')

    return find_product_data(product_to_search2)

@app.route('/search', methods=['GET', 'POST'])
def api_search():
    try:
        if request.method == 'POST':
            p = request.form['proc']

            return redirect(f'/api/find-all/{p}')
        else:
            return redirect('/error')
    except:
        return redirect('/error')

@app.route('/api/save/<string:product>/<int:p_id>/<string:email>/<string:email_provider>', methods=['GET', 'POST'])
def save_product(product, p_id, email, email_provider):
    return save_to_db(product, p_id, email, email_provider)

@app.route('/talk', methods=['GET', 'POST'])
def talk():
    if request.method == 'POST':
        p_content = request.form['txt']
        author = request.form['op']
        add_comment_to_db(author, p_content)
        posts = get_all_posts()

        return render_template(
            'talk.html',
            posts = posts
        )
    else:
        return redirect('/error')

if __name__ == '__main__':
    app.run(debug=True)