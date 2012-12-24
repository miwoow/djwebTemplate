#encoding:utf8
from django import forms
from django.utils.translation import ugettext as _

class RegisterForm(forms.Form):
    username = forms.CharField(label=_(u'用户名'))
    first_name = forms.CharField(label=_(u'真实姓名'))
    password = forms.CharField(label=_(u'密码'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u'密码确认'), widget=forms.PasswordInput)
    email = forms.EmailField(label=_(u'邮箱'))

class SelfInfoForm(forms.Form):
    first_name = forms.CharField(label=_(u'真实姓名'))
    email = forms.EmailField(label=_(u'邮箱'))

