__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"
import models
from peewee import *

def search(term):
    matched_products = []
    products = models.Product.select().where(models.Product.name.contains(term.lower()) | models.Product.description.contains(term.lower()))
    for product in products:
        matched_products.append(product.name)
    return matched_products

def list_user_products(user_id):
    owned_products = []
    query = (
        models.Product.select(models.Product, models.User)
        .join(models.User)
        .where(models.User.name == user_id)
        )
    for product in query:
        owned_products.append([product.name, product.description, float(product.price)])
    return owned_products

def list_products_per_tag(tag_id):
    products = []
    query = (models.Product
         .select()
         .join(models.ProductTags)
         .join(models.Tag)
         .where(models.Tag.name == tag_id.lower()))
    
    for product in query:
        products.append(product.name)

    return products

def add_product_to_catalog(user_id, product):
    user = models.User.select().where(models.User.name == user_id)
    for x in user:
        new_product = []
        new_product.append(product)
        for product in new_product:
            product = product + [x.id]
            models.Product.create(name=product[0], description=product[1], price=product[2], quantity=product[3], owned_by_user=product[4])

def update_stock(product_id, new_quantity):
    models.Product.update(quantity=new_quantity).where(models.Product.name == product_id).execute()
        
def purchase_product(product_id, buyer_id, quantity):
    query = models.Product.select().where(models.Product.name == product_id)
    for product in query:
        models.Transactions.create(buyer=buyer_id, product=product.id, quantity=quantity)
        new_quantity = product.quantity - quantity
    
    models.Product.update(quantity=new_quantity).where(models.Product.name == product_id).execute()

def remove_product(product_id):
    models.Product.delete().where(models.Product.name == product_id).execute()
    

if __name__ == "__main__": 
    print(search("Handcrafted"))
    print(list_user_products("Bob"))
    print(list_products_per_tag("lighT"))
    add_new_product = ["Lip Balsm", "Homemade Lip Balsm, made with natural ingredients", 2.50, 20]
    add_product_to_catalog("Bob", add_new_product )
    update_stock("Green Candles", 15)
    purchase_product("Necklaces", "Twan", 3)
    remove_product("Hats")