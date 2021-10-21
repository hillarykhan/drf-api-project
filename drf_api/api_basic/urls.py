from django import urls
from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/', include(router.urls)),
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),
    path('generic/articles/<int:id>/', GenericAPIView.as_view()),


]