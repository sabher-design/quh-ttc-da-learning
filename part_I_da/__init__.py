from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'part_I_da'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass

class Player(BasePlayer):

    ctrq1_da = models.IntegerField(label='1. Wie viele Schüler:innen bewerben sich für einen Schulplatz?', min=0)
    ctrq2_da = models.IntegerField(label='2. Sobald alle Schüler:innen an einer Schule zugelassen wurden, wie viele Plätze bleiben übrig?', min=0)
    ctrq3_da_blue = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    ctrq3_da_yellow = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    ctrq3_da_orange = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    ctrq3_da_purple = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    mc1_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='1. Bei der Entscheidung, welche Präferenzliste man an die zentrale Zulassungsstelle übermittelt, sollte man darauf achten, dass man sich nicht bei der beliebtesten Schule zuerst bewirbt.')
    mc2_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='2. Es ist ausschlaggebend für die Erstellung der eigenen Präferenzliste, die Wertetabelle für alle anderen Schüler:innen zu kennen.')
    mc3_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='3. Das Zulassungsverfahren ist so konstruiert, dass die übermittelte Präferenzliste immer mit der Reihenfolge übereinstimmen sollte, die sich aus der Wertetabelle ergibt.')
    mc4_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='4. Ihre Präferenzliste sollte nur mit der Reihenfolge aus der Wertetabelle übereinstimmen, wenn Sie sicher sind, dass alle Schüler:innen ebenso verfahren.')
class p5a_mechanism(Page):
    form_model = 'player'

class p6a_example(Page):
    form_model = 'player'

class p7a_ctrq_1(Page):
    form_model = 'player'
    form_fields = ['ctrq1_da', 'ctrq2_da']

class p7a_ctrq_2(Page):
    form_model = 'player'
    form_fields = ['ctrq3_da_blue', 'ctrq3_da_yellow', 'ctrq3_da_orange', 'ctrq3_da_purple']

class p7a_mc(Page):
    form_model = 'player'
    form_fields = ['mc1_da', 'mc2_da', 'mc3_da', 'mc4_da']

class p8a_info_decision_start(Page):
    form_model = 'player'

page_sequence = [p5a_mechanism, p6a_example, p7a_ctrq_1, p7a_ctrq_2, p7a_mc, p8a_info_decision_start]