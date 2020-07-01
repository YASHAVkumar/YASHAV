from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name='index'),
    path('search/', views.search, name='index1'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('pay/', views.pay, name='pay'),
    path('login/', views.login, name='login'),
    path('sign/',views.sign,name='sign'),
    path('contact/contact', views.contact, name='contact1'),
    path('login/gold', views.gold, name='gold'),
    path('login/search', views.search, name='gold1'),
    path('login/gold/cart', views.cart, name='cart1'),
    path('search/search', views.search, name='gold2'),
    path('sign/login',views.login,name='sign1'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)