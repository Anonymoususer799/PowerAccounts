from django.urls import path
from app import views

urlpatterns = [
    path('reports/profit-loss/', views.generate_profit_loss_report),
    path('tax/calculate/', views.calculate_tax),
    path('currency/exchange-rates/', views.get_exchange_rates),
    path('currency/convert/', views.convert_currency),
    path('pdf/generate/', views.generate_report_pdf),
    path('templates/list/', views.list_templates),
    path('templates/render/', views.render_template),
    path('email/send/', views.send_email),
]