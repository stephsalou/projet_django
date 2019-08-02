from thesportsdb import thesportsdb


class API:
    def __init__(self, sport):
        self.api = thesportsdb.Api(key="1")
        self.data = {}
        self.data['events'] = []
        self.data['league_info'] = []
        self.data['day_events'] = []
        self.sport = sport

    def league_info(self, league_id=None):
        if league_id is not None:
            leagues = self.api.Lookups().League(leagueid=league_id)
            for l in leagues:
                self.data['league_info'].append({
                    'id_league': l.idLeague,
                    'nom_league': l.strLeague,
                    'description_league': l.strDescription,
                    'logo_league': l.strLogo
                })
        else:
            leagues = self.api.Search().Leagues(sport=self.sport)
            for l in leagues:
                self.data['league_info'].append({
                    'id_league': l.idLeague,
                    'nom_league': l.strLeague,
                    'description_league': l.strDescription,
                    'logo_league': l.strLogo,
                    'sport': self.sport
                })

    def event_league(self, leagueid: int, mode="next", **kwargs):  # date = "25-05-2019"
        if mode == 'next':
            events = self.api.Schedules().Next().League(leagueid=leagueid)
            for e in events:
                self.data['events'].append({
                    'mode': mode,
                    'e': e.strEvent,
                    'home_team': e.strHomeTeam,
                    # 'home_team_logo': e.HomeTeamObj.strTeamLogo,
                    'away_team': e.strAwayTeam,
                    # 'away_team_logo': e.AwayTeamObj.strTeamLogo,
                    'id_event': e.idEvent,
                    'id_home_team': e.idHomeTeam,
                    'id_away_team': e.idAwayTeam,
                    'id_league': e.idLeague,
                    'name_event': e.strEvent,
                    'date_event': e.dateEvent,
                    'home_score': e.intHomeScore,
                    'away_score': e.intAwayScore,
                    'time_event': e.eventDateTime,
                })
        elif mode == 'last':
            events = self.api.Schedules().Last().League(leagueid=leagueid)
            for e in events:
                self.data['events'].append({
                    'mode': mode,
                    'e': e.strEvent,
                    'home_team': e.strHomeTeam,
                    'home_team_logo': e.HomeTeamObj.strTeamLogo,
                    'away_team': e.strAwayTeam,
                    'away_team_logo': e.AwayTeamObj.strTeamLogo,
                    'id_event': e.idEvent,
                    'id_home_team': e.idHomeTeam,
                    'id_away_team': e.idAwayTeam,
                    'id_league': e.idLeague,
                    'name_event': e.strEvent,
                    'date_event': e.dateEvent,
                    'home_score': e.intHomeScore,
                    'away_score': e.intAwayScore,
                    'time_event': e.eventDateTime,
                })
        elif mode == 'date':
            events = self.api.Schedules().Lookup(datestring=kwargs['date'], sport=self.sport)
            for e in events:
                self.data['events'].append({
                    'mode': mode,
                    'e': e.strEvent,
                    'home_team': e.strHomeTeam,
                    'away_team': e.strAwayTeam,
                    # 'away_team_logo': e.AwayTeamObj.strTeamLogo,
                    # 'home_team_logo': e.HomeTeamObj.strTeamLogo,
                    'id_event': e.idEvent,
                    'id_home_team': e.idHomeTeam,
                    'id_away_team': e.idAwayTeam,
                    'id_league': e.idLeague,
                    'name_event': e.strEvent,
                    'date_event': e.dateEvent,
                    'home_score': e.intHomeScore,
                    'away_score': e.intAwayScore,
                    'time_event': e.eventDateTime,
                })

    def day_event(self, date):
        events = self.api.Schedules().Lookup(datestring='2019-08-01', sport=self.sport)
        for e in events:
            self.data['day_events'].append({
                'e': e.strEvent,
                'home_team': e.strHomeTeam,
                'away_team': e.strAwayTeam,
                # 'away_team_logo': e.AwayTeamObj.strTeamLogo,
                # 'home_team_logo': e.HomeTeamObj.strTeamLogo,
                'id_event': e.idEvent,
                'id_home_team': e.idHomeTeam,
                'id_away_team': e.idAwayTeam,
                'id_league': e.idLeague,
                'name_event': e.strEvent,
                'date_event': e.dateEvent,
                'home_score': e.intHomeScore,
                'away_score': e.intAwayScore,
                'time_event': e.eventDateTime,
                'logo': e.strThumb,
                'result': e.strResult,
            })
