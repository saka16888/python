__author__ = 'mihung'

import json

#1 Acquire the data
with open('notes/team_history.json') as f:
    hist = json.load(f)

#2 Convert to a convenient form
record = [game['result'] for game in hist]
scores = [game['score'] for game in hist]
dates = [game['date'] for game in hist]

#3 Do the actual testing or data analysis
print('This season, we played %d games from %s to %s' % (len(dates), dates[0], dates[-1]))
print('Our record was %d-%d' % (record.count('won'), record.count('lost')))
print('We %s the first game and %s the last game' % (record[0], record[-1]))
print('We scored %d goals this season' % sum(scores))
print('Our best game had %d goals and our fewest was %d goal' % (max(scores), min(scores)))
