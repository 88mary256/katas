def days_in_month(month):
    months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
             'September': 30, 'Octuber': 31, 'November': 30, 'December': 31}
    print months[month]
    return months[month]


days_in_month('November')
