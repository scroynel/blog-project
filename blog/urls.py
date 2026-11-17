from django.urls import path
from .views import MainView, CreateCommentView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('posts/<uuid:post_id>/comment/', CreateCommentView.as_view(), name='create_comment'),
]