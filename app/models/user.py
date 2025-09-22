from datetime import datetime
from zoneinfo import ZoneInfo
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

class Users(db.Model):
    __tablename__ = "cal_users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), onupdate=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Users {self.id}>'