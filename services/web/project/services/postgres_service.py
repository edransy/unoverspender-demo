import pandas as pd
from sqlalchemy import create_engine
from project.functions.check_fileformat import check_fileformat


def update_limit(db, Campaign, campaign, new_limit):
    db.session.query(Campaign).filter_by(campaign=campaign).update({'budget': new_limit})
    db.session.commit()
    return

def add_campaign(db, Campaign, campaign, new_limit):
    db.session.add(Campaign(campaign, new_limit))
    db.session.commit()
    return

def delete_campaign(db, Campaign, campaign):
    db.session.query(Campaign).filter_by(campaign=campaign).delete()
    db.session.commit()
    return

def get_all(Campaign):
    users = Campaign.query.all()
    users = {i.campaign: i.budget for i in users}

    return users