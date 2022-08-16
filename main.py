import argparse
import logging
from datetime import datetime, timezone, timedelta

import holiday


def main(date):
    date_str = date.strftime('%Y%m%d')
    print(f'Hi, {date_str}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date',
                        default=datetime.now(tz=timezone(timedelta(hours=9))).strftime('%Y%m%d'),
                        type=lambda s: datetime.strptime(s, '%Y%m%d').date(),
                        help='format(YYYYMMDD)')

    args = parser.parse_args()

    week = args.date.weekday()
    holiday = holiday.holiday_info(args.date)

    if 5 <= week <= 6:
        logging.warning('weekend')
    elif args.date in holiday:
        logging.warning('holiday')
    else:
        main(args.date)
