'''models.py的功能主要為處理資料庫與網頁間的存取關係
'''
from django.db import models

# Create your models here.
class Name(models.Model):
    姓名 = models.CharField(max_length=200)
    手機號碼 = models.CharField(max_length=10)
    我想兌換的東西 = models.TextField()
    def __str__(self):
        return self.姓名
