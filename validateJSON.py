import json
from jsonschema import validate

#Here Iam open the JSON file through python
f = open('transaction.json');
data = json.load(f);

# Here Iam checking if the tax from the JSON file is a number or not
schema = {
    "type" : "number",
    "property" : {
        "data['taxes'][0]['rate']" : {"type"}}}
validate(instance=data['taxes'][0]['rate'], schema=schema)

tax_rate =data['taxes'][0]['rate']; 
price_with_tax = data["total_collected_money"]["amount"];
net_sale = data["itemization"][0]["net_sales_money"]["amount"];
net_sale_calculated  = int(price_with_tax / (tax_rate+1) );

#Python function to check if the tax is valid or not
def validate_json():
    print("The tax rate retrieved from JSON file =" , tax_rate);
    print("The total price retrieved from JSON file =" , price_with_tax);
    print("The net sale retrieved from JSON file =" , net_sale);
    print("The net sale calculated from this program =" , net_sale_calculated);
    if (net_sale_calculated) == (net_sale):
        return("The net sale calculated is equal to the net sale retrieved from JSON file");
    else:
        return("The net sale calculated is not equal to the net sale retrieved from JSON file");


print(validate_JSON())

