import os

def construct_url():
    client_id = os.environ.get('CLIENT_ID')
    permissions = os.environ.get('BOT_PERMISSIONS')
    url = 'https://discordapp.com/oauth2/authorize?&client_id={}&scope=bot&permissions={}'.format(client_id, permissions)
    print(url)

construct_url()
