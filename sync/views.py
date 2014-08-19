import json
from hashlib import md5

from django.shortcuts import render, render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required
from sync.models import Hash
from tasks.models import Task

@login_required
def poll(request):
    """
    The application will check to see if its hash is the same as the hash on the server and update accordingly
    """
    if request.method == "GET":
        try:
            hash = Hash.objects.filter(account=request.user).order_by('-timestamp')[0]
        except Exception as ex:
            print ex
            hash = ""
        return HttpResponse(status=200, content_type='application/json', content=json.dumps({'hash': hash}))
    else:
        return HttpResponse(status=403)

@login_required
def sync(request):
    """
    Takes the post of the json object, and syncs according to last date_modified per UUID
    """
    if request.method == "POST":
        tasks = json.loads(request.POST['tasks'])
        for task in tasks:
            old = Task.objects.get(account=request.user, key=task['uuid'])
            if old['date_modified'] < task['timestamp']:
                old.title = task.title
                old.completed = task.completed
                old.save()
        hash = md5(str(dict((t.key, t.date_modified) for t in Task.objects.filter(account=request.user))))
        updated = Hash.objects.create(
            account=request.user,
            hash = hash
        )
        updated.save()
        return HttpResponse(status=201, content_type="application/json", content=render(request, 'tasks.json', {'tasks':tasks}))
    else:
        return HttpResponse(status=403)