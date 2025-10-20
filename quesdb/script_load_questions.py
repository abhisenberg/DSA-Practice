from database import Base, engine, SessionLocal
from models import Questions

Base.metadata.create_all(engine)

def load_questions():
    db = SessionLocal()

    ques_to_store = []
    with open("ques_19oct.txt") as qfile:
        for line in qfile:
            qdata = line.strip().split(".")
            if len(qdata) != 2:
                print("Check this:", qdata)
                continue

            lcid = int(qdata[0])
            question_text = qdata[1].strip()

            q = Questions(lc_id=lcid, question=question_text)
            ques_to_store.append(q)

    print(f"Prepared {len(ques_to_store)} questions.")

    db.bulk_save_objects(ques_to_store)
    db.commit()
    db.close()
    print("✅ Inserted all questions successfully.")

if __name__ == "__main__":
    load_questions()