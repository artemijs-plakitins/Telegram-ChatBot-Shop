
from sqlalchemy.future import select

from app.database.models import Orders, City, async_session
import app.database.requests as rq


async def insert_data():
    async with async_session() as session:
    
        resultOrders = await session.execute(select(Orders))
        resultCity = await session.execute(select(City))
        in_baseOrders = resultOrders.scalars().all()
        in_baseCity = resultCity.scalars().all()

        if not in_baseOrders:
            session.add_all([
                Orders(order_id=1, city="Riga",recipient="Jack",address_street="Brivibas street",postal_code="IK-4286",payment_amount=50,paid_status="Yes",delivery_status=0),
                Orders(order_id=2, city="Liepaja",recipient="Olga",address_street="Brivibas street",postal_code="VC-4020",payment_amount=50,paid_status="No",delivery_status=0),
                Orders(order_id=3, city="Daugavpils",recipient="Janis",address_street="Brivibas street",postal_code="SM-4531",payment_amount=80,paid_status="Yes",delivery_status=0),
                Orders(order_id=4, city="Riga",recipient="Michael",address_street="Lomonosova street",postal_code="XC-4582",payment_amount=20,paid_status="Yes",delivery_status=0),
                Orders(order_id=5, city="Riga",recipient="Bob",address_street="Brivibas street",postal_code="KL-4589",payment_amount=90,paid_status="No",delivery_status=0),
                Orders(order_id=7, city="Riga",recipient="Lisa",address_street="Brivibas street",postal_code="BC-4583",payment_amount=50,paid_status="No",delivery_status=0),
                Orders(order_id=8, city="Liepaja",recipient="Alice",address_street="Brivibas street",postal_code="RD-4109",payment_amount=28,paid_status="Yes",delivery_status=0),
                Orders(order_id=9, city="Riga",recipient="Mark",address_street="Brivibas street",postal_code="CL-1289",payment_amount=20,paid_status="Yes",delivery_status=0),
                Orders(order_id=10, city="Liepaja",recipient="Jonathan",address_street="Brivibas street",postal_code="DE-7289",payment_amount=15,paid_status="No",delivery_status=0),
                Orders(order_id=11, city="Daugavpils",recipient="Dmitry",address_street="Brivibas street",postal_code="PO-4509",payment_amount=20,paid_status="Yes",delivery_status=0),
            ])
            await session.commit()
            print("The data has been successfully added!")
        else:
            print("Data already exist, skipping insertion.")
        
        if not in_baseCity:
            session.add_all([
                City(city_id=1, city_name="Riga"),
                City(city_id=2, city_name="Liepaja"),
                City(city_id=3, city_name="Daugavpils")
            ])
            await session.commit()
            print("The data has been successfully added!")
        else:
            print("Data already exist, skipping insertion.")