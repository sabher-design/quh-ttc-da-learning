#from otree.api import Currency as c, currency_range
#from ._builtin import Page, WaitPage
#from .models import Constants
from itertools import chain
from .user_settings import Constants
from otree.api import *

# METHOD: =================================================================================== #
# DEFINE VARIABLES USED IN ALL TEMPLATES ==================================================== #
# =========================================================================================== #
print(f"val12 SHttc12: {Constants.val12}")
print(f"prio12 SHttc12: {Constants.prio12}")


def vars_for_all_templates(self):
    return {
        'nr_courses': Constants.nr_courses,
        'players_per_group': Constants.players_per_group,
        'indices': [j for j in range(1, Constants.nr_courses + 1)],
        'val12': self.participant.vars['val12'],
        'val12_others': zip(self.participant.vars['other_types_names'],
                                 self.participant.vars['val12_others']),
        'prio12': self.participant.vars['prio12'],
        'capacities': Constants.capacities
    }


class Instructions(Page):
    pass


class InstructionsFramed(Page):
    pass


class Decision(Page):

    form_model = 'player'

    # METHOD: =================================================================================== #
    # RETRIEVE FORM FIELDS FROM MODELS.PY ======================================================= #
    # =========================================================================================== #
    def get_form_fields(self):
        form_fields = \
            list(chain.from_iterable([list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1:]))

        return form_fields

    # METHOD: =================================================================================== #
    # CREATE VARIABLES TO DISPLAY ON DECISION.HTML ============================================== #
    # =========================================================================================== #
    def vars_for_template(self):
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]

        return {
                'form_fields': form_fields,
                'nr_courses': Constants.nr_courses,
                'indices': [j for j in range(1, Constants.nr_courses + 1)],
                'val12': self.participant.vars['val12'],
                'val12_others': zip(self.participant.vars['other_types_names'],
                                     self.participant.vars['val12_others']),
                'players_per_group': Constants.players_per_group,
                'prio12': self.participant.vars['prio12'],
                'capacities': Constants.capacities,
                'player.role': self.participant.vars['role']
                }

    # METHOD: =================================================================================== #
    # BEFORE NEXT PAGE: WRITE BACK PLAYER PREFS TO PARTICIPANT VARS ============================= #
    # =========================================================================================== #
    def before_next_page(self):
        # CREATE INDICES FOR MOST IMPORTANT VARS ================================================ #
        indices = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][0]
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]

        # DYNAMICALLY WRITE BACK PLAYER PREFS TO A LIST OF PREFS ================================ #
        for n, pref in zip(indices, form_fields):
            choice_i = getattr(self.player, pref)
            self.participant.vars['player_prefs'][n - 1] = [int(choice_i)]

    # METHOD: =================================================================================== #
    # CONTROL PREFS: PREFERENCES MUST BE UNIQUE ================================================= #
    # =========================================================================================== #
    def error_message(self, values):
        indices = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][0]
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]
        sum_of_prefs = sum([values[i] for i in form_fields])

        if sum_of_prefs != sum(indices):
            return 'Ihre Präferenzen müssen von 1 bis %s angegeben werden!' % (indices[-1])


class ResultsWaitPage(WaitPage):

    # METHOD: =================================================================================== #
    # AFTER ALL PLAYERS HAVE SUBMITTED PREFS: RUN TTC MECHANISM AND SET PLAYERS' PAYOFFS ======== #
    # =========================================================================================== #
    def after_all_players_arrive(self):
        self.group.get_allocation()
        self.group.set_payoffs()


class Results(Page):

    # METHOD: =================================================================================== #
    # CREATE VARIABLES TO DISPLAY ON RESULTS.HTML =============================================== #
    # =========================================================================================== #
    def vars_for_template(self):
        player_prefs = [i[0] for i in self.participant.vars['player_prefs']]
        success12 = [i for i in self.participant.vars['success12']]

        return {
                'player_prefs': player_prefs,
                'success12': success12,
                'indices': [j for j in range(1, Constants.nr_courses + 1)],
                'val12': self.participant.vars['val12']
                }


class Thanks(Page):
    pass


page_sequence = [
    Decision,
    ResultsWaitPage,
    Results,
]

#if Constants.application_framing:
 #   if Constants.instructions:
  #      page_sequence.insert(0, InstructionsFramed)

   # if Constants.results:
    #    page_sequence.insert(-1, Results)

#else:
 #   if Constants.instructions:
  #      page_sequence.insert(0, Instructions)

   # if Constants.results:
    #    page_sequence.insert(-1, Results)
