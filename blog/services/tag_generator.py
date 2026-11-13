import requests
import json


def generate_tags(post_text):
    '''
    Generate tags and remove spaces and hashtags from the generated tags.  
    '''


    url = "http://localhost:11434/api/generate"

    prompt = f"""
    Generate 5 relevant hashtags for this social media post.

    Rules:
    - Return only relevant hashtags.
    - Do not include explanations.
    - Do not include duplicate hashtags.
    - Return valid JSON in this format:
      {{"tags": ["tag1", "tag2", "tag3"]}}

    Post:
    {post_text}
    """
    response = requests.post(
        url,
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False,
            "format": "json"
        },
        timeout=120
    )

    response.raise_for_status()

    result = response.json()
    data = json.loads(result["response"])

    return [tag.lower().replace('#', '').replace(' ', '') for tag in data.get("tags", [])[:5]]