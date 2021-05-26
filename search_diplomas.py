from email_utils import EmailUtils
from page import Page
import json
import logging

class CheckIfDiplomasAreReady():   

        with open('people.json') as json_file:
            data=json.load(json_file)        


        #TODO add while loop for this
        pagina=Page('https://registro.daac.coppe.ufrj.br/relacao-de-diplomas/')
        pagina=Page('https://registro.daac.coppe.ufrj.br/relacao-de-diplomas/')
        
       
        for person in data['people']:
            if pagina.name_is_there(person['name']):
                EmailUtils.send_email(person['email'])

        pagina.close()

            
CheckIfDiplomasAreReady()



 
