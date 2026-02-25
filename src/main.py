from rich import print
from weather_api import get_weather

def main():
    city = input("Введите город: ")
    weather = get_weather(city)

    temp = weather["main"]["temp"]
    desc = weather["weather"][0]["description"]

    print(f"[bold cyan]Weather Vibes[/bold cyan]")
    print(f"City: [green]{city}[/green]")
    print(f"Temperature: [yellow]{temp}°C[/yellow]")
    print(f"Description: [magenta]{desc}[/magenta]")

if __name__ == "__main__":
    main()
