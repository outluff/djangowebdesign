from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': 'Family', 'url_name': 'fam'},
        {'title': 'Sport', 'url_name': 'sport'},
        {'title': 'Cybersport', 'url_name': 'cs'},
        {'title': 'Plains', 'url_name': 'plains'},
        {'title': 'Family_2', 'url_name': 'fam2'},
        {'title': 'Sport_2', 'url_name': 'sport2'},
        {'title': 'Cybersport_2', 'url_name': 'cs2'},
        {'title': 'Plains_2', 'url_name': 'plains2'},
        {'title': 'HOME_2', 'url_name': 'home2'},
        ]

menu_4_lab = [{'title': 'Family', 'url_name': 'fam1_lab4'},
              {'title': 'Sport', 'url_name': 'sport1_lab4'},
              {'title': 'Cybersport', 'url_name': 'cybersport1_lab4'},
              {'title': 'Plains', 'url_name': 'plains1_lab4'},
              {'title': 'Общие сведения пункт 2 задание 2', 'url_name': 'index2_2_lab4'},
              {'title': 'Family пункт 2 задание 2', 'url_name': 'fam2_2_lab4'},
              {'title': 'Sport пункт 2 задание 2', 'url_name': 'sport2_2_lab4'},
              {'title': 'Cybersport пункт 2 задание 2', 'url_name': 'cybersport2_2_lab4'},
              {'title': 'Plains пункт 2 задание 2', 'url_name': 'plains2_2_lab4'},
              {'title': 'Общие сведения пункт 1 задание 2', 'url_name': 'index2_lab4'},
              {'title': 'Family пункт 1 задание 2', 'url_name': 'fam2_lab4'},
              {'title': 'Sport пункт 1 задание 2', 'url_name': 'sport2_lab4'},
              {'title': 'Cybersport пункт 1 задание 2', 'url_name': 'cybersport2_lab4'},
              {'title': 'Plains пункт 1 задание 2', 'url_name': 'plains2_lab4'},
              {'title': 'Общие сведения задание 3', 'url_name': 'index2_3_lab4'},
              {'title': 'Family задание 3', 'url_name': 'fam2_3_lab4'},
              {'title': 'Sport задание 3', 'url_name': 'sport2_3_lab4'},
              {'title': 'Cybersport задание 3', 'url_name': 'cybersport2_3_lab4'},
              {'title': 'Plains задание 3', 'url_name': 'plains2_3_lab4'},
              ]

menu_4_lab2 = [{'title': 'Family', 'url_name': 'fam2_lab4'},
               {'title': 'Sport', 'url_name': 'sport2_lab4'},
               {'title': 'Cybersport', 'url_name': 'cybersport2_lab4'},
               {'title': 'Plains', 'url_name': 'plains2_lab4'},
               {'title': 'Общие сведения пункт 2 задание 2', 'url_name': 'index2_2_lab4'},
               {'title': 'Family пункт 2 задание 2', 'url_name': 'fam2_2_lab4'},
               {'title': 'Sport пункт 2 задание 2', 'url_name': 'sport2_2_lab4'},
               {'title': 'Cybersport пункт 2 задание 2', 'url_name': 'cybersport2_2_lab4'},
               {'title': 'Plains пункт 2 задание 2', 'url_name': 'plains2_2_lab4'},
               {'title': 'Общие задание 1', 'url_name': 'index1_lab4'},
               {'title': 'Family задание 1', 'url_name': 'fam1_lab4'},
               {'title': 'Sport задание 1', 'url_name': 'sport1_lab4'},
               {'title': 'Cybersport задание 1', 'url_name': 'cybersport1_lab4'},
               {'title': 'Plains задание 1', 'url_name': 'plains1_lab4'},
               {'title': 'Общие сведения задание 3', 'url_name': 'index2_3_lab4'},
               {'title': 'Family задание 3', 'url_name': 'fam2_3_lab4'},
               {'title': 'Sport задание 3', 'url_name': 'sport2_3_lab4'},
               {'title': 'Cybersport задание 3', 'url_name': 'cybersport2_3_lab4'},
               {'title': 'Plains задание 3', 'url_name': 'plains2_3_lab4'},
               ]

