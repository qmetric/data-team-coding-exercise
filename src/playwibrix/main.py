
from src.playwibrix.component import load_components
from src.playwibrix.order import load_orders
from src.playwibrix.summary import summarise_order


def main():

    components = load_components()
    orders = load_orders()

    summary = summarise_order(
        orders=orders,
        components=components,
    )

    print(summary)
