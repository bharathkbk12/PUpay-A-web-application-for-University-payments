from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import razorpay
import os
from config import *
from students_data import students


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

razorpay_client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)

# ---------------- MODELS ----------------


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    password = db.Column(db.String(200))   # 🔐 NEW
    due_amount = db.Column(db.Integer)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id"),
        nullable=False
    )
    razorpay_order_id = db.Column(db.String(100))
    razorpay_payment_id = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    status = db.Column(db.String(30))

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        roll = request.form.get("roll")
        password = request.form.get("password")

        student = Student.query.filter_by(roll=roll).first()

        if student and check_password_hash(student.password, password):
            return redirect(url_for("dashboard", roll=roll))
        else:
            return "Invalid Roll Number or Password", 401

    return render_template("login.html")



@app.route("/dashboard/<roll>")
def dashboard(roll):
    student = Student.query.filter_by(roll=roll).first()

    if not student:
        return "Student not found", 404

    payments = Payment.query.filter_by(student_id=student.id).all()

    return render_template(
        "dashboard.html",
        student=student,
        payments=payments,
        razorpay_key=RAZORPAY_KEY_ID
    )


@app.route("/create_order/<roll>")
def create_order(roll):
    student = Student.query.filter_by(roll=roll).first()

    if not student or student.due_amount <= 0:
        return jsonify({"error": "Invalid student or amount"}), 400

    amount = student.due_amount * 100  # paise

    order = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    payment = Payment(
        student_id=student.id,
        razorpay_order_id=order["id"],
        amount=student.due_amount,
        status="created"
    )
    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "order_id": order["id"],
        "amount": amount
    })

@app.route("/payment_success", methods=["POST"])
def payment_success():
    order_id = request.form["razorpay_order_id"]
    payment_id = request.form["razorpay_payment_id"]

    payment = Payment.query.filter_by(razorpay_order_id=order_id).first()
    payment.razorpay_payment_id = payment_id
    payment.status = "success"

    student = Student.query.get(payment.student_id)
    student.due_amount = 0

    db.session.commit()
    return render_template("success.html", student=student)

@app.route("/admin")
def admin():
    students = Student.query.all()
    return render_template("admin.html", students=students)

@app.route("/fake_payment_success/<order_id>")
def fake_payment_success(order_id):
    payment = Payment.query.filter_by(razorpay_order_id=order_id).first()

    if not payment:
        return "Invalid order", 400

    # Mark payment as simulated success
    payment.razorpay_payment_id = "FAKE_PAYMENT_ID"
    payment.status = "success"

    student = Student.query.get(payment.student_id)
    student.due_amount = 0

    db.session.commit()

    return redirect(url_for("dashboard", roll=student.roll))


# ---------------- INIT DB ----------------


with app.app_context():
    os.makedirs("database", exist_ok=True)
    db.create_all()

    if Student.query.count() == 0:
        objs = []
        for s in students:
            objs.append(
                Student(
                    roll=s["roll"],
                    name=s["name"],
                    email=s["email"],
                    password=generate_password_hash(s["password"]),
                    due_amount=500
                )
            )

        db.session.bulk_save_objects(objs)
        db.session.commit()
        print("✅ Students with passwords created")




if __name__ == "__main__":
    app.run(debug=True)
