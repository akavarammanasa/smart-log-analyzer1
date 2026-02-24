from smart_log_analyzer.analyzer import count_errors

def test_count_errors():
    logs = [
        "INFO Server started",
        "ERROR Database failed",
        "ERROR Timeout occured"
    ]

    assert count_errors(logs) == 2