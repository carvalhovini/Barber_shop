from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbershop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')

# Inicialização das extensões
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

# Modelos do banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'employee', 'customer'

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # duration in minutes
    price = db.Column(db.Float, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

# Rotas
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity={'username': user.username, 'role': user.role, 'id': user.id})
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user['id']).first()
    return jsonify({
        'user': {
            'username': user.username,
            'role': user.role,
            'id': user.id
        }
    }), 200

@app.route('/services', methods=['GET', 'POST'])
@jwt_required()
def services():
    current_user = get_jwt_identity()
    if request.method == 'POST':
        if current_user['role'] != 'admin':
            return jsonify({'message': 'Only admin can add services'}), 403

        data = request.get_json()
        new_service = Service(name=data['name'], duration=data['duration'], price=data['price'])
        db.session.add(new_service)
        db.session.commit()
        return jsonify({'message': 'Service added successfully'}), 201

    services = Service.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'duration': s.duration, 'price': s.price} for s in services]), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
@jwt_required()
def delete_service(service_id):
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Only admin can delete services'}), 403

    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404

    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully'}), 200

@app.route('/appointments', methods=['GET', 'POST'])
@jwt_required()
def appointments():
    current_user = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        new_appointment = Appointment(user_id=current_user['id'], service_id=data['service_id'], appointment_time=datetime.fromisoformat(data['appointment_time']))
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment booked successfully'}), 201

    appointments = Appointment.query.all()
    return jsonify([{
        'id': a.id,
        'service_id': a.service_id,
        'appointment_time': a.appointment_time,
        'user': {
            'id': a.user_id,
            'username': User.query.get(a.user_id).username,
            'role': User.query.get(a.user_id).role
        },
        'service': {
            'id': a.service_id,
            'name': Service.query.get(a.service_id).name,
            'duration': Service.query.get(a.service_id).duration,
            'price': Service.query.get(a.service_id).price
        }
    } for a in appointments]), 200

# Função para criar serviços padrão
def create_default_services():
    if not Service.query.first():
        services = [
            Service(name='Haircut', duration=30, price=20.00),
            Service(name='Beard Trim', duration=20, price=15.00),
            Service(name='Shave', duration=25, price=18.00),
            Service(name='Hair Coloring', duration=60, price=50.00)
        ]
        db.session.bulk_save_objects(services)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_default_services()
    app.run(debug=True)
