can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & 0b1000


def get_review_bits(user_permissions):
    return user_permissions & 0b0100


def get_delete_bits(user_permissions):
    return user_permissions & 0b0010


def get_edit_bits(user_permissions):
    return user_permissions & 0b0001
