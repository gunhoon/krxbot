# This is a sample Python script.
import argparse
import datetime


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help='YYYYMMDD')

    args = parser.parse_args()
    print(args)

    if args.date is None:
        # today
        date = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))).date()
    else:
        date = datetime.datetime.strptime(args.date, '%Y%m%d').date()

    print(date)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
