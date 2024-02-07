from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'part_I_ttc'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass

class Player(BasePlayer):

    ctrq1_ttc = models.IntegerField(label='1. Wie viele Schüler:innen bewerben sich für einen Schulplatz?', min=0)
    ctrq2_ttc = models.IntegerField(
        label='2. Sobald alle Schüler:innen an einer Schule zugelassen wurden, wie viele Plätze bleiben übrig?', min=0)
    ctrq3_ttc_blue = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    ctrq3_ttc_yellow = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    ctrq3_ttc_orange = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    ctrq3_ttc_purple = models.StringField(choices=['A', 'B', 'C', 'D'], label=' ')
    mc1_ttc = models.StringField(choices=['Richtig', 'Falsch'],
                                label='1. Bei der Entscheidung, welche Präferenzliste man an die zentrale Zulassungsstelle übermittelt, sollte man darauf achten, dass man sich nicht bei der beliebtesten Schule zuerst bewirbt.')
    mc2_ttc = models.StringField(choices=['Richtig', 'Falsch'],
                                label='2. Es ist ausschlaggebend für die Erstellung der eigenen Präferenzliste, die Wertetabelle für alle anderen Schüler:innen zu kennen.')
    mc3_ttc = models.StringField(choices=['Richtig', 'Falsch'],
                                label='3. Das Zulassungsverfahren ist so konstruiert, dass die übermittelte Präferenzliste immer mit der Reihenfolge übereinstimmen sollte, die sich aus der Wertetabelle ergibt.')
    mc4_ttc = models.StringField(choices=['Richtig', 'Falsch'],
                                label='4. Ihre Präferenzliste sollte nur mit der Reihenfolge aus der Wertetabelle übereinstimmen, wenn Sie sicher sind, dass alle Schüler:innen ebenso verfahren.')


class p5b_mechanism(Page):
    form_model = 'player'


class p6b_example(Page):
    form_model = 'player'


class p7b_ctrq_1(Page):
    form_model = 'player'
    form_fields = ['ctrq1_ttc', 'ctrq2_ttc']


class p7b_ctrq_2(Page):
    form_model = 'player'
    form_fields = ['ctrq3_ttc_blue', 'ctrq3_ttc_yellow', 'ctrq3_ttc_orange', 'ctrq3_ttc_purple']


class p7b_mc(Page):
    form_model = 'player'
    form_fields = ['mc1_ttc', 'mc2_ttc', 'mc3_ttc', 'mc4_ttc']


class p8b_info_decision_start(Page):
    form_model = 'player'


page_sequence = [p5b_mechanism, p6b_example, p7b_ctrq_1, p7b_ctrq_2, p7b_mc, p8b_info_decision_start]