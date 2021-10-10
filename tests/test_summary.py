
from order import load_orders
from component import load_components
from summary import summarise_order


def test_summarise_order():
    """Test for the summarise_order function."""

    orders = load_orders(file_path="../data/orders.json.txt")
    components = load_components(file_path="../data/components.csv")

    summary = summarise_order(orders=orders, components=components)

    assert summary["Black"] == 4773
