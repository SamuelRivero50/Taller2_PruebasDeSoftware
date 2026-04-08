from order_service import create_order
from database import SessionLocal, Base, engine
from models import Order
from user_repository import FakeUserRepository

Base.metadata.create_all(bind=engine)

# ---- Fake usado en la APP ----
class FakeUserRepository:
    def get_user_email(self, user_id):
        return f"user{user_id}@fake.local"
        
class DummyLogger:
    def log(self, msg):
        pass

class NullNotifier:
    def send(self, to, message):
        pass

def test_create_order_integration_with_fake():
    db = SessionLocal()
    order = create_order(3, 60, NullNotifier(), DummyLogger(), db, FakeUserRepository())
    assert order.status == 'CREATED'
    assert order.user_email == "user3@fake.local"
    db.query(Order).delete()
    db.commit()
    db.close()
