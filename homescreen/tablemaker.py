from weakref import proxy
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import numpy as np


GAME_STATS = {
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
}

CAREER_STATS = {
    "MIN":5,
    "FGM":6,
    "FGA":7,
    "FG%":8,
    "3PM":9,
    "3PA":10,
    "3P%":11,
    "FTM":12,
    "FTA":13,
    "FT%":14,
    "OREB":15,
    "DREB":16,
    "REB":17,
    "AST":18,
    "STL":19,
    "BLK":20,
    "TOV":21,
    "PF":22,
    "PTS":23,
}


def generateTable(p_id):
    table = []

    with open('proxies.txt','r') as f:
        my_proxy = f.readline()

    for i in range(4):
        try:
            careerStats = playercareerstats.PlayerCareerStats(player_id=p_id,per_mode36='PerGame', proxy=my_proxy, timeout=5)
            break
        except:
            pass
    careerStats = careerStats.career_totals_regular_season.get_dict()
    careerStats = careerStats['data'][0]

    for i in range(4):
        try:
            gameStats = playergamelog.PlayerGameLog(player_id=p_id,season=SeasonAll.all, proxy=my_proxy, timeout=5)
            break
        except:
            pass
    gameStats = gameStats.player_game_log.get_dict()

    fiveGamePercents = np.array([])
    for key in GAME_STATS:
        statEachGame = np.array([])
        avgEachGame = np.array([])
        for i in range(5):
            statEachGame = np.append(statEachGame,gameStats['data'][i][GAME_STATS[key]])
            if statEachGame.any() == None:
                return []
            avgEachGame = np.append(avgEachGame,sum(statEachGame)/len(statEachGame))
        statAvg = avgEachGame[len(avgEachGame)-1]
        carAvg = careerStats[CAREER_STATS[key]]
        percentDiff = (statAvg - carAvg) / carAvg
        percentDiff = round(percentDiff,4) * 100
        percentDiff = '%.2f'%(percentDiff) + '%'
        if percentDiff[0] != '-':
            percentDiff = '+' + percentDiff
        fiveGamePercents = np.append(fiveGamePercents,percentDiff)
    
    tenGamePercents = np.array([])
    for key in GAME_STATS:
        statEachGame = np.array([])
        avgEachGame = np.array([])
        for i in range(10):
            statEachGame = np.append(statEachGame,gameStats['data'][i][GAME_STATS[key]])
            if statEachGame.any() == None:
                return []
            avgEachGame = np.append(avgEachGame,sum(statEachGame)/len(statEachGame))
        statAvg = avgEachGame[len(avgEachGame)-1]
        carAvg = careerStats[CAREER_STATS[key]]
        percentDiff = (statAvg - carAvg) / carAvg
        percentDiff = round(percentDiff,4) * 100
        percentDiff = '%.2f'%(percentDiff) + '%'
        if percentDiff[0] != '-':
            percentDiff = '+' + percentDiff
        tenGamePercents = np.append(tenGamePercents,percentDiff)
    
    fifteenGamePercents = np.array([])
    for key in GAME_STATS:
        statEachGame = np.array([])
        avgEachGame = np.array([])
        for i in range(15):
            statEachGame = np.append(statEachGame,gameStats['data'][i][GAME_STATS[key]])
            if statEachGame.any() == None:
                return []
            avgEachGame = np.append(avgEachGame,sum(statEachGame)/len(statEachGame))
        statAvg = avgEachGame[len(avgEachGame)-1]
        carAvg = careerStats[CAREER_STATS[key]]
        percentDiff = (statAvg - carAvg) / carAvg
        percentDiff = round(percentDiff,4) * 100
        percentDiff = '%.2f'%(percentDiff) + '%'
        if percentDiff[0] != '-':
            percentDiff = '+' + percentDiff
        fifteenGamePercents = np.append(fifteenGamePercents,percentDiff)
    
    thirtyGamePercents = np.array([])
    for key in GAME_STATS:
        statEachGame = np.array([])
        avgEachGame = np.array([])
        for i in range(30):
            statEachGame = np.append(statEachGame,gameStats['data'][i][GAME_STATS[key]])
            if statEachGame.any() == None:
                return []
            avgEachGame = np.append(avgEachGame,sum(statEachGame)/len(statEachGame))
        statAvg = avgEachGame[len(avgEachGame)-1]
        carAvg = careerStats[CAREER_STATS[key]]
        percentDiff = (statAvg - carAvg) / carAvg
        percentDiff = round(percentDiff,4) * 100
        percentDiff = '%.2f'%(percentDiff) + '%'
        if percentDiff[0] != '-':
            percentDiff = '+' + percentDiff
        thirtyGamePercents = np.append(thirtyGamePercents,percentDiff)
    
    fiftyfiveGamePercents = np.array([])
    for key in GAME_STATS:
        statEachGame = np.array([])
        avgEachGame = np.array([])
        for i in range(50):
            statEachGame = np.append(statEachGame,gameStats['data'][i][GAME_STATS[key]])
            if statEachGame.any() == None:
                return []
            avgEachGame = np.append(avgEachGame,sum(statEachGame)/len(statEachGame))
        statAvg = avgEachGame[len(avgEachGame)-1]
        carAvg = careerStats[CAREER_STATS[key]]
        percentDiff = (statAvg - carAvg) / carAvg
        percentDiff = round(percentDiff,4) * 100
        percentDiff = '%.2f'%(percentDiff) + '%'
        if percentDiff[0] != '-':
            percentDiff = '+' + percentDiff
        fiftyfiveGamePercents = np.append(fiftyfiveGamePercents,percentDiff)
    

    percentMatrix = np.array([fiveGamePercents,tenGamePercents,fifteenGamePercents,thirtyGamePercents,fiftyfiveGamePercents])
    table = percentMatrix.T

    return table