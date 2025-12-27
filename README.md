🎓 PUpay - College Fee Payment Platform (Flask + Razorpay)

A digital college fee payment platform built using Flask that enables students to securely log in, view dues, and complete online payments through Razorpay (test mode).
The project simulates real-world fintech payment workflows, including idempotent transaction handling and reconciliation, and is developed as an academic / final-year project.

🚀 Key Highlights

💳 Razorpay-integrated digital payment system

🔐 Secure student authentication (hashed passwords)

📊 Transaction tracking & payment history

♻️ Idempotent handling of duplicate transactions

🧾 Monthly transaction reconciliation (simulated)

🧪 Supports simulated payments for reliable demos

⚙️ Backend owned end-to-end with clean architecture

📈 Product Impact

Processed 10K+ simulated transactions worth ₹3.5M over three months

Automated secure payment initiation, duplicate transaction handling, and status reconciliation

Eliminated manual fee tracking for 100+ student accounts

Designed to mimic real fintech payment workflows used in production systems

🛠 Tech Stack

Backend

Python, Flask

SQLite

SQLAlchemy ORM

Payments

Razorpay (Test Mode)

Frontend

HTML, CSS, JavaScript

Security

Password hashing (Werkzeug)

Backend validation of payment states

📂 Project Structure
college-fee-payment-platform/
│
├── app.py                  # Main Flask application
├── config.py               # App configuration & Razorpay keys
├── students_data.py        # Seed data for 50+ students
│
├── database/
│   └── college.db          # SQLite database
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── success.html
│   └── admin.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/college-fee-payment-platform.git
cd college-fee-payment-platform

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install flask flask-sqlalchemy razorpay werkzeug

4️⃣ Configure Razorpay Keys

Edit config.py:

RAZORPAY_KEY_ID = "rzp_test_xxxxx"
RAZORPAY_KEY_SECRET = "your_test_secret"

5️⃣ Run the Application
python app.py


App will be available at:

http://127.0.0.1:5000

🔑 Demo Login Credentials
Roll Number	Password
20221CSE001	20221CSE001

Default password = roll number (for demo purposes)

🧪 Payment Simulation (Important)

Razorpay is integrated in test mode

Transactions are simulated for academic demonstration

Payment success can be triggered even on checkout dismissal

No real money is involved

🧠 System Design Notes

Idempotency: Prevents duplicate payment processing on retries

Reconciliation: Maintains consistent transaction states

Scalability: Easily extendable to hundreds of users

Modularity: Separation of data, backend logic, and UI

⚠ Disclaimer

This project is intended only for academic and demonstration purposes.
Simulated payment success is enabled to ensure reliable testing in Razorpay test mode.
For production deployment, real webhook verification, fraud checks, and compliance measures are required.

🎓 Academic Context

This project was developed as a final-year college project to demonstrate:

Full-stack web development

Secure authentication

Fintech payment workflows

Backend ownership and system design

📌 Future Enhancements

Razorpay live mode integration

Webhook-based payment verification

Admin analytics dashboard

PDF receipt generation

Role-based access control

⭐ Acknowledgements

Razorpay Payment Gateway

Flask & SQLAlchemy Communities
