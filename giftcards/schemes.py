from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CreateGiftcardRequest (BaseModel):
    # author: str
    text: str
    keywords: str
    created_at: datetime

class EditGiftcardRequest(BaseModel):
    # author: Optional[str] = None
    text: Optional[str] = None
    keywords: Optional[str] = None
    updated_at: Optional[datetime] = None
    