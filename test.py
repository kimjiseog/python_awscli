import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess

awsinfo=subprocess.check_output('aws ec2 describe-instances --query Reservations[].Instances[].[PrivateIpAddress,PublicIpAddress,InstanceId,SubnetId,InstanceType,State.Name,KeyName,SecurityGroups,LaunchTime,Tags[?Key==`Name`].Value[]] --profile platform --output text', shell=True)
SPREAD_SHEET_NAME ="test"

scope =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('D:/python/awscli/test-4db795ba475c.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open(SPREAD_SHEET_NAME).sheet1
# wks.delete_row(2)
# print(wks.get_all_records())
wks.append_row()

# wks.update_acell('A1', "Hello, gunman !")
