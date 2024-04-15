import asyncio
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from config import DB_HOST, DB_PASSWORD, DB_NAME, DB_USERNAME
from models import User, Address

db_url = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(url=db_url)

SessionLocal = Session(engine)


async def create_record():
    """
    create user with address
    """
    # krishna: User = User(name='krishna', email='krishna@gmail.com', company='Srinsoft',
    #                      addresses=[Address(city='Chennai', state='Tamilnadu', country='India'),
    #                                 Address(city='Cuddalore', state='Tamilnadu', country='India')])
    # bala: User = User(name='bala', email='bala@gmail.com', company='thinQ24')
    # SessionLocal.add_all([krishna, bala])
    # SessionLocal.commit()
    # SessionLocal.close()
    pass


async def read_all_users():
    """
    read all the users from user table
    """
    all_users = select(User).where(User.is_active==True)
    for user in SessionLocal.scalars(all_users):
        print(f"Hi {user.name}")


async def get_user_by_id(pk: int):
    """
    get user by id from user table
    :param pk:
    :return:
    """
    user = SessionLocal.get(User, pk)
    print(f"The mail was sent to {user.name}-{user.email}")


async def update_user_by_id(pk: int, email: str):
    """
    update the user by id
    :param email:
    :param pk:
    :return:
    """
    user = SessionLocal.get(User, pk)
    user.email = email
    SessionLocal.commit()


async def delete_user_by_id(pk: int):
    """
    delete the user by id
    :param pk:
    :return:
    """
    user = SessionLocal.get(User, pk)
    if user:
        SessionLocal.delete(user)
        SessionLocal.commit()


async def main():
    await create_record()
    await read_all_users()
    await get_user_by_id(1)
    await update_user_by_id(1, "kalaiselvan@gmail.com")
    await delete_user_by_id(4)

asyncio.run(main())
