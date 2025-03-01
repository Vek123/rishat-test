from django.conf import settings
import stripe

__all__ = ["BasePayment"]

stripe.api_key = settings.STRIPE_SECRET_API_KEY


class BasePayment:
    @classmethod
    def get_price(cls, price_id):
        return stripe.Price.retrieve(price_id)

    @classmethod
    def get_product(cls, product_id):
        return stripe.Product.retrieve(product_id)

    @classmethod
    def delete_product(cls, product_id):
        stripe.Product.delete(product_id)

    @classmethod
    def archive_price(cls, price):
        stripe.Price.modify(
            price.id,
            active=False,
        )
