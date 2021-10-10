
from component import load_components


def test_load_components():
    """Test that the correct number of components are loaded."""
    components = load_components(file_path="../data/components.csv")
    assert len(components.index) == 10


def test_components_lookup():
    """Test that the data has imported correctly."""
    components = load_components(file_path="../data/components.csv")
    assert components.loc["BKRED01"]["colour"] == "Red"
