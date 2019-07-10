from pypot.creatures import AbstractPoppyCreature


class PoppyBuggy(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        for m in robot.motors:
            m.goto_behavior = 'dummy'
