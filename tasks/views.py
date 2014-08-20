from django.shortcuts import  render_to_response, RequestContext
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return render_to_response('angular.html', {}, RequestContext(request))