
from component import load_components


def test_load_components():
    components = load_components()
    assert len(components.index) == 10
