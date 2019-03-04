from django.urls import path, include
from . import views

urlpatterns = [
  path('api/location/', views.LocationListCreate.as_view() ),
  path('api/location/<int:pk>', views.LocationDetail.as_view() ),
  path('rest-auth/', include('rest_auth.urls')),

]