menu_4_lab2_2 = [{'title': 'Family', 'url_name': 'fam2_2_lab4'},
                 {'title': 'Sport', 'url_name': 'sport2_2_lab4'},
                 {'title': 'Cybersport', 'url_name': 'cybersport2_2_lab4'},
                 {'title': 'Plains', 'url_name': 'plains2_2_lab4'},
                 {'title': 'Общие сведения предыдуший пункт', 'url_name': 'index2_lab4'},
                 {'title': 'Family предыдуший пункт', 'url_name': 'fam2_lab4'},
                 {'title': 'Sport предыдуший пункт', 'url_name': 'sport2_lab4'},
                 {'title': 'Cybersport предыдуший пункт', 'url_name': 'cybersport2_lab4'},
                 {'title': 'Plains предыдуший пункт', 'url_name': 'plains2_lab4'},
                 {'title': 'Общие сведения задание 1', 'url_name': 'index1_lab4'},
                 {'title': 'Family задание 1', 'url_name': 'fam1_lab4'},
                 {'title': 'Sport задание 1', 'url_name': 'sport1_lab4'},
                 {'title': 'Cybersport задание 1', 'url_name': 'cybersport1_lab4'},
                 {'title': 'Plains задание 1', 'url_name': 'plains1_lab4'},
                 {'title': 'Общие сведения задание 3', 'url_name': 'index2_3_lab4'},
                 {'title': 'Family задание 3', 'url_name': 'fam2_3_lab4'},
                 {'title': 'Sport задание 3', 'url_name': 'sport2_3_lab4'},
                 {'title': 'Cybersport задание 3', 'url_name': 'cybersport2_3_lab4'},
                 {'title': 'Plains задание 3', 'url_name': 'plains2_3_lab4'},
                 ]

menu_4_lab3 = [{'title': 'Family', 'url_name': 'fam2_3_lab4'},
               {'title': 'Sport', 'url_name': 'sport2_3_lab4'},
               {'title': 'Cybersport', 'url_name': 'cybersport2_3_lab4'},
               {'title': 'Plains', 'url_name': 'plains2_3_lab4'},
               {'title': 'Общие сведения пункт 2 задание 2', 'url_name': 'index2_2_lab4'},
               {'title': 'Family пункт 2 задание 2', 'url_name': 'fam2_2_lab4'},
               {'title': 'Sport пункт 2 задание 2', 'url_name': 'sport2_2_lab4'},
               {'title': 'Cybersport пункт 2 задание 2', 'url_name': 'cybersport2_2_lab4'},
               {'title': 'Plains пункт 2 задание 2', 'url_name': 'plains2_2_lab4'},
               {'title': 'Общие пункт 1 задание 2', 'url_name': 'index2_lab4'},
               {'title': 'Family пункт 1 задание 2', 'url_name': 'fam2_lab4'},
               {'title': 'Sport пункт 1 задание 2', 'url_name': 'sport2_lab4'},
               {'title': 'Cybersport пункт 1 задание 2', 'url_name': 'cybersport2_lab4'},
               {'title': 'Plains пункт 1 задание 2', 'url_name': 'plains2_lab4'},
               {'title': 'Общие сведения задание 1', 'url_name': 'index1_lab4'},
               {'title': 'Family задание 1', 'url_name': 'fam1_lab4'},
               {'title': 'Sport задание 1', 'url_name': 'sport1_lab4'},
               {'title': 'Cybersport задание 1', 'url_name': 'cybersport1_lab4'},
               {'title': 'Plains задание 1', 'url_name': 'plains1_lab4'},
               ]

menu_lab5_1 = [{'title': 'Family', 'url_name': 'fam_1_lab5'},
               {'title': 'Sport', 'url_name': 'sport_1_lab5'},
               {'title': 'Cybersport', 'url_name': 'cybersport_1_lab5'},
               {'title': 'Plains', 'url_name': 'plains_1_lab5'},
               {'title': 'Общие сведения задание 2', 'url_name': 'index_2_lab5'},
               ]

menu_lab5_2 = [{'title': 'Family', 'url_name': 'fam_2_lab5'},
               {'title': 'Sport', 'url_name': 'sport_2_lab5'},
               {'title': 'Cybersport', 'url_name': 'cybersport_2_lab5'},
               {'title': 'Plains', 'url_name': 'plains_2_lab5'},
               {'title': 'Общие сведения задание 1', 'url_name': 'index_1_lab5'},
               {'title': 'Общие сведения задание 3', 'url_name': 'index_3_lab5'},
               ]


