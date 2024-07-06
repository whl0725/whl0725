from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField

# 这里是文章的数据库
class titlies(models.Model):
    # 文章的数据库
    text = models.TextField()
    # 标题的数据库
    title = models.CharField(max_length=100)
    # 副标题的数据库
    subtitle = models.CharField(max_length=1024, default='', null=True)

    class Meta:
        db_table = 'whl_Article'
        verbose_name = '我的文章'

    def __str__(self):
        return self.title



# 这里是个人中心的数据库
class Personal(models.Model):

     #文章的数据库
    text = models.TextField()
    # 标题的数据库
    title = models.CharField(max_length=100)
    # 副标题的数据库
    subtitle = models.CharField(max_length=1024, default='')
    # 浏览量的数据库
    Clicks = models.PositiveIntegerField(default=0)
    # 有必要记录一下我写个人中心的时间
    created = models.DateTimeField(default=timezone.now)

    # 图片
    image = ProcessedImageField(
        upload_to='static/images/',
        blank=True,
    )
    ppp = ProcessedImageField(
        upload_to='static/images/',
        blank=True,
    )
    lll = ProcessedImageField(
        upload_to='static/images/',
        blank=True,
    )

    class Meta:
       db_table = 'whl_PersonalCenter'
       verbose_name = '我个人中心的文章'

    def __str__(self):
       return self.title

    def increase_views(self):
        self.Clicks += 1
        self.save(update_fields=['Clicks'])

class Www(models.Model):
    name = models.CharField(max_length=10)
    comments=models.TextField()
    created = models.DateTimeField(default=timezone.now)
    password=models.CharField(max_length=100)
    It = models.IntegerField()

    class Meta:
        verbose_name = '评论'

    def __str__(self):
        return self.comments


class information(models.Model):
    content =  models.TextField()
    it = models.IntegerField()

    class Meta:
        verbose_name='资料'

    def __str__(self):
        return self.content