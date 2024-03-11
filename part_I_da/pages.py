from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


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