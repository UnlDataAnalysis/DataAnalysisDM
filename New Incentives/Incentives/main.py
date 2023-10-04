import pandas as pd
import numpy as np
from datetime import datetime

participants = pd.read_csv("Incentives.csv", skiprows=4)
participant_questions1 = pd.read_csv("exportData.csv", skiprows=4)
participant_questions2 = pd.read_csv("exportData1.csv", skiprows=4)
participant_questions3 = pd.read_csv("exportData2.csv", skiprows=4)
participant_questions4 = pd.read_csv("exportData3.csv", skiprows=4)
participant_questions = pd.concat([participant_questions1, participant_questions2, participant_questions3, participant_questions4])
received_qdoba = pd.read_csv("receivedQdoba.csv")
received_starbucks = pd.read_csv("receivedStarbucks.csv")

nuid_list = {}
added_to_qdoba_list = {}
added_to_starbucks_list = {}
individual_sheet = []
incentives_sheet = []
qboda_sheet = []
starbucks_sheet = []

incentives = [
    (25, "Key Chain"),
    (30, "Starbucks 5 dollars"),
    (40, "Ring Gong"),
    (50, "Qdoba Burrito"),
    (60, "Plastic Cup"),
    (75, "75 dollar incentive"),
    (100, "Drawstring bag"),
    (250, "250 dollar incentive"),
    (400, "400 dollar incentive"),
    (500, "Mug"),
    (750, "Headbands"),
    (1000, "Powerbank"),
    (1000, "Comma Club Shirt"),
]
QBODA_VALUE = 50
STARBUCKS_VALUE = 30
# Loop through received qdoba
for index in range(len(received_qdoba)):
    received_qdoba_row = received_qdoba.iloc[index]
    first_name = received_qdoba_row["First Name"]
    last_name = received_qdoba_row["Last Name"]
    nuid = received_qdoba_row["NUID"]
    added_to_qdoba_list[first_name+" "+last_name] = nuid
# Loop through received starbucks
for index in range(len(received_starbucks)):
    received_starbucks_row = received_starbucks.iloc[index]
    first_name = received_starbucks_row["First Name"]
    last_name = received_starbucks_row["Last Name"]
    nuid = received_starbucks_row["NUID"]
    added_to_starbucks_list[first_name+" "+last_name] = nuid
# Loop through participant questions
for index in range(len(participant_questions)):
    participant_question_list = participant_questions.iloc[index]
    first_name = participant_question_list["FIRSTNAME"]
    last_name = participant_question_list["LASTNAME"]
    nuid_list[first_name+" "+last_name] = participant_question_list["NUID"]
# Loop through incentive csv
for index in range(len(participants)):
    participant = participants.iloc[index]
    if participant["EVENTNAME"] == 'University of Nebraska, Lincoln - HuskerThon 2023':
        first_name = participant["PARTICIPANTFIRSTNAME"]
        last_name = participant["PARTICIPANTLASTNAME"]
        email = participant["PARTICIPANTEMAIL"]
        phone_number = participant["PARTICIPANTMOBILEPHONE"]
        sum_donations = participant["PARTICIPANTSUMDONATIONS"]
        incentive_array = [""]*17
        incentive_array[0] = first_name + " " + last_name
        current_index = 1
        for i in range(len(incentives)):
            if sum_donations >= incentives[i][0]:
                incentive_array[current_index] = incentives[i][1]
                current_index = current_index + 1
        if sum_donations>0:
            individual_sheet.append([first_name, last_name, email, phone_number, sum_donations])
            incentives_sheet.append(incentive_array)
        if first_name+" "+last_name in nuid_list.keys():
            nuid = nuid_list[first_name+" "+last_name]
            if sum_donations > QBODA_VALUE and not first_name+" "+last_name in added_to_qdoba_list.keys():
                added_to_qdoba_list[first_name+" "+last_name] = nuid
                qboda_sheet.append([first_name,last_name,int(nuid),sum_donations])
            if sum_donations > STARBUCKS_VALUE and not first_name+" "+last_name in added_to_starbucks_list.keys():
                added_to_starbucks_list[first_name + " " + last_name] = nuid
                starbucks_sheet.append([first_name,last_name,int(nuid),sum_donations])

column_names = [""] * 17
column_names[0] = "Full Name"
print_individual_sheet = pd.DataFrame(individual_sheet, columns=['First Name', 'Last Name', 'Email', 'Phone Number', 'Sum Donation'])
print_individual_sheet.to_csv('individual_sheet.csv')
print_incentive_sheet = pd.DataFrame(incentives_sheet, columns=column_names)
print_incentive_sheet.to_csv('incentive_sheet.csv')

qdoba_new_sheet = pd.DataFrame(qboda_sheet, columns=["First Name","Last Name", 'NUID',"Total Amount Raised"])
qdoba_new_sheet.to_csv('new_qdoba_sheet.csv')

starbucks_new_sheet = pd.DataFrame(starbucks_sheet, columns=["First Name","Last Name", 'NUID',"Total Amount Raised"])
starbucks_new_sheet.to_csv('new_starbucks_sheet.csv')