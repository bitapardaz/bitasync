from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.http import HttpResponse


def login(request):
        c = {}
        c.update(csrf(request))
        template = loader.get_template('user_profile/login.html')
        context = RequestContext(request, c)
        return HttpResponse(template.render(context))


def logout(request):
    auth.logout(request)
    template = loader.get_template('user_profile/loggedout.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def auth_view(request):
    # this view only performs an action based on the authentication form.
    # therefore, it does not need a template
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    template = loader.get_template('user_profile/loggedin.html')
    name = request.user.username
    context = RequestContext(request, {'fullname': name})
    return HttpResponse(template.render(context))


def invalid(request):
    template = loader.get_template('user_profile/invalid.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
