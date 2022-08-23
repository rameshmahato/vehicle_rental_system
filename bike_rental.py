class BikeShop:

    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes", self.stock)

    
    def BikeforRent(self, a): # a is variable of available bikes
        if a <= 0:
            print('Please enter the positive value.')

        elif a > self.stock:
            print('Enter the value less than available stock')

        else:
            print("Price per bike in rent is 100 for 1 hours.\nPrice may vary depent up on use.\nHave a safe ride.\nAccidental insurance is not included in this bill amount.")
            print("Total Prices", a*100) # enter the amount of per bike service

            print("Total Bikes available in stock: ", self.stock - a)


while True:
    obj = BikeShop(100)
    uc = int(input('''
    1. Display Stocks
    2. Rent a Bike
    3. Exit
    '''))

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        # create a variable with any name like n
        n = int(input('Enter the number of Bike required: '))
        obj.BikeforRent(n)

    else:
        break





