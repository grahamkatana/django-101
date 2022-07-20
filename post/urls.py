from django.urls import path
from  .views import show

urlpatterns = [
    path('<slug:slug>',show,name="show.post"),
]