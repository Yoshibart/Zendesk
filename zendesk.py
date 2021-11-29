import requests
import json
from requests.auth import  HTTPBasicAuth

username = "oworibarnet@gmail.com"
password = "qadmin-vybwy1-munBuc"
url = "https://zccbarnet.zendesk.com/api/v2/tickets"

class ZenCoding:
    '''
    Program prints certain elements of the class for the API
    '''
    def __init__(self, url, username, password):
        self.response = requests.get(url, auth=HTTPBasicAuth(username, password))
        self.start_program()
    
    def Menu(self):
        print("\nWelcome to Zendesk Coding Assessment\n")
        print("\n--------------Menu----------------\n")
        print("\nPress 1: Display all the tickets\n")
        print("\nPress 2: Display a ticket\n") 
        print("\nPress 3: Exit\n") 

    def start_program(self):
        if(self.response.status_code == 400):
            print("\nInvalid syntax for this request was provided.\n")

        elif(self.response.status_code == 401):
            print("\nYou are unauthorized to access the requested resource. Please log in.")

        elif(self.response.status_code == 404):
            print("\nWe could not find the resource you requested")

        elif(self.response.status_code == 200):
            self.program()

    def print_data(self, tick):
        print("\n-------------------------- TICKET "+str(tick["id"])+" -----------------------")
        print("\n---------------------------------------------------------------")
        print("\nCreatedAt:      " + tick["created_at"])
        print("\nSubject:        " + tick["subject"])
        print("\nAssignedTo:     " + str(tick["assignee_id"]))
        print("\nRequestedBy:    " + str(tick["requester_id"]))
        print("\nLocatedAt:      " + tick["url"])
        print("\n---------------------------------------------------------------")


    def program(self):
        self.response = json.loads(self.response.text)
        self.response = [ticket for ticket in self.response["tickets"]]
        while(True):
            self.Menu()
            opt = input("\nEnter Option 1, 2 or 3: ")
            if(opt.isdecimal()):
                opt = int(opt)
        
                if(opt == 1):
                    for tick in self.response:
                        self.print_data(tick)
                if(opt == 2):
                    option = input("\nEnter the TICKET ID: ")
                    if(option.isdecimal()):
                        option = int(option)
                        if(option in [ticket["id"] for ticket in self.response]):
                            tick = [ticket for ticket in self.response if(ticket["id"] == option)]
                            self.print_data(tick[0])
                        else:
                            print("\n------------------------------------")
                            print("\nTICKET NOT FOUND")
                            print("\n------------------------------------")
                if(opt == 3):
                    print("\nThanks!!!!!\n")
                    break


ZenCoding(url, username, password)
