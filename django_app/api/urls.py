from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('goods', views.index, name='goods'),
  path('plast', views.plast, name='plast'),
  path('plast/<str:mode>', views.plast, name='plast'),
  path('msgs/<int:page>', views.msgs, name='msgs'),
  path('myposts/<int:page>', views.myposts, name='myposts'),
  path('usr_goods/<int:page>', views.usr_goods, name='usr_goods'),
  path('usr', views.usr, name='usr'),
  path('usr/<int:usr_id>', views.usr, name='usr'),
  path('post', views.post, name='post'),
  path('good/<int:good_id>', views.good, name='good'),
]