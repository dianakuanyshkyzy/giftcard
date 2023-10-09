from giftcards.schemes import CreateGiftcardRequest, EditGiftcardRequest
from database import database
from sqlalchemy import insert, select, update, delete
from database import giftcards as Giftcards
from fastapi import HTTPException


async def create_giftcard(Giftcard: CreateGiftcardRequest):
    # insert_query = f'INSERT INTO Giftcards (author, text, key_words, created_at) VALUES (\'{Giftcard.author}\', \'{Giftcard.text}\', \'{Giftcard.key_words}\', \'{Giftcard.created_at}\')'
    insert_query = insert(Giftcards).values(
        Giftcard.dict()
    ).returning(Giftcards.columns.id)

    return await database.fetch_one(insert_query)


async def get_Giftcards():
    # select_query = 'SELECT * FROM Giftcards'
    select_query = select(Giftcards)

    return await database.fetch_all(select_query)


async def get_Giftcard_by_id(Giftcard_id: int):
    # select_query = f'SELECT * FROM Giftcards WHERE id={Giftcard_id}'
    select_query = select(Giftcards).where(Giftcards.columns.id == Giftcard_id)

    Giftcard = await database.fetch_one(select_query)
    if not Giftcard:
        raise HTTPException(status_code=404, detail="Giftcard not found")

    return Giftcard


async def edit_Giftcard(Giftcard_id: int, Giftcard: EditGiftcardRequest):
    Giftcard_db = await get_Giftcard_by_id(Giftcard_id)

    # UPDATE Giftcards SET , content = 'content'
    update_query = (
        update(Giftcards)
        .values(Giftcard.dict(exclude_none=True))
        .where(Giftcards.c.id == Giftcard_id)
        .returning(Giftcards)
    )
    return await database.fetch_one(update_query)


async def delete_Giftcard(Giftcard_id: int):
    delete_query = delete(Giftcards).where(Giftcards.columns.id == Giftcard_id)

    return await database.execute(delete_query)