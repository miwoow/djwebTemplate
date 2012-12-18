#encoding:utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(req):
    '''首页'''
    return render_to_response('homepage/index.html', context_instance=RequestContext(req))

def help(req):
    '''帮助'''
    return render_to_response('homepage/help.html', )

@login_required
def profile(req):
    return render_to_response('homepage/profile.html', context_instance=RequestContext(req))

@login_required
def changepwd(req):
    if req.method == 'POST':
        return render_to_response('homepage/profile.html', context_instance=RequestContext(req))
    else:
        return render_to_response('homepage/changepwd.html', context_instance=RequestContext(req))

