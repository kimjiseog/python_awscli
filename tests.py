import gspread
from oauth2client.service_account import ServiceAccountCredentials


SPREAD_SHEET_NAME = "test" #잠시전 생성한후 공유했던  스프레드시트의 이름입니다

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# credentials = ServiceAccountCredentials.from_json_keyfile_name('D:/python/awscli/credentials/test-9bfcceda0cb0.json', scope)
credentials = ServiceAccountCredentials.from_json_keyfile_name('D:/python/awscli/credentials/hulpei3_credentials.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open(SPREAD_SHEET_NAME).sheet1
wks.update_acell('A1', "Hello, gunman !")
