from django.shortcuts import render
from django.views.generic import DetailView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import requests
from django.shortcuts import render
from django.db.models import Sum
import re
from django.utils import timezone
import os
import time
from .models import Product, Cart, MyOrder, Merchant, Review
from django.shortcuts import get_object_or_404, redirect
import json


def home(request):
    product_list = Product.objects.all()
    new_arival = Product.objects.order_by('-date')[:6]
    return render(request, "index.html", {'product_list': product_list, 'new_arival':new_arival})


def contact(request):
    return render(request, "index.html")


def tshirt(request):
    tshirt = Product.objects.filter(
        product_category='T-Shirt')
    return render(request, "tshirt.html", {'tshirt': tshirt})

def shirt(request):
    shirt = Product.objects.filter(
        product_category='Shirt')
    return render(request, "shirt.html", {'shirt': shirt})

def jacket(request):
    jacket = Product.objects.filter(
        product_category='Winter Jacket')
    return render(request, "jacket.html", {'jacket': jacket})

def jeans(request):
    jeans = Product.objects.filter(
        product_category='Jeans')
    return render(request, "jeans.html", {'jeans': jeans})

def panjabi(request):
    panjabi = Product.objects.filter(
        product_category='Panjabi')
    return render(request, "panjabi.html", {'panjabi': panjabi})

def pajama(request):
    pajama = Product.objects.filter(
        product_category='Pajama')
    return render(request, "pajama.html", {'pajama': pajama})

def polo(request):
    polo = Product.objects.filter(
        product_category='Polo')
    return render(request, "polo.html", {'polo': polo})

def tops(request):
    tops = Product.objects.filter(
        product_category='Tops & T-Shirt')
    return render(request, "tops.html", {'tops': tops})

def kamiz(request):
    kamiz = Product.objects.filter(
        product_category='Kamiz/Kurti')
    return render(request, "kamiz.html", {'kamiz': kamiz})

def wallet(request):
    wallet = Product.objects.filter(
        product_category='Wallet')
    return render(request, "wallet.html", {'wallet': wallet})

def bag(request):
    bag = Product.objects.filter(
        product_category='Bag')
    return render(request, "bag.html", {'bag': bag})

def cap(request):
    cap = Product.objects.filter(
        product_category='Cap')
    return render(request, "cap.html", {'cap': cap})

def sunglasses(request):
    sunglasses = Product.objects.filter(
        product_category='Sunglasses')
    return render(request, "sunglasses.html", {'sunglasses': sunglasses})



def fullsleeve(request):
    organic_product = Product.objects.filter(product_category='Full Sleeve')
    return render(request, "organic.html", {'organic_product': organic_product})


def winter_jacket(request):
    hospital_product = Product.objects.filter(
        product_category='Winter Jacket')
    return render(request, "hospital.html", {'hospital_product': hospital_product})


def pant(request):
    beauty_product = Product.objects.filter(product_category='Pant')
    return render(request, "beauty.html", {'beauty_product': beauty_product})


def ladies_tshirt_c(request):
    surgical_product = Product.objects.filter(
        product_category='Ladies T-Shirt Collection')
    return render(request, "surgical.html", {'surgical_product': surgical_product})


def beauty(request):
    lab_product = Product.objects.filter(product_category='Beauty Product')
    return render(request, "lab.html", {'lab_product': lab_product})


def profile(request):
    # Retrieve MyOrder objects for the current user
    my_orders = MyOrder.objects.filter(username=request.user)

    context = {
        'my_order': my_orders,
    }

    return render(request, "profile.html", context)





def shop(request):
    return render(request, "shop.html")


def all_product(request):
    product = Product.objects.all()
    return render(request, "all_product.html", {'product': product})


def seller(request):
    if Merchant.objects.filter(username=request.user).exists():
        if Merchant.objects.filter(verified=True).exists():
            product = Product.objects.filter(username=request.user)
            merchant = "yes"
            return render(request, "dashboard.html", {'product': product, 'merchant': merchant})
        else:
            pending = "Your merchant request is under review. Please wait for verified."
            return render(request, "dashboard.html", {'pending': pending})
    else:
        merchant_not = "You are not a merchant."
        return render(request, "dashboard.html", {'merchant_not': merchant_not})


