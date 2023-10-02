# currency converter

amount =input('Enter the amount of cash you want to be converted:  ')
rate=str(input('Enter conversion unit:')).lower()

def converter(amount,currency,rate):
    currency = ['USD','KSH','POUND']
    
    KSH_to_USD = 0.01
    KSH_to_POUND = 0.75
    USD_to_POUND = 0.82

    if currency == 'USD' and rate == 'KSH':
        converted = amount * KSH_to_USD
        print(f'your{currency} to {rate} is: {converted} ')
    elif currency == 'KSH' and rate == 'USD':
        converted = amount/KSH_to_USD
        print(f'your{currency} to {rate} is: {converted} ')
    elif currency == 'KSH' and rate == 'POUND':
        converted = amount * KSH_to_POUND
        print(f'your{currency} to {rate} is: {converted} ')
    elif currency == 'USD' and rate == 'POUND':
        converted = amount * USD_to_POUND
        print(f'your{currency} to {rate} is: {converted} ')
    elif currency == 'POUND' and rate == 'USD':
        converted = amount/ USD_to_POUND
        print(f'your{currency} to {rate} is: {converted} ')
    else:
        converted = None
        print('No currency inserted')
    


amount_ = float(amount)
usercurrency = input('Select USD , KSH or POUND: ').lower()
rate_=float(rate)

converter(amount_,usercurrency,rate_)
