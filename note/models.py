from django.db import models
from user import models as usermodels
# Create your models here.


class Note(models.Model):
    title = models.CharField('标题',max_length=50,
                             default='')
    content = models.TextField('内容',null=True)
    create_time = models.DateField('创建时间',
                                   auto_now_add=True)
    mod_time = models.DateField('修改时间',
                                auto_now=True)
    author = models.ForeignKey(usermodels.User)  #author是随便起的名字  ,一对多


    def __str__(self):
        return "ID:{},标题:{},内容:{},创建时间:{},修改时间:{}"\
            .format(self.id,self.title,self.content,self.create_time,self.mod_time)