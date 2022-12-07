from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from advertisement.views import index, IndexDetail, index_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='home'),
    # path('ad/<int:pk>', IndexDetail.as_view(), name='ad_detail'),
    # path('ad/<int:pk>', index_detail, name='ad_detail'),
    path('board/', include('advertisement.urls')),
    path('accounts/', include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('advertisement.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
