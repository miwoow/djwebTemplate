#encoding:utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from homepage.forms import RegisterForm,SelfInfoForm

def index(req):
    '''首页'''
    form = RegisterForm()
    return render_to_response('homepage/index.html', {'form':form}, context_instance=RequestContext(req))

@login_required
def profile(req):
    '''我的资料'''
    if req.method == "POST":
        form = SelfInfoForm(req.POST)
        
    else:
        form = SelfInfoForm({'first_name':req.user.first_name, 'email':req.user.email})
    return render_to_response('homepage/profile.html',{'form':form},  context_instance=RequestContext(req))

@login_required
def changepwd(req):
    '''修改密码'''
    if req.method == 'POST':

        return HttpResponseRedirect('/info/'+_(u'修改成功！'))
        #return render_to_response('homepage/profile.html', context_instance=RequestContext(req))
    else:
        return render_to_response('homepage/changepwd.html', context_instance=RequestContext(req))


def info(req, msg):
    '''提示信息'''
    return render_to_response('homepage/info.html', {'msg':msg}, context_instance=RequestContext(req))
        
def signup(req):
    ''' 注册'''
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            '''保存用户'''

            return HttpResponseRedirect('/info/'+_(u'注册成功，请登录。'))
        else:
            '''用户数据有错误'''
            return render_to_response('homepage/signup.html', {'form': form}, context_instance=RequestContext(req))
    else:
        form = RegisterForm() 
        return render_to_response('homepage/signup.html', {'form': form}, context_instance=RequestContext(req))
