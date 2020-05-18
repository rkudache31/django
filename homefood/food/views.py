from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from rest_framework import viewsets,generics
from .serializers import ItemSeri
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def type_list(request,name):
    if request.method == 'GET':
        itemlist=Item.objects.all()
        itemlist=itemlist.filter(Item_Type=name)
        serializer = ItemSeri(itemlist, many=True)
        return Response(serializer.data)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class =  ItemSeri


class ItemVgeViewSet(viewsets.ModelViewSet):
      queryset = Item.objects.filter(Item_Type='Veg')
      serializer_class =  ItemSeri

class ItemSelectViewSet(generics.ListAPIView):
       serializer_class =  ItemSeri  
       def get_queryset(self):
           queryset = Item.objects.all()
           type_name=self.request.query_params.get('name',None)
           if type_name is not None:
               queryset = queryset.filter(Item_name=type_name)

           return  queryset



# Create your views here.
'''
def foodlist(request):
    itemlist=Item.objects.all()

    template=loader.get_template('food/index.html')
    context={
        'itemlist':itemlist,
    }
    return HttpResponse(template.render(context,request))
'''
#This is function based views

def foodlist(request):
     itemlist=Item.objects.all()
     item_name=request.GET.get('name')
     if item_name != '' and  item_name is not None :
         itemlist=itemlist.filter(Item_name__icontains=item_name)
     paginator=Paginator(itemlist,2)
     page = request.GET.get('page')

     
     itemlist=paginator.get_page(page)
     context={
         'itemlist':itemlist,
     }
     return render(request,'food/index.html',context)

#There is anoter way to replace above code using listview

# you can use listview insted function based view
class classfoodlist(ListView):
    model = Item
    template_name ='food/index.html'
    context_object_name ='itemlist'


def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context = {

        'item':item,
    }
    return render(request,'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{ 'form':form })

    # This class based view for create item
class CreateItem(CreateView):
        model= Item
        fields=['Item_name','Item_desc','Item_price','Item_image','Item_Type']
        template_name='food/item-form.html'
        def form_valid(self,form):
            form.instance.user_name=self.request.user

            return super().form_valid(form)


def update_item(request,id):
    item=Item.objects.get(pk=id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{ 'form':form, 'item':item })


def delete_item(request,id):
    item=Item.objects.get(pk=id)
    form = ItemForm(request.POST or None,instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/delete-item.html',{'form':form,'item':item})
    