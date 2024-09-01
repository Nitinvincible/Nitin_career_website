from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Witch',
    'location': 'Bengaluru, Laal Pahadi, India ',
    'salary': 'Rs. 5,00,00,000'
}, {
    'id': 2,
    'title': 'White Devil',
    'location': 'Delhi, kali Minar, India',
    'salary': 'Rs. 3,50,00,000'
}, {
    'id': 3,
    'title': 'Sarkata',
    'location': 'Remote',
    'salary': 'Rs. 4,00,00,000'
}, {
    'id': 4,
    'title': 'Munjya',
    'location': 'Jamna par, Delhi, India',
    'salary': '$6,00,50,000'
}, {
    'id': 5,
    'title': 'Nagin',
    'location': 'Jamna par, Delhi, India',
    'salary': '$12,00,50,000'
}]


@app.route("/")
def hello_Nitian():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Abnormal Recruiters')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
