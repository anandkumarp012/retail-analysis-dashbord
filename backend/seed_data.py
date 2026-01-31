import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import datetime
import random

MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "retail_dashboard"

async def seed_data():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DATABASE_NAME]
    
    # 1. Clear existing data
    await db.products.delete_many({})
    await db.sales.delete_many({})
    await db.forecasts.delete_many({})
    await db.users.delete_many({})
    
    print("Seeding Products...")
    products = [
        {"product_id": 101, "product_name": "Wireless Mouse", "category": "Electronics", "unit_price": 1299.0, "current_inventory": 150},
        {"product_id": 102, "product_name": "Mechanical Keyboard", "category": "Electronics", "unit_price": 4500.0, "current_inventory": 50},
        {"product_id": 103, "product_name": "USB-C Cable", "category": "Accessories", "unit_price": 499.0, "current_inventory": 300},
    ]
    
    for p in products:
        p["created_at"] = datetime.datetime.utcnow()
        await db.products.insert_one(p)

    print("Seeding Sales Data...")
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=60)
    
    sales_to_insert = []
    for p in products:
        current_date = start_date
        while current_date < today:
            qty = random.randint(5, 20) if current_date.weekday() > 4 else random.randint(1, 10)
            is_promo = random.random() > 0.9
            if is_promo: qty *= 2
            
            sales_to_insert.append({
                "product_id": p["product_id"],
                "date": str(current_date),
                "quantity_sold": qty,
                "revenue": qty * p["unit_price"],
                "promotion_active": is_promo,
                "created_at": datetime.datetime.utcnow()
            })
            current_date += datetime.timedelta(days=1)
            
    if sales_to_insert:
        await db.sales.insert_many(sales_to_insert)
        
    print(f"Seeded {len(sales_to_insert)} sales records.")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_data())
