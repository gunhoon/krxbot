import argparse
from datetime import datetime, timezone, timedelta


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

    main(args.date)
