from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class p1_Consent(Page):
    form_model = 'player'


class p2_GeneralInstructions(Page):
    form_model = 'player'


class p3_GeneralProcedure(Page):
    form_model = 'player'


class p4_DecisionPage(Page):
    form_model = 'player'


page_sequence = [p1_Consent, p2_GeneralInstructions, p3_GeneralProcedure, p4_DecisionPage]