import requests


class Brewery:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.brewery_type = data.get('brewery_type')
        self.street = data.get('street')
        self.city = data.get('city')
        self.state = data.get('state')
        self.postal_code = data.get('postal_code')
        self.country = data.get('country')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')

    def __str__(self):
        return f"Brewery ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\n" \
               f"Address: street-{self.street}, city-{self.city}, state-{self.state}, postal code-{self.postal_code}, country-{self.country}\n" \
               f"Phone: {self.phone}\nWebsite: {self.website_url}\n"


def get_breweries():
    # get API data
    api_url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(api_url, params={"per_page": 20})
    if response.status_code == 200:
        breweries_data = response.json()
        breweries_list = [Brewery(data) for data in breweries_data]
        return breweries_list
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    breweries = get_breweries()

    if breweries:
        for brewery in breweries:
            print(brewery)
    else:
        print("Nie udało się pobrać danych z API.")
