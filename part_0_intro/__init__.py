
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'part_0_intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass

class p1_Consent(Page):
    form_model = 'player'

class p2_GeneralInstructions(Page):
    form_model = 'player'

class p3_GeneralProcedure(Page):
    form_model = 'player'

class p4_DecisionPage(Page):
    form_model = 'player'

page_sequence = [p1_Consent, p2_GeneralInstructions, p3_GeneralProcedure, p4_DecisionPage]