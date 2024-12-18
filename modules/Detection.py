import requests, re, urllib3, html, threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def findDarkchain(url, re_rules_list):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    try:
        req = requests.get(url, headers=headers, timeout=10).text
        res = html.unescape(req)
        rules = []
        host = True
        for re_rules in re_rules_list:
            match = re.findall(r'{}'.format(re_rules), res, re.S | re.I)
            if match != []:
                rules.append(re_rules)
                host = False
        return host, rules
    except:
        return False
