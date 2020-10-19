# hello.py

import json

from github3 import login

@csrf_exempt
def post_list(request):
    jsondata = request.body
    print(jsondata)

    d = json.loads(jsondata)
    state = d['action']
    issues = d['issue']

    title = issues['title']
    body = issues['body']
    label = issues['labels']
    number = issues['number']
    
    print(body)
