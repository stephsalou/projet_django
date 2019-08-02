"""playeur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from .views import inscription, acceuil, list_league, list_match, pari

urlpatterns = [
    re_path(r'^acceuil$', acceuil.affichage, name='index'),
    re_path(r'^inscription$', inscription.affichage, name='register_login'),
    re_path(r'^register$', inscription.sport_register, name='register'),
    re_path(r'^login$', inscription.sport_login, name='login'),
    re_path(r'^logout$', inscription.sport_logout, name='logout'),
    # re_path(r'^$',acceuil.affichage),
    path('list_match/<str:sport>/<int:leagueid>', list_match.affichage, name='list_match'),
    path("listage_league/<str:sport>", list_league.listleague, name='list_league'), #probleme au niveau de url.py changer gere le listage des match et test de parie ne pas oublier de migrate la bd
    path("next_event/<str:sport>/<int:leagueid>", list_match.next_event, name='nextevent'),
    path("result/<str:sport>", list_match.result, name='result'),
    path('parie/<str:sport>/<str:league_id>/<str:mode>/<int:id_event>', pari.save,name='parie'),
    re_path(r'^$', acceuil.affichage)

]