def seller_form(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        shop_name = request.POST['shop_name']
        email = request.POST['email']
        if Merchant.objects.filter(username=username).exists():
            messages.success(
                request, "You are already applied for merchant. Please wait for confirmation."

            )
            return redirect("seller")
        else:
            merchant_database = Merchant(username=username, first_name=first_name,
                                         last_name=last_name, address=address, shop_name=shop_name, email=email)
            merchant_database.save()
            return redirect('seller')
    return redirect('seller')


def became_a_seller(request):
    return render(request, "seller_form.html")


class detail(DetailView):
    model = Product
    template_name = "detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from AnotherModel (replace this with your actual query)
        another_model_data = Product.objects.all()
        review = Review.objects.all()

        # Add the data to the context
        context['another_model_dat'] = another_model_data
        context['review'] = review

        return context


def cart_form(request):
    product_name = request.POST.get('product_name', "")
    product_price = request.POST.get('product_price', "")
    photo = request.POST.get('photo', "")
    size = request.POST.get('size', "")

    if request.method == "POST" and request.user.is_authenticated:
        username = request.user
        if product_price and product_name and photo:
            cart_item = Cart(username=username, product_price=product_price,
                             product_name=product_name, photo=photo, size = size)
            cart_item.save()
            return redirect('cart')  # Redirect to the 'cart' URL name

    cart = Cart.objects.filter(username=request.user)
    return render(request, "cart.html", {'cart': cart, 'product_name': product_name, 'product_price': product_price, 'photo': photo})

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart(request):
    cart = Cart.objects.filter(username=request.user)
    cart_info = '\n'.join(
        [f"Product: {item.product_name}, Price: {item.product_price}" for item in cart])
    return render(request, "cart.html", {'cart': cart, 'cart_info': cart_info})


def remove_product_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        # Check if the product exists in the cart and belongs to the current user
        cart_item = Cart.objects.filter(
            username=request.user, id=product_id).first()
        if cart_item:
            # Remove the product from the cart
            cart_item.delete()
            messages.success(request, 'Product removed from the cart.')
    return redirect('cart')


def checkout(request):
    if request.method == "POST":
        subtotal = request.POST['subtotal']
        total = request.POST['total']
        product_details = request.POST['product_details']
        return render(request, "checkout.html", {'subtotal': subtotal, 'total': total, 'product_details': product_details})
    return render(request, "checkout.html")


# def order(request):
#     my_order = MyOrder.objects.filter(username = request.user)
#     return render(request, "order.html", {'my_order':my_order})


def order(request):
    # Retrieve MyOrder objects for the current user
    my_orders = MyOrder.objects.filter(username=request.user)

    context = {
        'my_order': my_orders,
    }

    return render(request, "order.html", context)


def review_form(request):
    if request.method == "POST":
        username = request.POST['username']
        product_id = request.POST['product_id']
        review = request.POST['review']
        review_database = Review(
            username=username, product_id=product_id, review=review)
        review_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_order(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        country = request.POST.get("country")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip")
        subtotal = request.POST.get("subtotal")
        total = request.POST.get("total")
        product_details = request.POST.get("product_details")
        payment_details = request.POST.get("payment_details")
        if payment_details == "":
            payment_details = "Cash On Delivery"
        # Create a new MyOrder instance with the form data
        order = MyOrder.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address1=address1,
            address2=address2,
            country=country,
            city=city,
            state=state,
            zip=zip_code,
            subtotal=subtotal,
            total=total,
            product_details=product_details,
            payment_details=payment_details,
            # Add other model fields as needed
        )
        order.save()
        # # Email details
        # sender_email = 'order@aspen-bd.com'
        # receiver_email = email
        # subject = 'We received your order successfully'
        # message = 'Dear ' + first_name + \
        #     ',\n\nWe have received your order. Please wait for payment confirmation.\n\nThank You\nFrom AspenBD'

        # receiver_email2 = 'aspen.salesbd@gmail.com'
        # subject2 = 'New Order Sir'
        # message2 = 'Dear ' + 'AspenBD' + \
        #     ',\n\nYou have got a new order. Please check and confirm.\nDetail:' + product_details + '\n' 'Order By:' + first_name + '\nNo: ' + phone + \
        #     '\nAdress 1:' + address1 + '\nAdress 2:' + address2 + '\nCity:' + city + \
        #     '\nState:' + state + '\Zip Code:' + zip_code + 'Thank You\nFrom AspenBD'

        # # Send email
        # send_mail(
        #     subject,
        #     message,
        #     sender_email,
        #     [receiver_email],
        #     fail_silently=False,
        # )

        # send_mail(
        #     subject2,
        #     message2,
        #     sender_email,
        #     [receiver_email2],
        #     fail_silently=False,
        # )

        # You can perform additional actions here if needed
        messages.success(
            request, "You have successfully place your order. Check your order details from my_order")
        return redirect('order')  # Redirect to a success page

    return render(request, 'order.html')


def upload_product(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST['username']
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_category = request.POST['product_category']
        product_description = request.POST['product_description']
        photo = request.FILES['photo']
        extra_photo1 = request.FILES['extra_photo1']
        extra_photo2 = request.FILES['extra_photo2']
        extra_photo3 = request.FILES['extra_photo3']
        extra_photo4 = request.FILES['extra_photo4']

        # Create a new Product object
        new_product = Product(
            username=username,
            product_name=product_name,
            product_price=product_price,
            product_category=product_category,
            product_description=product_description,
            photo=photo,
            extra_photo1=extra_photo1,
            extra_photo2=extra_photo2,
            extra_photo3=extra_photo3,
            extra_photo4=extra_photo4,
        )

        # Save the new product to the database
        new_product.save()

        # Redirect to a success page or any other desired page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    if request.method == "GET":
        search_query = request.GET.get('search', '')
        if search_query:
            # Use case-insensitive search on the product_name field
            results = Product.objects.filter(
                product_name__icontains=search_query)
        else:
            # Handle the case when there's no search query provided
            results = None

        return render(request, 'search.html', {'results': results})
