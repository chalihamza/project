from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
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

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                message.error(request, 'You have already made the inquery of this car.')
                return redirect('/cars/'+car_id)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New car inquery',
            'You have a new inquiry'+str(car_tital) +'.please check your dashboard.',
            'alihamzahamza211@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact = Contact(car_id=car_id, user_id=user_id, FirstName=firstname, LastName=lastname,
                          car_tital=car_tital, customer_need=customer_need, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your request has been sub')
        return redirect('/cars/' + car_id)
