from app.db.crud import init_db,add_incident, get_all_incidents, get_incident_by_id,reset_and_insertDummyDate

# 1. Initialize DB
init_db()
#reset_and_insertDummyDate()
get_all_incidents()

