from flask import Flask, render_template 
app = Flask(__name__)
title='offigne'
menu = ['Установка', 'Первое использование', 'Обратная связь']
@app.route('/')
def index():
    return render_template('index.html', title='variable', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='about flask', menu=menu)

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
