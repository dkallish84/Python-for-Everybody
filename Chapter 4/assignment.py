# Compute the pay, inncluding 1.5 pay rate above 40 hours, includes error checking

def computepay(h, r):
    if h > 40:
        return (40 * r) + ((h - 40) * (r * 1.5))
    else:
        return h * r

hrs = input('Enter Hours: ')
try:
    h = float(hrs)
    rate = input('Enter Rate: ')
    try:
        r = float(rate)
        p = computepay(h, r)
        print('Pay', p)
    except:
        print('Please enter a number for your pay rate.')
except:
    print('Please enter a number for your hours.')
