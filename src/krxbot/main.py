import datetime
import logging

from . import stock


task_functions = {
    'stock.stock_price': stock.stock_price
}


def main(task, date):
    """main function

    :param task: str
    :param date: str
    :return: None
    """
    if date is None:
        # today
        tz = datetime.timezone(datetime.timedelta(hours=9))
        dt = datetime.datetime.now(tz=tz)
    else:
        dt = datetime.datetime.strptime(date, '%Y%m%d')

    date = dt.strftime('%Y%m%d')
    logging.info(date)

    func = task_functions.get(task)

    if func is None:
        logging.error(f'Invalid task: {task}')
    else:
        filename = f'{task}_{date}.csv'
        logging.info(filename)

        func(date, filename)
