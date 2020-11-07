from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View

from .models import *
from .forms import *
from .utils import *

from django.contrib.auth.mixins import LoginRequiredMixin

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

# Create your views here.
def customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'COC/customers_list.html', context={'customers': customers})

def products_list(request):
    products = Product.objects.all()
    return render(request, 'COC/products_list.html', context={'products': products})

def price_groups_list(request):
    pricegroups = PriceGroup.objects.all()
    return render(request, 'COC/price_groups_list.html', context={'pricegroups': pricegroups})

def price_group_discounts(request):
    pricegroupdiscounts = PriceGroupDiscount.objects.all()
    return render(request, 'COC/price_group_discounts_list.html', context={'pricegroupdiscounts': pricegroupdiscounts})


class CustomerDetail(ObjectsDetailMixin, View):
    model = Customer
    template = 'COC/customer_ditail.html'

class ProductDetail(ObjectsDetailMixin, View):
    model = Product
    template = 'COC/product_ditail.html'

class PriceGroupDetail(ObjectsDetailMixin, View):
    model = PriceGroup
    template = 'COC/price_groups_ditail.html'

class PriceGroupDiscountDetail(ObjectsDetailMixin, View):
    model = PriceGroupDiscount
    template = 'COC/price_group_discount_ditail.html'


class CustomerCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = CustomerForm
    template  = 'COC/customer_create.html'
    raise_exeption = True

class ProductCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = ProductForm
    template  = 'COC/product_create.html'
    raise_exeption = True

class PriceGroupCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PriceGroupFrom
    template  = 'COC/price_group_create.html'
    raise_exeption = True

class PriceGroupDiscountCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PriceGroupDiscountFrom
    template  = 'COC/price_group_discount_create.html'
    raise_exeption = True


class CustomerUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Customer
    model_form = CustomerForm
    template = 'COC/customer_update.html'
    raise_exeption = True

class ProductUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Product
    model_form = ProductForm
    template = 'COC/product_update.html'
    raise_exeption = True

class PriceGroupUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = PriceGroup
    model_form = PriceGroupFrom
    template = 'COC/price_group_update.html'
    raise_exeption = True

class PriceGroupDiscountUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = PriceGroupDiscount
    model_form = PriceGroupDiscountFrom
    template = 'COC/price_group_discount_update.html'
    raise_exeption = True


class CustomerDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Customer
    template = 'COC/customer_delete.html'
    redirect_url = 'customers_list_url'
    raise_exeption = True

class ProductDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Product
    template = 'COC/product_delete.html'
    redirect_url = 'products_list_url'
    raise_exeption = True

class PriceGroupDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = PriceGroup
    template = 'COC/price_group_delete.html'
    redirect_url = 'price_groups_list_url'
    raise_exeption = True

class PriceGroupDiscountDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = PriceGroupDiscount
    template = 'COC/price_group_discount_delete.html'
    redirect_url = 'price_group_discounts_list_url'
    raise_exeption = True


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

seller = {
	"denomination": "Dennnis Ivanov Company",
	"address": "123 Street name",
    "index": "1234",
	"telephone": "88005553535",
	"contactPersonPhoneNumber": "86665554433",
	"contactPersonEmail": "email@mail.com",
	}

customer = {
	"denomination": "Dennnis Ivanov Company",
	"address": "123 Street name",
    "index": "1234",
	"telephone": "88005553535",
	"contactPersonPhoneNumber": "86665554433",
	"contactPersonEmail": "email@mail.com",
	}

products = [
    {
        "denomination": "Alfa pump",
    	"id": 1,
        "box_quantity": "1",
    	"price_group": "pumps",
    	"list_price": 1.5,
    },
    {
        "denomination": "Beta pump",
    	"id": 2,
        "box_quantity": "1",
    	"price_group": "pumps",
    	"list_price": 3,
    },
]


    #Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('COC/pdf_template.html', context_dict={'seller': seller, 'customer': customer, 'products': products})
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('COC/pdf_template.html', context_dict={'seller': seller, 'customer': customer, 'products': products})

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

def index(request):
	context = {}
	return render(request, 'COC/index.html', context)
