from fastapi import FastAPI
from pydantic import BaseModel
from models import Questions, Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/parse")
async def parse():
    ques_to_store = []
    with open("ques_19oct.txt") as qfile:
        for quesline in qfile:
            qdata = quesline.strip().split(".")
            if len(qdata) != 2:
                print("Check this: ", qdata)
                continue
        
            lcid = int(qdata[0])
            ques_string = qdata[1].strip()
            
            q = Questions(lc_id=lcid, question=ques_string)
            ques_to_store.append(q)
    
    print(len(ques_to_store))
    print(ques_to_store)
            

