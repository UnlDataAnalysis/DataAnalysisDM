import pandas as pd
import numpy as np
from datetime import datetime

donations = pd.read_csv("Test Donation Pull.csv",skiprows=4)
participants= pd.read_csv("Top 5 Fundraiser Stuff.csv",skiprows=4)
amountRaised = {}
firstName = {}
lastName = {}
participant_teams = {}
team_raised = {}
total_raised = 0
for index in range(len(participants)):
    participant = participants.iloc[index]
    participant_email = participant["PARTICIPANTEMAIL"]
    amountRaised[participant_email] = 0
    participant_team = participant["TEAMNAME"]
    if not isinstance(participant_team,float):
        participant_teams[participant_email] = participant_team
        team_raised[participant_team] = 0
for index in range(len(donations)):
    donation = donations.iloc[index]
    donation_deposit_date = donation["DONATIONENTEREDDATE"]
    if datetime.strptime(donation_deposit_date,'%Y-%m-%d') == datetime.strptime("2022-10-03",'%Y-%m-%d'):
        donation_amount = donation["DONATIONAMOUNT"]
        total_raised += donation_amount
        participant_first_name = donation["PARTICIPANTFIRSTNAME"]
        participant_last_name = donation["PARTICIPANTLASTNAME"]
        participant_email = donation["PARTICIPANTEMAIL"]
        if not isinstance(participant_email ,float):
            amountRaised[participant_email] = amountRaised[participant_email] + donation_amount
            firstName[participant_email] = participant_first_name
            lastName[participant_email] = participant_last_name
            if participant_email in participant_teams.keys():
                team_raised[participant_teams[participant_email]] = team_raised[participant_teams[participant_email]]  + donation_amount
out_arr = []
out_par = []

for key in team_raised.keys():
    out_arr.append((key, team_raised[key]))
for key in firstName.keys():
    out_par.append((firstName[key] + " " +lastName[key], amountRaised[key]))
out_arr.sort(key=lambda x: x[1])
out_arr.reverse()
out_par.sort(key=lambda x: x[1])
out_par.reverse()
print("Total Raised: "+str(total_raised))
print("Top Teams")
print(out_arr)
print("Individual Fundraisers")
print(out_par)
test = 1


