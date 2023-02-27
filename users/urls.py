from django.urls import path
from . import views
# from . import views

app_name = "users"

# urlpatterns = [
#     path("register/", views.register_view, name="register"),
#     path("login/", views.login_view, name="login"),
#     path("logout/", views.logout_view, name="logout"),
#     path("dashboard/", views.dashboard, name="dashboard"),
# ]

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('me', views.RetrieveUserView.as_view(), name='me'),

]
