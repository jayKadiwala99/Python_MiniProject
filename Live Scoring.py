from pycricbuzz import Cricbuzz
import time
k = Cricbuzz()
matches = k.matches()
while True:
    print('\t************** IPL Live Scoring **************')
    for match in matches:
        if match['srs'] == 'Indian Premier League 2020':
            if match['mchstate']=='inprogress':
                print(str(match['team1']['name'])+' VS '+str(match['team2']['name']))
                print('Match Status : ',match['status'])
            else :
                print('No live matches available.')
    print('\t************** Upcoming IPL Matches **************')
    for match in matches:
        if match['srs'] == 'Indian Premier League 2020':
           if match['mchstate']=='preview':
                print(str(match['team1']['name'])+' VS '+str(match['team2']['name']))
                print('Match Status : ',match['status'])
            else :
                print("No Upcoming matches.")
    time.sleep(10)
           
       
