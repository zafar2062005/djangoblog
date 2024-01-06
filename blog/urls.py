# from django.contrib import admin
# from django.urls import path,include
# from .views import HomeView, ArticleDetail, AddPost, EditBlog, DeleteBlog
# from django.contrib.auth.views import LogoutView
# #here we are using class based views, classes not funcions that why it is different

# #most common mistake: kindly use commas in url pattern list 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', HomeView.as_view(), name='home' ),
#     path ('add_post/', AddPost.as_view(), name='add_post' ),
#     # pk refers to as primary key when we are accessing elements from models we use priamry key 
#     path('article/<int:pk>', ArticleDetail.as_view(), name='article' ),
#     path('article/edit/<int:pk>', EditBlog.as_view(), name='update_post' ),   
#     path('article/remove/<int:pk>', DeleteBlog.as_view(), name='delete_post' ),
#      path('logout/', LogoutView.as_view(next_page='home'), name='logout'),   
# ]

from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetail, AddPost, EditBlog, DeleteBlog
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article'),
    path('article/edit/<int:pk>', EditBlog.as_view(), name='update_post'),
    path('article/remove/<int:pk>', DeleteBlog.as_view(), name='delete_post'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
