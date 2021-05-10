from app import db


class Key(db.Model):

    __tablename__ = "key"

    id = db.Column(db.Integer, primary_key=True)
    p_key = db.Column(db.String(544),unique=True, nullable=False)
    pr_key = db.Column(db.String(700), unique=True, nullable=False)
    device_id = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, device_id: str, p_key: str, pr_key: str):
        self.device_id = device_id
        self.p_key = p_key
        self.pr_key = pr_key

    def __repr__(self):
        return f"<Device {self.device_id}>"

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()