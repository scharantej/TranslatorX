
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_translation', methods=['POST'])
def get_translation():
    text = request.form.get('text')
    src_lang = request.form.get('src_lang')
    tgt_lang = request.form.get('tgt_lang')
    translated_text = translate(text, src_lang, tgt_lang)
    return translated_text

@app.route('/replace_text', methods=['POST'])
def replace_text():
    translated_text = request.form.get('translated_text')
    element_id = request.form.get('element_id')
    replace_slide_text(element_id, translated_text)
    return "Success"

@app.route('/open_sidebar', methods=['POST'])
def open_sidebar():
    open_sidebar_script()
    return "Sidebar opened"

@app.route('/options')
def options():
    return render_template('options.html')

if __name__ == '__main__':
    app.run()
