
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Blog Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("cms.urls"))
]
