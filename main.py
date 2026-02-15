from fastapi import FastAPI, HTTPException
from database import get_connection, create_table
from Model import Lead

app = FastAPI(title = "Lead Managemnt system with MySql Server")

create_table()

@app.post("/leads")
def create_lead(lead:Lead):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
       INSERT INTO leads(name, email, industry, status)
       VALUES(%s,%s,%s,%s)
    """,(lead.name,lead.email,lead.industry,lead.status)
    )
    conn.commit()
    conn.close()
    return {"message":"Lead Created successfully"}
    

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.get("/get_lead")
def get_all_leads():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
       SELECT * FROM leads
    """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.put("/lead/{lead_id}")
def update_lead(lead_id:int,lead:Lead):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE leads
        SET name = %s,email =%s,industry = %s, status = %s WHERE id=%s
    """,(lead.name,lead.email,lead.industry,lead.status,lead_id)
    )
    conn.commit()
    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(status_code=404,details ="link not found")
    conn.close()
    return {"message":"Lead Updated successfully"}

@app.put("/lead/{lead_id}")
def update_lead(lead_id:int,lead:Lead):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE leads
        SET name = %s,email =%s,industry = %s, status = %s WHERE id=%s
    """,(lead.name,lead.email,lead.industry,lead.status,lead_id)
    )
    conn.commit()
    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(status_code=404,details ="link not found")
    conn.close()
    return {"message":"Lead Updated successfully"}

@app.delete("/delete_lead/{lead_id}")
def delete_lead(lead_id:int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM leads WHERE id =%s
    """,(lead_id,)
    )
    conn.commit()
    if cursor.rowcount==0:
        conn.close()
        raise HTTPException(status_code=404,details ="link not found")
    conn.close()
    return {"message":"Lead deleted successfully"}








    
    








    
    

