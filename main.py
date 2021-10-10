
from datetime import date
from component import load_components
from order import load_orders
from summary import summarise_order


def main(summary_date: str = "2021-06-03"):

    components = load_components()
    orders = load_orders()

    summary = summarise_order(
        orders=orders,
        components=components,
        summary_date=date.fromisoformat(summary_date)
    )

    print(summary)


if __name__ == "__main__":
    main()
