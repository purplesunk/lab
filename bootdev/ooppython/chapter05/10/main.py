class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type != other.sword_type:
            raise Exception("can not craft")
        if self.sword_type == "iron":
            return Sword("steel")
        elif self.sword_type == "bronze":
            return Sword("iron")
        else:
            raise Exception("can not craft")
