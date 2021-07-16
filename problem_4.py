class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    
    if user in group.get_users():
        return True
    else:
        if len(group.get_groups()) == 0:  # Keep searching
            return False
        else:
            for i in group.get_groups():
                if is_user_in_group(user, i):
                    return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("", child))
# Should return False
print(is_user_in_group("sub_child_user", parent))
# Should return True
print(is_user_in_group(sub_child_user, sub_child))
# Should return True
print(is_user_in_group(sub_child_user, child))
# Should return True
print(is_user_in_group(sub_child_user, parent))
# Should return "True


#Edge Cases
#user not found in the group = parent
print(is_user_in_group('', parent))
# False
#user not found in the group child
print(is_user_in_group('', child))
#False
