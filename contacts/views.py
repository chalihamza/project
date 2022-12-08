from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from contacts.models import Contact


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        firstname = request.POST.get('firstname', False)
        lastname = request.POST.get('lastname', False)
        car_tital = request.POST.get('car_tital', False)
        customer_need = request.POST['customer_need']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(car_id=car_id, user_id=user_id, FirstName=firstname, LastName=lastname,
                          car_tital=car_tital, customer_need=customer_need, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your request has been sub')
        return redirect('/cars/' + car_id)
