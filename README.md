# smart-log-analyzer1

Smart Log Analyzer is a Python-based tool that analyzes log files,
detects errors and warnings, and generates meaningful summaries.
It includes automated testing using pytest.

## Features

- Parse log files
- Count errors and warnings
- Filter logs by level
- Generate summary reports
- Automated unit testing with pytest
- HTML test report support

## Installation

Clone the repository:

```bash
git clone https://github.com/akavarammanasa/smart-log-analyzer1.git
cd smart-log-analyzer
pip install -r requirements.txt
```

## running tests

```python
pytest -v

pytest --html=report.html --self-contained-html
```
