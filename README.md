# Pandemic Preparedness Index

Composite pandemic preparedness scoring system aggregating WHO JEE assessments, GHS Index indicators, and custom capacity metrics.

## Architecture

```
pandemic-preparedness-index/
  src/           # Core modules
  tests/         # Unit and integration tests
  config/        # Configuration files
  docs/          # Documentation
```

## Modules

- **jee_scorer**: Core jee scorer functionality
- **ghs_aggregator**: Core ghs aggregator functionality
- **capacity_mapper**: Core capacity mapper functionality
- **risk_calculator**: Core risk calculator functionality
- **benchmark_engine**: Core benchmark engine functionality

## Quick Start

```bash
pip install -r requirements.txt
python -m pandemic_preparedness_index.main
```

## Testing

```bash
pytest tests/ -v
```

## License

MIT License - see LICENSE for details.
