from src.client_collection import ClientCollection
from src.sales_collection import SalesCollection
from src.client import Client
from src.sale import Sale

def test_collections():
    c = ClientCollection([Client(1, "Alice", "Spain", "2022-01-01")])
    s = SalesCollection([Sale("S1", 1, "Laptop", "Electronics", 100, "2023-01-01")])

    assert c.get_client_by_id(1).name == "Alice"
    assert len(s.sales_by_client(1)) == 1
    assert s.total_amount_by_client(1) == 100
