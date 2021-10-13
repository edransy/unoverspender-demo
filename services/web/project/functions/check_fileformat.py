def check_fileformat(number):
    
    in_cents = number * 100
    is_int = in_cents.is_integer()

    if(is_int):
        return True

    else:
        return False