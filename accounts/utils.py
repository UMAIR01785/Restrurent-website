from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def detectuser(user):
    if user.role == 1:
        redirectUrl = 'cusdashboard'
    elif user.role == 2:
        redirectUrl = 'vendordashboard'
    elif user is not None and user.is_superuser:   # ✅ fix here
        redirectUrl = '/admin'
    else:
        redirectUrl = 'login'  # optional fallback
    return redirectUrl



def send_verfication_email(request,user):
    current_url=get_current_site(request)
    mail_subject="Open this link to active the account"
    messages=render_to_string('accounts/activate.html',{
        'user': user,
        'domain' : current_url,
        'uid'   : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : default_token_generator.make_token(user),

    })
    to_email=user.email
    mail =EmailMessage(mail_subject,messages,to=[to_email])
    mail.send()



def reset_password_email(request,user):
    current_url=get_current_site(request)
    mail_subject="Resset the password "
    messages=render_to_string('accounts/reset_password.html',{
        'user': user,
        'domain' : current_url,
        'uid'   : urlsafe_base64_encode(force_bytes(user.pk)),
        'token' : default_token_generator.make_token(user),

    })
    to_email=user.email
    mail =EmailMessage(mail_subject,messages,to=[to_email])
    mail.send()


def send_verfication_mail(mail_subject,mail_templates,context):
    messages=render_to_string(mail_templates,context)
    to_email=context['user'].email
    mail=EmailMessage(mail_subject,messages,to=[to_email])
    mail.send()