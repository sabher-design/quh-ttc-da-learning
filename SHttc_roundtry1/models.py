# coding=utf-8
from otree.api import *
import csv
import os
c = cu
from itertools import chain

from SHttc_roundtry1.user_settings import *

author = 'Benjamin Pichl'

doc = """
This app is intended to model a school choice problem. It implements the Gale's Top Trading Cycles for School Choice
Mechanism within the oTree framework. If you have any questions, comments, feature requests, or bug reports, 
please write me an eMail: benjamin.pichl@outlook.com.

If you intend to use this code for your own research purposes, please cite:

t.b.d.

"""


class Subsession(BaseSubsession):

    # METHOD: =================================================================================== #
    # THINGS TO DO BEFORE THE SESSION STARTS  =================================================== #
    # =========================================================================================== #
    def creating_session(self):
        #if self.round_number == 1:
        #self.group_randomly()
        ''' players = self.get_players()
            print(f"players: {players}")
            for p in players:

        else:
            self.group_like_round(1)'''

        current_round = self.round_number
        print(f"current_round: {current_round}")

        # CREATE INDICES FOR MOST IMPORTANT VARS ================================================ #
        indices = [j for j in range(1, Constants.nr_courses + 1)] # creates a list of indices to create form fields dynamically for each course in decision-making form
        print(f"indices: {indices}")

        players = self.get_players()
        print(f"players: {players}")

        for p in self.get_players():
            # Reset or initialize round-specific variables
            p.participant.vars['player_prefs'] = []
            p.participant.vars['successful'] = []
            # If tracking data across rounds, ensure you initialize the structure once
            if 'round_specific_data' not in p.participant.vars:
                p.participant.vars['round_specific_data'] = {}

        # Directly test the role assignment
        '''for p in self.get_players():
            player_role = p.role()  # This should invoke the role method and return 'Type X'
            print(f"Direct role test for player {p.id_in_group}: {player_role}")

            # Just for debugging: Directly accessing participant.vars to confirm role assignment
            print(
                f"Stored role in participant.vars for player {p.id_in_group}: {p.participant.vars.get('player_type', 'Role not assigned')}")'''

        # CREATE FORM TEMPLATES FOR DECISION.HTML  ============================================== #
        form_fields = ['pref_c' + str(j) for j in indices] # generates form field names dynamically based on the number of courses
        #print(f"form_fields: {form_fields}")

        for p in players:
            p.participant.vars['form_fields_plus_index'] = list(zip(indices, form_fields)) # list of tuples to render form fields on decision page
            p.participant.vars['player_prefs'] = [None for n in indices] # storage of players' course preferences
            p.participant.vars['successful'] = [False for n in indices] # tracks whether player was successfully matched to a course

        # ALLOCATE THE CORRECT VALUATIONS VECTOR TO PLAYER (DEPENDING ON TYPE) ================== #
        # AND GET OTHER PLAYERS' VALUATIONS AND TYPES TO DISPLAY IF DESIRED                       #
        type_names = ['Type ' + str(i) for i in range(1, Constants.nr_types + 1)] # generates a list of type names
        #print(f"type_names: {type_names}")

        ## in the following: assignment of valuations based on type --> needs to be adjusted, works with valuations.
        ## initialization of lists to store valuations of other types and names of other types
        print(f"Constants.valuations_rounds[current_round]: {Constants.valuations_rounds[current_round]}")
        print(self.get_players()[0].participant.vars.get('player_type', 'No role assigned yet'))

        for p in players:
            print(f"Attempting to access role for player {p.id_in_group}")
            print(f"role: {p.role()}")
            p.participant.vars['valuations_others'] = []
            p.participant.vars['other_types_names'] = []

            for t in type_names:
                print(f"Checking role for {p.id_in_group}: {p.role()} against {t}")
                if p.role() == t:
                    print(f"Role match for player {p.id_in_group}: {p.role()} == {t}")
                    p.participant.vars['valuations'] = Constants.valuations_rounds[current_round][t]
                    print(f"check1 : {Constants.valuations_rounds[current_round][t]}")
                else:
                    print(f"No role match for player {p.id_in_group}: {p.role()} != {t}")
                    if Constants.nr_types > 1:
                        p.participant.vars['valuations_others'].append(Constants.valuations_rounds[current_round][t])
                        #print(f"check2: {p.participant.vars['valuations_others'].(Constants.valuations_rounds[current_round][t])}")
                        p.participant.vars['other_types_names'] = [t for t in type_names if p.role() != t]

        #print(f"players' valuations: {p.participant.vars}")

        # ALLOCATE THE CORRECT PRIORITIES VECTOR TO PLAYER (DEPENDING ON ID) ==================== #

        ## also adjusted, because works with priorities
        print(f"Constants.priorities_rounds[current_round]: {Constants.priorities_rounds[current_round]}")
        for p in players:
            print(f"Setting priorities for Player {p.id_in_group}")
            p.participant.vars['priorities'] = []
            for priorities_list in Constants.priorities_rounds[current_round].values():
                print(f"Current priority list: {priorities_list}")
                player_priority = [(priorities_list.index(j) + 1) for j in priorities_list if j == p.id_in_group]
                p.participant.vars['priorities'].extend(player_priority)
                print(f"Priorities for Player {p.id_in_group}: {p.participant.vars['priorities']}")


    # METHOD: =================================================================================== #
    # PREPARE ADMIN REPORT ====================================================================== #
    # =========================================================================================== #
    def vars_for_admin_report(self):
        indices = [j for j in range(1, Constants.nr_courses + 1)]
        players = self.get_players()
        current_round = self.round_number
        table_nr_tds_decisions = Constants.nr_courses + 2
        table_nr_tds_priorities = Constants.nr_courses + 1
        player_prefs = [p.participant.vars['player_prefs'] for p in players]
        last_player_per_group = [i[-1] for i in self.get_group_matrix()]
        player_valuations = [p.participant.vars['valuations']for p in players]
        player_priorities = [p.participant.vars['priorities'] for p in players]
        types = ['Type ' + str(i) for i in range(1, Constants.nr_types + 1)]
        valuations = [i for i in Constants.valuations_rounds[current_round]]
        capacities = [i for i in Constants.capacities]
        decisions = zip(players, player_prefs)
        successful = [p.participant.vars['successful'] for p in players]
        successful_with_id = zip(players, successful)
        valuations_all_types = zip(types, valuations)
        priorities_all_players = zip(players, player_priorities)

        data_all = zip(players, player_valuations, player_prefs, successful)

        return {
            'indices': indices,
            'players': players,
            'current_round': current_round,
            'table_nr_tds_decisions': table_nr_tds_decisions,
            'table_nr_tds_priorities': table_nr_tds_priorities,
            'player_prefs': player_prefs,
            'last_player_per_group': last_player_per_group,
            'player_priorities': player_priorities,
            'capacities': capacities,
            'decisions': decisions,
            'successful': successful,
            'successful_with_id': successful_with_id,
            'valuations_all_types': valuations_all_types,
            'priorities_all_players': priorities_all_players,

            'data_all': data_all
        }


