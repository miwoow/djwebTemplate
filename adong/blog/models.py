#encoding:utf8
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

# Create your models here.

class TagsManager(models.Manager):
    def incr_num(self, ids):
        self.filter(id__in=ids).update(F('counts')+1)

    def decr_num(self, ids, isolate=True):
        self.filter(id__in=ids).update(F('counts')-1)
        if isolate:
            self.filter(id__in=ids, counts__lte=0).delete()

    def decr_num_by_name(self, names, user, isolate=True):
        self.filter(name__in=names, user=user).update(F('counts')-1)
        if isolate:
            self.filter(name__in=names, counts__lte=0).delete()

class Tags(models.Model):
    '''文章标签'''
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, verbose_name=u'用户')
    counts = models.IntegerField(default=1, editable=False, verbose_name=u'文章数')
    objects = TagsManager()

    def __unicode__(self,):
        return self.name

class Post(models.Model):
    '''文章'''
    title = models.CharField(max_length=255, verbose_name=u'标题')
    pub_date = models.DateTimeField(u'发布日期')
    content = models.TextField(u'内容')
    user = models.ForeignKey(User, verbose_name=u'作者')
    tags = models.ManyToManyField(Tags, verbose_name=u'标签')

    def __unicode__(self,):
        return self.title

class Comment(models.Model):
    '''回复'''
    content = models.TextField(u'回复内容')
    name = models.CharField(max_length=32, verbose_name=u'名称')
    home = models.CharField(max_length=256, verbose_name=u'主页')
    post = models.ForeignKey(Post, verbose_name=u'文章')

    def __unicode__(self,):
        return u'For post %s : %s' % (post, content)


