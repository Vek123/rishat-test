from django.urls import path

from catalog.views import item_buy, item_detail, item_list


app_name = "catalog"

urlpatterns = [
    path("item/", item_list, name="item_list"),
    path("item/<int:pk>/", item_detail, name="item_detail"),
    path("buy/<str:price_id>/", item_buy, name="item_buy"),
]
