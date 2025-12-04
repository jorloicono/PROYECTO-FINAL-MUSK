from src.sale import Sale

def test_sale_creation():
    s = Sale("S1", 1, "Laptop", "Electronics", 999.99, "2023-01-01")
    assert s.client_id == 1
    assert s.amount == 999.99
