from google.oauth2 import service_account
from googleapiclient.discovery import build
import csv, qrcode, os


class formConfig():
    #get necessary permissions from google
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            'config_files/service_account.json',
            scopes=['https://www.googleapis.com/auth/forms.body',
                    'https://www.googleapis.com/auth/forms.responses.readonly']
        )
        self.service = build('forms', 'v1', credentials=creds)
    
    #create form's body
    def createForm(self):
        self.form_config = {
            "info": {
                "title": "Mark your presence",
                "documentTitle": "ScanPresence"
            }
        }

        self.id_input = {
            "requests": [{
                "createItem": {
                    "item": {
                        "title": "Enter school ID",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {
                                    "paragraph": False
                                }
                            }
                        }
                    },
                    "location": {
                        "index": 0
                    }
                }
            }]
        }
        self.form_body = self.service.forms().create(body=self.form_config).execute()
        self.question = self.service.forms().batchUpdate(formId=self.form_body["formId"], body=self.id_input).execute()

    #generate qrcode with form's link and save it
    def saveQr(self):
        qr = qrcode.make(form.form_body["responderUri"])
        qr.save("images/qrcode.png")

    #count every new response
    def countResponses(self):
        length = 0
        while length < 5:
            self.form_responses = self.service.forms().responses().list(formId=self.form_body["formId"]).execute()
            if self.form_responses:
                responses_count = len(self.form_responses['responses'])
                if length != responses_count:
                    length = responses_count
                    print(length)

    #save responses into a csv file
    def recordResponses(self):
        with open("database/csv_files/id_list.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id"])

            if self.form_responses:
                for item in self.form_responses['responses']:
                    id = item['answers'][self.question['replies'][0]['createItem']['questionId'][0]]['textAnswers']['answers'][0]['value']
                    if id.isdigit():
                        writer.writerow([int(id)])

    #when done, delete form's question and qrcode image
    def finish(self):
        self.deleteQuestion()
        os.remove("images/qrcode.png")

    #delete form's question    
    def deleteQuestion(self):
        delete_item = {
            "requests": [
                {
                    "deleteItem": {
                        "location": {
                            "index": 0
                        }
                    }
                }
            ]
        }
        self.service.forms().batchUpdate(formId=self.form_body["formId"], body=delete_item).execute()
            

#run code
if __name__ == "__main__":
    form = formConfig()
    form.createForm()
    form.saveQr()
    form.countResponses()
    form.recordResponses()
    form.finish()
