import random

from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import MyProfile, MyListing, Category, Product, Favorite, My_wallets, Product_detail, \
    Write_to_Author
from apps.serializer import LoginRegisterModelSerializer, MyProfileModelSerializer, MyListingModelSerializer, \
    CategoryModelSerializer, ProductModelSerializer, FavoriteModelSerializer, My_walletsModelSerializer, \
    Product_detailModelSerializer, Write_to_AuthorModelSerializer
from .models import LoginRegister


class VerifySMSAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        sms_verify_code = request.data.get('sms_verify')

        try:
            user = LoginRegister.objects.get(user_id=user_id)
            if user.sms_verify == sms_verify_code:
                user.is_verified = True
                user.save()
                return Response({"message": "User successfully verified."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)
        except LoginRegister.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
@extend_schema(tags=["LoginRegister"])
class LoginRegisterListCreateAPIView(ListCreateAPIView):
    queryset = LoginRegister.objects.all()
    serializer_class = LoginRegisterModelSerializer

    def post(self, request, *args, **kwargs):
        sms_verify_code = str(random.randint(1000, 9999))

        data = request.data.copy()
        data['sms_verify'] = sms_verify_code

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)

            email = serializer.validated_data['email']
            send_mail(
                'SMS Verification Code',
                f'Your verification code is: {sms_verify_code}',
                'Uy_Bor@example.com',
                [email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["LoginRegister"])
class LoginRegisterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LoginRegister.objects.all()
    serializer_class = LoginRegisterModelSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Create your views here.
@extend_schema(tags=["MyProfile"])
class MyProfileListCreateAPIView(ListCreateAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileModelSerializer


@extend_schema(tags=["MyProfile"])
class MyProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileModelSerializer


# Create your views here.
@extend_schema(tags=["MyListing"])
class MyListingListCreateAPIView(ListCreateAPIView):
    queryset = MyListing.objects.all()
    serializer_class = MyListingModelSerializer


@extend_schema(tags=["MyListing"])
class MyListingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyListing.objects.all()
    serializer_class = MyListingModelSerializer


# Create your views here.
@extend_schema(tags=["Category"])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=["Category"])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


# Create your views here.
@extend_schema(tags=["Product"])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


@extend_schema(tags=["Product"])
class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


# Create your views here.
@extend_schema(tags=["Favorite"])
class FavoriteListCreateAPIView(ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteModelSerializer


@extend_schema(tags=["Favorite"])
class FavoriteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteModelSerializer


# Create your views here.
@extend_schema(tags=["My_wallets"])
class My_walletsListCreateAPIView(ListCreateAPIView):
    queryset = My_wallets.objects.all()
    serializer_class = My_walletsModelSerializer


@extend_schema(tags=["My_wallets"])
class My_walletsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = My_wallets.objects.all()
    serializer_class = My_walletsModelSerializer


# Create your views here.
@extend_schema(tags=["Product_detail"])
class Product_detailListCreateAPIView(ListCreateAPIView):
    queryset = Product_detail.objects.all()
    serializer_class = Product_detailModelSerializer


@extend_schema(tags=["Product_detail"])
class Product_detailRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product_detail.objects.all()
    serializer_class = Product_detailModelSerializer


# Create your views here.
@extend_schema(tags=["Write_to_Author"])
class Write_to_AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Write_to_Author.objects.all()
    serializer_class = Write_to_AuthorModelSerializer


@extend_schema(tags=["Write_to_Author"])
class Write_to_AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Write_to_Author.objects.all()
    serializer_class = Write_to_AuthorModelSerializer
