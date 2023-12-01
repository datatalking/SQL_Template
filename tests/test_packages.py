# tests/test_packages.py

import importlib


def test_imports():
    packages = [
        "pytest",
        "numpy",
        "pandas",
        "python_dotenv",
        "dask",
        "sqlalchemy",
        "psycopg2",
        "seaborn",
        "matplotlib",
        "cursor",
        "pyodbc",
    ]

    for package in packages:
        assert importlib.util.find_spec(package) is not None, f"{package} is not installed."
