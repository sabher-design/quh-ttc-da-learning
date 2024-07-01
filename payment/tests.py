from otree.api import expect, Submission
from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    def play_round(self):
        if self.participant.label is None:
            yield pages.HrootID, dict(hroot_id="test-id")
        expect(str(self.participant.payoff_plus_participation_fee()), "in", self.html)
        yield Submission(pages.Payoff, check_html=False)
