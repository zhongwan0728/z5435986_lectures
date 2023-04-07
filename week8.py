import pandas as pd
dates = ['2020‑01‑02', '2020‑01‑03', '2020‑01‑06', '2020‑01‑07', '2020‑01‑08',
'2020‑01‑09', '2020‑01‑10', '2020‑01‑13', '2020‑01‑14', '2020‑01‑15',
]
prices = [7.1600, 7.1900, 7.0000, 7.1000, 6.8600,
6.9500, 7.0000, 7.0200, 7.1100, 7.0400,]
ser = pd.Series(data=prices, index=dates)
print(ser)

a_little_ago =dt.datetime(year=2023,month=8,day=21,hour=13,minute=27,second=1, microsecond=283311)
print(a_little_ago)

dt_other = dt.datetime(
    year=2021,
    month=8,
    day=21,)
print(dt_other)

dt0 = dt.datetime(year=2019, month=12, day=31)
dt1 = dt.datetime(year=2020, month=1, day=1)
delta = dt1 ‑ dt0
print(delta)

date = dt.datetime(2023, 12, 31, 9, 30, 33)
s = date.strftime('%d %b %Y, %I‑%M‑%S%p')
print(s)

x = dt.datetime(2023, 12, 31, 9, 30, 33)
result = x.strftime("%A of week number of the year %Y")
print(result)

prc = pd.read_csv(CSVLOC, parse_dates=['Date'], index_col='Date')
result = prc.loc['2019‑03'].iloc[14]
print(result)
