import os

HOST = 'https://dev-gs.qa-playground.com/api/v1' if os.environ['STAGE'] == 'qa' else 'https://release-gs.qa-playground.com/api/v1'


class Endpoints:

    get_users_list = f'{HOST}/users'
    create_user = f'{HOST}/users'
    def get_user_by_id(self, uuid): return f'{HOST}/users/{uuid}'
