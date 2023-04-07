fobj = open(SRCFILE, mode='r')
for line in fobj:
 print(line)

 with open(DSTFILE, mode='w') as fobj:
     fobj.write('This is a line')
     fobj.write('This is a another line')
 print_lines(DSTFILE)

 with open(DSTFILE, mode='w') as fobj:
     fobj.write('This is a line\n')
     fobj.write('This is a another line')
 print_lines(DSTFILE)


 def freqword(filepath):
     with open(filepath) as file:
     # Count word frequency
     counts = dict()
     for line in file:
         words = line.split()
     for word in words:
         counts[word] = counts.get(word, 0) + 1
     # Find the most frequent word
     maxcount = None
     maxword = None
     for word, count in counts.items():
         if maxcount is None or count > maxcount:
             maxword = word
     maxcount = count
     # Return the result
     return (f"The most frequent word is: {maxword}, and the number of times appeared is: {maxcount}")
 freqword('iso.txt')

 prcs = ser['2020-01-06':'2020-01-10']
 print(prcs)

 ser = pd.Series(data=prices, index=dates)
 # Use the `index` attribute to get the index from a series
 the_index = ser.index
 print(the_index)

 # Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
 # '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
 # dtype='object')
 # Replace the existing index with another with different values
 ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000]  # Note the -4 and 1000
 print(ser.index)

 import pandas as pd

 df = pd.DataFrame(
     {
         'a': [1, 2, 3],
         'b': [4, 5, 6],
     },
     index=['c', 'd', 'e']
 )
 print(df)

 new_ser = pd.Series(data=[1, 3, 2], index=['a', 'c', 'b'])
 print(new_ser.is_monotonic_increasing)