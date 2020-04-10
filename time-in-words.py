hr = int(input())
min = int(input())
def totext(num):
    numbers = [
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"]
    return numbers[num]
if(min == 0):
    print(totext(hr)+" o' clock")
elif(min < 30):
    if(min == 15):
        print("quarter past "+totext(hr))
    elif(min == 1):
        print(totext(min)+" minute past "+totext(hr))
    else:
        print(totext(min)+" minutes past "+totext(hr))
elif(min == 30):
    print("half past "+totext(hr))
else:
    if(min == 45):
        print("quarter to "+totext(hr+1))
    elif(min == 59):
        print(totext(30-min)+" minute to "+totext(hr+1))
    else:
        print(totext(30-min)+" minutes to "+totext(hr+1))
