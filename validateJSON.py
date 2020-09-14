import json


class JsonData:
    def __init__(self):
        self.data = []

        
    def validate(self):
        with open("transaction.json") as read_file:
          self.data = json.load(read_file)

        tax_rate =self.data["taxes"][0]["rate"]
        price_with_tax = self.data["total_collected_money"]["amount"]
        net_sale = self.data["itemization"][0]["net_sales_money"]["amount"]
        net_sale_calculated  = int(price_with_tax / (tax_rate+1) )

        if (net_sale_calculated) == (net_sale):
            return("The net sale calculated is equal to the net sale retrieved from JSON file")
        else:
            return("The net sale calculated is not equal to the net sale retrieved from JSON file")



test1 = JsonData()
print(test1.validate())