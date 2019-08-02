from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sport import api_data
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from sport.models import Paris
from sport.views import list_match
# Create your views here.
@login_required(login_url='register_login')
def affichage(request):
    sport = False
    return render(request, 'public/listage_league.html', {'sport': sport})
@login_required(login_url='register_login')
def save(request, sport, league_id, mode, id_event):
    new_pari = Paris(
        userid=request.user.id,
        matchid=id_event,
        leagueid=league_id,
        type=mode,
    )
    new_pari.save()
    return list_match.result(request, sport)
@login_required(login_url='register_login')
def list_league(request, sport):
    api = api_data.API(sport)
    api.league_info()
    league = api.data['league_info']
    paginator = Paginator(league, 6)
    page = request.GET.get('page', False)
    try:
        league = paginator.page(page)
    except PageNotAnInteger:
        league = paginator.page(1)
    except EmptyPage:
        league = paginator.page(paginator.num_pages)
    return render(request, 'public/listage_league.html', {'leagues': league, 'sport': sport})
