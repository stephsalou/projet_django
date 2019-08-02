from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from sport.api_data import API
from datetime import *
from sport.models import Paris


# Create your views here.
@login_required(login_url='register_login')
def affichage(request, sport, leagueid):
    api = API(sport)
    api.event_league(leagueid)
    api.league_info(leagueid)
    event = api.data['events']
    paginator = Paginator(event, 6)
    page = request.GET.get('page', False)
    try:
        event = paginator.page(page)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)
    data = {
        'league_table': api.data['league_info'],
        'events': event,
        'sport': sport
    }
    return render(request, 'public/list.html', data)

@login_required(login_url='register_login')
def next_event(request, sport, leagueid):
    api = API(sport)
    api.event_league(leagueid, 'next')
    event = api.data['events']
    api.league_info(leagueid)
    paginator = Paginator(event, 6)
    page = request.GET.get('page', False)
    try:
        event = paginator.page(page)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)
    return render(request, 'public/list.html', dict(league_table=api.data['league_info'], events=event, sport=sport))

@login_required(login_url='register_login')
def result(request, sport):
    time = datetime.date(datetime.now())
    time = time.strftime('%Y-%m-%d')
    api = API(sport)
    api.day_event(time)
    data = api.data['day_events']
    match_user = Paris.objects.all().filter(userid=request.user.id).values()
    match_user = match_user.all()
    table = []
    for c in data:
        if int(c['id_event']) in [i['matchid'] for i in match_user]:
            table.append(c)
    data=table.copy()
    del table
    for c in data:
        if c['home_score'] is not None:
            print('pass if')
            if int(c['home_score']) == int(c['away_score']):
                c['statut'] = 'null'
            elif int(c['home_score']) < int(c['away_score']):
                c['statut'] = 'defaite'
            elif int(c['home_score']) > int(c['away_score']):
                c['statut'] = 'victoire'
            t = []
            for i in match_user:
                if int(i['matchid'])==int(c['id_event']):
                    print('pass if if')
                    t.append(i)
            try:
                match=t[0]
                if c['statut'] == match['type']:
                    c['win'] = True
                else:
                    c['win'] = False
            except IndexError:
                c['statut'] = False
        else:
            print('pass else')
            c['statut'] = False
    paginator = Paginator(data, 6)
    page = request.GET.get('page', 1)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(0)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'public/result.html', {'data': data, 'sport': sport})
