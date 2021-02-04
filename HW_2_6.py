products = []
describe_items = []
describe_template = {}
item_description = {}
analytics = {}
describe_items_number = int(input('Enter a number of characteristic you want to add to describe products: '))
i = 0
while i < describe_items_number:
    describe_items.append(input('Type the description element: '))
    i += 1
describe_template = dict.fromkeys(describe_items)
num_of_products = int(input('Enter a number of products you want to add: '))
i = 0
while i < num_of_products:
    for items in describe_items:
        describe_item_value = input('Enter a value for \"{0}\" for product {1} '.format(items, i + 1))
        try:
            describe_item_value = int(describe_item_value)
            item_description[items] = describe_item_value
            continue
        except ValueError:
            try:
                describe_item_value = float(describe_item_value)
                item_description[items] = describe_item_value
                continue
            except ValueError:
                item_description[items] = describe_item_value
    products.append((i + 1, item_description.copy()))
    i += 1
print('\nProducts:')
for prod_items in products:
    print(prod_items)
for items in describe_items:
    item_analytics = []
    for prod_items in products:
        item_analytics.append(prod_items[1].get(items))
    analytics[items] = item_analytics
print('\nAnalytics:')
for items in analytics.items():
    print(items)
