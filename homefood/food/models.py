from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Item(models.Model):
     def __str__(self):
          return self.Item_name
     user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
     Item_name= models.CharField(max_length=200)
     Item_desc= models.CharField(max_length=300)
     Item_price= models.IntegerField()
     Item_image= models.CharField(max_length=500,default="https://www.google.com/url?sa=i&url=http%3A%2F%2Fchaysendo.com%2Fthuc-uong-162&psig=AOvVaw0svv7irjRzq-nhIkbJkkUz&ust=1589142336011000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMiFn9XOp-kCFQAAAAAdAAAAABAI")
     Item_Type=models.CharField(max_length=50, default='Veg')
     def get_absolute_url(self):
          return reverse("food:detail",kwargs={"item_id":self.pk})  