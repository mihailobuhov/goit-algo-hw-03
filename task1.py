from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів між заданою датою та поточною датою.
    
    :param date: Рядок у форматі 'YYYY-MM-DD'
    :return: Ціле число (може бути від’ємним)
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - target_date
        return delta.days
    except ValueError:
        raise ValueError("Дата повинна бути у форматі 'YYYY-MM-DD'")

print(get_days_from_today("2021-10-09"))
