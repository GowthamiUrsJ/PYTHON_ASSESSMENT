import requests
import pandas as pd

url = "https://run.mocky.io/v3/0ff9b004-fb7a-4d8a-9c95-43f96080d0e6"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    df.to_csv("api_output.csv", index=False)

    print("Data saved to 'api_output.csv'")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
