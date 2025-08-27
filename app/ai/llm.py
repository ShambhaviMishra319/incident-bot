from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(issue, similar_incidents):
    context = "\n".join(
        [f"Incident {i['incident_number']}: Issue: {i['issue']} | Solution: {i['solution']}"
         for i in similar_incidents]
    )
    
    prompt = f"""
    A new incident has been reported: {issue}.
    Based on past incidents below, suggest how to approach it:

    {context}

    Provide a clear step-by-step answer.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # can use smaller/cheaper models too
        messages=[{"role": "system", "content": "You are a helpful support engineer."},
                  {"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
