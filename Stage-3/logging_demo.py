import requests
import logging

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    logging.info("Sending GET request")

    response = requests.get(url)

    if response.status_code == 200:
        logging.info("API request successful")
        print(response.json())
    else:
        logging.warning(
            f"API returned status code {response.status_code}"
        )

except Exception:
    logging.exception("API request failed")