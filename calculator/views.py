from django.shortcuts import render
from django.contrib import admin

# Create your views here.


def index(request):
    return render(request, "index.html")


def calculator(request):
    return render(request, "calculator.html")


def about_per(request):
    return render(request, "about per.html")


def contact_us(request):
    return render(request, "contact us.html")


def per_rating(request):

    Minutes = float(request.POST['minutes'])
    FGA = float(request.POST['fga'])
    FGM = float(request.POST['fgm'])
    three_pointer = float(request.POST['3pm'])
    FTA = float(request.POST['fta'])
    FTM = float(request.POST['ftm'])
    Assists = float(request.POST['assists'])
    Steals = float(request.POST['steals'])
    Blocks = float(request.POST['blocks'])
    Offensive_Reb = float(request.POST['orb'])
    Defensive_Reb = float(request.POST['drb'])
    Foul = float(request.POST['fouls'])
    TO = float(request.POST['tov'])
    FT_Miss = float(FTA-FTM)
    FG_Miss = float(FGA-FGM)
    per = ((FGM * 85.910) + (Steals * 53.897) + (three_pointer * 51.757) + (FTM * 46.845) + (Blocks * 39.190) + (Offensive_Reb * 39.190) +
           (Assists * 34.677) + (Defensive_Reb * 14.707) - (Foul * 17.174) - (FT_Miss * 20.091) - (FG_Miss * 39.190) - (TO * 53.897))*(1 / Minutes)
    per_final = round(per, 2)
    return render(request, 'result.html', {'result': per_final})
