from . import views
from django.urls import path, re_path

urlpatterns=[
    # 封面路由
    path('',views.cover,name='cover'),
    #首页的路由
    path('Home',views.Home,name='Home'),
    #个人中心路由
    path('personal/',views.personal,name='personal'),
    #关于本站路由
    path('site/',views.site,name='site'),
    #
    #path('article/',views.article,name='article'),

    #re_path(r'^diary/(\d*)', views.article, name='article'),
    #搜索功能的路由
    re_path('search/',views.search,name='search'),
    #空间的路由
    re_path(r'^kongjian/(\d*)',views.kongjian,name='kongjian'),
    #评论的增加路由
    re_path(r'^add/(\d*)', views.add, name='add'),
    #评论的删除路由
    re_path(r'^delete/(\d*)/(\w*)', views.delete, name='delete'),
]