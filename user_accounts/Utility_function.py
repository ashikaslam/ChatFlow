
# ............................. email send code .................
# email send moudles
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
import random





     
     
     
   
# email sendgin functons .......................
def send_link_for_pass_set(email,link):
    try:
        email_id = email
        email_subject = "Reste your password!!!"
        email_body = render_to_string('pass_set.html', {'link' : link})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return True
    except Exception as  e:
        print(e)
        return False 
   
def send_otp_for_registration(email,otp):
    try:
        otp = str(otp)
        email_id = email
        email_subject ="Varify your email"
        email_body = render_to_string('create_id.html', {'otp':otp,'otp1':otp[0],'otp2':otp[1],'otp3':otp[2],'otp4':otp[3],'otp5':otp[4],'otp6':otp[5]})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return True
    except Exception as  e:
        print(e)
        return False


# others  functions

def generate_otp():
        """Generate a random 4-digit OTP."""
        return random.randint(100000, 999999)  






# unused functions....

def send_email(email,link): 
    try:
        email_id = email
        email_subject = "sub!!!"
        email_body = render_to_string('active_email.html', {'link' : link})
        email = EmailMultiAlternatives(email_subject , '', to=[email_id])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return Response({"message":"successsfully email sent","status":1},status=status.HTTP_200_OK)

    except Exception as  e:
               print('here')
               return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)