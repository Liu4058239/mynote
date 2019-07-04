from django.conf.urls import url
from . import  views


urlpatterns = [
    #查看个人笔记
    url(r'^$', views.homepage),
    url(r'^new$', views.new_note), #新建笔记
    url(r'^showall$', views.showall),  #查看本人的全部笔记
    url(r'^mod/(\d+)$', views.mod_note_info), #修改笔记
    url(r'^del/(\d+)$', views.del_note), #删除笔记
    url(r'^notes', views.notes_page, name='note')
]
