from . import views
from django.urls import path
from django.contrib.auth import views as authentication_views
app_name='food'
urlpatterns = [
    # /food/
    # path('',views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    #food/1
    # path('<int:item_id>',views.detail,name='detail'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    # add item 
    path('add',views.create_item,name="create_item"), 
    path('update/<int:id>',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item')
]