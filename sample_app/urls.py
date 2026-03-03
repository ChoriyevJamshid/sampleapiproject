from django.urls import path

from sample_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductAPIView.as_view(),
         name='product-list'),

    path('products/<int:pk>/', views.ProductProcessAPIView.as_view(),
         name='product-process'),
]


