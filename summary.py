
import pandas as pd
from datetime import date
from order import get_order_details


def summarise_order(
        orders: pd.DataFrame,
        components: pd.DataFrame,
        summary_date: date = date(2021, 6, 3)
) -> pd.DataFrame:
    """Summarise a set of orders.

    Args:
        orders: A dataframe of orders to be summarised
        components: A dataframe of components.
        summary_date: The date on which to conduct the summary (default '2021-06-03').

    Returns:
        summary (pd.DataFrame): A dataframe summary.
    """

    filtered_orders = orders[orders["timestamp"].dt.date == summary_date]  # filter by summary date

    if len(filtered_orders.index) == 0:
        raise ValueError(f"No orders found on given summary date: {summary_date}")

    order_details = get_order_details(orders=filtered_orders)  # retrieve the order details

    summary = order_details.join(  # summarise
        components,
        on="componentId",
        how="inner"
    ).groupby(
        "colour"
    )["volume"].sum()

    return summary
