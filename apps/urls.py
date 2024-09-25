from django.urls import path

from apps.views import LoginRegisterListCreateAPIView, LoginRegisterRetrieveUpdateDestroyAPIView, \
    MyProfileListCreateAPIView, MyProfileRetrieveUpdateDestroyAPIView, MyListingListCreateAPIView, \
    MyListingRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, \
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, FavoriteListCreateAPIView, \
    FavoriteRetrieveUpdateDestroyAPIView, My_walletsListCreateAPIView, My_walletsRetrieveUpdateDestroyAPIView, \
    Product_detailListCreateAPIView, Product_detailRetrieveUpdateDestroyAPIView, Write_to_AuthorListCreateAPIView, \
    Write_to_AuthorRetrieveUpdateDestroyAPIView, VerifySMSAPIView

urlpatterns = [
    path('login/register/', LoginRegisterListCreateAPIView.as_view(), name='login-register'),
    path('login/verify/', VerifySMSAPIView.as_view(), name='verify-sms'),
    path('LoginRegister/<int:pk>', LoginRegisterRetrieveUpdateDestroyAPIView.as_view()),
    path('MyProfile/', MyProfileListCreateAPIView.as_view()),
    path('MyProfile/<int:pk>', MyProfileRetrieveUpdateDestroyAPIView.as_view()),
    path('MyListing/', MyListingListCreateAPIView.as_view()),
    path('MyListing/<int:pk>', MyListingRetrieveUpdateDestroyAPIView.as_view()),
    path('Category/', CategoryListCreateAPIView.as_view()),
    path('Category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('Product/', ProductListCreateAPIView.as_view()),
    path('Product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('Favorite/', FavoriteListCreateAPIView.as_view()),
    path('Favorite/<int:pk>', FavoriteRetrieveUpdateDestroyAPIView.as_view()),
    path('My_wallets/', My_walletsListCreateAPIView.as_view()),
    path('My_wallets/<int:pk>', My_walletsRetrieveUpdateDestroyAPIView.as_view()),
    path('Product_detail/', Product_detailListCreateAPIView.as_view()),
    path('Product_detail/<int:pk>', Product_detailRetrieveUpdateDestroyAPIView.as_view()),
    path('Write_to_Author/', Write_to_AuthorListCreateAPIView.as_view()),
    path('Write_to_Author/<int:pk>', Write_to_AuthorRetrieveUpdateDestroyAPIView.as_view()),
]
