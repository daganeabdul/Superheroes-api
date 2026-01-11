from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecret'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
mail = Mail(app)


from models import Hero, Power, HeroPower




@app.route('/heroes')
def get_heroes():
    return jsonify([h.to_dict() for h in Hero.query.all()]), 200


@app.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify({
        **hero.to_dict(),
        "hero_powers": [hp.to_dict() for hp in hero.hero_powers]
    }), 200


@app.route('/powers')
def get_powers():
    return jsonify([p.to_dict() for p in Power.query.all()]), 200


@app.route('/powers/<int:id>')
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200


@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    try:
        power.description = request.json['description']
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400


@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    try:
        hp = HeroPower(strength=data['strength'], hero_id=data['hero_id'], power_id=data['power_id'])
        db.session.add(hp)
        db.session.commit()
        return jsonify(hp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400


@app.route('/send-email')
def send_email():
    msg = Message(
        "Test Email",
        sender="your_email@gmail.com",
        recipients=["recipient@example.com"]
    )
    msg.body = "Flask mail works!"
    mail.send(msg)
    return {"message": "Email sent"}, 200

if __name__ == "__main__":
    app.run(debug=True)
