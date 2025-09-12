import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Генерує відсортований список унікальних випадкових чисел для лотереї.
    
    :param min_num: Мінімальне можливе число (не менше 1)
    :param max_num: Максимальне можливе число (не більше 1000)
    :param quantity: Кількість чисел, які потрібно вибрати
    :return: Відсортований список унікальних випадкових чисел
    """
    if not (1 <= min_num <= max_num <= 1000):
        return []
    if not (min_num <= quantity <= max_num - min_num + 1):
        return []
    
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
