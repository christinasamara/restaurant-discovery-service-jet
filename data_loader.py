import requests

def load_data(postcode="EC4M7RF"):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        full_data = response.json()
        raw_restaurants = full_data.get('restaurants', [])[:10]

        restaurants = []
        for res in raw_restaurants:
            cuisine_list = [c.get('name') for c in res.get('cuisines', [])]
            addr = res.get('address', {})
            full_address = f"{addr.get('firstLine')}, {addr.get('city')}, {addr.get('postalCode')}"

            restaurants.append({
                "name": res.get('name'),
                "cuisines": ", ".join(cuisine_list),
                "rating": res.get('rating', {}).get('starRating'),
                # get also count else get 0
                "rating_count": res.get('rating', {}).get('count', 0),
                "address": full_address,
                "logo_url": res.get('logoUrl')
            })

        return restaurants

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    data = load_data("EC4M7RF")
    if data:
        print(f"Fetched {len(data)} restaurants.")

        print(f"all data: {data}")
        
        print(f"First Restaurant: {data[2].get('name')}")
        print(f"First Restaurant Cuisine: {data[2].get('cuisines')}")
        print(f"First Restaurant Rating: {data[2].get('rating')}")
        print(f"First Restaurant Address: {data[2].get('address')}")