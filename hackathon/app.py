from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Create Flask app
app = Flask(__name__)

# Load the dataset
df = pd.read_csv(r"C:\Users\SIC\Documents\Python - SIC\sic_033\hackathon\india_births_2011_2021.csv")

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Normal Delivery vs C-section Deliveries
@app.route('/normal_vs_csection')
def normal_vs_csection():
    delivery_counts = df['Type of Delivery'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(delivery_counts.index, delivery_counts.values)
    ax.set_xlabel('Delivery Type')
    ax.set_ylabel('Count')
    ax.set_title('Normal vs C-section Deliveries')
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url, title="Normal vs C-section Deliveries")

# State-wise C-Section Deliveries
@app.route('/state_csection')
def state_csection():
    state_csection = df[df['Type of Delivery'] == 'C-Section'].groupby('State of Birth').size()
    fig, ax = plt.subplots()
    state_csection.plot(kind='bar', ax=ax)
    ax.set_xlabel('State')
    ax.set_ylabel('C-section Deliveries')
    ax.set_title('State-wise C-section Deliveries')
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url, title="State-wise C-section Deliveries")

# Hospitals with more C-Section Deliveries
@app.route('/hospital_csection')
def hospital_csection():
    hospital_csection = df[df['Type of Delivery'] == 'C-Section'].groupby('Hospital Name').size()
    hospital_csection = hospital_csection.sort_values(ascending=False).head(10)  # Top 10 hospitals
    fig, ax = plt.subplots()
    hospital_csection.plot(kind='bar', ax=ax)
    ax.set_xlabel('Hospital')
    ax.set_ylabel('C-section Deliveries')
    ax.set_title('Top 10 Hospitals with More C-Section Deliveries')
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url, title="Top 10 Hospitals with More C-Section Deliveries")

# C-Section Deliveries and Seasons Relationship
@app.route('/season_csection')
def season_csection():
    df['Season'] = df['Delivery Date'].apply(lambda x: 'Summer' if 'June' in x or 'July' in x or 'August' in x else 'Winter')  # Simplified season logic
    season_csection = df[df['Type of Delivery'] == 'C-Section'].groupby('Season').size()
    fig, ax = plt.subplots()
    season_csection.plot(kind='bar', ax=ax)
    ax.set_xlabel('Season')
    ax.set_ylabel('C-section Deliveries')
    ax.set_title('C-Section Deliveries and Seasons')
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url, title="C-Section Deliveries and Seasons")

# Percentage of Second Child Birth with Normal Delivery if First Delivery was C-Section
@app.route('/second_child_normal_delivery')
def second_child_normal_delivery():
    second_child = df[df['Child Number'] == 2]
    second_child_normal = second_child[second_child['Type of Delivery'] == 'Normal']
    percentage = (len(second_child_normal) / len(second_child)) * 100
    return render_template('percentage.html', percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
