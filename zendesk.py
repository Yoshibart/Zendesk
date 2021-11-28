import requests
import json
from requests.auth import  HTTPBasicAuth
url = "https://zccbarnet.zendesk.com/api/v2/tickets"

response = requests.get(url, auth=HTTPBasicAuth("oworibarnet@gmail.com", "qadmin-vybwy1-munBuc"))
    
if(response.status_code == 400):
        print("\nInvalid syntax for this request was provided.\n")

elif(response.status_code == 401):
    print("\nYou are unauthorized to access the requested resource. Please log in.")

elif(response.status_code == 404):
    print("\nWe could not find the resource you requested")

elif(response.status_code == 200):
    response = json.loads(response.text)
    options = ["id","url","created_at","requester_id","assignee_id", "subject"]
    response = [ticket for ticket in response["tickets"]]
    
    while(True):
        print("\nWelcome to Zendesk Coding Assessment\n")
        print("\n--------------Menu----------------\n")
        print("\nPress 1: Display all the tickets\n")
        print("\nPress 2: Display a ticket\n") 
        print("\nPress 3: Exit\n") 

        opt = input("\nEnter Option 1, 2 or 3: ")
        if(opt.isdecimal()):
            opt = int(opt)
           
            if(opt == 1):
                for ticket in response:
                    print("\n-------------------------- TICKET "+str(ticket["id"])+" -----------------------")
                    print("\n---------------------------------------------------------------")
                    print("\nCreatedAt:      " + ticket["created_at"])
                    print("\nSubject:        " + ticket["subject"])
                    print("\nAssignedTo:     " + str(ticket["assignee_id"]))
                    print("\nRequestedBy:    " + str(ticket["requester_id"]))
                    print("\nLocatedAt:      " + ticket["url"])
                    print("\n---------------------------------------------------------------")

            if(opt == 2):
                option = input("\nEnter the TICKET ID: ")
                if(option.isdecimal()):
                    option = int(option)
                    if(option in [ticket["id"] for ticket in response]):
                        for ticket in response:
                            if(ticket["id"] == option):
                                print("\n-------------------------- TICKET "+str(ticket["id"])+" -----------------------")
                                print("\n---------------------------------------------------------------")
                                print("\nCreatedAt:      " + ticket["created_at"])
                                print("\nSubject:        " + ticket["subject"])
                                print("\nAssignedTo:     " + str(ticket["assignee_id"]))
                                print("\nRequestedBy:    " + str(ticket["requester_id"]))
                                print("\nLocatedAt:      " + ticket["url"])
                                print("\n---------------------------------------------------------------")
                                break
                    else:
                        print("\n------------------------------------")
                        print("\nTICKET NOT FOUND")
                        print("\n------------------------------------")
            if(opt == 3):
                break
