"""Meetup"""

from datetime import date, timedelta


class MeetupDayException(Exception):
    pass


def last_day_of_month(d: date) -> date:
    """Return a date that is the last day of the month of the date passed in as d."""
    if d.month == 12:
        d = date(d.year + 1, 1, 1)
    else:
        d = date(d.year, d.month + 1, 1)
    d -= timedelta(days=1)

    return d


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    # Start with the frist day of the month of the given year
    test_date = date(year, month, 1)

    if week == "teenth":
        # Go through the days until the week is reached
        while True:
            if test_date.strftime("%A") == day_of_week and (13 <= test_date.day <= 19):
                # Grab the day from that date
                day = test_date.day

                break
            test_date += timedelta(days=1)
    else:
        if week == "last":
            # Start from the last day of the month and go backwards
            # Crude way to get to the last day of the month: go 1 day before the next month
            test_date = last_day_of_month(test_date)
            
            while True:
                if test_date.strftime("%A") == day_of_week:
                    day = test_date.day
                    break
                test_date -= timedelta(days=1)
        else:
            TRANSLATOR = {
                "1st": 1,
                "2nd": 2,
                "3rd": 3,
                "4th": 4,
                "5th": 5
            }
            number = TRANSLATOR[week]

            encountered_query_days = 0
            while True:
                if test_date.strftime("%A") == day_of_week:
                    encountered_query_days += 1

                if encountered_query_days == number:
                    break

                test_date += timedelta(days=1)

                # If we go through the whole month and encountered_query_days doesn't reach number, then the date doesn't exist
                if test_date.month != month:
                    raise MeetupDayException("Date doesn't exist")

            day = test_date.day

    return date(year, month, day)
