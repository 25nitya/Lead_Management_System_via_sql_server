import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("DB")
        user = os.getenv("User")
        password = os.getenv("DB_psswrd")
        database = os.getenv("DB_url")
        port = os.getenv("DB_port")
        
    )
    
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS leads(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(200),
        industry VARCHAR(100),
        status VARCHAR(20)  
    )
    
    """
    )
    conn.commit()
    conn.close()
    print("Table 'lead' ready")