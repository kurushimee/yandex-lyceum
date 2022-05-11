friends_lists = {}


def add_friends(name_of_person, list_of_friends):
    friends_lists[name_of_person] = (
        friends_lists.get(name_of_person, []) + list_of_friends
    )


def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in friends_lists[name_of_person1]:
        return True
    return False


def print_friends(name_of_person):
    friends_lists[name_of_person].sort()
    print(" ".join(friends_lists[name_of_person]))
