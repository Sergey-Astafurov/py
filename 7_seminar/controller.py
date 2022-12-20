import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d,%(name)s,%(levelname)s,%(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    encoding='UTF-8',)


def main_function():
    try:
        select = view.greeting()
        if select == 1:
            logging.info('вы выбрали калькулятор! Отлично!')
            exp = view.get_math_example()
            logging.info(f'Ваш пример "{exp}"')
            result = model.calc(exp)
            view.view_result(result)
            logging.info(f'Результат "{result}"')

        elif select == 2:
            logging.info('вы выбрали конвектер! Супер!')
            mass = view.get_massa()
            logging.info(f'Вы ввели массу "{mass}" кг')
            mass_result = model.convert(mass)
            view.view_result_mass(mass_result)
            logging.info(f'Результат "{mass_result}"')
    except Exception as er:
        logging.warning(f'"ERROR",{er}')
