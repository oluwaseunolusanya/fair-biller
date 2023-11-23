''' 
Fair Billing Program
====================
1. Takes a log file as input.
2. Processes each line in the log file.
3. Prints out a report of the users, the number of sessions, and the minimum possible total duration of their sessions in seconds.

Assumptions
===========
1. Data in the log file are correctly ordered chronologically.
2. All records in the file are from within a single day with no span over midnight.
3. There are only 3 records per line in the log - the timestamp, username and state of the session e.g Start or End.
'''

import sys,re

# Get data from the sessions log.'
sessionsLog = open(sys.argv[1])

# Create a storage for raw data from the log file
sessionsData = {}

# Validating input data
def timestampIsValid (timestamp_string):
    valid_timestamp = r'^d{2}:\d{2}:\d{2}$'
    return re.match(valid_timestamp, timestamp_string)

# Represent timestamp as integer
def get_sec(timestamp_string):
    h,m,s = timestamp_string.split(':')
    h = int(h) * 3600
    m = int(m) * 60
    s = int(s)
    return h + m + s

# Get the timestamp of the first line and the last line in the log.
sessionsLogList= list(sessionsLog)
firstLine = sessionsLogList[0]
firstLineWords = firstLine.split()
firstTimestamp = get_sec(firstLineWords[0])
lastLine = sessionsLogList[-1]
lastLineWords = lastLine.split()
lastTimestamp = get_sec(lastLineWords[0])

# Create an dictionary to store sessions used per user.
for line in sessionsLogList:
    line = line.rstrip()
    words = line.split()
    # Checking lines for valid input data.
    if (len(words) != 3) or (timestampIsValid(words[0]) == False) or (words[1].isalnum() == False) or (words[2] not in ['Start', 'End']):  
        continue
    else:
        timestamp = get_sec(words[0])
        username = words[1]
        sessionState = words[2]
        if username not in sessionsData:
            sessionsData[username] = {}
            sessionsData[username] = [[sessionState, timestamp]]
        else:
            sessionsData[username].append([sessionState, timestamp])
            
processedSessionsData = {}  # To store session data in 'Start and End' pairs.
totalSessions = 0
totalSessionTime = 0
result = " "

for username in sessionsData.keys():
    processedSessionsData[username] = [sessionsData[username][0]]
    #print(processedSessionsData)
    # Rearrange items for each username as pair of 'Start' and 'End'
    # print(username)
    processedCounter = len(processedSessionsData[username])
    unprocessedCounter = len(sessionsData[username])
    # print(processedCounter)
    # print(unprocessedCounter)
    while processedCounter < unprocessedCounter:
        # print(processedCounter)
        for i in range(1,unprocessedCounter):
            if processedSessionsData[username][-1][0] != sessionsData[username][i][0]:
                if sessionsData[username][i] not in processedSessionsData[username]:
                    processedSessionsData[username].append(sessionsData[username][i])
        processedCounter += 1
    # Ensure that the processed data has the same length as the raw data
    for item in sessionsData[username]:
        if item not in processedSessionsData[username]:
            processedSessionsData[username].append(item)

    # Pad the processed data such that the beginning 'Marker and Timestamp' pair for each user is 'Start and the earliest timestamp'
    if processedSessionsData[username][0][0] == 'End':
        processedSessionsData[username].insert(0,['Start',firstTimestamp])      # No matching 'Start' hence earliest time in the log file is assumed
    
    if processedSessionsData[username][-1][0] == 'Start':
        processedSessionsData[username].append(['End',lastTimestamp])           # No matching 'End' hence latest time in the log file is assumed
    
    if processedSessionsData[username][-2][0] == 'End':
        processedSessionsData[username].insert(-1, ['Start',firstTimestamp])    # No matching 'Start' hence earliest time in the log file is assumed

    # For each user, calculate the total time
    totalSessions = len(processedSessionsData[username]) / 2
    totalStartTime = 0
    totalEndTime = 0
    for i in range(0, len(processedSessionsData[username])):
        if i % 2 == 0:
            totalStartTime += processedSessionsData[username][i][1]
        else:
            totalEndTime += processedSessionsData[username][i][1]

    totalSessionTime = totalEndTime - totalStartTime
    
    result = username + ' ' + str(totalSessions) + ' ' + str(totalSessionTime)
    print(result)