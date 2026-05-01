import pprint
from databases import Session, Product
import requests



names = {"title": "name", "image": "image_filename"}


def get_all_products():
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()

    result = []
    with Session() as session:
        count = session.query(Product).count()
    for product in products:
        new_product = {}
        for key, value in product.items():
            new_key = names.get(key, key)
            new_product[new_key] = value
        new_product["id"] += count

        result.append(new_product)

    return result


if __name__ == "__main__":
    pprint.pprint(get_all_products())
