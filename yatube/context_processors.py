import datetime as dt


def year(request):
    today = dt.datetime.now()

    return {
        "year" : today.year
    }