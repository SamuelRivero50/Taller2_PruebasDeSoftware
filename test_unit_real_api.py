from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository
from models import Order

Base.metadata.create_all(bind=engine)

class DummyLogger:
    def log(self, msg):
        # TODO: implementar un logger que no haga nada
        pass

class NullNotifier:
    def send(self, to, message):
        # TODO: implementar un notifier que no haga nada
        pass


def test_create_order_with_real_api():
    db = SessionLocal()
    order = create_order(1, 100, NullNotifier(), DummyLogger(), db, JsonPlaceholderUserRepository())
    assert order.status == 'CREATED'
    assert order.amount == 100
    assert order.user_email == 'Sincere@april.biz'
    db.query(Order).delete()
    db.commit()
    db.close()
