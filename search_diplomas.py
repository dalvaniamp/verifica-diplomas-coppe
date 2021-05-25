from page import Page
import json

class CheckIfDiplomasAreReady():
    def __init__(self):
        #TODO finish the settings
        config = open('people.json')
        people=json.load(config)

        #TODO add while loop for this
        pagina=Page('https://registro.daac.coppe.ufrj.br/relacao-de-diplomas/')
        pagina=Page('https://registro.daac.coppe.ufrj.br/relacao-de-diplomas/')
        
       
        for person in people:
            if pagina.name_is_there(person.name):
                #TODO send email
                print('achou')   

        pagina.close()

            
CheckIfDiplomasAreReady()


 
