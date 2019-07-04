from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('用户名', max_length=50,
                            unique=True)
    password = models.CharField('密码', max_length=30)
    email =models.EmailField('邮箱',max_length=50,
                             default='963217296@qq.com')

    # role = models.IntegerField('角色') #1校长,2学生
    def __str__(self):
        return '用户:{}'.format(self.name)