from flask import Flask, render_template, request, redirect
from get_label_from_url import get_label_from_url

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/first')
# def first_page():
#     return render_template('first_page.html')

@app.route('/first', methods=['POST'])
def calculate():
    if request.method == 'POST':
        url = request.form['query']
        label = get_label_from_url(url)

        return render_template('first_page.html', result = label)

if __name__ == '__main__':
    app.run(debug=True)
