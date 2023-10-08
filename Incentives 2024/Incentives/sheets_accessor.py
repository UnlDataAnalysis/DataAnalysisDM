# Landry Geiger
# 10/4/2022

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from typing import List


class SheetsAccessor:
    def __init__(self, path_to_keys: str):
        # Create API connection
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        creds = service_account.Credentials.from_service_account_file(path_to_keys, scopes=scopes)
        service = build('sheets', 'v4', credentials=creds)
        self.sheets_api = service.spreadsheets()

    def get(self, sheet_id: str, range: str) -> List[List[str]]:
        '''Returns a 2D list of the data in the specified spreadsheet over the specified range.'''
        result = self.sheets_api.values().get(spreadsheetId=sheet_id, range=range).execute()

        # Get values, if no values: []
        values = result.get('values', [])

        return values

    def update(self, sheet_id: str, range: str, data: List[List[any]]) -> None:
        '''Inserts a 2D list of data into the specified spreadsheet at the specified range.'''
        self.sheets_api.values().update(spreadsheetId=sheet_id, range=range, valueInputOption='USER_ENTERED', body={'values': data}).execute()


def main():
    # Initialize our SheetsAccessor with the service account keys found in keys.json
    accessor = SheetsAccessor('keys.json')

    # ID of the spreadsheet we'd like to read/write
    spreadsheet_id = '1tqX-bPdAKCI-IeOYLVt0Ij543Teph02BNeTby0_G0hA'

    # Print out some data from a specified range
    range = 'Sheet1!A1:E1'
    print(accessor.get(spreadsheet_id, range))

    # # Insert some data at a specified point
    # data_to_insert = [['test', 'eegs'],
    #                   ['yo yo', 3.98]]
    # accessor.update(spreadsheet_id, 'Sheet1!E4', data_to_insert)


if __name__ == '__main__':
    main()