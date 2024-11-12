from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/token/', views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path("api/token/refresh/", jwt_views.TokenRefreshView.as_view(),
         name="token_refresh"),
    path("api/register/", views.CreateUser.as_view(), name="register"),
    path("api/clientInfo/", views.clientInfo.as_view(), name="clientInfo"),
    path("api/propertyInfo/", views.propertyInformation.as_view(), name="propertyInfo"),
    path("api/propertyInfo/patch/", views.propertyInformation.as_view(), name="propertyInfo"),
    path("api/propertyInfo/delete/", views.propertyInformation.as_view(), name="propertyInfo"),
    path("api/onLoad/", views.onLoad.as_view(), name="onLoad"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
