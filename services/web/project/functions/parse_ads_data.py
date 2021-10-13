def parse_ads_data(file):

    #TODO: implement less specific case for general report cases!!!
    campaigns = file["Campaign"]
    budget = file["Budget"]

    real_usage = {}
    for i in range(len(budget)):
        real_usage[campaigns[i]] = float(100 * budget[i])
        #100 is multiplier because we want to work with integers
        #or in this case whole number of Cents

    return real_usage