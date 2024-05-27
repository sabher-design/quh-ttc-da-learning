# coding=utf-8
from otree.api import *
import csv
import os
from itertools import chain

from SHttc_test2.user_settings import *

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
        print(f"Starting session for SHttc_test2: {self.__class__.__name__}")

        # Reset other participant.vars as needed
        # CREATE INDICES FOR MOST IMPORTANT VARS ================================================ #
       # indices = [j for j in range(1, Constants.nr_courses + 1)]
        players = self.get_players()
        num_players = len(players)

        # Debugging: Print number of players
        print(f"Number of players: {num_players}")


        group_matrix = [players[i:i + 4] for i in range(0, num_players, 4)]
        self.set_group_matrix(group_matrix)

        for group in self.get_groups():
            players_in_group = group.get_players()
            for p in players_in_group:
                p.participant.vars['role'] = p.role()
                # Other participant vars as needed

                # Store group ID in participant vars
                p.participant.vars['group_id'] = group.id

                print(f"Player {p.id_in_group}'s role: {p.participant.vars['role']}")
                print(f"Player {p.id_in_group} is in group {group.id}")

        indices = [j for j in range(1, Constants.nr_courses + 1)]

        #self.group_randomly() dont do that, this leads to weird color assigment

       # for p in players:
        #    p.participant.vars['role'] = p.role()  # This stores the result of p.role() in participant.vars
        #print(f"Player {p.id_in_group}'s role: {p.participant.vars['role']}")


        # CREATE FORM TEMPLATES FOR DECISION.HTML  ============================================== #
        form_fields = ['pref_c' + str(j) for j in indices]

        for p in players:
            p.participant.vars['form_fields_plus_index'] = list(zip(indices, form_fields))
            p.participant.vars['player_prefs'] = [None for n in indices]
            p.participant.vars['successful'] = [False for n in indices]
            #p.participant.vars['role'] = p.role()

        # ALLOCATE THE CORRECT VALUATIONS VECTOR TO PLAYER (DEPENDING ON TYPE) ================== #
        # AND GET OTHER PLAYERS' VALUATIONS AND TYPES TO DISPLAY IF DESIRED                       #
        type_names = ['Type ' + str(i) for i in range(1, Constants.nr_types + 1)]

        for p in players:
            p.participant.vars['valuations_others'] = []
            p.participant.vars['other_types_names'] = []
            for t in type_names:
                if p.role() == t:
                    p.participant.vars['valuations'] = Constants.valuations[type_names.index(t)]
                else:
                    if Constants.nr_types > 1:
                        p.participant.vars['valuations_others'].append(Constants.valuations[type_names.index(t)])
                        p.participant.vars['other_types_names'] = [t for t in type_names if p.role() != t]
        print(f"others' vals: {p.participant.vars['valuations_others']}")
        print(f"own vals: {p.participant.vars['valuations']}")
        # ALLOCATE THE CORRECT PRIORITIES VECTOR TO PLAYER (DEPENDING ON ID) ==================== #
        for p in players:
            p.participant.vars['priorities'] = []
            for i in Constants.priorities:
                p.participant.vars['priorities'].extend([(i.index(j) + 1) for j in i if j == p.id_in_group])

    # METHOD: =================================================================================== #
    # PREPARE ADMIN REPORT ====================================================================== #
    # =========================================================================================== #

    def vars_for_admin_report(self):
        indices = [j for j in range(1, Constants.nr_courses + 1)]
        players = self.get_players()
        table_nr_tds_decisions = Constants.nr_courses + 2
        table_nr_tds_priorities = Constants.nr_courses + 1
        player_prefs = [p.participant.vars['player_prefs'] for p in players]
        last_player_per_group = [i[-1] for i in self.get_group_matrix()]
        player_valuations = [p.participant.vars['valuations'] for p in players]
        player_priorities = [p.participant.vars['priorities'] for p in players]
        types = ['Type ' + str(i) for i in range(1, Constants.nr_types + 1)]
        valuations = [i for i in Constants.valuations]
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

    def get_allocation(self):
        players = self.get_players()
        indices = [j for j in range(1, Constants.nr_courses + 1)]

            # Collect prepared_list from all players and order them in one single list in descending order of prefs.
        all_prefs = []
        for p in players:
            for n in indices:
                if not isinstance(p.participant.vars['player_prefs'][n - 1], list):
                    p.participant.vars['player_prefs'][n - 1] = []
                p.participant.vars['player_prefs'][n - 1].append(p.id_in_group)
                p.participant.vars['player_prefs'][n - 1].append(n)
                all_prefs.extend(p.participant.vars['player_prefs'])

        all_prefs = list(chain.from_iterable(all_prefs))
        all_prefs.sort(key=lambda sublist: sublist[0], reverse=False)

        cycles_found = []
        size_counter = 1
        pass_nr = 1
        players_in_round = players

        player_resource = [[] for p in players]
        seats_left = Constants.capacities.copy()
        priorities_left = Constants.priorities.copy()

        while size_counter <= len(players_in_round) - 1:

            players_in_round = []
            for i in all_prefs:
                player_list = [p for p in players if p.id_in_group == i[1]]
                if player_list:
                    players_in_round.append(player_list)
            players_in_round = set(list(chain.from_iterable(players_in_round)))

            top_prefs_in_round = []
            for p in players_in_round:
                min_pref = min((i[0] for i in all_prefs if i[1] == p.id_in_group), default=None)
                if min_pref is not None:
                    top_prefs_in_round.append(
                        [[b[1], b[2]] for b in all_prefs if b[0] == min_pref and b[1] == p.id_in_group])
            top_prefs_in_round = list(chain.from_iterable(top_prefs_in_round))

            top_priorities_in_round = []
            for i, j in zip(indices, priorities_left):
                if seats_left[i - 1] > 0 and j:
                    top_priorities_in_round.append([i, j[0]])

            cycles_check = []
            for i in top_prefs_in_round:
                j = next((j for j in top_priorities_in_round if j[0] == i[1]), None)
                if j:
                    cycles_check.append([i, j])

            if size_counter > 1:
                m = 0
                while m < size_counter - 1:
                    for i in cycles_check:
                        j = next((j for j in top_prefs_in_round if j[0] == i[-1][1]), None)
                        k = next((k for k in top_priorities_in_round if k[0] == j[-1]), None) if j else None
                        if j and k:
                            cycles_check[cycles_check.index(i)].append(j)
                            cycles_check[cycles_check.index(i)].append(k)
                    m += 1

            cycles_found = [i for i in cycles_check if i[0][0] == i[-1][-1]]

            if cycles_found:
                remove_seats = [j[0][1] for j in cycles_found]
                for i in remove_seats:
                    seats_left[i - 1] -= 1

                for i in cycles_found:
                    for j in priorities_left:
                        if i[0][0] in j:
                            j.remove(i[0][0])
                    all_prefs = [k for k in all_prefs if not i[0][0] == k[1]]

                    if seats_left[(i[0][1] - 1)] < 1:
                        all_prefs = [k for k in all_prefs if i[0][1] != k[2]]

                    for b in top_prefs_in_round:
                        if i[0] == b:
                            player_resource[b[0] - 1] = b

                size_counter = 1
            else:
                size_counter += 1

            if not all_prefs:
                break

            pass_nr += 1

        for p in players:
            p.participant.vars['player_resource'] = player_resource[p.id_in_group - 1]
            print(f"Player {p.id_in_group} is matched with resource: {p.participant.vars['player_resource']}")

    # METHOD: =================================================================================== #
    # SET PAYOFFS =============================================================================== #
    # =========================================================================================== #

    def set_payoffs(self):
        players = self.get_players()

        for p in players:
            print(f"Player {p.id_in_group} is matched with resource: {p.participant.vars['player_resource']}")
            # Assuming the second element in player_resource is the course number
            matched_course = p.participant.vars['player_resource'][1]
            p.payoff = p.participant.vars['valuations'][matched_course - 1]
            p.participant.vars['successful'][matched_course - 1] = True
            print(
                f"  Matched with Course {matched_course}. Payoff: {p.payoff}. successful: {p.participant.vars['successful'][matched_course - 1]}")


class Player(BasePlayer):

    # METHOD: =================================================================================== #
    # DEFINE ROLES ACCORDING TO INPUT IN USER_SETTINGS.PY ======================================= #
    # =========================================================================================== #
    def role(self):
        # DESIGN TYPES ========================================================================== #
        all_ids = list(range(1, Constants.players_per_group + 1))
        nr_ids_per_type = int(Constants.players_per_group / Constants.nr_types)
        type_for_id = list(chain.from_iterable([[i] * nr_ids_per_type for i in range(1, Constants.nr_types + 1)]))
        type_matrix = [[i, j] for i, j in zip(all_ids, type_for_id)]

        for i in range(0, len(type_matrix)):
            if self.id_in_group == type_matrix[i][0]:
                return 'Type ' + str(type_matrix[i][1])

    # DYNAMICALLY CREATE N FORM TEMPLATES FOR PREFS ============================================= #
    for j in range(1, Constants.nr_courses + 1):
        locals()['pref_c' + str(j)] = models.IntegerField()
    del j
