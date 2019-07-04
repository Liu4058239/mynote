from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import Http404
from django.http import HttpResponseRedirect
from user.models import User
import random
# Create your views here.

def homepage(request):
    return render(request, 'note_index.html')

def showall(request):
    '''
    显示笔记信息
    :param request:
    :return:
    '''
    if hasattr(request,'session') and 'userinfo' in request.session:
        #此时用户已经登录
        #拿到用户id
        user_id = request.session['userinfo']['id']
        #根据当前登录用户找到当前用户
        user = User.objects.get(id=user_id)
        #根据当前用户筛选出当前用户的笔记
        notes = models.Note.objects.filter(author=user)
        return render(request,'showall.html',locals())
    else:
        raise Http404

def new_note(request):
    '''
    新建笔记信息
    :param request:
    :return:
    '''
    if hasattr(request, 'session') and 'userinfo' in request.session:
        # 此时用户已经登录
        # 拿到用户id
        user_id = request.session['userinfo']['id']
        # 根据当前登录用户找到当前用户
        user = User.objects.get(id=user_id)
        # 根据当前用户筛选出当前用户的笔记
        # notes = models.Note.objects.filter(author=user)
        anote = models.Note(author=user)
        anote.title = '自定义当前用户的标题%d' \
                      % random.randrange(10000)
        anote.content = '这是随便写的内容'
        anote.save()
        return HttpResponse('<a href="/note">添加笔记成功，点我跳转到首页</a>')
    else:
        raise Http404

def mod_note_info(request, note_id):
    # 先根据note_id 找到对应的一本书
    # 　权限管理
    if 'userinfo' not in request.session:
        # 如果没登录，则抛出404异常
        raise Http404

    try:
        anote = models.Note.objects.get(id=note_id)
    except:
        return HttpResponse("没有找到ID为" + note_id + "的笔记信息")

    if request.method == 'GET':
        return render(request, "mod_note.html", locals())
    elif request.method == 'POST':
        try:
            content = request.POST.get('content', '')
            anote.content = content
            anote.save()  # 提交修改
            return HttpResponse("修改笔记内容成功")
        except:
            return HttpResponse("修改笔记内容失败")

# 改入 HttpResponseRedirect模块用于 重定向url
def del_note(request, id):
    '''
    删除笔记
    :param request:
    :param book_id:
    :return:
    '''
    # 权限管理
    if hasattr(request,'session') and 'userinfo' in request.session:
        #此时用户已经登录
        #拿到用户id
        user_id = request.session['userinfo']['id']
        #根据当前登录用户找到当前用户
        user = User.objects.get(id=user_id)
        try:
            #用户是当前用户,并且ID正确才可以删除掉!
            anote = models.Note.objects.get(author=user,id=id)
            anote.delete()
            return HttpResponseRedirect('/note/showall')
        except:
            return HttpResponse("删除失败")
    else:
        raise Http404

from django.core.paginator import Paginator
def notes_page(request):
    '''
    分页显示当前的书籍
    :param request:
    :return:
    '''
    books = models.Note.objects.all()
    paginator = Paginator(books, 5)
    print(paginator.page_range)
    cur_page = request.GET.get('page', '1')
    page = paginator.page(cur_page)
    return render(request, 'book.html', locals())