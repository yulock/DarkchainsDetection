from flask import Flask, render_template, request
from modules import Detection
from modules.Detection import findDarkchain

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    with open('rules.txt', 'r', encoding='utf-8') as f:
        re_rules_list = f.read().split('\n')

    if request.method == 'POST':
        url = request.form['url']
        host = findDarkchain(url, re_rules_list)[0]
        if not host:
            return render_template('index.html', url=url, rules=findDarkchain(url, re_rules_list)[1])
        else:
            return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
