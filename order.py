
import json
import pandas as pd
from typing import Dict
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    """Class to represent an order."""
    timestamp: datetime.timestamp
    orderId: str
    units: Dict[str, int]


def load_orders(file_path: str = "data/orders.json.txt") -> pd.DataFrame:
    """Load orders from file.

    Each order is validated against the Order model to ensure data integrity.
    
    Args:
        file_path: Path to the orders file (default 'data/orders.json.txt').

    Returns:
        orders (pd.DataFrame): A dataframe of orders.
    """

    orders_list = []

    # validate each order against the Order model
    with open(file=file_path, mode="r") as file:
        for row in file:
            data = json.loads(row)
            order = Order(**data)
            orders_list.append(order)

    orders = pd.DataFrame([order.__dict__ for order in orders_list])  # create a dataframe of orders
    orders["timestamp"] = pd.to_datetime(orders["timestamp"])
    orders.set_index(keys="orderId", inplace=True)

    return orders


def get_order_details(orders: pd.DataFrame) -> pd.DataFrame:
    """Get dataframe of order details from a given set of orders.

    Args:
        orders: A set of orders.

    Returns:
        (pd.DataFrame): A dataframe of order details.
    """

    order_details = orders.units.to_dict().values()  # retrieve values from the units column
    order_list = [
        {"componentId": component, "volume": order[component]}
        for order in order_details for component in order
    ]
    return pd.DataFrame(order_list)
