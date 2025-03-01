from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from catalog.models import Item
from catalog.payment import ItemPayment

__all__ = ["item_buy", "item_detail", "item_list"]


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.values("id", "name", "price")
    context = {"items": items}
    return render(request, template, context)


def item_detail(request, pk):
    template = "catalog/item.html"
    try:
        item = Item.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    context = {
        "item": item,
        "stripe_public_key": settings.STRIPE_PUBLIC_API_KEY,
    }
    return render(request, template, context)


def item_buy(request, price_id):
    session = ItemPayment.create_session(
        price_id,
        request.build_absolute_uri(reverse("catalog:item_list")),
        request.build_absolute_uri(reverse("catalog:item_list")),
    )
    return JsonResponse(data={"id": session.id})
