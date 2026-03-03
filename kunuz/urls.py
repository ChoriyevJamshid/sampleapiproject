from django.urls import path

from kunuz import views


urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(),),
    path('posts/',views.PostListAPIView.as_view(),),
    path('posts/create/', views.PostCreateAPIView.as_view(),),
    path('posts/<int:post_id>/',views.PostDetailAPIView.as_view(),),
    path('posts/<int:post_id>/update/', views.PostUpdateAPIView.as_view(),),
    path('posts/<int:post_id>/delete/', views.PostDeleteAPIView.as_view(),),
]


