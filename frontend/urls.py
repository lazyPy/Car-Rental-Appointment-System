from django.urls import path

from frontend import views


urlpatterns = [
    # Core Pages
    path('', views.view_home, name='home'),

    # Authentication URLs
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Password Management
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uuid:token>/', views.reset_password, name='reset_password'),

    # User Profile Management
    path('profile/', views.user_profile, name='profile'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),

    # Car Browsing
    path('cars/', views.view_cars, name='cars'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('check-car-availability/', views.check_car_availability, name='check_car_availability'),

    # Reservation Management
    path('create-reservation/<int:car_id>/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.view_reservations, name='reservations'),
    path('cancel-reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),

    # Payment Processing
    path('payment/<int:reservation_id>/', views.view_payment, name='payment'),
    path('process-receipt/<int:reservation_id>/', views.process_payment, name='process_payment'),
    path('payment-confirmation/<int:reservation_id>/', views.payment_confirmation,
         name='payment_confirmation'),

    # Static Pages and Support
    path('contact-us/', views.contact_us, name='contact_us'),
    path('rental-policy/', views.rental_policy, name='rental_policy'),
]