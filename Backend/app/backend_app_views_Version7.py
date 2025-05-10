from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .reports import FinancialReports
from .tax import TaxCalculator
from .currency import CurrencyConverter
from .pdf import generate_pdf
from .templates_manager import TemplateManager
import json

# Dummy transactions for demonstration purposes
TRANSACTIONS = [
    {"date": "2025-01-01", "type": "Income", "amount": 1000},
    {"date": "2025-01-02", "type": "Expense", "amount": 200},
    {"date": "2025-01-03", "type": "Income", "amount": 500},
    {"date": "2025-01-04", "type": "Expense", "amount": 300},
]

template_manager = TemplateManager()


@csrf_exempt
def generate_profit_loss_report(request):
    if request.method == "POST":
        data = json.loads(request.body)
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        reports = FinancialReports(TRANSACTIONS)
        report = reports.generate_profit_and_loss(start_date, end_date)
        return JsonResponse(report.to_dict(orient="records"), safe=False)


@csrf_exempt
def calculate_tax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get("amount")
        tax_rate = data.get("tax_rate")

        tax_calculator = TaxCalculator(tax_rate)
        result = tax_calculator.calculate_tax(amount)
        return JsonResponse(result)


@csrf_exempt
def get_exchange_rates(request):
    if request.method == "GET":
        currency_converter = CurrencyConverter()
        rates = currency_converter.fetch_exchange_rates()
        return JsonResponse(rates)


@csrf_exempt
def convert_currency(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = data.get("amount")
        from_currency = data.get("from_currency")
        to_currency = data.get("to_currency")

        currency_converter = CurrencyConverter()
        result = currency_converter.convert_currency(amount, from_currency, to_currency)
        return JsonResponse(result)


@csrf_exempt
def generate_report_pdf(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")

        file_path = generate_pdf(title, content)
        with open(file_path, "rb") as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="{title}.pdf"'
            return response


@csrf_exempt
def list_templates(request):
    if request.method == "GET":
        templates = template_manager.list_templates()
        return JsonResponse({"templates": templates})


@csrf_exempt
def render_template(request):
    if request.method == "POST":
        data = json.loads(request.body)
        template_name = data.get("template_name")
        context = data.get("context", {})

        rendered_template = template_manager.render_template(template_name, context)
        return HttpResponse(rendered_template, content_type="text/html")


@csrf_exempt
def send_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        recipient_email = data.get("recipient_email")
        subject = data.get("subject")
        body = data.get("body")
        attachment_path = data.get("attachment_path", None)

        from .email_service import EmailService

        email_service = EmailService(
            smtp_server="smtp.example.com",
            smtp_port=587,
            username="your_email@example.com",
            password="your_password",
        )

        result = email_service.send_email(
            recipient_email, subject, body, attachment_path
        )
        return JsonResponse({"message": result})