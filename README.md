# MLApp

A sample Data Engineering pipeline built with **Python**, **PySpark**, and **SQL** for the Apprentices2026 Fundamentals track.

## Project Overview

MLApp is a customer analytics data pipeline that:
- Ingests raw transaction data (CSV / Parquet)
- Cleans and transforms data using PySpark
- Segments customers based on spend behavior
- Stores processed data for downstream analytics

## Repo Structure

```
MLApp/
├── src/
│   ├── data_loader.py         # Data ingestion utilities
│   ├── transformations.py     # PySpark transformation logic
│   └── spark_utils.py         # Spark session helpers
├── sql/
│   ├── create_tables.sql      # DDL scripts
│   └── queries.sql            # Analytical queries
├── config/
│   └── pipeline_config.yaml   # Pipeline configuration
├── tests/
│   └── test_transformations.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.10+
- Java 11+ (for PySpark)
- Git Bash (Windows) or Terminal (Mac/Linux)

### Setup
```bash
git clone https://github.com/fractal-training/MLApp.git
cd MLApp
pip install -r requirements.txt
```

### Run the Pipeline
```bash
python src/data_loader.py
```

## Contributing

1. Create a feature branch: `git checkout -b feature/JIRA-XXXX-short-description`
2. Make changes and commit: `git commit -m "feat: your change"`
3. Push and raise a PR: `git push -u origin feature/JIRA-XXXX-short-description`

## Team

- **Track Owner:** Kiran Kumar (FAA)
- **Cohort:** Apprentices2026

---

*Fractal Analytics Academy · Internal Training Repository*
