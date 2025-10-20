from database import Base
from sqlalchemy import Column, Integer, String, Date

class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    lc_id = Column(Integer, unique=True)
    question = Column(String)
    done_on = Column(Date)
    started = Column(Date)

    def __str__(self):
        return f"{self.lc_id}: {self.question} (DB ID: {self.id})"
    