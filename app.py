from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
#@app.route('/about')
def home_page():
    return render_template('home.html')

@app.route('/Theory')
def theory_page():
    return render_template('theory.html')

@app.route('/Quickstart')
def quickstart_page():
    return render_template('quick_start.html')

@app.route('/Download')
def download_page():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)


