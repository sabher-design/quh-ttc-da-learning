from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [
    dict(
        name='SH_ttc_test',
        display_name="SH_t_test",
        num_demo_participants=12,
        # app sequence test:
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'part_II_survey_ttc']
    ),
    dict(
        name='SH_da_test',
        display_name="SH_d_test",
        num_demo_participants=16,
        # app sequence test:
        # app sequence session 1:
        app_sequence=['part_0_intro_da', 'part_I_da', 'part_II_survey_da']
    ),
    dict(
        name='SH_ttc_labtest',
        display_name="SH_t",
        num_demo_participants=12,
        # app sequence session 1:
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17',
        'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8', 'part_II_survey_ttc']
    ),
    dict(
        name='SH_da_labtest',
        display_name="SH_d",
        num_demo_participants=16,
        # app sequence session 1:
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda11', 'SHda7', 'SHda1', 'SHda12', 'SHda19', 'SHda14', 'SHda9', 'SHda5', 'SHda13', 'SHda17',
        'SHda3', 'SHda15', 'SHda20', 'SHda4', 'SHda10', 'SHda16', 'SHda18', 'SHda6', 'SHda2', 'SHda8', 'part_II_survey_da']
    ),
    dict(
        name='SH_ttc_addtest1',
        display_name="SH_t",
        num_demo_participants=12,
        # app sequence session 1:
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17',
        'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8', 'part_II_survey_ttc']
    ),
    dict(
        name='SH_da_addtest1',
        display_name="SH_d",
        num_demo_participants=16,
        # app sequence session 1:
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda11', 'SHda7', 'SHda1', 'SHda12', 'SHda19', 'SHda14', 'SHda9', 'SHda5', 'SHda13', 'SHda17',
        'SHda3', 'SHda15', 'SHda20', 'SHda4', 'SHda10', 'SHda16', 'SHda18', 'SHda6', 'SHda2', 'SHda8', 'part_II_survey_da']
    ),
    dict(
        name='SH_ttc_addtest2',
        display_name="SH_t",
        num_demo_participants=12,
        # app sequence session 1:
        app_sequence=['part_0_intro_ttc', 'part_I_ttc', 'SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17',
        'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8', 'part_II_survey_ttc']
    ),
    dict(
        name='SH_da_addtest2',
        display_name="SH_d",
        num_demo_participants=16,
        # app sequence session 1:
        app_sequence=['part_0_intro_da', 'part_I_da', 'SHda11', 'SHda7', 'SHda1', 'SHda12', 'SHda19', 'SHda14', 'SHda9', 'SHda5', 'SHda13', 'SHda17',
        'SHda3', 'SHda15', 'SHda20', 'SHda4', 'SHda10', 'SHda16', 'SHda18', 'SHda6', 'SHda2', 'SHda8', 'part_II_survey_da']
    )
]


# session1 app_sequence=['SHttc11', 'SHttc7', 'SHttc1', 'SHttc12', 'SHttc19', 'SHttc14', 'SHttc9', 'SHttc5', 'SHttc13', 'SHttc17'
# 'SHttc3', 'SHttc15', 'SHttc20', 'SHttc4', 'SHttc10', 'SHttc16', 'SHttc18', 'SHttc6', 'SHttc2', 'SHttc8']

# session2 app_sequence=['SHttc7', 'SHttc12', 'SHttc19', 'SHttc15', 'SHttc9', 'SHttc5', 'SHttc4', 'SHttc6', 'SHttc20', 'SHttc16'
# 'SHttc11', 'SHttc1', 'SHttc17', 'SHttc13', 'SHttc2', 'SHttc3', 'SHttc14', 'SHttc8', 'SHttc10', 'SHttc18']

# session3 app_sequence=['SHttc20', 'SHttc9', 'SHttc7', 'SHttc16', 'SHttc13', 'SHttc3', 'SHttc4', 'SHttc5', 'SHttc12', 'SHttc15'
# 'SHttc18', 'SHttc10', 'SHttc11', 'SHttc19', 'SHttc14', 'SHttc2', 'SHttc8', 'SHttc17', 'SHttc1', 'SHttc6']

# session4 app_sequence=['SHttc5', 'SHttc2', 'SHttc8', 'SHttc1', 'SHttc19', 'SHttc11', 'SHttc16', 'SHttc12', 'SHttc10', 'SHttc14'
# 'SHttc9', 'SHttc18', 'SHttc7', 'SHttc13', 'SHttc15', 'SHttc20', 'SHttc3', 'SHttc4', 'SHttc6', 'SHttc17']

LANGUAGE_CODE = 'de'
#LANGUAGE = 'de'

REAL_WORLD_CURRENCY_CODE = 'EUR'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = True
USE_POINTS = True
POINTS_CUSTOM_NAME = 'ECU'
DEMO_PAGE_INTRO_HTML = ''
POINTS_DECIMAL_PLACES = False
PARTICIPANT_FIELDS = []
#SESSION_FIELDS = []
#ROOMS = []


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = '3=&13do*ayi(=fc0a_t1!*n&pwa$q1myi!q0cdit+pk-9-_7t('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

