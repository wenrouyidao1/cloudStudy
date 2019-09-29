from django.db import models
from django.utils import timezone
from django.contrib import auth

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    identifier = models.CharField(max_length=40, unique=True)
    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class ArticlePost(models.Model):
    '''
    博客文章数据模型
    文章作者：author，  参数 on_delete 用于指定数据删除的方式
    文章标题：title   字符串
    文章正文：body    文本
    创建时间：created  时间
    更新时间：updated  时间
    '''

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
        verbose_name = '文章'
        verbose_name_plural = '文章'

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title