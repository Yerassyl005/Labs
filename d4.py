from datetime import datetime

date1 = datetime(2024, 2, 19, 15, 30, 45)
date2 = datetime(2024, 2, 20, 10, 15, 30)

time_dif = date2 - date1

time_dif_sec = time_dif.total_seconds()

print("date1: ", date1)
print("date2: ", date2)
print("difference in seconds: ", time_dif_sec)