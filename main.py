import asyncio
import aiomysql

async def fetch_users():
    """
    Асинхронна функція для отримання інформації про користувачів із бази даних MySQL.
    """
    
    db_config = {
        'host': 'localhost',       
        'port': 3306,              
        'user': 'your_username',  
        'password': 'your_password',  
        'db': 'your_database',     
    }

    
    try:
        conn = await aiomysql.connect(**db_config)
        async with conn.cursor() as cursor:
            
            query = "SELECT id, name, email FROM users;"
            await cursor.execute(query)

            
            result = await cursor.fetchall()

            
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    except aiomysql.MySQLError as e:
        print(f"Помилка MySQL: {e}")

    finally:
        
        conn.close()


if __name__ == "__main__":
    asyncio.run(fetch_users())


