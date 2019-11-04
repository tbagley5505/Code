def is_even(bunnies):
    if isinstance(bunnies,int):
        if bunnies % 2 == 0:
            return True
        else:
            return False
    else:
        print("number please")
        return None

is_even(8)
is_even(5)
is_even("cow")        