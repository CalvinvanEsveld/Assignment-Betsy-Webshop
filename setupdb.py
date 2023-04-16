from models import (db, User, Product, Transactions, Address, Billing, Tag, ProductTags)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_test_data():
    db.connect()

    db.create_tables(
        [
            Address,
            Billing,
            User,
            Product,
            Transactions,
            Tag,
            ProductTags
        ]
    )

    addresses = [
        ["Bobstreet 18", "1234BB", "Bobville", "Netherlands"],
        ["Carlosstreet 15", "5432CC", "Carlosville", "Netherlands"],
        ["Paulstreet 9", "3455PP", "Paulville", "Netherlands"],
        ["Jessicastreet 78", "2833JJ", "Jessicatown", "Netherlands"],
        ["Ericastreet 34", "2433EE", "Ericaville", "Netherlands"]
    ]
    billings = [
        ["Paypal", "bobpy@wincpy.com"],
        ["Credit card", "carlospy@winpcy.com"],
        ["Ideal", "paulpy@wincpy.com"],
        ["Credit card", "jessicapy@wincpy.com"],
        ["Ideal", "ericapy@wincpy.com"]
    ]
    users = [
        ["Bob", 1, 1],
        ["Carlos", 2, 2],
        ["Paul", 3, 3],
        ["Jessica", 4, 4],
        ["Erica", 5, 5]
    ]
    transactions = [
        ["Eric", 1, 5],
        ["Tom", 2, 2]
    ]

    for address in addresses:
        Address.create(street_and_number=address[0], postcode=address[1], city=address[2], country=address[3])

    for billing in billings:
        Billing.create(payment_method=billing[0], email_address=billing[1])

    for user in users:
        User.create(name=user[0], address=user[1], billing=user[2])

    for transaction in transactions:
        Transactions.create(buyer=transaction[0], product=transaction[1], quantity=transaction[2])

    p1 = Product.create(name="Green Candles", description= "Homemade Candles", price=2.50, quantity=20, owned_by_user=1)
    p2 = Product.create(name="Blue Candles", description= "Homemade Candles", price=2.50, quantity=20, owned_by_user=2)
    p3 = Product.create(name="Soap", description= "High-quality homemade soap", price=1.50, quantity=40, owned_by_user=3)
    p4 = Product.create(name="Greeting cards", description= "Handmade greeting cards", price=0.75, quantity=20, owned_by_user=4)
    p5 = Product.create(name="Necklaces", description= "Handcrafted necklaces made with passion", price=13.00, quantity=15, owned_by_user=5)
    p6 = Product.create(name="Bracelets", description= "Handcrafted bracelets made with passion", price=13.00, quantity=15, owned_by_user=3)
    p7 = Product.create(name="Scarves", description= "Hand-knitten scarves for winter", price=10.75, quantity=13, owned_by_user=2)
    p8 = Product.create(name="Hats", description= "Hand-sewn hats for summer", price=7.50, quantity=10, owned_by_user=5)

    t1 = Tag.create(name='candles')
    t2 = Tag.create(name='scented')
    t3 = Tag.create(name='homemade')
    t4 = Tag.create(name='green')
    t5 = Tag.create(name='blue')
    t6 = Tag.create(name='soap')
    t7 = Tag.create(name='bathing')
    t8 = Tag.create(name='writing')
    t9 = Tag.create(name='cards')
    t10 = Tag.create(name='jewelry')
    t11 = Tag.create(name='necklaces')
    t12 = Tag.create(name='bacelets')
    t13 = Tag.create(name='winter')
    t14 = Tag.create(name='clothing')
    t15 = Tag.create(name='summer')
    t16 = Tag.create(name='sun')
    t17 = Tag.create(name='hat')
    t18 = Tag.create(name='light')

    p1.tags.add([t1, t2, t3, t4, t18])
    p2.tags.add([t1, t2, t3, t5, t18])
    p3.tags.add([t2, t6, t7])
    p4.tags.add([t8, t9])
    p5.tags.add([t10, t11])
    p6.tags.add([t10, t12])
    p7.tags.add([t13, t14])
    p8.tags.add([t15, t16, t17])