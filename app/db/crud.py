from .database import get_connection
from .models import INCIDENTS_TABLE

def init_db():
    con=get_connection() #open connection to db
    cursor=con.cursor() #create cursomr
    cursor.execute(INCIDENTS_TABLE)
    con.commit() #safving changes
    con.close() #closing the connection

def add_incident(incident_number:str,issue:str,solution:str):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("INSERT INTO incidents (incident_number, issue, solution) VALUES (?,?,?)",(incident_number, issue, solution))
    con.commit()
    con.close()

def get_incident_by_id(incident_number:str):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("SELECT * FROM incidents WHERE incident_number=?",(incident_number,))
    result = cursor.fetchone()
    con.close()
    return result

def get_all_incidents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    results = cursor.fetchall()
    conn.close()
    #print(results)
    return results

def reset_and_insertDummyDate():
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("DROP TABLE IF EXISTS incidents")
    cursor.execute(INCIDENTS_TABLE)

    dummy_incidents = [
        (f"INC{10000 + i}", f"Dummy issue {i} description", f"Dummy solution steps {i}")
        for i in range(1, 16)
    ]

    cursor.executemany(
        "INSERT INTO incidents (incident_number, issue, solution) VALUES (?, ?, ?)",
        dummy_incidents
    )

    con.commit()
    con.close()
    print("✅ DB reset and seeded with 15 dummy incidents.")