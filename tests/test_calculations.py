from src.analyze import generate_report

def test_calculations_values():
    report = generate_report()
    assert report["summary"]["total_clients"] == 3
    assert report["summary"]["total_sales"] == 7
    assert report["summary"]["total_revenue"] > 0
