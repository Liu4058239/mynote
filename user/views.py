from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import  models
# Create your views here.

def mylogin(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        #获取表单的数据
        remember = request.POST.get('remember')
        password = request.POST.get('password')
        username = request.POST.get('username')

        #验证用户名，密码是否正确
        try:
            user = models.User.objects.get(name=username,
                                    password=password)
            #在当前连接的session中记录当前用户的信息
            request.session['userinfo'] = {
                'username':user.name,
                'id':user.id
            }
            return HttpResponseRedirect('/') #登录成功后返回首页
        except:
            return HttpResponse('登录失败')



def myregister(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        if username == '':
            username_error = "用户名不能为空"
            return render(request, 'register.html', locals())
        if password == '':
            password_error1 = '密码不能为空'
            return render(request, 'register.html', locals())
        if password != password2:
            password_error2 = '两次密码不一致'
            return render(request, 'register.html', locals())
        # return HttpResponse('注册成功')

        #开始注册功能
        try:
            from . import models
            user = models.User.objects.create(name=username,
                                              password=password)
            return HttpResponse('注册成功')
        except:
            return HttpResponse('注册失败')

def mylogout(request):
    '''
    注销 退出登录
    :param request:
    :return:
    '''
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect("/") #注销后跳转到主页
