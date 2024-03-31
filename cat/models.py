from django.db import models
from django.urls import reverse

# Create your models here.
class Catagory(models.Model):
    cat_name    =       models.CharField(max_length = 50, unique = True)
    slug        =       models.SlugField(max_length = 100, unique = True)
    des         =       models.TextField(max_length = 250 , blank = True)
    cat_img     =       models.ImageField(upload_to = 'photos/catagories',blank = True)

    class meta:
        verbose = 'cat'
        varbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'
    
    def get_url(self):
        return reverse('product_by_catagory',args=[self.slug])

    def __str__(self):
        return self.cat_name 