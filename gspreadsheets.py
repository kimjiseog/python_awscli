from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('client_secret.json')
creds = store.get()

# if not creds or creds.invalid:
#     flow = client.flow_from_clientsecrets('D:/python/awscli/credentials/client_secret.json', SCOPES)
#     creds = tools.run_flow(flow, store)
# service = build('sheets', 'v4', http=creds.authorize(Http()))
#
# # Call the Sheets API
# SPREADSHEET_ID = '1i-WlketCcKEXP_p1289hK8tsZZncMq4Ff04Z5UeTuKY'
# RANGE_NAME = 'Class Data!A2:E'
# result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
#                                              range=RANGE_NAME).execute()
# values = result.get('values', [])
# if not values:
#     print('No data found.')
# else:
#     print('Name, Major:')
#     for row in values:
#         # Print columns A and E, which correspond to indices 0 and 4.
#         print('%s, %s' % (row[0], row[4]))
