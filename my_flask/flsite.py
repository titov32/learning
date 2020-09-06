from flask import Flask, render_template, url_for, request 

app = Flask(__name__)
title='offigne'
menu = [{'name': 'Установка', 'url': 'install-flask'},
        {'name': 'Первое использование', 'url': "first-app"},
        {"name": 'Обратная связь', 'url': 'contact'}]
@app.route('/')
def index():
    return render_template('index.html', title='variable', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='about flask', menu=menu)

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        print(request.form)
    if request.method == 'GET':
        print('Work Method GET', request.form)
    return render_template('contact.html', title='Обратная связь', menu = menu)

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
