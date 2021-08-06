from django.db import models

# Create your models here.

genders =[

     ('f','Female'),
     ('M','male')

]
class Post2(models.Model):

      name=models.CharField(max_length=100)
      address=models.CharField(max_length=100)
      gender=models.CharField(max_length=100,choices=genders, null=True)


class Book2(models.Model):
      book_name=models.CharField(max_length=100)
      author_name=models.CharField(max_length=100)
      comment=models.CharField(max_length=100,default="comment#")
      profile=models.ImageField(upload_to="media/images/%y/%m/%d/", null=True)
      resume=models.FileField(upload_to="media/userfiles/%y/%m/%d/",null=True)

      def __str__(self):
          return self.book_name
