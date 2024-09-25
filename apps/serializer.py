from rest_framework.serializers import ModelSerializer

from apps.models import LoginRegister, MyProfile, MyListing, Category, Product, Favorite, My_wallets, Product_detail, \
    Write_to_Author


class LoginRegisterModelSerializer(ModelSerializer):
    class Meta:
        model = LoginRegister
        fields = "__all__"
        read_only_fields = ['is_verified']


class MyProfileModelSerializer(ModelSerializer):
    class Meta:
        model = MyProfile
        fields = "__all__"


class MyListingModelSerializer(ModelSerializer):
    class Meta:
        model = MyListing
        fields = "__all__"


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class FavoriteModelSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class My_walletsModelSerializer(ModelSerializer):
    class Meta:
        model = My_wallets
        fields = "__all__"


class Product_detailModelSerializer(ModelSerializer):
    class Meta:
        model = Product_detail
        fields = "__all__"


class Write_to_AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Write_to_Author
        fields = "__all__"
