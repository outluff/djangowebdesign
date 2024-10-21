from django.contrib import admin
from django.urls import path, include

from conprogs.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('conprogs.urls'))
]

handler404 = page_not_found
