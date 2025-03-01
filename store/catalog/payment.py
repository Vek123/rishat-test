from django.conf import settings
import stripe

__all__ = ["ItemPayment"]


stripe.api_key = settings.STRIPE_SECRET_API_KEY


class ItemPayment:
    @staticmethod
    def create_product(item):
        try:
            return stripe.Product.create(
                name=item.name,
                description=item.description,
            )
        except Exception as e:
            return str(e)

    @staticmethod
    def create_price(item, product):
        try:
            return stripe.Price.create(
                unit_amount=int(
                    item.price
                    * (10**item.__class__.price.field.decimal_places),
                ),
                currency="usd",
                product=product,
            )
        except Exception as e:
            return str(e)

    @staticmethod
    def create_session(price_id, success_url, cancel_url):
        try:
            return stripe.checkout.Session.create(
                line_items=[
                    {
                        "price": price_id,
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=success_url,
                cancel_url=cancel_url,
            )
        except Exception as e:
            return str(e)
