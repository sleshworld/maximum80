from django.urls import path
from .views import example, top_sellers, advertisement_post, advertisement_detail

urlpatterns = [
    path("", example, name = "main-page"),
    path("top-sellers/", top_sellers, name="top-sellers"),
    # указываем ссылку для запуска функции отображения html и имя для удобного указания на ссылку
    path("advertisement-post/", advertisement_post, name="adv-post"),
    path("advertisement/<int:pk>", advertisement_detail, name="adv-detail")
]
