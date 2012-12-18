#encoding:utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def index(req):
    '''首页'''
    return render_to_response('blog/index.html', context_instance = RequestContext(req))
