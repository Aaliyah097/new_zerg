from . import Bitconce
from .models import (
    order_buy,
    order_sell
)


class OrdersRepo(Bitconce):
    def get_orders_sell(self, status: str = "all", page_number: int = 1, amount: int = 1) -> list[order_sell.OrderSell]:
        url = 'getOrders/'
        method = 'GET'
        params = {
            'status': status,
            'page_number': page_number,
            'amount': amount
        }

        if status not in order_sell.OrderSell.statuses:
            raise Exception(f"{status} not in {order_sell.OrderSell.statuses}")

        response = self.request(url=url, method=method, params=params)
        return [order_sell.OrderSell(source) for source in response]

    def get_orders_buy(self, status: str = "Active", page_number: int = 1, amount: int = 1) -> list[order_buy.OrderBuy]:
        url = 'getExchangeOrders/'
        method = 'GET'
        params = {
            'status': status,
            'page_number': page_number,
            'amount': amount
        }

        if status not in order_buy.OrderBuy.statuses:
            raise Exception(f"{status} not in {order_buy.OrderBuy.statuses}")

        response = self.request(url=url, method=method, params=params)
        return [order_buy.OrderBuy(source) for source in response]