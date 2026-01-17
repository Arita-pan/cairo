from datetime import datetime
from cairo.extensions import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    amount_cents = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    account = db.relationship("Account", back_populates="transactions")
    category = db.relationship("Category")

    def __repr__(self):
        return f"<Transaction {self.amount_cents}>"
