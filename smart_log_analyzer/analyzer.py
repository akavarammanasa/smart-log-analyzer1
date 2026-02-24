def count_errors(log_lines):
    return sum(1 for line in log_lines if "ERROR" in line)