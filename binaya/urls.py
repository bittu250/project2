
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "BINAYA Admin"
admin.site.site_title = "BINAYA'S Admin Portal"
admin.site.index_title = "Welcome to Gharjagga administration"


urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include('bittu.urls'))
   
]
