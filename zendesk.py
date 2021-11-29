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

    def program(self):
        self.response = json.loads(self.response.text)
        self.response = [ticket for ticket in self.response["tickets"]]
        while(True):
            self.Menu()
            opt = input("\nEnter Option 1, 2 or 3: ")
            if(opt.isdecimal()):
                opt = int(opt)
        
                if(opt == 1):
                    for ticket in self.response:
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
                        if(option in [ticket["id"] for ticket in self.response]):
                            for ticket in self.response:
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
                    print("\n")
                    break


ZenCoding(url, username, password)
