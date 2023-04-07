# Downloads Qantas share price beginning 1 January 2020
import yfinance # (1)
tic = "QAN.AX" # (2)
start = '2020-01-01' # (3)
end = None # (4)
df = yfinance.download(tic, start, end, ignore_tz=True) # (5)
print(df) # (6)
df.to_csv('cba_stk_prc.csv')


a= "1"+"2"
print(a)

a= 1+2
print(a)

a= 4
print(a)

b=2/1
print(b)
print(type(b))

a=2
b= 3**a
c= 3**2
print(c)
print(b)

print(1==2)


