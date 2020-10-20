from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.show_home_page,name="home"),
    path('category/<int:id>',views.show_category_page,name="home"),
]
