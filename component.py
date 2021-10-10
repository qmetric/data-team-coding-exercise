
import csv
import pandas as pd
from dataclasses import dataclass


@dataclass(frozen=True)
class Component:
    """Class to represent a component."""
    componentId: str
    colour: str
    costPrice: float


def load_components(file_path: str = "data/components.csv") -> pd.DataFrame:
    """Load components file into a dataframe.

    Each row is first validated against the Component model to ensure data integrity.
    
    Args:
        file_path: Path to the components file (default data/components.csv).

    Returns:
        components (pd.DataFrame): A dataframe of component information.
    """

    components_list = []

    # validate each row against the Component data model
    with open(file=file_path, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data = {column_name: value for value, column_name in zip(row, headers)}
            components_list.append(Component(**data))

    components = pd.DataFrame([component.__dict__ for component in components_list])  # create a dataframe
    components.set_index(keys="componentId", inplace=True)  # set the index to componentId for faster lookups
    
    return components
