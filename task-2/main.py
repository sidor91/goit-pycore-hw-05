import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None]:
    # Регулярний вираз для пошуку дійсних чисел, що відокремлені пробілами
    pattern = r"(?<= )\d+\.\d+(?= )|(?<= )\d+(?= )"

    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None]]) -> float:
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
