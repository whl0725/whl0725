from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User


'''    用户注册'''
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            return HttpResponse("已有这个账号,请重新注册")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        auth.login(request, user)
        return redirect('web:Home')
    return render(request, 'registration.html')


'''用户登录'''
def login(request):
    user = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("这个账号不存在或账号密码错误")
    if user:
        auth.login(request, user)
        return redirect('web:Home')

    return render(request, "login.html")



'''用户登出'''
def logout(request):
    auth.logout(request)
    return redirect('web:Home')
