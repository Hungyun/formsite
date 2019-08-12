'''models.py的功能主要為處理資料庫與網頁間的存取關係
'''
from django.db import models
from django.utils import timezone

# Create your models here.
class Name(models.Model):
    姓名 = models.CharField(max_length=200)
    手機號碼 = models.CharField(max_length=10)
    numberchoices = [('1','1(5張發票)'),('2','2(10張發票)'),('3','3(30張發票)'),('4','4(40張發票)'),('5','5(50張發票)')]
    我要幾台iphone = models.CharField(max_length=10,choices=numberchoices)

    我想兌換的東西 = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return (self.姓名, self.created_date)
