from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

doc = ''

## everything here changed, so if I want to go back to the previous version, I need to look at the local program

'''def read_csv_stimuli():
    import csv

    f = open('part_II_survey\static\part_II_survey\stimuli.csv', encoding='utf-8-sig')
    rows = [row for row in csv.DictReader(f)]
    for row in rows:
        # all values in CSV are string unless you convert them
        row['loss'] = (row['loss'])
    return rows'''


class Constants(BaseConstants):
    name_in_url = 'part_II_survey_ttc'
    players_per_group = None
    num_rounds = 1
    loss = [2, 3, 4, 5, 6, 7] #read_csv_stimuli()
    gain = 6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# define the questions a player must answer here
class Player(BasePlayer):
    ### MODELS/FUNCTIONS

    '''def make_field(self):
        return models.IntegerField(
            choices=[[float(Constants.loss[self]['loss']), Constants.loss[self]['loss']], ['toss', Constants.gain]],
            # label='',  # f"{C.GAIN} right now or {C.LOSS[number]['loss']} in ",
            widget=widgets.RadioSelect
        )'''

    q1 = models.IntegerField(choices=[(0, 'Ich möchte die Münze nicht werfen'), (1, 'Ich möchte die Münze werfen')], widget=widgets.RadioSelectHorizontal(), label="2€")
    q2 = models.IntegerField(choices=[(0, 'Ich möchte die Münze nicht werfen'), (1, 'Ich möchte die Münze werfen')], widget=widgets.RadioSelectHorizontal(), label="3€")
    q3 = models.IntegerField(choices=[(0, 'Ich möchte die Münze nicht werfen'), (1, 'Ich möchte die Münze werfen')], widget=widgets.RadioSelectHorizontal(), label="4€")
    q4 = models.IntegerField(choices=[(0, 'Ich möchte die Münze nicht werfen'), (1, 'Ich möchte die Münze werfen')], widget=widgets.RadioSelectHorizontal(), label="5€")
    q5 = models.IntegerField(choices=[(0, 'Ich möchte die Münze nicht werfen'), (1, 'Ich möchte die Münze werfen')], widget=widgets.RadioSelectHorizontal(), label="6€")
    q6 = models.IntegerField(choices=[(0, 'Ich möchte die Münze nicht werfen'), (1, 'Ich möchte die Münze werfen')], widget=widgets.RadioSelectHorizontal(), label="7€")


    pref_decision = models.LongStringField(
        label='1. Wie haben Sie Ihre Entscheidung über die Präferenzlisten getroffen?')
    '''truth_telling_decision = models.StringField(choices=[['yes',
                                                          'Ja, ich habe meine Präferenzlisten so erstellt, dass sie der Reihenfolge der Werte aus der Wertetabelle entsprachen.'],
                                                         ['no',
                                                          'Nein, ich habe meine Präferenzlisten nicht so erstellt.']],
                                                label='2. Haben Sie Ihre Präferenzlisten meistens oder immer so erstellt, dass sie der Reihenfolge der Werte aus der Wertetabelle entsprachen?',
                                                widget=widgets.RadioSelect)'''
    truth_telling_decision = models.BooleanField(
        label='2. Haben Sie Ihre Präferenzlisten meistens oder immer so erstellt, dass sie der Reihenfolge der Werte aus der Wertetabelle entsprachen?',
        widget=widgets.RadioSelect,
        choices=[[True, 'Ja, ich habe meine Präferenzlisten so erstellt, dass sie der Reihenfolge der Werte aus der Wertetabelle entsprachen.'], [False, 'Nein, ich habe meine Präferenzlisten nicht so erstellt.']]
    )
    explanation_tt_yes = models.LongStringField(
        label='Warum haben Sie Ihre Präferenzliste so erstellt, dass Sie der Reihenfolge der Werte aus der Wertetabelle entsprachen?',
        blank=True)
    explanation_tt_no = models.LongStringField(
        label='Warum haben Sie Ihre Präferenzliste nicht so erstellt, dass Sie der Reihenfolge der Werte aus der Wertetabelle entsprachen?',
        blank=True)
    mechanism_fair = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''3. ... für fair?'''
    )
    mechanism_efficient = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''4. ... für effizient?'''
    )
    mechanism_comprehensive = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''5. ... für verständlich?'''
    )
    trust_general = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''6. Solange ich nicht vom Gegenteil überzeugt bin, gehe ich davon aus, dass Menschen nur die besten
        Absichten haben.'''
    )
    trust_mechanism = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''7. Ich bin davon überzeugt, dass das Zulassungsverfahren aus dem ersten Teil gut funktioniert.'''
    )
    trust_institutions_gvmnt = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''8. Im Allgemeinen habe ich Vertrauen in die Regierung.'''
    )
    trust_institutions_city = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''9. Im Allgemeinen habe ich Vertrauen in städtischen Behörden.'''
    )
    trust_institutions_educ = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''10. Im Allgemeinen habe ich Vertrauen in Bildungsbehörden.'''
    )
    crt_bat = models.DecimalField(max_digits=4, decimal_places=2, label='11. Ein Schläger und ein Ball kosten insgesamt 1,10€. Der Schläger kostet 1€ mehr als der Ball. Wie viel kostet der Ball?')
    crt_widget = models.DecimalField(max_digits=4, decimal_places=2, label='12. Wenn 5 Maschinen 5 Minuten brauchen um 5 Produkte herzustellen, wie lange benötigen dann 100 Maschinen, um 100 Produkte herzustellen?')
    crt_lake = models.DecimalField(max_digits=4, decimal_places=2, label='13. In einem See wachsen Seerosen, die sich jeden Tag verdoppeln. Wenn es 48 Tage dauert, bis der ganze See bedeckt ist, wie lange dauert es, bis die Seerosen die Hälfte des Sees bedecken?')
    gender = models.StringField(choices=[['female', 'Weiblich'], ['male', 'Männlich'], ['diverse', 'Divers'],
                                         ['no_gender', 'Ich identifiziere mich mit keinem Geschlecht']],
                                label='Mit welchem Geschlecht identifizieren Sie sich?',
                                widget=widgets.RadioSelect)
    age = models.IntegerField(label='Wie alt sind Sie?', max=125, min=16)
    studying_currently = models.StringField(
        label="Studieren Sie derzeit oder haben Sie ein Studium abgeschlossen?",
        widget=widgets.RadioSelect,
        choices=[
            ['1 - currently student', "Ich studiere derzeit."],
            ['2 - currently doctoral student', "Ich promoviere."],
            ['3 - has graduated from university', "Ich habe ein Studium abgeschlossen."],
            ['0 - no university education', "Nein."],
        ]
    )
    study_field = models.StringField(
        label="In welchem Studiengang studieren Sie bzw. haben Sie studiert?",
        choices=[
            ['Humanities',
             "Geisteswissenschaften (z. B. Sprachen, Medienwissenschaften, Philosophie, Kunstgeschichte)"],
            ['Art and music', "Kunst und Musik"],
            ['Mathematics', "Mathematik, Informatik, Technik oder Ingenieurwissenschaften"],
            ['Natural sciences', "Naturwissenschaften (z. B. Biologie, Chemie, Physik, Agrarwissenschaften)"],
            ['Medicine', "Medizin"],
            ['Psychology', "Psychologie"],
            ['Law', "Rechtswissenschaft"],
            ['Social sciences',
             "Sozial- oder Kulturwissenschaften (inkl. z. B. Politikwissenschaft, Anthropologie, Geschichte)"],
            ['Economic sciences',
             "Wirtschaftswissenschaften (BWL, VWL, Wirtschaftsingenieurwesen, Wirtschaftsmathematik)"],
            ['Other', "Anderer Studiengang"],
        ],
        blank=True
    )
    current_occupation = models.StringField(
        label="Welcher Beschäftigung gehen Sie derzeit nach?",
        choices=[
            ['Occupied', "Ich bin erwerbstätig."],
            ['Jobless', "Ich bin arbeitslos."],
            ['Retired', "Ich bin im Ruhestand."],
            ['Parental leave', "Ich befinde mich in Elternzeit."],
            ['Student', "Ich studiere."],
            ['Apprentice', "Ich absolviere eine Ausbildung."],
            ['Sabbatical', "Ich mache ein Sabbatical."],
            ['Other', "Sonstiges."],
        ],
        blank=True
    )
    # subject = models.LongStringField(label='In welchem Studienfach sind Sie (hauptsächlich) eingeschrieben?')
    semester = models.StringField(choices=[['semester_1', '1. Fachsemester'], ['semester_2', '2. Fachsemester'],
                                           ['semester_3', '3. Fachsemester'], ['semester_4', '4. Fachsemester'],
                                           ['semester_5', '5. Fachsemester'], ['semester_6', '6. Fachsemester'],
                                           ['semester_7', '7. Fachsemester'], ['semester_8', '8. Fachsemester'],
                                           ['semester_9', '9. Fachsemester'], ['semester_10', '10. Fachsemester'],
                                           ['semester_11', '11. Fachsemester'], ['semester_12', '12. Fachsemester'],
                                           ['semester_13', '13. Fachsemester'], ['semester_14', '14. Fachsemester'],
                                           ['semester_15', '15. Fachsemester'], ['semester_16', '16. Fachsemester'],
                                           ['semester_17', '17. Fachsemester'], ['semester_18', '18. Fachsemester'],
                                           ['semester_19', '19. Fachsemester'], ['semester_20', '20. Fachsemester']],
                                    blank=True,
                                  label='In welchem Fachsemester sind Sie eingeschrieben?')
    math_grade = models.FloatField(label='Was war Ihre letzte Mathenote?')
    abi_grade = models.FloatField(label='Mit welcher Note haben Sie Ihr Abitur abgeschlossen?')
    risk = models.IntegerField(
        choices=list(range(11)),
        widget=widgets.RadioSelectHorizontal,
        label='''
        Wie nehmen Sie sich selbst wahr? 
        Sind Sie generell ein Mensch, der voll und ganz bereit ist, Risiken einzugehen, oder versuchen Sie eher, Risiken zu vermeiden?

        Bitte kreuzen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: "nicht bereit, Risiken einzugehen" und der 
        Wert 10 bedeutet: "voll und ganz bereit, Risiken einzugehen".''')



#  def form_fields(player):
#     if player.truth_telling_decision == 'yes':
#        return ['explanation_tt_yes']  # display explanation_tt_yes if truth_telling_decision has answer 'yes'
#   else:
#      return ['explanation_tt_no']
# return ['truth_telling_decision']  # display q1 by default
