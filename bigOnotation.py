
def find_name(name, phone_book):
    a = 2
    b = 10**a
    c = 3 + 4
    for person in phone_book:
        if name == person:
            return True

name = "Kim"
phone_book = ["oliver", "BobbyG", "tim", "Dan", "oliver", "kim"]

O(n)

def find_name(austin_phone_book, philly_phone_book):
    for austinite in austin_phone_book:
        print(austinite)

        c = 3 + 4

        for austinite in austin_phone_book:
            for philadelphia in philly_phone_book:
                if austinite == philadelphia:
                    return True
# Rule Book-
#  Rule 1: Always worst Case
#  Rule 2: Remove Constants
#  Rule 3: Different inputs should have different variables. O(a+b). A and B arrays nested would be O(a*b)
#     + for steps in order
#     * for nested steps
#  Rule 4: Drop Non-dominant terms