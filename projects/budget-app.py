class Category:

    def __init__(self, name_of_category):
        self.name_of_category = name_of_category
        self.total = 0
        self.spend = 0
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.total = self.total + amount
        self.ledger.append({"amount": amount, "description": description})
        # print("deposit: ", self.total, self.ledger)

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            self.total = self.total - amount
            self.ledger.append({"amount": -amount, "description": description})
            self.spend = self.spend + amount
            # print("withdraw: ", self.total, self.ledger)
            return True
        else:
            return False

    def get_balance(self, ):
        # print("balance: ", self.total)
        return(self.total)

    def transfer(self, amount, destination_category):
        if self.check_funds(amount) == True:
            self.total = self.total - amount
            self.ledger.append({"amount": -amount, "description": "Transfer to {}".format(destination_category.name_of_category)})
            destination_category.deposit(amount, "Transfer from {}".format(self.name_of_category) )
            # print("transfer: ", self.total, self.ledger)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True

    def __str__(self):
        '''
        input: self.ledger loop item in self.ledger
        output: print_ledger consists of title_line + print_ledger + total
        
        '''
        title_line = self.name_of_category.center(30, "*") + "\n"
        
        str_ledger = ""
        for item in self.ledger:
            item["description"] = item["description"][:23].ljust(23)
            item["amount"] = f'{item["amount"]:.2f}'.rjust(7)
            str_ledger = str_ledger + item["description"] + item["amount"] + "\n"
        total = "Total: " + f'{self.total:.2f}'
        
        display_output = title_line + str_ledger + str(total)
        return display_output

# food = Category("Food")
# auto = Category("Auto")
# clothing = Category("Clothing")
# rental = Category("Rental")
# food_deposit = food.deposit(1000, "initial deposit")
# auto_deposit = auto.deposit(1000, "initial deposit")
# food_withdraw = food.withdraw(20, "groceries")
# food_withdraw = food.withdraw(15.89, "restaurant and more food for dessert")
# auto_withdraw = auto.withdraw(500, "auto parts")
# food_transfer = food.transfer(100, auto)
# food_balance = food.get_balance()
# auto_balance = auto.get_balance()

# categories = [food, clothing, auto]
def create_spend_chart(categories):
    chart_result = "Percentage spent by category\n"
    
    #calculate spend percentage
    category_list = []
    category_spend_list = []
    pct_list = []
    for category in categories:
        category_list.append(category.name_of_category)
        category_spend_list.append(category.spend)
    sum_spend = sum(category_spend_list)
    if sum_spend == 0:
        pct_list = 0 * len(category_list)
    else:
        for spend_item in category_spend_list:
            pct_item = spend_item/sum_spend 
            pct_list.append(round(pct_item * 10) * 10)

    #draw chart label and percentage
    chart_label = ''
    for i in range(100, -1, -10):
        
        chart_label = ' ' * (3-len(str(i))) + str(i) + "|"
        for pct_item in pct_list:
            if pct_item >= i:
                chart_label = chart_label + " o " 
            else:
                chart_label = chart_label + "   "
            remain = 14 - len(chart_label)
        chart_result += chart_label + ' ' * remain + "\n" 
    chart_result +=  "    " + "-" * 10 + "\n"
    
    max_len_name = max(category_list, key = len)
    horizontal = " " * 5
    name_line = ''
    for j in range(len(max_len_name)):
        name_line += horizontal
        for category_name in category_list:
            if j >= len(category_name):
                name_line += " " * 3
            else:
                name_line +=  category_name[j] + "  "
        name_line += '\n'
    chart_result = chart_result + name_line
    return chart_result[:-1]
