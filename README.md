step-1
1.1>>
dEFINING Schema>>models.py
1.2>>
Connecting to database>>database.py
1.3>>
CRUD>>crud.py

FLOW>>
/ Query Flow (When a new issue comes in):
    # We generate its embedding.
    # The embedding is compared against all past       incidents in FAISS.
    # The system retrieves the Top K similar    incidents.
    # It returns the incident numbers, issues, and solutions to guide on how to approach the problem.


###############################################
FUTURE SCOPE>
## ADD LLM => RAG
## 