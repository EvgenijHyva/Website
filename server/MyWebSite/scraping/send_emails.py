from django.core.mail import EmailMultiAlternatives
import os
import sys
import django
from django.contrib.auth import get_user_model

project = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(project)
os.environ["DJANGO_SETTINGS_MODULE"] = "MyWebSite.settings"
django.setup()

User = get_user_model()
users_to_send = User.objects.filter(send_email=True).values("city", "email")


#more for configuring:
#https://docs.djangoproject.com/en/3.2/topics/email/

#template
subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
text_content = 'This is an important message.'
html_content = '<p>This is an <strong>important</strong> message.</p>'
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()

