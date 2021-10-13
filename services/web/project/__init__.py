import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from flask_sqlalchemy import SQLAlchemy
from project.services.postgres_service import add_campaign, get_all, update_limit
from project.functions.statistical_functions import calcualte_mean
from project.functions.check_overspending import check_overspending
from project.services.google_service import get_new_data


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Campaign(db.Model):
    __tablename__ = "campaigns"

    campaign = db.Column(db.String(128), primary_key=True)
    budget = db.Column(db.Integer())

    def __init__(self, campaign, budget):
        self.campaign = campaign
        self.budget = budget



@app.route("/")
def index():
    status = get_all(Campaign)
    for key, value in status.items():
        print(f'{key}: {value/100}$')

    return render_template('index.html')



@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]        
        new_data, csv = get_new_data(file)
        csv.to_csv(os.path.join(app.config["MEDIA_FOLDER"], 'temp.csv'), index=False)

        old_data = get_all(Campaign)

        mean = calcualte_mean(old_data.values())
                
        risky_limits_count = 0

        for key in new_data.keys():
            if(key not in old_data):
                if(len(old_data) != 0):
                    if(check_overspending(new_data[key], mean, 4)):
                        risky_limits_count += 1
                else:
                    add_campaign(db, Campaign, key, new_data[key])
            elif(check_overspending(new_data[key], old_data[key], 4)):
                risky_limits_count += 1
            else:
                update_limit(db, Campaign, key, new_data[key])


        if(risky_limits_count>0):
            return redirect(url_for('warning'))

        else:
            return redirect(url_for('success'))


    return redirect(url_for('index'))



@app.route("/warning", methods=["GET", "POST"])
def warning():

    new_data, _ = get_new_data(os.path.join(app.config["MEDIA_FOLDER"], 'temp.csv'))
    old_data = get_all(Campaign)

    mean = calcualte_mean(old_data.values())
    risky_budgets = {}

    for key in new_data.keys():
        if key not in old_data.keys():
            if(check_overspending(new_data[key], mean, 4)):
                risky_budgets[key] = new_data[key]
        elif(check_overspending(new_data[key], old_data[key], 4)):
            risky_budgets[key] = new_data[key]
    
    if request.method == "POST":
        for key in risky_budgets.keys():
            update_limit(db, Campaign, key, risky_budgets[key])

        #TODO: email client send warning mails!!
        
        return redirect(url_for('imported_with_warnings'))
    

    return render_template('warning.html', result=risky_budgets)



@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/imported_with_warnings")
def imported_with_warnings():
    return render_template('imported_with_warnings.html')