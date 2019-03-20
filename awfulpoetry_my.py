import random
import sys

art = ["the", "a", "another", "her", "his"]
suzh = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
glag = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
nar = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]
pred = [[art,suzh,glag,nar],[art,suzh,glag]]

strings = 5
count = 0
if len(sys.argv) > 1:
    tmp = int(sys.argv[1])
    if 1 <= tmp <= 10:
        strings = tmp
    else:
        print("Usage: aw.py <num> , 1<=num<=10" )  
else:
    print("Usage: aw.py <num> , 1<=num<=10" )
    print("Using default value 5 now:")      
while count < strings:
    string = ""
    pred1 = pred[random.randint(0,1)]
    for word in pred1:
        string += random.choice(word)
        string += " "
    count += 1
    print(string)

