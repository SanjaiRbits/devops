from flask import Flask, jsonify

app = Flask(__name__)

# 1 Home Route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})


# 2 Members Route
@app.route('/members')
def members():
    members_list = [
        {"id": 1, "name": "Rahul", "plan": "Gold"},
        {"id": 2, "name": "Anita", "plan": "Silver"}
    ]
    return jsonify(members_list)


# 3 Workouts Route
@app.route('/workouts')
def workouts():
    workouts = [
        {"day": "Monday", "workout": "Chest"},
        {"day": "Tuesday", "workout": "Back"}
    ]
    return jsonify(workouts)


# 4 Trainers Route
@app.route('/trainers')
def trainers():
    trainers = [
        {"id": 1, "name": "Arjun", "specialization": "Strength"},
        {"id": 2, "name": "Priya", "specialization": "Yoga"}
    ]
    return jsonify(trainers)


# 5 Membership Plans Route
@app.route('/plans')
def plans():
    plans = [
        {"plan": "Silver", "price": 2000},
        {"plan": "Gold", "price": 3500},
        {"plan": "Platinum", "price": 5000}
    ]
    return jsonify(plans)


# 6 Gym Schedule Route
@app.route('/schedule')
def schedule():
    schedule = [
        {"time": "6 AM", "activity": "Cardio"},
        {"time": "8 AM", "activity": "Weight Training"},
        {"time": "6 PM", "activity": "Zumba"}
    ]
    return jsonify(schedule)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)