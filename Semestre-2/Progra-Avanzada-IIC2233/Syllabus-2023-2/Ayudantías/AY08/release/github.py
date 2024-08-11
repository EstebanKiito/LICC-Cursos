import json, requests

github_repo = ''
token = ""

body = {
    # Completar con lo que quieran!
    'title': "",
    'body': ""
}

my_headers = {
    'Authorization': 'token ' + token,
    'Accept': 'application/vnd.github.v3+json'
}

url = f"https://api.github.com/repos/IIC2233/{github_repo}/issues"

response = requests.post(url, data=json.dumps(body), headers=my_headers)
print(response.status_code)