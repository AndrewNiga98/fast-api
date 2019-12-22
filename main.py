from fastapi import FastAPI

app = FastAPI()


person = [
    {
        'id': 0,
        'name': u'Andrew',
        'surname': u'Nigaychuk'
    },
    {
        'id': 1,
        'name' : u'Bogdan',
        'surname' : u'Ivanyuk'
    }
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/person")
def read_person():
    return {"person": person}

@app.get("/api/person/{person_id}")
def read_person(person_id: int):
    return {"person": person[person_id]}