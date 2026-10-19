import argparse
import json
from typing import Optional
import urllib.parse
import urllib.request


class Brewery:

    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: Optional[str],
        address_2: Optional[str],
        address_3: Optional[str],
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str],
        state: Optional[str],
        street: Optional[str],
    ):
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = brewery_type
        self.address_1: Optional[str] = address_1
        self.address_2: Optional[str] = address_2
        self.address_3: Optional[str] = address_3
        self.city: str = city
        self.state_province: str = state_province
        self.postal_code: str = postal_code
        self.country: str = country
        self.longitude: Optional[str] = longitude
        self.latitude: Optional[str] = latitude
        self.phone: Optional[str] = phone
        self.website_url: Optional[str] = website_url
        self.state: Optional[str] = state
        self.street: Optional[str] = street

    def __str__(self) -> str:
        return (
            f"Browar: {self.name} [{self.brewery_type.capitalize()}]\n"
            f"Lokalizacja: {self.city}, {self.state_province} ({self.country})\n"
            f"Adres: {self.street or 'Brak adresu'}\n"
            f"Strona WWW: {self.website_url or 'Brak strony'}\n"
            f"Telefon: {self.phone or 'Brak telefonu'}\n"
            f"{'-' * 40}"
        )


def fetch_breweries(
    city: Optional[str] = None, per_page: int = 20
) -> list[Brewery]:
    base_url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": per_page}

    if city:
        formatted_city = city.strip().replace(" ", "_")
        params["by_city"] = formatted_city

    # Budujemy pełny URL wraz z parametrami (np. ?per_page=20&by_city=berlin)
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 (Python Brewery App)"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                breweries_list = []

                for item in data:
                    brewery = Brewery(
                        id=item.get("id"),
                        name=item.get("name"),
                        brewery_type=item.get("brewery_type"),
                        address_1=item.get("address_1"),
                        address_2=item.get("address_2"),
                        address_3=item.get("address_3"),
                        city=item.get("city"),
                        state_province=item.get("state_province"),
                        postal_code=item.get("postal_code"),
                        country=item.get("country"),
                        longitude=item.get("longitude"),
                        latitude=item.get("latitude"),
                        phone=item.get("phone"),
                        website_url=item.get("website_url"),
                        state=item.get("state"),
                        street=item.get("street"),
                    )
                    breweries_list.append(brewery)

                return breweries_list
            else:
                print(f"Błąd serwera API: HTTP {response.status}")
                return []

    except Exception as e:
        print(f"Wystąpił błąd podczas połączenia z API: {e}")
        return []


if __name__ == "__main__":
    # Konfiguracja parsera argumentów linii poleceń
    parser = argparse.ArgumentParser(
        description="Pobieranie i wyświetlanie danych o browarach z Open Brewery DB."
    )
    parser.add_argument(
        "--city",
        type=str,
        help="Nazwa miasta, do którego mają zostać ograniczone wyniki (np. Berlin, New York)",
    )

    args = parser.parse_args()

    # Informacja dla użytkownika o trybie działania skryptu
    if args.city:
        print(f"Pobieranie 20 pierwszych browarów dla miasta: {args.city}...\n")
    else:
        print("Pobieranie 20 pierwszych browarów (brak filtru miasta)...\n")

    # Wywołanie funkcji pobierającej z opcjonalnym parametrem miasta
    lista_browarow = fetch_breweries(city=args.city, per_page=20)

    # Wyświetlenie wyników
    if isinstance(lista_browarow, list) and lista_browarow:
        for nr, browar in enumerate(lista_browarow, start=1):
            print(f"Pozycja {nr}:")
            print(browar)
    else:
        print("Nie znaleziono browarów spełniających kryteria lub wystąpił błąd.")
