from database import SessionLocal
from models import Questions
from sqlalchemy import func
from datetime import date
import sys

def mark_done_question(lc_id: int):
    db = SessionLocal()

    try:
        question: Questions = (db.query(Questions)
            .filter(Questions.lc_id == lc_id)
            .first())
        
        if question:
            question.done_on = date.today()
            db.commit()
            print(f"Marked done for {question}")

        return question
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Pls supply question number")
        exit()

    try:
        lc_id = int(args[1])
        mark_done_question(lc_id)

    except Exception as e:
        print("Error encountered: ", e)
        exit()
