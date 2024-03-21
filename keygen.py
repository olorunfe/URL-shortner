import random
import string
from database import database

async def generate_short_url(length=8):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(length))
        query = "SELECT COUNT(*) FROM shortened_urls WHERE short_url = :short_url"
        result = await database.fetch_val(query=query, values={"short_url": short_url})
        if result == 0:
            return short_url
