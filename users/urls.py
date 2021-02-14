from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

#Url for logging in



urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),

    path('logged_out/', auth_views.LogoutView.as_view(template_name="users/logged_out.html"), name="logout"),

    path('register/', user_views.register, name= 'register'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
]
