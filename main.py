
from component import load_components
from order import load_orders
from summary import summarise_order


def main():
    """Main function of the playwibrix package."""

    components = load_components()
    orders = load_orders()

    summary = summarise_order(
        orders=orders,
        components=components,
    )

    print(summary)


if __name__ == "__main__":
    main()
