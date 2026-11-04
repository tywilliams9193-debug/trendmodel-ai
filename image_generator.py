import requests

API_TOKEN = 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

API_URL = (
    "https://api-inference.huggingface.co/models/"
    "runwayml/stable-diffusion-v1-5"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_image(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    return response.content
