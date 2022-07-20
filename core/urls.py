
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from  .views import index,about

urlpatterns = [
    path('',index,name="index.page"),
    path('about',about,name="about.page")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)