from pydantic import BaseModel, ConfigDict

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseOut(ExpenseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)