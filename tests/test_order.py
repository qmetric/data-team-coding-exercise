
from order import load_orders


def test_load_orders():
    """Test for the load_orders function."""

    orders = load_orders(file_path="../data/orders.json.txt")
    assert len(orders.index) == 1000
