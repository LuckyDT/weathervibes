import os
import requests
from dotenv import load_dotenv
from rich import print

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Sofia"

def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    weather = get_weather(CITY)
    temp = weather["main"]["temp"]
    desc = weather["weather"][0]["description"]

    print(f"[bold cyan]Weather Vibes[/bold cyan]")
    print(f"City: [green]{CITY}[/green]")
    print(f"Temperature: [yellow]{temp}°C[/yellow]")
    print(f"Description: [magenta]{desc}[/magenta]")

if __name__ == "__main__":
    main()
