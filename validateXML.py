import xml.etree.ElementTree as ET

tree = ET.parse('transaction.xml')
root = tree.getroot()

find_net_sale = root.find('./itemization/element/gross_sales_money/amount')
net_sale = find_net_sale.text


find_tax_rate = root.find("./itemization/element/taxes/element/rate")
tax_rate = find_tax_rate.text


find_price_with_tax = root.find("./itemization/element/total_money/amount")
price_with_tax = find_price_with_tax.text

net_sale_calculated = int(int(price_with_tax) / (float(tax_rate) + 1))


def validate_xml():
    print("The tax rate retrieved from XML file =" , tax_rate)
    print("The total price retrieved from XML file =" , price_with_tax)
    print("The net sale retrieved from XML file =" , net_sale)
    print("The net sale calculated from this program =" , net_sale_calculated)
    if int(net_sale_calculated) == int(net_sale):
        return("The net sale calculated is equal to the net sale retrieved from XML file")
    else:
        return("The net sale calculated is not equal to the net sale retrieved from XML file")


print(validate_XML())
