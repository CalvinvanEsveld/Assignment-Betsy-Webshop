from peewee import *

db = SqliteDatabase('betsy.db')

class BaseModel(Model):
    class Meta:
        database = db

class Address(BaseModel):
    street_and_number = CharField()
    postcode = CharField()
    city = CharField()
    country = CharField()

class Billing(BaseModel):
    payment_method = CharField()
    email_address = CharField()

class User(BaseModel):
    name = CharField()
    address = ForeignKeyField(Address)
    billing = ForeignKeyField(Billing)

class Tag(BaseModel):
    name = CharField(unique=True)

class Product(BaseModel):
    name = CharField()
    description = CharField()
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity = IntegerField()
    tags = ManyToManyField(Tag)
    owned_by_user = ForeignKeyField(User)

class Transactions(BaseModel):
    buyer = CharField()
    product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField()

ProductTags = Product.tags.get_through_model()