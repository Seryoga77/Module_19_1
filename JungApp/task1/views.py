from .forms import UserRegister
from .models import Buyer  # Импортируйте модель Buyer
from django.contrib.auth.models import User  # Импортируйте модель User
from django.core.exceptions import ValidationError
from .models import Game
from django.http import HttpResponse# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import News

def platform(request):
    text = 'купить'
    context = {
        'text': text,
    }

    return render(request, 'platform.html', context)


def games(request):
    text = 'купить'
    text1 = 'Attomic Heart '
    text2 = 'Cyberpunc 2077 '
    text3 = 'PayDay2 '
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {
        'mydict': mydict,
    }

    return render(request, 'games.html', context)


def cart(request):
    text = 'купить'
    context = {
        'text': text,
    }

    return render(request, 'cart.html', context)

# Create your views here.
users = ['user1', 'user2', 'user3']

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            buyers_list = Buyer.objects.values_list('name', flat=True)

            if username in buyers_list:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')

            else:
                Buyer.objects.create(username, age, balance=1000)
                info['respond'] = f'Приветствуем, {username}!'
                return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'registration_page.html', context)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        buyers_list = Buyer.objects.values_list('name', flat=True)

        if username in buyers_list:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')

        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse('Вы должны быть старше 18')

        else:
            Buyer.objects.create(username, age, balance=1000)
            info['respond'] = f'Приветствуем, {username}!'
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', {'info': info})

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news.html', {'news': page_obj})
# def sign_up_by_django(request):
#     if request.method == "POST":
#         username = request.POST.get('username')  # Получить имя пользователя из POST-запроса
#         # Проверяем, существует ли пользователь
#         if Buyer.objects.filter(name=username).exists():
#             # Можно добавить сообщение об ошибке здесь
#             return render(request, 'registration_page.html', {'error': 'Пользователь с таким именем уже существует.'})
#
#         # Если пользователя нет, создаем новую запись
#         new_buyer = Buyer(name=username)
#         new_buyer.save()  # Сохраняем нового покупателя
#
#         return redirect('home')  # Перенаправляем на главную страницу
#
#     return render(request, 'registration_page.html')
    # info = {}
    # if request.method == 'POST':
    #     form = UserRegister(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         repeat_password = form.cleaned_data['repeat_password']
    #         age = form.cleaned_data['age']
    #
    #         if password != repeat_password:
    #             info['error'] = 'Пароли не совпадают'
    #         elif age < 18:
    #             info['error'] = 'Вы должны быть старше 18'
    #         elif username in users:
    #             info['error'] = 'Пользователь уже существует'
    #         else:
    #             return render(request, 'registration_page.html', {'message': f'Приветствуем, {username}!'})
    #
    # else:
    #     form = UserRegister()
    #
    # info['form'] = form
    # return render(request, 'registration_page.html', info)
# def product_list(request):
#     games = Game.objects.all()  # Получаем все записи из таблицы Game
#     return render(request, 'menu.html', {'games': games})  # Передаем коллекцию в контекст
#
# def sign_up_by_html(request):
#     return sign_up_by_django(request)
