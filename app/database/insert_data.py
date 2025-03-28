
from sqlalchemy.future import select

from app.database.models import Orders, async_session


async def insert_orders():
    async with async_session() as session:
    
        result = await session.execute(select(Orders))
        in_base = result.scalars().all()

        if not in_base:
            session.add_all([
                Orders(order_id=1, city="Riga",recipient="Jack",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="Yes"),
                Orders(order_id=2, city="Liepaja",recipient="Olga",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="No"),
                Orders(order_id=3, city="Daugavpils",recipient="Janis",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="Yes"),
                Orders(order_id=4, city="Riga",recipient="Michael",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="Yes"),
                Orders(order_id=5, city="Riga",recipient="Bob",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="No"),
                Orders(order_id=7, city="Riga",recipient="Lisa",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="No"),
                Orders(order_id=8, city="Liepaja",recipient="Alice",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="Yes"),
                Orders(order_id=9, city="Riga",recipient="Mark",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="Yes"),
                Orders(order_id=10, city="Liepaja",recipient="Jonathan",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="No"),
                Orders(order_id=11, city="Daugavpils",recipient="Dmitry",address_street="Brivibas iela",postal_code="XC-4589",payment_amount=20,paid_status="Yes"),
            ])
            await session.commit()
            print("The data has been successfully added!")
        else:
            print("Data already exist, skipping insertion.")
