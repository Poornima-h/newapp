from django.contrib import admin

# Register your models here.
from .models import Post ,Book,Employee,salary,author,novel,member,club

class BookAdmin(admin.ModelAdmin):
    fields=['book_name','author_name','created','updated','new_content','email','profile','resume','comment','rating']
    readonly_fields=['created','updated','new_content']

    def new_content(self,obj,*args,**kwargs):
        return str(obj.book_name)

    class Meta:
        model=Book

admin.site.register(Post)
admin.site.register(Book,BookAdmin)
admin.site.register(Employee)
admin.site.register(salary)
admin.site.register(author)
admin.site.register(novel)
admin.site.register(member)
admin.site.register(club)
