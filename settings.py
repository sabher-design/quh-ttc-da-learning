from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [
    dict(
        name='SH',
        num_demo_participants=4,
        app_sequence=['SHda','SHda1'],
    )
]
# session1 app_sequence=['SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17'
# 'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8']

# session2 app_sequence=['SHttc7', 'SHttc12', 'SHttc19', 'SHttc15', 'SHttc9', 'SHttc5', 'SHttc4', 'SHttc6', 'SHttc20', 'SHttc16'
# 'SHttc11', 'SHttc1', 'SHttc17', 'SHttc13', 'SHttc2', 'SHttc3', 'SHttc14', 'SHttc8', 'SHttc10', 'SHttc18']

LANGUAGE_CODE = 'de'
LANGUAGE = 'de'
REAL_WORLD_CURRENCY_CODE = 'EUR'
#REAL_WORLD_CURRENCY_DECIMAL_PLACES = True
USE_POINTS = True
POINTS_CUSTOM_NAME = 'ECU'
DEMO_PAGE_INTRO_HTML = ''
#POINTS_DECIMAL_PLACES = False
PARTICIPANT_FIELDS = []
#SESSION_FIELDS = []
#ROOMS = []


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = '3=&13do*ayi(=fc0a_t1!*n&pwa$q1myi!q0cdit+pk-9-_7t('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


