from django.urls import path

from .views import RegisterView, LoingView, ConfirmView, UserCenterInfoView,UserCenterOrderView

app_name='user'
urlpatterns = [
    path('login/', LoingView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('user_center_info/', UserCenterInfoView.as_view(), name='user_center_info'),
    path('user_center_order/', UserCenterOrderView.as_view(), name='user_center_order'),
]