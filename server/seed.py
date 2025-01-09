from models import db, Admin
from auth import bcrypt
from app import app

with app.app_context():
    hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
    admin = Admin(password=hashed_password)
    db.session.add(admin)
    db.session.commit()
    print("Admin user created with default password: admin123")
