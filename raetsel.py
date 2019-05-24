class PetShop:
    money_limit = 10000
    animal_limit = 100

    pig_price = 1500
    dog_price = 100
    mouse_price = 15

    pig_name = 'pig'
    dog_name = 'dog'
    mouse_name = 'mouse'

    pig_counter = 0
    dog_counter = 0
    mouse_counter = 0
    animal_counter = 0
    money = 0
    prev_money = 0

    def __init__(self, money_limit, animal_limit):
        self.money_limit = money_limit
        self.animal_limit = animal_limit

    def buy_pig(self):
        self.pig_counter = self.buy_animal(self.pig_name, self.pig_price, self.pig_counter)

    def buy_dog(self):
        self.dog_counter = self.buy_animal(self.dog_name, self.dog_price, self.dog_counter)

    def buy_mouse(self):
        self.mouse_counter = self.buy_animal(self.mouse_name, self.mouse_price, self.mouse_counter)

    def buy_animal(self, name, price, counter):
        if counter is None:
            counter = 0

        if self.money + price <= self.money_limit and self.animal_counter + 1 <= self.animal_limit:
            counter += 1
            self.animal_counter += 1
            self.money += price
            # print("buyed " + name + " nr: " + str(counter))
        return counter

    def sell_pig(self):
        self.pig_counter = self.sell_animal(self.pig_name, self.pig_price, self.pig_counter)

    def sell_dog(self):
        self.dog_counter = self.sell_animal(self.dog_name, self.dog_price, self.dog_counter)

    def sell_mouse(self):
        self.mouse_counter = self.sell_animal(self.mouse_name, self.mouse_price, self.mouse_counter)

    def sell_animal(self, name, price, counter):
        if counter > 1:
            counter -= 1
            self.animal_counter -= 1
            self.money -= price
            print("selled " + name + ". now we have " + str(counter) + " " + name + " left.")
        return counter

    def first_try(self):
        while self.money != self.prev_money:
            self.prev_money = self.money
            self.buy_pig()
            self.buy_dog()
            self.buy_mouse()

        self.print_results('first')
        self.reset()

    def second_try(self):
        self.buy_pig()
        self.buy_dog()
        while self.money != self.prev_money:
            self.prev_money = self.money
            self.buy_mouse()

        self.print_results('second')
        self.reset()

    def third_try(self):


        self.print_results('third')
        self.reset()

    def print_results(self, name):
        money_done = False
        animals_done = False
        print("------------------------- result " + name + "-------------------------------")
        print("money spend: " + str(self.money) + " / " + str(self.money_limit))
        if self.money == self.money_limit:
            print("money SUCCESS!")
            money_done = True
        else:
            print("money FAIL!")
        print("animals buyed: " + str(self.animal_counter) + " / " + str(self.animal_limit))
        if self.animal_counter == self.animal_limit and self.pig_counter > 0 and self.dog_counter > 0 and self.mouse_counter > 0:
            print("animals SUCCESS!")
            animals_done = True
        else:
            print("animals FAIL!")
        print("pigs buyed: " + str(self.pig_counter))
        print("dogs buyed: " + str(self.dog_counter))
        print("mice buyed: " + str(self.mouse_counter))
        if money_done and animals_done:
            print("IT IS DONE!")

    def reset(self):
        self.pig_counter = 0
        self.dog_counter = 0
        self.mouse_counter = 0
        self.animal_counter = 0
        self.money = 0
        self.prev_money = self.money_limit
        print("------------------------- reset -------------------------------")


p = PetShop(10000, 100)
p.reset()
p.first_try()
p.second_try()
p.third_try()
