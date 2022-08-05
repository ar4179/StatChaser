from dataclasses import fields
from django import forms
from nba_api.stats.static import players

player_list = []
for player in players.get_players():
    player_list.append((player['id'],player['full_name']))

STATS_OPTIONS = [
    ("MIN","Minutes"),
    ("FGM","Field Goals Made"),
    ("FGA","Field Goals Atmpt."),
    ("FG%","Field Goal Pct."),
    ("3PM","3 Pointers Made"),
    ("3PA","3 Pointers Atmt."),
    ("3P%","3 Pointers Pct."),
    ("FTM","Free Throws Made"),
    ("FTA","Free Throws Atmpt."),
    ("FT%","Free Throw Pct."),
    ("OREB","Off. Rebounds"),
    ("DREB","Def. Rebounds"),
    ("REB","Rebounds"),
    ("AST","Assists"),
    ("STL","Steal"),
    ("BLK","Blocks"),
    ("TOV","Turnovers"),
    ("PF","Personal Fouls"),
    ("PTS","Points"),
    ("PLUS MINUS","Plus Minus")
]

class PlayerDropDown(forms.Form):
    playerID = forms.CharField(widget=forms.Select(choices=player_list))
    player2ID = forms.CharField(widget=forms.Select(choices=player_list))
    xrange = forms.IntegerField(label='xrange',min_value=1)
    xrange.widget.attrs.update({'class':'form-control','style':'width:7%'})
    stat = forms.CharField(widget=forms.Select(choices=STATS_OPTIONS))    