from rest_framework import serializers
from .models import Item
class ItemSeri(serializers.ModelSerializer):
    Item_image= serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Item
        fields=['id','user_name','Item_name','Item_desc','Item_price','Item_image','Item_Type']


