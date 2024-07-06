from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse


from .models import *

# 封面
def cover(request):
    return render(request, 'cover.html',)

# 首页
def Home(request):
    article_list = titlies.objects.all().order_by("id")
    # 实例化paginator对象，一页显示4篇文章
    paginator = Paginator(article_list, 4)
    # 获取url中的页面
    page = request.GET.get('page')
    # 返回第 page 页
    articles = paginator.get_page(page)
    name = request.user.username
    zl = information.objects.filter(it=1)
    www = 0
    hot = 0
    personals = Personal.objects.all()
    for i in personals:
        if (i.Clicks > www):
            hot = i.id
            www = i.Clicks
    c = Personal.objects.filter(id=hot)
    return render(request, 'Home.html', locals())

# 个人空间
def personal(request):
    article_list = Personal.objects.all().order_by("id")
    # 实例化paginator对象，一页显示4篇文章
    paginator = Paginator(article_list, 3)
    # 获取url中的页面
    page = request.GET.get('page')
    # 返回第 page 页
    articles = paginator.get_page(page)
    name = request.user.username
    zl = information.objects.filter(it=1)
    www = 0
    hot = 0
    personals = Personal.objects.all()
    for i in personals:
        if (i.Clicks > www):
            hot = i.id
            www = i.Clicks
    c = Personal.objects.filter(id=hot)
    return render(request, 'Personal.html', locals())

# 关于本站
def site(request):
    name = request.user.username
    zl = information.objects.filter(it=1)
    www = 0
    hot = 0
    personals = Personal.objects.all()
    for i in personals:
        if (i.Clicks > www):
            hot = i.id
            www = i.Clicks
    c = Personal.objects.filter(id=hot)
    return render(request, 'site.html',locals())

def search(request):
    tag = request.GET.get('search')
    search = request.POST.get('s')
    if search:
        aee = Personal.objects.filter(
            Q(title=search) |
            Q(subtitle=search)
        ).order_by("id")
    if tag:
        aee = Personal.objects.filter(
            Q(title=tag) |
            Q(subtitle=tag)
        ).order_by("id")
    paginator = Paginator(aee, 3)
    # 获取url中的页面
    page = request.GET.get('page')
    # 返回第 page 页
    articles = paginator.get_page(page)
    zl = information.objects.filter(it=1)
    www = 0
    hot = 0
    personals = Personal.objects.all()
    for i in personals:
        if (i.Clicks > www):
            hot = i.id
            www = i.Clicks
    c = Personal.objects.filter(id=hot)
    name = request.user.username
    if not search:
        search=tag
    return render(request, 'search.html', locals())

#这是用来具体展示个人中心的文章
def kongjian(request, aid):
    art = Personal.objects.get(id=aid)
    comment_list = Www.objects.filter(It=aid).order_by("-id")
    paginator = Paginator(comment_list, 3)
    page = request.GET.get('page')
    comment_list = paginator.get_page(page)
    art = Personal.objects.get(id=aid)
    art.increase_views()
    name = request.user.username
    return render(request, 'kongjian.html', locals())

@login_required(login_url='user:login')
def add(request,aid):
    if request.method == 'GET':
        aid=aid
        return render(request, 'add.html',locals())
    comments = request.POST.get('comments')
    name=request.user
    password=request.user.password
    it=aid
    Www.objects.create(name=name, comments=comments,password=password,It=it)
    return redirect('web:kongjian',it)

@login_required(login_url='user:login')
def delete(request,aid,id):
    name = request.user
    password = request.user.password
    sum=Www.objects.filter(name=name,password=password)
    id=id
    if sum:
        whl=Www.objects.filter(id=aid).delete()
        return redirect('web:kongjian', id)
    else:
        return HttpResponse("您只能删除自己的评论")
