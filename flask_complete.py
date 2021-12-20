from flask import Flask, request, render_template
import pickle
import numpy as np
import csv
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

#flask app
app = Flask(__name__)

@app.route('/')
def default():
    return render_template('main.html')

@app.route('/currentstatistics')
def currentstatistics():
    return render_template('current_statistics.html')

@app.route('/cropregistration')
def cropregistration():
    return render_template('crop_registration.html')

@app.route('/cropyield')
def cropyield():
    return render_template('crop_estimation.html')

def reg_dist(name, crop_name, dist, area, pro_predictions):
    if dist == 63:
        with open('adilabad_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 62:
        with open('karimnagar_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 55:
        with open('hyderabad_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 61:
        with open('khammam_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 58:
        with open('mahabubnagar_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 57:
        with open('medak_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 59:
        with open('nalgonda_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 56:
        with open('nizamabad_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    elif dist == 60:
        with open('warangal_user_crop_entry.csv', 'a', newline='') as crop_entry:
            write_data = csv.writer(crop_entry, delimiter=',')
            write_data.writerow([name, 2022, crop_name, int(area), int(pro_predictions)])

    crop_entry.close()

@app.route('/estimation', methods=["POST","GET"])
def estimation():
    dist = int(request.form.get("dist"))
    n = int(request.form.get("crop"))
    area = int(request.form.get("area"))
    crop=''
    if n == 1:
        crop="paddy"
    elif n == 2:
        crop="sorghum"
    elif n == 3:
        crop="arhar"
    elif n == 4:
        crop="groundnut"
    elif n == 5:
        crop="sesamum"

    production=0
    price=0

    if crop == 'paddy':
        pro = pickle.load(open("paddy_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        pri = pickle.load(open("paddy_pri_model.pkl", "rb"))
        price = pri.predict([[2022, int(area / 2.47), int(production)]])

    elif crop == 'sorghum':
        pro = pickle.load(open("sorghum_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        pri = pickle.load(open("sorghum_pri_model.pkl", "rb"))
        price = pri.predict([[2022, int(area / 2.47), int(production)]])

    elif crop == 'arhar':
        pro = pickle.load(open("arhar_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        pri = pickle.load(open("arhar_pri_model.pkl", "rb"))
        price = pri.predict([[2022, int(area / 2.47), int(production)]])

    elif crop == 'groundnut':
        pro = pickle.load(open("groundnut_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        pri = pickle.load(open("groundnut_pri_model.pkl", "rb"))
        price = pri.predict([[2022, int(area / 2.47), int(production)]])

    elif crop == 'sesamum':
        pro = pickle.load(open("sesamum_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        pri = pickle.load(open("sesamum_pri_model.pkl", "rb"))
        price = pri.predict([[2022, int(area / 2.47), int(production)]])

    return render_template("result_page.html", prediction_text = "Yield = {} Quintals\nPrice = {} Rs per Quintal".format(int(production), int(price)))

@app.route("/registration", methods=["POST", "GET"])
def registration():
    name = request.form.get("user")
    dist = int(request.form.get("dist"))
    n = int(request.form.get("crop"))
    area = int(request.form.get("area"))

    crop = ''
    if n == 1:
        crop = "paddy"
    elif n == 2:
        crop = "sorghum"
    elif n == 3:
        crop = "arhar"
    elif n == 4:
        crop = "groundnut"
    elif n == 5:
        crop = "sesamum"

    if crop == 'paddy':
        pro = pickle.load(open("paddy_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        reg_dist(name, crop, dist, area, production)

    elif crop == 'sorghum':
        pro = pickle.load(open("sorghum_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        reg_dist(name, crop, dist, area, production)

    elif crop == 'arhar':
        pro = pickle.load(open("arhar_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        reg_dist(name, crop, dist, area, production)

    elif crop == 'groundnut':
        pro = pickle.load(open("groundnut_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        reg_dist(name, crop, dist, area, production)

    elif crop == 'sesamum':
        pro = pickle.load(open("sesamum_pro_model.pkl", "rb"))
        production = pro.predict([[dist, 2022, int(area / 2.47)]])
        reg_dist(name, crop, dist, area, production)

    return render_template("result_page.html", prediction_text="Registration Successful!!!")

def current_total(crop):

    x=0

    crop_entry = pd.read_csv('adilabad_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('karimnagar_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('hyderabad_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('warangal_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('nalgonda_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('medak_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('nizamabad_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('khammam_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    crop_entry = pd.read_csv('mahabubnagar_user_crop_entry.csv')
    index = crop_entry.index
    for i in range(0, len(index)):
        if crop_entry.iloc[i]['Crop'] == crop:
            x+= crop_entry.iloc[i]['Production']

    return x

@app.route("/statistics", methods=["POST", "GET"])
def statistics():
    #dist = int(request.form.get("dist"))
    n = int(request.form.get("crop"))

    crop = ''
    if n == 1:
        crop = "paddy"
    elif n == 2:
        crop = "sorghum"
    elif n == 3:
        crop = "arhar"
    elif n == 4:
        crop = "groundnut"
    elif n == 5:
        crop = "sesamum"

    threshold=0
    total = current_total(crop)

    if crop=='paddy':
        demand = pickle.load(open('paddy_district_model.pkl', 'rb'))
        threshold = demand.predict([[2022]])

    elif crop=='sorghum':
        demand = pickle.load(open('sorghum_district_model.pkl', 'rb'))
        threshold = demand.predict([[2022]])

    elif crop=='arhar':
        demand = pickle.load(open('arhar_district_model.pkl', 'rb'))
        threshold = demand.predict([[2022]])

    elif crop=='groundnut':
        demand = pickle.load(open('groundnut_district_model.pkl', 'rb'))
        threshold = demand.predict([[2022]])

    elif crop=='sesamum':
        demand = pickle.load(open('sesamum_district_model.pkl', 'rb'))
        threshold = demand.predict([[2022]])

    x = '2022'
    y = total

    fig = Figure()
    ax = fig.subplots()
    ax.bar(x, y, color='g')
    ax.axhline(threshold, xmin=0, xmax=1, color='r')
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

@app.route('/recommendfile', methods=["POST", "GET"])
def recommendfile():
    return render_template('recommend.html')

@app.route('/fertilizersfile', methods=["POST", "GET"])
def fertilizersfile():
    return render_template('fertilizers.html')

@app.route("/recommend", methods=["POST", "GET"])
def recommend():
    model = pickle.load(open("model.pkl", "rb"))
    n = int(request.form.get('n'))
    p = int(request.form.get('p'))
    k = int(request.form.get('k'))
    temp = int(request.form.get('temp'))
    ph = float(request.form.get('ph'))
    rain = int(request.form.get('rain'))
    humidity = int(request.form.get('h'))
    # if state == 1:
    #     temp=
    #     ph=!
    #     rain=
    #     humidity=
    # ph = int(request.form.get('ph'))
    # rain = int(request.form.get('rain'))
    # humidity = int(request.form.get('h'))
    # if weather_fetch(city) is not None:
    #     temperature, humidity = weather_fetch(city)
    # print(n)
    prediction = model.predict([[n, p, k, temp, humidity, ph, rain]])
    # prediction = model.predict([[90, 42, 43, 21, 82, 6.5, 203]])
    return render_template("result_page.html", prediction_text="crop Recommended is {}".format(prediction[0]))

@app.route("/fertilizers", methods=["POST", "GET"])
def fertilizers():
    fertilizer = pickle.load(open("fertilizer.pkl", "rb"))
    temp = int(request.form.get('temp'))
    humidity = int(request.form.get('h'))
    mc = int(request.form.get('mc'))
    crop = int(request.form.get('crop'))
    n = int(request.form.get('n'))
    p = int(request.form.get('p'))
    k = int(request.form.get('k'))
    # state = int(request.form.get('state'))
    # n = int(request.form.get('state'))
    # p = int(request.form.get('p'))
    # k = int(request.form.get('k'))
    #  district gives us temp and humidity
    # prediction = fertilizer.predict([[26, 58, 38, 1, 37, 0, 0]])
    # prediction = model.predict([[n, p, k, temp, humidity, ph, rain]])
    # return render_template("result.html", prediction_text="crop Recommend is {}".format(prediction))

    prediction = fertilizer.predict([[temp, humidity, mc, crop, n, k, p]])
    return render_template("result_page.html", prediction_text="Recommended Fertilizer  is {}".format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)