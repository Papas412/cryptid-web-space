from model.explorer import Explorer
import fake.explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

def modify(explorer: Explorer) -> Explorer:
    return data.modify(id, explorer)

def replace(explorer: Explorer) -> Explorer:
    return data.replace(id, explorer)

def delete(id: int, explorer: Explorer) -> bool:
    return data.delete(id)
