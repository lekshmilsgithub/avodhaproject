
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.avodha, name='avodha'),
    path('shop/<int:shop_id>', views.detail, name='detail'),
    path('add', views.add_product, name='add_product'),

]
