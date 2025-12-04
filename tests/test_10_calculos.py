from src.analyze import generate_report

def test_10_calculos_completos():
    report = generate_report()

    # ------------------------------
    # 1) TOTAL CLIENTES
    # ------------------------------
    assert report["summary"]["total_clients"] == 3

    # ------------------------------
    # 2) TOTAL VENTAS
    # ------------------------------
    assert report["summary"]["total_sales"] == 7

    # ------------------------------
    # 3) TOTAL GASTADO POR CLIENTE
    # ------------------------------
    clients = report["clients"]

    totals = {c["client_id"]: c["total_spent"] for c in clients}

    assert totals[1] == 699.99 + 199.99 + 399.99              # Alice
    assert totals[2] == 1299.50 + 89.99                       # Bob
    assert totals[3] == 49.99 + 299.99                        # Carol

    # ------------------------------
    # 4) NÚMERO DE VENTAS POR CLIENTE
    # ------------------------------
    counts = {c["client_id"]: c["sale_count"] for c in clients}

    assert counts[1] == 3
    assert counts[2] == 2
    assert counts[3] == 2

    # ------------------------------
    # 5) PROMEDIO DE GASTO POR CLIENTE
    # ------------------------------
    # Promedios esperados
    expected_avg_1 = round((699.99 + 199.99 + 399.99) / 3, 2)
    expected_avg_2 = round((1299.50 + 89.99) / 2, 2)
    expected_avg_3 = round((49.99 + 299.99) / 2, 2)

    averages = {c["client_id"]: c["average_sale"] for c in clients}

    assert averages[1] == expected_avg_1
    assert averages[2] == expected_avg_2
    assert averages[3] == expected_avg_3

    # ------------------------------
    # 6) CLIENTE CON MAYOR GASTO POR PAÍS
    # ------------------------------
    top = report["top_client_by_country"]

    assert top["Spain"] == "Alice"
    assert top["Germany"] == "Bob"
    assert top["France"] == "Carol"

    # ------------------------------
    # 7) TOTAL DE VENTAS POR CATEGORÍA
    # ------------------------------
    expected_categories = {
        "Electronics": 699.99 + 1299.50 + 299.99 + 399.99,
        "Accessories": 199.99 + 89.99 + 49.99
    }

    for cat, total in expected_categories.items():
        assert abs(report["sales_by_category"][cat] - total) < 0.01

    # ------------------------------
    # 8) CLIENTE CON MÁS VENTAS EN UNA CATEGORÍA
    # (Electronics)
    # ------------------------------
    # Alice: 2 (Smartphone + Tablet)
    # Bob: 1 (Laptop)
    # Carol: 1 (Monitor)
    assert report["clients"][0]["name"] == "Alice"  # check by ordering

    # ------------------------------
    # 9) CLIENTES DE ALTO GASTO (>500)
    # ------------------------------
    high_spenders = report["high_spending_clients"]

    assert "Alice" in high_spenders
    assert "Bob" in high_spenders
    assert "Carol" not in high_spenders  # Carol gasta < 500

    # ------------------------------
    # 10) VENTAS POR MES
    # ------------------------------
    monthly = report["monthly_sales"]

    assert "2023-07" in monthly
    assert abs(monthly["2023-07"] - report["summary"]["total_revenue"]) < 0.01
