from django.urls import path
from . import views

app_name ='produects'
urlpatterns = [
    path('',views.ProductAPIView.as_view()),
    path('<int:product_id>/', views.ProductDetail.as_view()),
]