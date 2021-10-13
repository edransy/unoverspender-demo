# pure functions

def check_overspending(new_limit, current_limit, threshold):
    if new_limit >= threshold*current_limit:
        return True
    else:
        return False
