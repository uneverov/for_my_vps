from flask import Flask, render_template, send_file
import os
app = Flask(__name__)


@app.route('/')
def page_1():
    return render_template('page_1.html')


@app.route('/download_gpal')
def download_gpal():
    path = f"{os.getcwd()}{os.sep}gpal.rar"
    return send_file(path, as_attachment=True)


@app.route('/download_game_1')
def download_game_1():
    path = f"{os.getcwd()}{os.sep}catch_a_square.rar"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
