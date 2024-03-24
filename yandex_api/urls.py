from django.urls import path
from .views import FindRouteView

urlpatterns = [
    path('', FindRouteView.as_view(), name='find_route'),
]
