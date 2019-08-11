from django.contrib import admin
from googleform.models import Name

# Register your models here.
'''請記得在此處import並register 你的model
django預設的admin page才看的到model內容
'''
admin.site.register(Name)
