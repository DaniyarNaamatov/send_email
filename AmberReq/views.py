from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from AmberReq.forms import RequestForm
from django.core.mail import EmailMessage
from AmberSoft import settings
from django.http import HttpResponse




def home(request):
    return render(request, 'request.html')






def send_email(request):
    if request.method == "POST":
        username = request.POST['username']
        sender_email = request.POST['email']
        msg = request.POST['msg']
        phone = request.POST['phone']

        email = EmailMessage(
            f'привет {sender_email}'
            f'Здрав: {username}\n\n Новости:{msg}\n\n Почта:{sender_email}\n\n Telefon:{phone}',
            settings.EMAIL_HOST_USER,
            [sender_email]
        )
        email.fail_silently = True
        email.send()
        return HttpResponse('Отправилось на почту')
    else:
        return HttpResponse('не отправилось')



























# def test(request):
#     if request.method == 'POST':
#         form = RequestForm(request.POST)
#         if form.is_valid():
#             mail = send_mail(form.cleaned_data['username'], form.cleaned_data['phone'], 'mr.naamatov@mail.ru', ['mrnaamatov@gmail.ru'], fail_silently=False)
#             if mail:
#                 messages.success(request, 'Письмо отправлено')
#                 return redirect('request')
#             else:
#                 messages.error(request, 'ошибка отправки')
#         else:
#             messages.error(request, 'ошибка заполнения')
#     else:
#         form = RequestForm
#     return render(request, 'request.html', {"form": form})


