import os
import time


def logger(old_function):
    def new_function(*args, **kwargs):
        start_f = time.perf_counter()
        func = old_function(*args, **kwargs)
        end_f = time.perf_counter()
        result = (end_f - start_f)

        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(
                f'Время выполнения: {result:.8f} -  должно записаться имя функции {old_function.__name__}, аргументы функции: {args},{kwargs}, должен быть записан в файл: {func}\n')
        return func

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

import os


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            start_f = time.perf_counter()
            func = old_function(*args, **kwargs)
            end_f = time.perf_counter()
            result = (end_f - start_f)

            with open(path, 'a', encoding='utf-8') as f:
                f.write(
                    f'Время выполнения: {result:.8f} -  должно записаться имя функции {old_function.__name__}, аргументы функции: {args},{kwargs}, должен быть записан в файл: {func}\n')
            return func

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
