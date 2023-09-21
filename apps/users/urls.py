from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import RegisterAPIView, LoginAPIView, ConfirmAPIView, LogoutView, PasswordResetRequestAPIView, \
    PasswordResetCodeAPIView, PasswordResetNewPasswordAPIView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('confirm/', ConfirmAPIView.as_view(), name='confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("reset-password-email/", PasswordResetRequestAPIView.as_view(), name="search user and send mail"),
    path("reset-password-code/", PasswordResetCodeAPIView.as_view(), name="write code"),
    path("reset-new-password/<str:code>/", PasswordResetNewPasswordAPIView.as_view(), name="write new password"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
