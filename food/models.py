from django.db import models

# Create your models here.
class item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)

    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.foodiesfeed.com/wp-content/uploads/2019/04/mae-mu-oranges-ice-cream-1024x683.jpg")