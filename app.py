from flask import Flask, render_template, request, jsonify
from modules import Detection
from modules.Detection import findDarkchain

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url_result = None
    re_result = None
    with open('rules.txt', 'r', encoding='utf-8') as f:
        re_rules_list = f.read().split('\n')

    if request.method == 'POST':
        urls = request.form.get('urls')
        if urls:
            url_list = [url.strip() for url in urls.split("\n") if url.strip()]
            dark_url = []
            re_rules = []
            for url in url_list:
                dc = findDarkchain(url, re_rules_list)
                host = dc[0]
                rules = dc[1]
                if not host:
                    dark_url.append(url)
                    re_rules.append(rules)
            url_result = dark_url
            re_result = re_rules
        return render_template('index.html', urls=url_result, rules=re_result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
