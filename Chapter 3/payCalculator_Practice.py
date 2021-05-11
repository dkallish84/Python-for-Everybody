hrs = input("Enter hours: ")
h = float(hrs)
rate = input("Enter rate: ")
r = float(rate)

if h > 40 :
    over_h = h - 40
    over_r = r * 1.5
    print((40 * r) + (over_h * over_r))
else :
    print(h * r)
