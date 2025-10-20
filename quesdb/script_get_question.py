from database import SessionLocal
from models import Questions
from sqlalchemy import func
from datetime import date

def get_question():
    db = SessionLocal()

    try:
        question: Questions = (db.query(Questions)
            .filter(Questions.started.is_(None))
            .order_by(func.random())
            .first())
        
        if question:
            question.started = date.today()
            db.commit()
            print(question)

        return question
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    get_question()