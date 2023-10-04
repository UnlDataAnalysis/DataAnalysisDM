import pandas as pd
import numpy as np
from datetime import datetime
newParticipants = pd.read_csv("newParticipants_event5128.csv",skiprows=3)
returningParticipants = pd.read_csv("returningParticipants_event5128.csv",skiprows=3)
facebookFundraiserAndMobileData = pd.read_csv("Miracle Cup_ Facebook Fundraiser and Mobile Data.csv", skiprows=4)
newParticipantsTEAMS = newParticipants["TEAM"].unique()
returningParticipantsTEAMS = returningParticipants["CURRENTTEAM"].unique()
teamTotalPoints = {}

for team in newParticipantsTEAMS:
    if isinstance(team,str):
        teamTotalPoints[team] = ()
for team in returningParticipantsTEAMS:
    if isinstance(team,str):
        teamTotalPoints[team] = ()

teamMembersRegistered = {}
registeredByFirstDate = {}
registeredBySecondDate = {}
registeredByThirdDate = {}
amountFundraised = {}
facebookFundraiserCreated = {}
registeredMobileApp = {}

for team in teamTotalPoints.keys():
    teamMembersRegistered[team] = 0
    registeredByFirstDate[team] = 0
    registeredBySecondDate[team] = 0
    registeredByThirdDate[team] = 0
    amountFundraised[team] = 0
    facebookFundraiserCreated[team] = 0
    registeredMobileApp[team] = 0

firstRegistrationDate = datetime.strptime("2022-09-23",'%Y-%m-%d')
secondRegistrationDate = datetime.strptime("2022-12-31",'%Y-%m-%d')
thirdRegistrationDate = datetime.strptime("2023-01-31",'%Y-%m-%d')
#NEW PARTICIPANT COLUMNS

#TEAM
#REGISTRATIONDATE
#TOTALRAISEDCURRENTEVENT

for index in range(len(newParticipants)):
    participant = newParticipants.iloc[index]
    team = participant["TEAM"]
    if isinstance(team,str):
        registrationDate = participant["REGISTRATIONDATE"]
        totalRaised = participant["TOTALRAISEDCURRENTEVENT"]
        formattedDate = datetime.strptime(registrationDate,'%Y-%m-%d')
        if formattedDate <= firstRegistrationDate:
            registeredByFirstDate[team] = registeredByFirstDate[team]+1
        if formattedDate <= secondRegistrationDate:
            registeredBySecondDate[team] = registeredBySecondDate[team]+1
        if formattedDate <= thirdRegistrationDate:
            registeredByThirdDate[team] = registeredByThirdDate[team]+1
        teamMembersRegistered[team] = teamMembersRegistered[team] + 1
        amountFundraised[team] = amountFundraised[team] + totalRaised

#RETURNING PARTICIPANT COLUMNS

#CURRENTTEAM
#CURRENTREGISTRATIONDATE
#TOTALRAISEDCURRENTEVENT
for index in range(len(returningParticipants)):
    participant = returningParticipants.iloc[index]
    team = participant["CURRENTTEAM"]
    if isinstance(team, str):
        registrationDate = participant["CURRENTREGISTRATIONDATE"]
        totalRaised = participant["TOTALRAISEDCURRENTEVENT"]
        formattedDate = datetime.strptime(registrationDate,'%Y-%m-%d')
        if formattedDate <= firstRegistrationDate:
            registeredByFirstDate[team] = registeredByFirstDate[team]+1
        if formattedDate <= secondRegistrationDate:
            registeredBySecondDate[team] = registeredBySecondDate[team]+1
        if formattedDate <= thirdRegistrationDate:
            registeredByThirdDate[team] = registeredByThirdDate[team]+1
        teamMembersRegistered[team] = teamMembersRegistered[team] + 1
        amountFundraised[team] = amountFundraised[team] + totalRaised
for index in range(len(facebookFundraiserAndMobileData)):
    row = facebookFundraiserAndMobileData.iloc[index]
    created = row["CREATEDFACEBOOKFUNDRAISER"]
    mobile_app = row["MOBILEREGISTRATION"]
    event = row["EVENTNAME"]
    team = row["TEAMNAME"]
    if event == "University of Nebraska, Lincoln - HuskerThon 2023":
        if isinstance(team, str):
            registeredMobileApp[team] = registeredMobileApp[team] + int(mobile_app == "Yes")
            if created == "Yes":
                facebookFundraiserCreated[team] = facebookFundraiserCreated[team] + 1



# teamMembersRegistred = {}
# registeredByFirstDate = {}
# registeredBySecondDate = {}
# registeredByThirdDate = {}
# amountFundraised = {}
# facebookFundraiserCreated = {}

dataEntries = []
for team in teamMembersRegistered.keys():
    dataEntries.append([team, teamMembersRegistered[team], registeredByFirstDate[team], registeredBySecondDate[team], registeredByThirdDate[team], amountFundraised[team], facebookFundraiserCreated[team],registeredMobileApp[team]])
printableData = pd.DataFrame(dataEntries, columns = ['Team', 'Team Members Registered','Number Registered By First Date','Number Registered By Second Date','Number Registered By Third Date','Amount Fundraised', 'Number of Facebook Fundraisers Created','Registered Mobile App'])
printableData = printableData.sort_values(by='Team', key=lambda col: col.str.lower())
printableData.to_csv('dataByTeam.csv')