def frames(request):
    return render(request, 'conprogs/frames.html')


def frames2(request):
    return render(request, 'conprogs/frames_2.html')


def frames3(request):
    return render(request, 'conprogs/frames_3.html')


def index(request):
    data = {'title': 'Main',
            'menu': menu
            }
    return render(request, 'conprogs/index.html', context=data)


def index2(request):
    data = {'title': 'Main',
            'menu': menu
            }
    return render(request, 'conprogs/index_2.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")


def family(request):
    data = {'title': "Семья", 'menu': menu}
    return render(request, 'conprogs/fam.html', data)


def cybersport(request):
    return render(request, 'conprogs/cybersport.html', {'title': 'Киберспорт', 'menu': menu})


def sport(request):
    return render(request, 'conprogs/sport.html', {'title': 'Спорт', 'menu': menu})


def plains(request):
    return render(request, 'conprogs/plains.html', {'title': 'Перелеты, поезда', 'menu': menu})


def family2(request):
    data = {'title': "Семья", 'menu': menu}
    return render(request, 'conprogs/fam_2.html', data)


def cybersport2(request):
    return render(request, 'conprogs/cybersport_2.html', {'title': 'Киберспорт', 'menu': menu})


def sport2(request):
    return render(request, 'conprogs/sport_2.html', {'title': 'Спорт', 'menu': menu})


def plains2(request):
    return render(request, 'conprogs/plains_2.html', {'title': 'Перелеты, поезда', 'menu': menu})


def family3(request):
    data = {'title': "Семья", 'menu': menu}
    return render(request, 'conprogs/fam_3.html', data)


def cybersport3(request):
    return render(request, 'conprogs/cybersport_3.html', {'title': 'Киберспорт', 'menu': menu})


def sport3(request):
    return render(request, 'conprogs/sport_3.html', {'title': 'Спорт', 'menu': menu})


def plains3(request):
    return render(request, 'conprogs/plains_3.html', {'title': 'Перелеты, поезда', 'menu': menu})


def nav(request):
    return render(request, 'conprogs/includes/nav.html')


def nav2(request):
    return render(request, 'conprogs/includes/nav_2.html')


def nav3(request):
    return render(request, 'conprogs/includes/nav_3.html')


def footer(request):
    return render(request, 'conprogs/includes/footer.html')


def header(request):
    return render(request, 'conprogs/includes/header.html')


def index3(request):
    return render(request, 'conprogs/index_3.html')


def lab4_1_index(request):
    data = {'title': "Общие сведения", 'menu_4_lab': menu_4_lab}
    return render(request, 'lab4/index_2.html', context=data)


def lab4_1_fam(request):
    data = {'title': "Семья", 'menu_4_lab': menu_4_lab}
    return render(request, 'lab4/fam_2.html', context=data)


def lab4_1_sport(request):
    data = {'title': "Спорт", 'menu_4_lab': menu_4_lab}
    return render(request, 'lab4/sport_2.html', context=data)


def lab4_1_cybersport(request):
    data = {'title': "Киберспорт", 'menu_4_lab': menu_4_lab}
    return render(request, 'lab4/cybersport_2.html', context=data)


def lab4_1_plains(request):
    data = {'title': "Перелеты, поезда", 'menu_4_lab': menu_4_lab}
    return render(request, 'lab4/plains_2.html', context=data)


def lab4_2_index(request):
    data = {'title': "Общие сведения", 'menu_4_lab2': menu_4_lab2}
    return render(request, 'lab4/index_3.html', context=data)


def lab4_2_fam(request):
    data = {'title': "Семья", 'menu_4_lab2': menu_4_lab2}
    return render(request, 'lab4/fam_3.html', context=data)


def lab4_2_sport(request):
    data = {'title': "Спорт", 'menu_4_lab2': menu_4_lab2}
    return render(request, 'lab4/sport_3.html', context=data)


def lab4_2_cybersport(request):
    data = {'title': "Киберспорт", 'menu_4_lab2': menu_4_lab2}
    return render(request, 'lab4/cybersport_3.html', context=data)


def lab4_2_plains(request):
    data = {'title': "Перелеты, поезда", 'menu_4_lab2': menu_4_lab2}
    return render(request, 'lab4/plains_3.html', context=data)


def lab4_2_2_index(request):
    data = {'title': "Общие сведения", 'menu_4_lab2_2': menu_4_lab2_2}
    return render(request, 'lab4/index_5_1.html', context=data)


def lab4_2_2_fam(request):
    data = {'title': "Семья", 'menu_4_lab2_2': menu_4_lab2_2}
    return render(request, 'lab4/fam_5_1.html', context=data)


def lab4_2_2_sport(request):
    data = {'title': "Спорт", 'menu_4_lab2_2': menu_4_lab2_2}
    return render(request, 'lab4/sport_5_1.html', context=data)


def lab4_2_2_cybersport(request):
    data = {'title': "Киберспорт", 'menu_4_lab2_2': menu_4_lab2_2}
    return render(request, 'lab4/cybersport_5_1.html', context=data)


def lab4_2_2_plains(request):
    data = {'title': "Перелеты, поезда", 'menu_4_lab2_2': menu_4_lab2_2}
    return render(request, 'lab4/plains_5_1.html', context=data)


def lab4_2_3_index(request):
    data = {'title': "Общие сведения", 'menu_4_lab3': menu_4_lab3}
    return render(request, 'lab4/index_3_3.html', context=data)


def lab4_2_3_fam(request):
    data = {'title': "Семья", 'menu_4_lab3': menu_4_lab3}
    return render(request, 'lab4/fam_3_3.html', context=data)


def lab4_2_3_sport(request):
    data = {'title': "Спорт", 'menu_4_lab3': menu_4_lab3}
    return render(request, 'lab4/sport_3_3.html', context=data)


def lab4_2_3_cybersport(request):
    data = {'title': "Киберспорт", 'menu_4_lab3': menu_4_lab3}
    return render(request, 'lab4/cybersport_3_3.html', context=data)


def lab4_2_3_plains(request):
    data = {'title': "Перелеты, поезда", 'menu_4_lab3': menu_4_lab3}
    return render(request, 'lab4/plains_3_3.html', context=data)


def lab5_1_index(request):
    data = {'title': "Общие сведения", 'menu': menu_lab5_1}
    return render(request, 'lab5/index_5_1.html', context=data)


def lab5_1_fam(request):
    data = {'title': "Семья", 'menu': menu_lab5_1}
    return render(request, 'lab5/fam_5_1.html', context=data)


def lab5_1_sport(request):
    data = {'title': "Спорт", 'menu': menu_lab5_1}
    return render(request, 'lab5/sport_5_1.html', context=data)


def lab5_1_cybersport(request):
    data = {'title': "Киберспорт", 'menu': menu_lab5_1}
    return render(request, 'lab5/cybersport_5_1.html', context=data)


def lab5_1_plains(request):
    data = {'title': "Перелеты, поезда", 'menu': menu_lab5_1}
    return render(request, 'lab5/plains_5_1.html', context=data)


def lab5_2_index(request):
    data = {'title': "Общие сведения", 'menu': menu_lab5_2}
    return render(request, 'lab5/index_5_2.html', context=data)


def lab5_2_fam(request):
    data = {'title': "Семья", 'menu': menu_lab5_2}
    return render(request, 'lab5/fam_5_2.html', context=data)


def lab5_2_sport(request):
    data = {'title': "Спорт", 'menu': menu_lab5_2}
    return render(request, 'lab5/sport_5_2.html', context=data)


def lab5_2_cybersport(request):
    data = {'title': "Киберспорт", 'menu': menu_lab5_2}
    return render(request, 'lab5/cybersport_5_2.html', context=data)


def lab5_2_plains(request):
    data = {'title': "Перелеты, поезда", 'menu': menu_lab5_2}
    return render(request, 'lab5/plains_5_2.html', context=data)


menu_lab5_3 = [{'title': 'Family', 'url_name': 'fam_3_lab5'},
               {'title': 'Sport', 'url_name': 'sport_3_lab5'},
               {'title': 'Cybersport', 'url_name': 'cybersport_3_lab5'},
               {'title': 'Plains', 'url_name': 'plains_3_lab5'},
               {'title': 'Общие сведения задание 2', 'url_name': 'index_2_lab5'},
               ]

menu_cat = [
    {'title': 'Общие сведения задание 1', 'url_name': 'index_1_lab5'},
    {'title': 'Family задание 1', 'url_name': 'fam_1_lab5'},
    {'title': 'Sport задание 1', 'url_name': 'sport_1_lab5'},
    {'title': 'Cybersport задание 1', 'url_name': 'cybersport_1_lab5'},
    {'title': 'Plains задание 1', 'url_name': 'plains_1_lab5'},
    {'title': 'Общие сведения задание 2', 'url_name': 'index_2_lab5'},
    {'title': 'Family задание 2', 'url_name': 'fam_2_lab5'},
    {'title': 'Sport задание 2', 'url_name': 'sport_2_lab5'},
    {'title': 'Cybersport задание 2', 'url_name': 'cybersport_2_lab5'},
    {'title': 'Plains задание 2', 'url_name': 'plains_2_lab5'},
]


def lab5_3_index(request):
    data = {'title': "Общие сведения", 'menu': menu_lab5_3, 'menu_cat': menu_cat}
    return render(request, 'lab5/index_5_3.html', context=data)


def lab5_3_fam(request):
    data = {'title': "Семья", 'menu': menu_lab5_3, 'menu_cat': menu_cat}
    return render(request, 'lab5/fam_5_3.html', context=data)


def lab5_3_sport(request):
    data = {'title': "Спорт", 'menu': menu_lab5_3, 'menu_cat': menu_cat}
    return render(request, 'lab5/sport_5_3.html', context=data)


def lab5_3_cybersport(request):
    data = {'title': "Киберспорт", 'menu': menu_lab5_3, 'menu_cat': menu_cat}
    return render(request, 'lab5/cybersport_5_3.html', context=data)


def lab5_3_plains(request):
    data = {'title': "Перелеты, поезда", 'menu': menu_lab5_3, 'menu_cat': menu_cat}
    return render(request, 'lab5/plains_5_3.html', context=data)


menu_lab6_1 = [{'title': 'Family', 'url_name': 'fam_1_lab6'},
               {'title': 'Sport', 'url_name': 'sport_1_lab6'},
               {'title': 'Cybersport', 'url_name': 'cybersport_1_lab6'},
               {'title': 'Plains', 'url_name': 'plains_1_lab6'},
               {'title': 'задание 2', 'url_name': 'index_2_lab6'},
               ]


def lab6_1_index(request):
    data = {'title': "Общие сведения", 'menu': menu_lab6_1}
    return render(request, 'lab6/index_6_1.html', context=data)


def lab6_1_fam(request):
    data = {'title': "Семья", 'menu': menu_lab6_1}
    return render(request, 'lab6/fam_6_1.html', context=data)


def lab6_1_sport(request):
    data = {'title': "Спорт", 'menu': menu_lab6_1}
    return render(request, 'lab6/sport_6_1.html', context=data)


def lab6_1_cybersport(request):
    data = {'title': "Киберспорт", 'menu': menu_lab6_1}
    return render(request, 'lab6/cybersport_6_1.html', context=data)


def lab6_1_plains(request):
    data = {'title': "Перелеты, поезда", 'menu': menu_lab6_1}
    return render(request, 'lab6/plains_6_1.html', context=data)


menu_lab6_2 = [{'title': 'Family', 'url_name': 'fam_2_lab6'},
               {'title': 'Sport', 'url_name': 'sport_2_lab6'},
               {'title': 'Cybersport', 'url_name': 'cybersport_2_lab6'},
               {'title': 'Plains', 'url_name': 'plains_2_lab6'},
               {'title': 'задание 1', 'url_name': 'index_1_lab6'},
               ]


def lab6_2_index(request):
    data = {'title': "Общие сведения", 'menu': menu_lab6_2}
    return render(request, 'lab6/index_6_2.html', context=data)


def lab6_2_fam(request):
    data = {'title': "Семья", 'menu': menu_lab6_2}
    return render(request, 'lab6/fam_6_2.html', context=data)


def lab6_2_sport(request):
    data = {'title': "Спорт", 'menu': menu_lab6_2}
    return render(request, 'lab6/sport_6_2.html', context=data)


def lab6_2_cybersport(request):
    data = {'title': "Киберспорт", 'menu': menu_lab6_2}
    return render(request, 'lab6/cybersport_6_2.html', context=data)


def lab6_2_plains(request):
    data = {'title': "Перелеты, поезда", 'menu': menu_lab6_2}
    return render(request, 'lab6/plains_6_2.html', context=data)
