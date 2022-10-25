from flask import Flask, render_template, request, url_for, redirect, render_template
import json
import requests
import numpy as np
import pandas as pd
from predict import get_prediction, load_data

app = Flask(__name__)


# @app.route('/')
# def dashboard():
#     r = requests.get('https://api.punkapi.com/v2/beers/random')
#     beerjson = r.json()
#     beer = {
#         'name': beerjson[0]['name'],
#         'abv': beerjson[0]['abv'],
#         'desc': beerjson[0]['description'],
#         'foodpair': beerjson[0]['food_pairing'][0]
#     }
#     # print(beer)
#     return render_template('index.html', beer=beer)

DISEASE = 'Jantung'
@app.route('/', methods=['GET', 'POST'])
def dashboard():
    title = 'dashboard'
    global DISEASE
    DISEASE = 'Jantung'
    return render_template('index.html', title=title, disease=DISEASE)

@app.route('/dash2', methods=['GET', 'POST'])
def dashboard2():
    title = 'dashboard2'
    global DISEASE
    DISEASE = 'Diabetes'
    return render_template('index_db.html', title=title, disease=DISEASE)

@app.route('/dash3', methods=['GET', 'POST'])
def dashboard3():
    title = 'dashboard3'
    global DISEASE
    DISEASE = 'Kanker Paru-Paru'
    return render_template('index_lc.html', title=title, disease=DISEASE)

@app.route('/dash4', methods=['GET', 'POST'])
def dashboard4():
    title = 'dashboard4'
    global DISEASE
    DISEASE = 'Stroke'
    return render_template('index_st.html', title=title, disease=DISEASE)

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    title = 'forum'
    global DISEASE
    return render_template('forum.html', title=title, disease=DISEASE)

@app.route('/info_rs', methods=['GET', 'POST'])
def info_rs():
    title = 'info_rs'
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('info_rs.html', title=title)


@app.route('/bpjs_pick_and_care', methods=['GET', 'POST'])
def bpjs_pick_and_care():
    title = 'bpjs_pick_and_care'
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('404.html', title=title)


@app.route('/promo_and_reward', methods=['GET', 'POST'])
def promo_and_reward():
    title = 'promo_and_reward'
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('promo_and_reward.html', title=title)


@app.route('/voucher_belanja', methods=['GET', 'POST'])
def voucher_belanja():
    title = 'voucher'
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('voucher_belanja.html', title=title)


@app.route('/challenges', methods=['GET', 'POST'])
def challanges():
    title = 'challanges'
    global DISEASE
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('challenges.html',title=title, disease=DISEASE)


@app.route('/challenges/sepeda5K', methods=['GET', 'POST'])
def sepeda5K():
    title = 'challanges'
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('sepeda5K.html',title=title)

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            BMI = int(request.form.get('WEIGHT'))*10000/(int(request.form.get('HEIGHT'))*int(request.form.get('HEIGHT')))
            formlist = ['GENDER','AGE_GROUP','BMI','HIGHCHOL','HIGHBP','PHYSACTIVITY','ALCOHOL','FRUITS','VEGGIES','SMOKING','YELLOW_FINGERS','COUGHING','SHORT_BREATH']
            float_features = [request.form.get(x) for x in formlist]
            float_features[2] = int(BMI*10)/10
            # float_features = [float(x) for x in request.form.values()]
            df = load_data(float_features)
            models = ['model_heart','model_diabetes','model_lung','model_stroke']
            prediction = [get_prediction(f'models/{x}.sav',df) for x in models]
            # prediction = float_features
            if BMI<18.5:
                kelas = "Underweight"
            elif BMI< 25:
                kelas = "Normal"
            elif BMI <30:
                kelas = "Overweight"
            else:
                kelas = "Obesitas"
            
            hasil = {
                'name': int(BMI*10)/10,
                'kelas':kelas
            }
            prediction_text = {
                'heart': ["Rendah" if prediction[0]==0 else "Tinggi"][0],
                'diabetes':["Tinggi" if prediction[1] == 2 else "Rendah"][0],
                'lung': ["Rendah" if prediction[2]==0 else "Tinggi"][0],
                'stroke':["Rendah" if prediction[3]==0 else "Tinggi"][0]
            }
        except:
            hasil = {
            'name': "Kesalahan Pengisian Parameter",
            'kelas': "-"
            }
            prediction_text = {
                'heart': "Belum Dijalankan",
                'diabetes':"Belum Dijalankan",
                'lung': "Belum Dijalankan",
                'stroke':"Belum Dijalankan"
            }
        return render_template("prediksi.html",hasil=hasil,title='predict', prediction = prediction_text)
    else:
        hasil = {
        'name': "Belum Dijalankan",
        'kelas': "-"
        }
        prediction_text = {
            'heart': "Belum Dijalankan",
            'diabetes':"Belum Dijalankan",
            'lung': "Belum Dijalankan",
            'stroke':"Belum Dijalankan"
        }
        return render_template("prediksi.html",hasil=hasil,title='predict', prediction = prediction_text)
