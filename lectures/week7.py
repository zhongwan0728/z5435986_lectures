x = df.loc['2020‑01‑03']
print(x)

x = df.loc[['2020‑01‑02', '2020‑01‑03'], 'Close']
print(x)

x = df.loc['2020‑01‑01'꞉'2020‑01‑10', ꞉]
print(x)

df2.sort_index(inplace=True) x = df2.loc['2020‑01‑03'꞉'2020‑01‑10', ꞉]
print(x)
x = df.loc['2020‑01‑03'꞉'2020‑01‑03']
print(x)

df = pd.DataFrame(
{
'col1'꞉ range(10),
'col2'꞉ range(10, 20) index=list('acgfhibdje') )
result = df.loc[['b', 'd', 'f', 'j'], ['col1']]
print(result)

x = ser.iloc[[0, 2]]
print(x)

