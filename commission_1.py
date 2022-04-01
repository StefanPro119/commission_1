import datetime

"""
High season: June - September => GuestReady commission is 15%
Other months: commission is 10%

Write a function that takes a date string in the format 'YYYY-MM-DD' and returns the commission:
get_commission(date_str) -> float
"""

format = '%Y/%m/%d'

def get_commission(data_str):
    june = '2021/06/01'
    september = '2021/09/01'
    data_str = datetime.datetime.strptime(data_str, format)
    june = datetime.datetime.strptime(june, format)
    september = datetime.datetime.strptime(september, format)
    if data_str >= june and data_str < september:
        return 0.15
    return 0.1

returned_commission = get_commission('2021/08/1')

if returned_commission < 0.15:
    print('Your given date is in low season and the commission is 10%')
else:
    print('Your given date is in high season and the commission is 15%')
print(type(returned_commission))





