import requests
import pandas as pd

url= "https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv"

df = pd.read_csv(url, sep="\t")

#resp = requests.get("https://api.telegram.org/bot6210930301:AAHYmBcf-KdVb0wqBJwyeYPiqTQX_YIi_Y4/getupdates?offset=82939876")

#{"ok":true,"result":[{"update_id":82939871,
#"message":{"message_id":4,"from":{"id":5474186099,"is_bot":false,"first_name":"Himanshu","username":"savage_psycho","language_code":"en"},"chat":{"id":-805186237,"title":"Bot testing"

base_url= "https://api.telegram.org/bot6210930301:AAHYmBcf-KdVb0wqBJwyeYPiqTQX_YIi_Y4"

#82939876
def readMessage(offset):
	parameters= {
	                   "offset": offset
	                   
	}
	resp=requests.get(base_url + "/getupdates", data=parameters)
	data = resp.json()
	
	print(data)
	
	for result in data["result"]:
		sendMessage(result)
		
		if data["result"]:
			return data["result"][-1]["update_id"] +1

def autoMsg(message):
	answer = df.loc[df["Question"].str.lower() == message.lower()]	
	if not answer.empty:
		answer= answer.iloc[0]["Answer"]
		return answer
	else:
		return "sorry i dont have answer for this"
				
def sendMessage(message):
		text = message["message"]["text"]
		message_id = message["message"]["message_id"]
		answer = autoMsg(text)
		parameters = {
         		     "chat_id": "@bottestn",
         		     "text":answer,
         		     "reply_to_message_id":message_id
         }
		
		resp= requests.get(base_url + "/sendMessage", data=parameters)
		print(resp.text)
offset=0
while True:		
	offset= readMessage(offset)
