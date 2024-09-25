from django.db.models import Model, IntegerField, CharField, ForeignKey, CASCADE, TextField, ImageField, EmailField, \
    BooleanField


class LoginRegister(Model):
    user_id = IntegerField(unique=True)
    phone_number = IntegerField(unique=True)
    sms_verify = CharField(max_length=10, unique=True)
    email = EmailField(unique=True)  # Email maydoni qo'shildi
    is_verified = BooleanField(default=False)

    def __str__(self):
        return f"User {self.user_id}"


class MyProfile(Model):
    user_id = ForeignKey('apps.LoginRegister', on_delete=CASCADE, related_name='my_profile')
    first_name = CharField(max_length=250)
    last_name = CharField(max_length=255)


class MyListing(Model):
    user_id = ForeignKey('apps.LoginRegister', on_delete=CASCADE, related_name='my_listing')
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='my_listing')
    apartment = CharField(max_length=250)
    address = CharField(max_length=250)
    numbOFRoom = CharField(max_length=250)
    floor = CharField(max_length=250)
    FloorBuilding = CharField(max_length=250)
    remontBuilding = CharField(max_length=250)
    price = CharField(max_length=250)
    description = TextField()
    Facilities = CharField(max_length=250)
    Photos = ImageField(upload_to='photos/%Y/%m/%d/')
    phone_number = CharField(max_length=20, unique=True)


class Category(Model):
    name = CharField(max_length=250)
    slug = CharField(max_length=250)


class Product(Model):
    category_id = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
    price = CharField(max_length=250)
    Size = CharField(max_length=250)
    location = CharField(max_length=250)
    picture = ImageField(upload_to='photos/%Y/%m/%d/')


class Favorite(Model):
    user_id = ForeignKey('apps.LoginRegister', on_delete=CASCADE, related_name='favorites')
    product_id = ForeignKey('apps.Product', on_delete=CASCADE, related_name='favorites')
    filter = CharField(max_length=250)


class My_wallets(Model):
    user_id = ForeignKey('apps.LoginRegister', on_delete=CASCADE, related_name='my_wallets')
    balance = CharField(max_length=250)
    topUpBalance = CharField(max_length=250)
    History = CharField(max_length=250)


class Product_detail(Model):
    product_id = ForeignKey('apps.Product', on_delete=CASCADE, related_name='prodcut_detail')
    information = CharField(max_length=250)
    picture = ImageField(upload_to='photos/%Y/%m/%d/')
    geo_location = CharField(max_length=250)
    seller_number = CharField(max_length=20)


class Write_to_Author(Model):
    seller_number = CharField(max_length=20)
    text = CharField(max_length=250)
    product_id = ForeignKey('apps.Product_detail', on_delete=CASCADE, related_name='write_to_author')
