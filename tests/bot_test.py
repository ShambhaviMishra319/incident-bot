# test.py
from app.chatbot.bot import init_search_index, handle_new_issue

# Step 1: Build the FAISS index
index, incidents, ids = init_search_index()

# Step 2: Query with a new issue
query = "API call fails with 500 error in CloudWatch"
results = handle_new_issue(query, index, incidents, ids)

print("Similar incidents found:")
for r in results:
    print(f"Incident: {r['incident_number']}")
    print(f"Issue: {r['issue']}")
    print(f"Solution: {r['solution']}")
    print("-" * 40)
