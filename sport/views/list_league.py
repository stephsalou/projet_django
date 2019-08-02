from django.shortcuts import render
from sport import api_data
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def affichage(request):
    sport = False
    return render(request, 'public/listage_league.html', {'sport': sport})


def listleague(request, sport):
    api = api_data.API(sport)
    api.league_info()
    league=api.data['league_info']
    paginator = Paginator(league, 6)
    page = request.GET.get('page',1)
    try:
        league = paginator.page(page)
    except  PageNotAnInteger:
        league = paginator.page(1)
    except EmptyPage:
        league = paginator.page(paginator.num_pages)
    return render(request, 'public/listage_league.html',{'leagues': league, 'sport': sport})
