from django.shortcuts import render
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .config import username, apikey
from django.views.decorators.csrf import csrf_exempt
from .models import User, session_levels
import datetime
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def callback(request):

    if request.method == 'POST' and request.POST:
        sessionId = request.POST.get('sessionId')
        serviceCode=request.POST.get('serviceCode')
        phoneNumber=request.POST.get('phoneNumber')
        text=request.POST.get('text')
        now = datetime.datetime.now()

        textList = text.split('*')
        userResponse = textList[-1].strip()

        if level == 0:
            if userResponse == "":
                session_level1 = User.objects.get(phonenumber=phoneNumber)
                session_level1.level=1
                session_level1.save()
                #Serve the options menu
                response = "CON Welcome to FarmerService. Are you buying or selling?\n"
                response += "1. Buyer. \n"
                response += "2. Seller. \n"

                return redirect(response, content_type='text/plain')

            if userResponse == '0':
                if level == 0:
                    #7b.Graduate user to next level and serve main menu
                    session1 = session_levels(session_id=sessionId, phoneNumber=phoneNumber, level=1)
                    session1.save()
                    # Serve the options menu
                    response = "CON Welcome to FarmerService. Are you buying or selling?\n"
                    response += "1. Buyer. \n"
                    response += "2. Seller. \n"

                    return redirect(response, content_type='text/plain')

            if userResponse == "":
                if level == 1:
                    #7b.Graduate user to next level and serve main menu
                    session_level1 = User.objects.get(phonenumber=phoneNumber)
                    session_level1.level=1
                    session_level1.save()
                    #Serve the options menu
                    response = "CON Welcome to FarmerService. Are you buying or selling?\n"
                    response += "1. Buyer. \n"
                    response += "2. Seller. \n"

                    return redirect(response, content_type='text/plain')
            if userResponse == '1':
                if level == 1:


                    return redirect(response, content_type='text/plain')
        else:
            print('pass')
