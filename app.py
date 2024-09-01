from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Witch',
    'location': 'Bengaluru, Laal Pahadi, India ',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'White Devil',
    'location': 'Delhi, kali Minar, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Sarkata',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Munjya',
    'location': 'Jamna par, Delhi, India',
    'salary': '$150,000'
}]


@app.route("/")
def hello_Nitian():
    return render_template('home.html', jobs=JOBS, company_name='Abnormal Recruiters')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
