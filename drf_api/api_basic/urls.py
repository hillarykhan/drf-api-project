from django.urls import path
from .views import ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),
    path('generic/articles/<int:id>/', GenericAPIView.as_view()),


]