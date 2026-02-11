from openai import OpenAI

client = OpenAI(api_key="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")

def generate_insights(total_visitors, avg_dwell):

    prompt = f"""
    Retail Analytics Report:
    Total Visitors: {total_visitors}
    Average Dwell Time: {avg_dwell} seconds

    Provide business insights and recommendations.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
