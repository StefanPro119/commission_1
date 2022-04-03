from datetime import datetime
"""
High season: June - September => GuestReady commission is 15%
Other months: commission is 10%

Write a function that takes a date string in the format 'YYYY-MM-DD' and returns the commission:
get_commission(date_str) -> float
"""

date1 = '2021-06-01'
date2 = '2021-09-01'
june = datetime.strptime(date1, "%Y-%m-%d")
september = datetime.strptime(date2, "%Y-%m-%d")

def get_commission(data_str):
    if data_str.month >= june.month and data_str.month < september.month:
        return 0.15
    return 0.1


your_date = input('Insert the date in format (YYYY-MM-DD): ')
converted_date = datetime.strptime(your_date, "%Y-%m-%d")
returned_commission = get_commission(converted_date)

if returned_commission < 0.15:
    print('Your given date is in low season and the commission is 10%')
else:
    print('Your given date is in high season and the commission is 15%')
print(type(returned_commission))





