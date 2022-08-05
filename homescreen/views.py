from socket import timeout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import STATS_OPTIONS, PlayerDropDown
from . import tablemaker
import time

# nba_api
import numpy as np
import math
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import players

MAPPED_STATS = {
    "MIN":6,
    "FGM":7,
    "FGA":8,
    "FG%":9,
    "3PM":10,
    "3PA":11,
    "3P%":12,
    "FTM":13,
    "FTA":14,
    "FT%":15,
    "OREB":16,
    "DREB":17,
    "REB":18,
    "AST":19,
    "STL":20,
    "BLK":21,
    "TOV":22,
    "PF":23,
    "PTS":24,
    "PLUS MINUS":25
}

statNames = ["Minutes","Field Goals Made","Field Goals Atmpt.","Field Goal Pct.","3 Pointers Made","3 Pointers Atmt.","3 Pointers Pct.","Free Throws Made","Free Throws Atmpt.","Free Throw Pct.","Off. Rebounds","Def. Rebounds","Rebounds","Assists","Steal","Blocks","Turnovers","Personal Fouls","Points"]

def graph(request):

    with open('proxies.txt','r') as f:
        my_proxy = f.readline()

    if request.method == 'GET':
        form = PlayerDropDown(request.GET)
        if form.is_valid():
            games = int(form.cleaned_data['xrange'])
            stat = form.cleaned_data['stat']
            statIndex = MAPPED_STATS[stat]

            selected_id = form.cleaned_data['playerID']
            name1 = players.find_player_by_id(selected_id)['full_name']
            for i in range(4):
                try:
                    lastN = playergamelog.PlayerGameLog(player_id=selected_id,season=SeasonAll.all, proxy=my_proxy, timeout=5)
                    break
                except:
                    pass
            lastN = lastN.player_game_log.get_dict()
            
            selected_id2 = form.cleaned_data['player2ID']
            name2 = players.find_player_by_id(selected_id2)['full_name']
            for i in range(4):
                try:
                    lastN_2 = playergamelog.PlayerGameLog(player_id=selected_id2,season=SeasonAll.all, proxy=my_proxy, timeout=5)
                    break
                except:
                    pass
            lastN_2 = lastN_2.player_game_log.get_dict()

            maxLastN = len(lastN['data'])
            maxLastN_2 = len(lastN_2['data'])
            maxGames = min(maxLastN,maxLastN_2)

            errorName = ""
            if maxGames < games:
                games = maxGames
                errorName = name1 if games == maxLastN else name2
            

            yvalues = np.array([])
            yvalues2 = np.array([])
            pointsEachGame1 = np.array([])
            pointsEachGame2 = np.array([])
            for i in range(games):
                pointsEachGame1 = np.append(pointsEachGame1,lastN['data'][i][statIndex])
                yvalues = np.append(yvalues,sum(pointsEachGame1)/len(pointsEachGame1))
                pointsEachGame2 = np.append(pointsEachGame2,lastN_2['data'][i][statIndex])
                yvalues2 = np.append(yvalues2,sum(pointsEachGame2)/len(pointsEachGame2))
            xvalues = np.arange(games)

            table = []
            table2 = []
            if maxLastN >= 50:
                table = tablemaker.generateTable(selected_id)
            if maxLastN_2 >= 50:
                table2 = tablemaker.generateTable(selected_id2)

            form = PlayerDropDown(initial={'playerID':str(selected_id), 'player2ID':str(selected_id2),'xrange':games, 'stat':stat})

            if errorName == "":
                htmlArgs = {'xvalues':xvalues,'yvalues':yvalues,'yvalues2':yvalues2,'name1':name1,'name2':name2,'form':form,'games':games, 'stat':stat,'table':table,'table2':table2,'statNames':statNames}
            else:
                htmlArgs = {'xvalues':xvalues,'yvalues':yvalues,'yvalues2':yvalues2,'name1':name1,'name2':name2,'form':form,'games':games, 'stat':stat,'errorName':errorName,'table':table,'table2':table2,'statNames':statNames}
            return render(request,'homescreen/homepage.html',context=htmlArgs)

    with open('proxies.txt','r') as f:
        my_proxy = f.readline()

    games = 50
    stat = 'PTS'
    statIndex = MAPPED_STATS[stat]

    main_lastN_id = 2544
    name1 = players.find_player_by_id(main_lastN_id)['full_name']
    for i in range(4):
        try:
            main_lastN = playergamelog.PlayerGameLog(player_id=main_lastN_id,season=SeasonAll.all, proxy=my_proxy, timeout=5)
            break
        except:
            pass
    main_lastN = main_lastN.player_game_log.get_dict()

    main2_lastN_id = 203954
    name2 = players.find_player_by_id(main2_lastN_id)['full_name']
    for i in range(4):
        try:
            main2_lastN = playergamelog.PlayerGameLog(player_id=main2_lastN_id,season=SeasonAll.all, proxy=my_proxy, timeout=5)
            break
        except:
            pass
    main2_lastN = main2_lastN.player_game_log.get_dict()
    
    yvalues = np.array([])
    yvalues2 = np.array([])
    pointsEachGame1 = np.array([])
    pointsEachGame2 = np.array([])
    for i in range(games):
        pointsEachGame1 = np.append(pointsEachGame1,main_lastN['data'][i][statIndex])
        yvalues = np.append(yvalues,sum(pointsEachGame1)/len(pointsEachGame1))
        pointsEachGame2 = np.append(pointsEachGame2,main2_lastN['data'][i][statIndex])
        yvalues2 = np.append(yvalues2,sum(pointsEachGame2)/len(pointsEachGame2))
    xvalues = np.arange(games)

    table = tablemaker.generateTable(main_lastN_id)
    table2 = tablemaker.generateTable(main2_lastN_id)

    form = PlayerDropDown(initial={'playerID':str(main_lastN_id), 'player2ID':str(main2_lastN_id),'xrange':games, 'stat':stat})
    htmlArgs = {'xvalues':xvalues,'yvalues':yvalues,'yvalues2':yvalues2,'name1':name1,'name2':name2,'form':form,'games':games, 'stat':stat,'table':table,'table2':table2,'statNames':statNames}
    return render(request,'homescreen/homepage.html',context=htmlArgs)

def aboutMe(request):
    return render(request,'homescreen/aboutme.html')