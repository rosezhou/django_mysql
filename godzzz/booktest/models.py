from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub = models.DateField()

    def __str__(self):
        return '%s''%s'% (self.btitle,self.bpub)


class HreoInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.TextField()
    hBook = models.ForeignKey('BookInfo')
    def __str__(self):
        return '%s' % self.hname

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    gender.short_description = '性别'