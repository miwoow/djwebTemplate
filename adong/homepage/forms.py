#encoding:utf8
from django import forms
from django.utils.translation import ugettext as _

class RegisterForm(forms.Form):
    username = forms.CharField(label=_(u'用户名'))
    password = forms.CharField(label=_(u'密码'))
    password2 = forms.CharField(label=_(u'密码确认'))
    email = forms.EmailField(label=_(u'邮箱地址'))
