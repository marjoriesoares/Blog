from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Blog.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', messages),
    path('', accounts),
    path('accounts/', include('Accounts.urls')),
    path('messages/', include('Messages.urls')),
    path('pages/', include('Pages.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)