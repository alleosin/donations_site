from django.urls import path
from .views import view_page, donate

urlpatterns = [
    path("<str:username>/", view_page, name="view_page"),
    path("donate/<str:username>/", donate, name="donate")
]
