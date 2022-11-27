from django.urls import path, include
from .views import PostListView, PostDetailView

app_name = 'blog_api'
urlpatterns = [
    path('<int:pk>', PostDetailView.as_view(), name="detailcreate" ),
    path('', PostListView.as_view(), name="listcreate" ),

]