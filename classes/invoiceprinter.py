class InvoicePrinter:
    @staticmethod
    def print_invoice(order):
        print(f"the items is {order.items} all the price is {order.total_price}")