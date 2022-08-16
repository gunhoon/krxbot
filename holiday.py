import csv
import datetime
import logging
import os.path


def holiday_info(date):
    holiday_set = set()

    year = date.year
    filename = os.path.join('holiday', f'holiday_{year}.csv')

    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                holiday_set.add(datetime.date.fromisoformat(row[0]))
    except OSError as e:
        logging.error('filename {}: {}'.format(filename, e))

    return holiday_set
