import re
import sys
from pathlib import Path

log_levels = ["info", "error", "debug", "warning"]

def main(file_path: str, level=None):
    logs = load_logs(file_path)
    filtered_logs = []

    if level:
        filtered_logs = filter_logs_by_level(logs, level)

    counted_logs = count_logs_by_level(logs)

    display_log_counts(counted_logs, filtered_logs)


def parse_log_line(line: str) -> dict:
    log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+)(.+)")
    match = log_pattern.match(line)

    if match:
        timestamp, level, message = match.groups()
        return {"timestamp": timestamp, "level": level, "message": message}


def load_logs(file_path: str) -> list:
    result = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                result.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return result

    return result


def filter_logs_by_level(logs: list, level: str = None) -> list:
    filtered_logs = [log for log in logs if log["level"] == level.upper()]
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    result = {level: 0 for level in log_levels}

    for log in logs:
        result[log["level"].lower()] += 1

    return result


def display_log_counts(counted_logs: dict, filtered_logs: list = None):

    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in ["info", "debug", "error", "warning"]:
        print(f"{level.upper():<16} | {counted_logs.get(level, 0)}")

    if not filtered_logs:
        return

    print(f"\nДеталі логів для рівня '{filtered_logs[0]['level']}':")
    for log in filtered_logs:
        print(f"{log['timestamp']} - {log['message']}")


if __name__ == "__main__":
    file_path = ""

    if len(sys.argv) < 2:
        print(
            "Please use the following command: python main.py /path/to/file [, level]"
        )
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_path = Path(sys.argv[1])
        main(file_path)
    else:
        file_path = Path(sys.argv[1])
        level = sys.argv[2].lower()

        if level not in log_levels:
            print(
                'The level argument should be one of the following: "info", "error", "debug"'
            )
            sys.exit(1)

        main(file_path, level)
