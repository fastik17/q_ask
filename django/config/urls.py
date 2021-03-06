
from django.contrib import admin
from django.urls import path, include

import qanda.urls
import user.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user.urls, namespace='user')),
    path('', include('contact.urls')),
    path('', include(qanda.urls, namespace='questions')),
    path('oauth/', include('social_django.urls', namespace='social')),
]