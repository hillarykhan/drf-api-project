from django.urls import path
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),


]