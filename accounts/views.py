from django.shortcuts import render_to_response, redirect, RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login


def login_user(request):
    errors = []
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home'))
            else:
                errors.append({'inactive': "Your account has been disabled"})
        else:
            errors.append({'invalid': "The username and password you have entered do not match our records"})
    return render_to_response("login.html", {'errors': errors}, RequestContext(request))
