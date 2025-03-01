from django.contrib import admin

from catalog.models import Item

__all__ = ["ItemAdmin"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = (
        Item.name.field.name,
        Item.description.field.name,
        Item.price.field.name,
    )
    list_display = (
        Item.name.field.name,
        Item.price.field.name,
    )
    list_display_links = (Item.name.field.name,)
