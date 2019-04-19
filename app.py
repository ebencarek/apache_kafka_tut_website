from flask import Flask, render_template, url_for, send_file
app = Flask(__name__)

@app.route('/')
#@app.route('/about')
def home_page():
    return render_template('home.html')

@app.route('/Reference')
def reference_page():
    return render_template('reference.html')

@app.route('/Quickstart')
def quickstart_page():
    return render_template('quick_start.html')

@app.route('/Demo')
def demo_page():
    return render_template('demo.html')

@app.route('/Download')
def download_page():
    return render_template('download.html')

@app.route('/download_zookeeper_properties')
def download_zookeeper_properties():
    return send_file("static/zookeeper.properties", attachment_filename="zookeeper.properties", as_attachment=True)

@app.route('/download_server_properties')
def download_server_properties():
    return send_file("static/server.properties", attachment_filename="server.properties", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
