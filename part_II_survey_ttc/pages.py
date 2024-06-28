from otree.api import  (
    Currency as c, currency_range
)
from ._builtin import Page, WaitPage
from .models import Constants


### PAGES

class SurveyStart(Page):
    form_model = 'player'  # tells me which model I use from above (player)


class SurveyStrategies(Page):
    form_model = 'player'
    form_fields = ['pref_decision', 'truth_telling_decision', 'explanation_tt_yes', 'explanation_tt_no']

    def error_message(self, values):
        if values['truth_telling_decision'] == 'yes' and not values['explanation_tt_yes']:
            return 'Please fill in the explanation for your YES decision.'
        elif values['truth_telling_decision'] == 'no' and not values['explanation_tt_no']:
            return 'Please fill in the explanation for your NO decision.'


class SurveyMechanism(Page):
    form_model = 'player'
    form_fields = ['mechanism_fair', 'mechanism_efficient', 'mechanism_comprehensive']


class SurveyTrust(Page):
    form_model = 'player'
    form_fields = ['trust_general', 'trust_mechanism', 'trust_institutions_gvmnt', 'trust_institutions_city', 'trust_institutions_educ']

'''class SurveyEconPrefsLoss(Page):
    form_model = 'player'
    #@staticmethod
    #def get_form_fields(player: Player):
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']  # tells me which field I want the input from
    #      return form_fields'''


class SurveyEconPrefsLoss(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']

    class MyPage(Page):
        form_model = 'player'
        form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']

        def get_form(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None,
                     label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None,
                     renderer=None):
            form = super().get_form(data, files, auto_id, prefix, initial, label_suffix, empty_permitted,
                                    instance, use_required_attribute, renderer)

            loss_choices = [[float(loss), f'{loss}'] for loss in Constants.loss] + [['toss', f'{Constants.gain}']]

            for field_name in self.form_fields:
                form.fields[field_name].choices = [('not_toss', 'Ich möchte die Münze nicht werfen'),
                                                   ('toss', 'Ich möchte die Münze werfen')]

            return form


class SurveyEconPrefsRisk(Page):
    form_model = 'player'
    form_fields = ['risk']

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


class SurveyDemographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'studying_currently', 'study_field', 'current_occupation', 'semester', 'math_grade',
                   'abi_grade']


class Payoff(Page):
    form_model = 'player'


page_sequence = [SurveyStart, SurveyStrategies, SurveyMechanism, SurveyTrust, SurveyEconPrefsLoss, SurveyEconPrefsRisk,
                 CognitiveReflectionTest, SurveyDemographics, Payoff]

#page_sequence = [Payoff]

# class LossAversion(Page):
# form_model = 'player'
#  @staticmethod ## I think this is for the results after people made a choice
#   def get_form_fields(player: Player):

#     import random

#     form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']
#    random.shuffle(form_fields)
#   return form_fields

# def form_fields(player):
#    if player.truth_telling_decision == 'no':
#       return ['explanation_tt_no']  # display explanation_tt_yes if truth_telling_decision has answer 'yes'
#  return ['truth_telling_decision']  # display q1 by default

#  def before_next_page(request):
#     if 'truth_telling_decision' in form_fields and 'truth_telling_decision' in request.POST:
#        player.truth_telling_decision_yes = request.POST[
#           'truth_telling_decision']  # store answer truth_telling decision in player model
