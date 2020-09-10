from django.db import models

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_title
    
class Biz(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    contact = models.IntegerField()
    email = models.EmailField()
    website = models.URLField(null=True,blank=True)
    image = models.ImageField(upload_to="image/")
    CITY = (("PRNA","PURNEA"),("PAT","PATNA"))
    city = models.CharField(max_length=20,choices=CITY)
    description = models.TextField()

    def __str__(self):
        return self.title

    
