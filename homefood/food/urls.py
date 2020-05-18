from django.urls import path,include
from . import views

from rest_framework import routers

from food.views import ItemViewSet,ItemVgeViewSet,ItemSelectViewSet

from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register('item',ItemViewSet)
router.register('veg',ItemVgeViewSet)











# This is help to  hard coded name use app_name concept
app_name='food'
urlpatterns = [
    
    # food
    path('', views.foodlist,name='index'),
    # food/1
    path('<int:item_id>/',views.detail,name='detail'),
    # add item
    path('add',views.CreateItem.as_view(),name='create_item'),
    # Edit item
    path('update/<int:id>',views.update_item,name='update_item'),
    #delete item
    path('delete/<int:id>',views.delete_item,name='delete_item'),
    #REST
    path('rest',include(router.urls)),
   # path('rest/(?P<name>.+)',views.ItemSelectViewSet.as_view()),
   path('<name>/',views.type_list,name='item_name')

       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
