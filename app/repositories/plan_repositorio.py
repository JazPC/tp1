from app import db
from app.models import Plan

class PlanRepository:
    @staticmethod
    def crear(plan: Plan):
      db.session.add(plan)
      db.session.commit()
        