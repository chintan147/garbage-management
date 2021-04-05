from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),
    path('sign-up', views.Signup, name='sign-up'),
    path('log-in', views.Login, name='log-in'),
    path('otp', views.OTPPage, name='otp-page'),
    path('otp_verify', views.OTPVerify, name='otp-verify'),

    #Admin
    path('adminindex/', views.AdminIndex, name='admin-index'),
    path('adminprofile/<int:pk>', views.GCProfile, name='admin-profile'),
    path('adminprofileedit/<int:pk>', views.GCProfileEdit, name='admin-profile-edit'),
    path('admininbox', views.AdminInBox, name='admin-inbox'),
    path('admin_payments', views.AdminPayments, name='admin-payments'),
    path('admin_posts', views.AdminPosts, name='admin-posts'),
    path('admin_products', views.AdminProducts, name='admin-products'),
    path('admin_product', views.AdminProduct, name='admin-product'),
    path('admin_order', views.AdminOrder, name='admin-order'),
    path('admin_orders', views.AdminOrders, name='admin-orders'),
    path('admin_requests', views.AdminViewRequests, name='admin-view-requests'),
    path('upload_product', views.UploadProduct, name='upload-product'),

    #User
    path('index', views.UserIndex, name='user-index'), #User logged In

    #Header
    path('shop', views.Shop, name='shop'),
    path('blog', views.Blog, name='blog'),
    path('contact', views.Contact, name='contact'),
   
    path('XX/', views.XX, name='XX'),
    path('services', views.Services, name='services'),

    #requests
    path('user_request/<int:pk>', views.UserRequests, name='user-requests'),


    #GC
    path('requests/', views.ViewRequests, name='requests'),
    path('gcprofile/<int:pk>', views.GCProfile, name='gc-profile'),
    path('gcprofileedit/<int:pk>', views.GCProfileEdit, name='gc-profile-edit'),
    path('gcinbox', views.GCInBox, name='gc-inbox'),
    path('gc_post', views.GCPost, name='gc-post'),
    path('gc_posts', views.GCPosts, name='gc-posts'),
    path('gc_products/<int:pk>', views.GCProducts, name='gc-products'),
    path('gc_product/<int:pk>', views.GCProduct, name='gc-product'),
    path('gc_order', views.GCOrder, name='gc-order'),
    path('gc_orders/<int:pk>', views.GCOrders, name='gc-orders'),
    path('select_gc', views.SelectGC, name='select-gc'),
    path('search_gc', views.SearchGC, name='search-gc'),
    path('schedule/<int:pk>', views.Schedule, name='schedulepickup'),
    path('reqstatus/<int:pk>', views.UpdateReqStatus, name='reqstatus'),
    
    #Consumer Details
    path('consumer_details/<int:pk>', views.ConsumerDetails, name='consumer-details'),

    #GC Payment Page
    path('gc_payment', views.GCPayment, name='gc-payment'),

    path('admin_payment_details/<int:pk>', views.AdminViewPaymentDetails, name='admin-payment-details'),


    #cart
    path('cart/<int:pk>', views.CartPage, name='cart'),
    path('cartitems/', views.CartItems, name='cartitems'),
    path('del_cart/<int:pk>', views.DelCartItem, name='delete-cartitem'),


    #functionality
    path('register-data', views.RegisterData, name='register-data'),
    path('login-data', views.LoginData, name='login-data'),
    path('log-out', views.LogOut, name='log-out'),
    path('gc_saveprofile/<int:pk>', views.GCProfileSave, name='gc-saveprofile'),
    path('request-pickup/<int:pk>', views.RequestPickup, name='request-pickup'),
    path('save-product/<int:pk>', views.SaveProduct, name='save-product'),
    path('show-products', views.ShowProducts, name='show-products'),
     path('sendmessage<int:pk>', views.SendMessage, name='send-message'),



]
