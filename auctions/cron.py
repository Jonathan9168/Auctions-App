from django.core.mail import send_mail

def my_scheduled_job():
  send_mail(
        'Subject here',
        'Here is the message.',
        'courseworkweb@gmail.com',
        ['atifar01@gmail.com'],
        fail_silently=False,
    )