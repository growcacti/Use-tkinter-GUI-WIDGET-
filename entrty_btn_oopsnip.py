

















self.e1 = tk.Entry(self, textvariable=num1)
self.e1.grid(row=1, column=1)
self.b1 = tk.Button(self, text="Calculate", command=generate)
self b1.button.grid(row=1, column=2)
self.e2= tk.Entry(self, textvariable=num1)
self.e2.grid(row=2, column=1)
self.b2 = tk.Button(self, text="Calculate", command=generate)
self b2.button.grid(row=2, column=2)
self.e3 = tk.Entry(self, textvariable=num1)
self.e3.grid(row=3, column=1)
self.b3 = tk.Button(self, text="Calculate", command=generate)
self b3.button.grid(row=3, column=2)
self.e4= tk.Entry(self, textvariable=num1)
self.e4.grid(row=4, column=1)
self.b4 = tk.Button(self, text="Calculate", command=generate)
self b4.button.grid(row=4, column=2)


''' Count_words101.py
experiments with string processing
preprocess the string then do a word frequency count
using Counter() from the Python module collections
display words with matching frequency in alphabetical order
tested with Python27 and Python33  by  vegaseat  06sep2013
'''

from string import punctuation
from collections import Counter

# sample text for testing (could come from a text file)
text = """\
If you see a turn signal blinking on a car with a southern license plate, 
you may rest assured that it was on when the car was purchased.
""" 

# preprocess text, remove punctuation marks and change to lower case    
text2 = ''.join(c for c in text.lower() if c not in punctuation)

# get word and frequency of the words in text2
# text2.split() splits text2 at white spaces
# most_common() gives a list of all (word, freq) tuples sorted by count
# eg. most_common(10) will return a list of the 10 most common words
mc_cnt = Counter(text2.split()).most_common()

print("Words with matching frequeny have no particular order:")
for word, freq in mc_cnt:
    # newer string formatting style Python27 and higher
    print("{:3d}  {}".format(freq, word))

# clean it up, showing words with matching freq in order 
# sort by word first then sort by frequency
mc_cnt_w = sorted(mc_cnt)
mc_cnt_fw = sorted(mc_cnt_w, key=lambda tup: tup[1], reverse=True)

'''
# optional testing ...
print(mc_cnt)
print(mc_cnt_w)
print(mc_cnt_fw)
'''

print("Words with matching frequency are in order:")
for word, freq in mc_cnt_fw:
    # newer string formatting style Python27 and higher
    print("{:3d}  {}".format(freq, word))

''' result ...
Words with matching frequeny have no particular order:
  3  a
  2  you
  2  on
  2  car
  2  was
  1  southern

'''



class Wordcount(object):

    def  __init__(self, text):

        self.text = text
        self.text2 =  ''.join(c for c in text.lower() if c not in punctuation)
        self.mostcommon_count = Counter(text2.split()).most_common()
        self.mc_cnt =  self.mostcommon_count
        self.search_loop()
    def search_loop(self):
        for self.word, self.freq in self.mc_cnt:
    # newer string formatting style Python27 and higher
            self.output_str ="{:3d}  {}".format(freq, word))
            print("{:3d}  {}".format(freq, word))


        self.mc_cnt_w = sorted(self.mc_cnt)
        self.mc_cnt_fw = sorted(self.mc_cnt_w, key=lambda tup: tup[1], reverse=True)
        
