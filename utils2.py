
# Define some products and their categories
PRODUCTS = {
    'smartx pro phone': {
        'category': 'Smartphones and Accessories',
        'description': 'A high-end smartphone with a 6.5-inch OLED display and a 5000mAh battery.',
        'price': '$999'
    },
    'fotosnap camera': {
        'category': 'Cameras and Camcorders',
        'description': 'A compact point-and-shoot camera with 20MP resolution and 5x optical zoom.',
        'price': '$299'
    },
    'dslr fotosnap camera': {
        'category': 'Cameras and Camcorders',
        'description': 'A professional DSLR camera with a full-frame sensor and interchangeable lenses.',
        'price': '$1299'
    },
    'tv': {
        'category': 'Televisions and Home Theater Systems',
        'description': 'A 55-inch 4K UHD Smart TV with HDR and built-in streaming apps.',
        'price': '$649'
    }
}

def get_products_from_query(query):
    # Extract product information based on user query
    found_products = {}
    for product_name, product_details in PRODUCTS.items():
        if product_name in query:
            found_products[product_name] = product_details
    return found_products

def read_string_to_list(product_string):
    # Convert the product string to a list of products
    return list(product_string.keys())

def get_mentioned_product_info(product_list):
    return {product_name: PRODUCTS[product_name] for product_name in product_list}

def answer_user_msg(user_msg, product_info):
    response = "Here's the information you requested:\n\n"
    for product, details in product_info.items():
        response += f"{product} ({details['category']}):\n"
        response += f"Description: {details['description']}\n"
        response += f"Price: {details['price']}\n\n"
    return response