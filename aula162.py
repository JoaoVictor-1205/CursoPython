from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('Asia/Tokyo'))
print(data.timestamp())
print(datetime.fromtimestamp(1771013157.536075))


# # data_str_data = '2022-04-20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# date = datetime.strptime(data_str_data, data_str_fmt).date()
# print(date)
