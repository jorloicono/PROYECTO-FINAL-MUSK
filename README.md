# PROYECTO-FINAL-MUSK

Este proyecto carga datos desde un JSON y un CSV, los cruza, calcula 10 métricas y genera un reporte final JSON.

Incluye:
- POO
- Programación funcional
- Pandas
- Bucles
- Condicionales
- GitHub Actions
- Tests automáticos

## Uso


python src/analyze.py

El resultado se guarda en final_report.json.

## Tests

pytest

## Validación automática

Cada push ejecuta GitHub Actions para validar:

- Estructura del JSON final
- Cálculos correctos
- Código ejecutable
