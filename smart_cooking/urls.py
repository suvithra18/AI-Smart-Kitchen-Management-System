
from django.contrib import admin
from django.urls import path,include
from .views import home
from rest_framework_simplejwt.views import (
TokenObtainPairView,TokenRefreshView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recipes/', include('recipes.urls')),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('recipes/', include('recipes.urls')),
    path('inventory/', include('inventory.urls')),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path( 'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('smartkitchen/',include('smartkitchen.urls')),
]
if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT
    )