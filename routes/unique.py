import requests
from flask import jsonify

def unique():
    response = requests.get('https://lager.emilfolino.se/v2/products/everything')
    data = response.json()
    print(data)

    if isinstance(data, dict):
        data = data.get('data', [])

    unique_items = {}
    for item in data:
        name = item['name']
        stock = item['stock']
        if stock is None:
            stock = 0
        elif isinstance(stock, str):
            try:
                stock = int(stock)
            except ValueError:
                stock = 0
        
        found = False
        for key in unique_items.keys():
            if name.lower() in key.lower() or key.lower() in name.lower():
                unique_items[key]['stock'] += stock
                found = True
                break
        
        if not found:
            unique_items[name] = {'name': name, 'stock': stock}

    return jsonify({"data": list(unique_items.values())})