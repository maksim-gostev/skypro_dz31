from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.user import views

urlpatterns = [
    path('', views.UsersListView.as_view()),
    path('<int:pk>/', views.UsersDetailView.as_view()),
    path('create/', views.UsersCreateView.as_view()),
    path('<int:pk>/update/', views.UsersUpdateView.as_view()),
    path('<int:pk>/delete/', views.UsersDeleteView.as_view()),
    path('Z/', views.UsersAdsDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]