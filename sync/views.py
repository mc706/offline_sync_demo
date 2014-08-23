import json
from hashlib import md5

from django.shortcuts import render, render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required(login_url='/login/')
def sync(request):
    """
    Takes the post of the json object, and syncs according to last date_modified per UUID
    """
    if request.method == "POST":
        tasks = json.loads(request.body.decode('utf-8'))
        for task in tasks:
            try:
                old = Task.objects.get(account=request.user, key=task['uuid'])
                if int(old.date_modified) < int(task['timestamp']):
                    old.title = task['title']
                    old.completed = task['completed']
                    old.date_modified = int(task['timestamp'])
                    old.deleted = task['deleted']
                    old.save()
                    if old.deleted:
                        old.deleted()
            except Exception as ex:
                print ex
                try:
                    if task['uuid'] != "":
                        Task.objects.create(
                            account=request.user,
                            key=task['uuid'],
                            title=task['title'],
                            date_modified=task['timestamp']
                        ).save()
                except Exception as inner:
                    print inner
        updated_tasks = Task.objects.filter(account=request.user)
        print updated_tasks
        deleted = [task.key for task in Task.objects.filter(account=request.user, deleted=True)]
        return HttpResponse(status=201, content_type="application/json",
                            content=render(request, 'response.json', {'tasks': updated_tasks, 'deleted': deleted}))
    else:
        return HttpResponse(status=403)