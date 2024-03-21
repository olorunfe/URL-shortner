import requests

async def generate_qr_code(url: str) -> str:
    # Call the QR code generation API
    response = requests.post(
        "https://api.qr-code-generator.com/v1/create",
        json={"url": url}
    )
    if response.status_code == 200:
        qr_code_data = response.json()
        return qr_code_data.get("imageUrl")
    else:
        # If the API call fails, return None
        return None
