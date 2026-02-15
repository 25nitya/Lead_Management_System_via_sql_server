import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = '40eqhe.h.filess.io',
        user = 'lead_management_bicycledug',
        password = '08beb0d3dce84b0122f6b8f51adb5f47d1489a7a',
        database = 'lead_management_bicycledug',
        port = 3306
        
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