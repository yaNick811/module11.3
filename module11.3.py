import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj)

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    obj_module = inspect.getmodule(obj)

    # Создаем словарь с информацией
    info = {
        "Тип объекта": obj_type,
        "Атрибуты объекта": attributes,
        "Методы объекта": methods,
        "Модуль объекта": obj_module.__name__ if obj_module else "Неизвестный модуль",
    }

    # Дополнительные интересные свойства, зависящие от типа объекта
    if isinstance(obj, int):
        info["Двоичное представление"] = bin(obj)
        info["Шестнадцатеричное представление"] = hex(obj)
    elif isinstance(obj, str):
        info["Длина строки"] = len(obj)
    elif isinstance(obj, list):
        info["Длина списка"] = len(obj)
        info["Первый элемент"] = obj[0] if len(obj) > 0 else "Пустой список"
    elif isinstance(obj, dict):
        info["Количество пар ключ-значение"] = len(obj)
        info["Первый ключ"] = next(iter(obj)) if len(obj) > 0 else "Пустой словарь"

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)