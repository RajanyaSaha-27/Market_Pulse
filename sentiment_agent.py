import json

from Market_Pulse.config import model
from Market_Pulse.utils import clean_text


def analyze_sentiment(ticker, headlines):
    results = []

    for news in headlines:
        cleaned = clean_text(news)

        prompt = f"""
        You are a financial market sentiment analysis agent.

        Analyze the following market-related news headline:

        "{cleaned}"

        Tasks:
        1. Determine sentiment: positive, negative, or neutral
        2. Give a sentiment score between -1 and +1
        3. Extract 2-3 finance-related keywords
        4. Give one-line explanation

        Respond ONLY in JSON:
        {{
          "sentiment": "",
          "score": 0.0,
          "keywords": [],
          "summary": ""
        }}
        """

        # response = model.generate_content(prompt)
        # results.append(response.text)
# added part
        try:
            response = model.generate_content(prompt)
            text = response.text
        except Exception as e:
            # Gemini failed → fallback
            results.append(json.dumps({
                "sentiment": "neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "Gemini API failed"
            }))
            continue

        # extract JSON safely
        import re
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            results.append(match.group())
        else:
            results.append(json.dumps({
                "sentiment": "neutral",
                "score": 0.0,
                "keywords": [],
                "summary": "Invalid Gemini response"
            }))


    return results


# import json
# from Market_Pulse.config import model

# def analyze_sentiment(ticker, _):
#     prompt = f"""
# You are a financial market analyst AI.

# TASK:
# - Fetch and analyze recent (last few days) market news for "{ticker}"
# - Consider earnings, macro news, stock performance, investor sentiment

# SCORING RULES:
# - Score range: -1.0 to +1.0
# - Strong positive news → > 0.4
# - Strong negative news → < -0.4
# - Mixed or unclear → neutral

# RETURN ONLY VALID JSON:

# {{
#   "sentiment": "positive | negative | neutral",
#   "score": number,
#   "articles_analyzed": number,
#   "summary": "one-line explanation"
# }}
# """

#     try:
#         response = model.generate_content(prompt)
#         text = response.text.strip()

#         start = text.index("{")
#         end = text.rindex("}") + 1
#         parsed = json.loads(text[start:end])

#         return [json.dumps(parsed)]

#     except Exception:
#         return [json.dumps({
#             "sentiment": "neutral",
#             "score": 0.0,
#             "articles_analyzed": 0,
#             "summary": "Fallback due to AI error"
#         })]
