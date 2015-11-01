from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.http import HttpResponse

def login(request):
        c = {}
        c.update(csrf(request))
        #return render_to_response('login.html', c)

        template = loader.get_template('user_profile/login.html')
        context = RequestContext(request, c)
        return HttpResponse(template.render(context))
 def auth_view(request):
     username = request.POST.get('username','')
     password = request.POST.get('password','')

     
