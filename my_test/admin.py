from django.contrib import admin
from .models import MyTest, Vote
from django.contrib import admin

class TestAdmin(admin.ModelAdmin):

    list_display = ("id","question", "my_test")

admin.site.register(MyTest)
admin.site.register(Vote,TestAdmin)

