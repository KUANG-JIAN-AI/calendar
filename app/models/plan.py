from datetime import datetime
from zoneinfo import ZoneInfo
from .. import db

class Plans(db.Model):
    __tablename__ = "cal_plans"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    plan_date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), onupdate=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "plan_date": self.plan_date.strftime("%Y-%m-%d") if self.plan_date else None,
            "title": self.title,
            "start": self.start_time.strftime("%H:%M") if self.start_time else None,
            "end": self.end_time.strftime("%H:%M") if self.end_time else None
        }

    def __repr__(self):
        return f'<Plans {self.id}>'