from giftcards.schemes import CreateGiftcardRequest, EditGiftcardRequest
from fastapi import HTTPException, APIRouter
import time
from giftcards import services

router = APIRouter()

@router.get('')
async def get_Giftcards():
    return await services.get_Giftcards()


@router.post('')
async def create_Giftcard(Giftcard: CreateGiftcardRequest):
    return await services.create_Giftcard(Giftcard)


@router.get('/{id}')
async def get_Giftcard(id: int):
    return await services.get_Giftcard_by_id(id)


@router.put('/{id}')
async def edit_Giftcard(id: int, Giftcard_data: EditGiftcardRequest):
    return await services.edit_Giftcard(id, Giftcard_data)


@router.delete('/{id}')
async def delete_Giftcard(id: int):
    await services.delete_Giftcard(id)

    return {"message": "ok, deleted"}