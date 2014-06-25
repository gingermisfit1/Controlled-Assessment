allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,1.7,1.25, 173] #shows exchange rates for each of the currencies
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter") #when it is started this will be shown so they know what it is

def getCurr(dir):
    answer = None
    while answer not in range(len(allowables)):
        print('Please type the currency you wish to convert {0}'.format(dir))
        for index, currency in enumerate(allowables):
            print ('enter {0} for {1}'.format(index, currency))
        answer = input("Please type what currency you wish to convert {0}".format(dir))
    return (answer)    

def getVal(c1, c2, c3):
    
    ammount = c3/rates[c1] *rates[c2]
    return (ammount)

if __name__ == "__main__":
    var1 = getCurr('from')
    var2 = getCurr('to')
    var3 = float(input("Please type the amount of currency you wish to convert "))
    print('Your converted ammount is {0:.2f}{1}'.format(getVal(var1,var2,var3),allowables[var2]))

  
