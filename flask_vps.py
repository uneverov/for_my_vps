from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def page_1():
    return render_template('page_1.html')


@app.route('/download_gpal')
def download_gpal():
    path = r"C:\Users\Uneverov\PycharmProjects\for_my_vps\gpal.rar"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='194.58.107.248', port=5000)
