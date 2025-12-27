import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "college.db")

SECRET_KEY = "college-payment-secret"

RAZORPAY_KEY_ID = "rzp_test_Rvq9RVXKxkK7gN"
RAZORPAY_KEY_SECRET = "s4mPZI6UYrWSEezZUghHCJYq"
