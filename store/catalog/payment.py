import stripe

from core.payment import BasePayment


__all__ = ["ItemPayment"]


class ItemPayment(BasePayment):
    @classmethod
    def create_product(cls, item):
        return stripe.Product.create(
            name=item.name,
            description=item.description,
        )

    @classmethod
    def create_price(cls, item, product):
        return stripe.Price.create(
            unit_amount=int(
                item.price * (10**item.__class__.price.field.decimal_places),
            ),
            currency="usd",
            product=product,
        )

    @classmethod
    def create_session(cls, price_id, success_url, cancel_url):
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