class Group(BaseGroup):

    # METHOD: =================================================================================== #
    # GET ALLOCATION (EXECUTED AFTER ALL PLAYERS SUBMITTED DECISION.HTML ======================== #
    # =========================================================================================== #
    def get_allocation(self):
        current_round = self.subsession.round_number
        # CREATE INDICES FOR MOST IMPORTANT VARS ================================================ #
        players = self.get_players()
        indices = [j for j in range(1, Constants.nr_courses + 1)]

        # COLLECT PREPARED_LIST FROM ALL PLAYERS AND ORDER THEM IN ONE SINGLE LIST IN =========== #
        # DESCENDING ORDER OF PREFS.                                                              #
        for p in players:
            for n in indices:
                p.participant.vars['player_prefs'][current_round][n - 1].append(p.id_in_group)
                p.participant.vars['player_prefs'][current_round][n - 1].append(n)

        all_prefs = [p.participant.vars['player_prefs'][current_round] for p in players]
        all_prefs = list(chain.from_iterable(all_prefs))
        all_prefs.sort(key=lambda sublist: sublist[0], reverse=False)

        # CREATE EMPTY LISTS AND COUNTERS FOR THE ALLOCATION PROCESS ============================ #
        cycles_found = []
        size_counter = 1
        pass_nr = 1
        players_in_round = players
        print(f"players_in_round1: {players_in_round}")

        player_resource = [[] for p in players]
        seats_left = Constants.capacities.copy()
        priorities_left = Constants.priorities_rounds[current_round].copy() # adjusted to new variable but i don't know if it understands that there are several rounds already

        # IMPLEMENTATION OF THE TTC MECHANISM =================================================== #
        while size_counter <= len(players_in_round) - 1:

            # DETERMINE WHICH PLAYERS ARE PLAYING IN THIS ROUND ================================= #
            players_in_round = []
            print(f"players_in_round2: {players_in_round}")

            for i in all_prefs:
                players_in_round.append([p for p in players if p.id_in_group == i[1]])
            players_in_round = set(list(chain.from_iterable(players_in_round)))
            print(f"players_in_round3: {players_in_round}")
            # DETERMINE THE TOP PREFERENCES IN THIS ROUND ======================================= #
            top_prefs_in_round = []
            for p in players_in_round:
                top_prefs_in_round.append([[b[1], b[2]] for b in all_prefs if
                                           b[0] == (min(i[0] for i in all_prefs if i[1] == p.id_in_group)) and b[
                                               1] == p.id_in_group])
            top_prefs_in_round = list(chain.from_iterable(top_prefs_in_round))
            print(f"top_preferences_in_round: {top_prefs_in_round}")
            # DETERMINE THE TOP PRIORITIES IN THIS ROUND ======================================== #
            top_priorities_in_round = []
            for i, j in zip(indices, priorities_left):
                if seats_left[i - 1] > 0:
                    top_priorities_in_round.append([i, j[0]])
                    print(f"top_priorities_in_round: {top_priorities_in_round}")
            # MAKE AN EMPTY LIST THAT CATCHES ALL FOUND CYCLES AND APPEND ALL CYCLES ============ #
            cycles_check = []

            for i in top_prefs_in_round:
                j = next(j for j in top_priorities_in_round if j[0] == i[1])
                cycles_check.append([i, j])
                print(f"cycles: {cycles_check}")
            # IF A CYCLE IS LARGER THAN 1 WE NEED TO APPEND MORE THAN 2 ITEMS TO THE CYCLE ====== #
            if size_counter > 1:
                m = 0
                while m < size_counter - 1:
                    for i in cycles_check:
                        j = next(j for j in top_prefs_in_round if j[0] == i[-1][1])
                        k = next(k for k in top_priorities_in_round if k[0] == j[-1])
                        cycles_check[cycles_check.index(i)].append(j)
                        cycles_check[cycles_check.index(i)].append(k)
                    m += 1

            cycles_found = [i for i in cycles_check if i[0][0] == i[-1][-1]]
            print(f"cycles_found: {cycles_found}")
            # IF A CYCLE WAS FOUND, WE NEED TO DELETE ALL PLAYERS IN THE CYCLE AND REDUCE THE === #
            # CAPACITIES OF RESOURCES IN THE CYCLE BY 1. WE ALSO UPDATE THE PREF_LIST.            #
            if cycles_found:
                remove_seats = [j[0][1] for j in cycles_found]
                for i in remove_seats:
                    seats_left[i - 1] -= 1

                for i in cycles_found:
                    for j in priorities_left:
                        j.remove(i[0][0])
                        print(f"priorities left: {priorities_left}")
                    all_prefs = [k for k in all_prefs if not i[0][0] == k[1]]

                    if seats_left[(i[0][1] - 1)] < 1:
                        all_prefs = [k for k in all_prefs if i[0][1] != k[2]]

                    for b in top_prefs_in_round:
                        if i[0] == b:
                            player_resource[b[0] - 1] = b
                            print(f"player resource?: {player_resource}")
                # UPDATE COUNTERS =============================================================== #
                size_counter = 1
            else:
                size_counter += 1
                print(f"size_counter: {size_counter}")
            if not all_prefs:
                break

            pass_nr += 1
            print(f"pass_nr: {pass_nr}")
        # ASSIGN RESOURCES TO PLAYERS' PARTICIPANT VARS ========================================= #
        for p in players:
            p.participant.vars['player_resource'] = player_resource[p.id_in_group - 1]
            print(f"Player {p.id_in_group} is matched with resource: {p.participant.vars['player_resource']}")

    # METHOD: =================================================================================== #
    # SET PAYOFFS =============================================================================== #
    # =========================================================================================== #

    def set_payoffs(self):
        players = self.get_players()
        current_round = self.subsession.round_number


        for p in players[current_round]:
            print(f"Player {p.id_in_group} is matched with resource: {p.participant.vars['player_resource'][current_round]}")
            # Assuming the second element in player_resource is the course number
            matched_course = p.participant.vars['player_resource'][current_round][1]
            p.payoff = p.participant.vars['valuations'][current_round][matched_course - 1]
            p.participant.vars['successful'][current_round][matched_course - 1] = True
            print(
                f"  Matched with Course {matched_course}. Payoff: {p.payoff}. Successful: {p.participant.vars['successful'][matched_course - 1]}")


class Player(BasePlayer):

    # METHOD: =================================================================================== #
    # DEFINE ROLES ACCORDING TO INPUT IN USER_SETTINGS.PY ======================================= #
    # =========================================================================================== #
    def role(self):
        if 'player_type' not in self.participant.vars:
            # Your existing role assignment logic...
            all_ids = list(range(1, Constants.players_per_group + 1))
            nr_ids_per_type = int(Constants.players_per_group / Constants.nr_types)
            type_for_id = list(chain.from_iterable([[i] * nr_ids_per_type for i in range(1, Constants.nr_types + 1)]))
            type_matrix = [[i, j] for i, j in zip(all_ids, type_for_id)]

            for i in range(0, len(type_matrix)):
                if self.id_in_group == type_matrix[i][0]:
                    assigned_role = 'Type ' + str(type_matrix[i][1])
                    self.participant.vars['player_type'] = assigned_role  # Store the role in participant.vars
                    return assigned_role
        else:
            return self.participant.vars['player_type']

    # DYNAMICALLY CREATE N FORM TEMPLATES FOR PREFS ============================================= #
    for j in range(1, Constants.nr_courses + 1):
        locals()['pref_c' + str(j)] = models.IntegerField()
    del j

