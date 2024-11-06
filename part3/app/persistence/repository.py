from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        from app import db  # Import db inside the method
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        from app import db  # Import db inside the method
        return self.model.query.get(obj_id)

    def get_all(self):
        from app import db  # Import db inside the method
        return self.model.query.all()

    def update(self, obj_id, data):
        from app import db  # Import db inside the method
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        from app import db  # Import db inside the method
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        from app import db  # Import db inside the method
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()