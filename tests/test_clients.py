from src.client import Client

def test_client_creation():
    c = Client(1, "Alice", "Spain", "2022-01-01")
    assert c.client_id == 1
    assert c.name == "Alice"
