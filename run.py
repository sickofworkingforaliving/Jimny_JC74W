from src.fetch_uk import fetch_uk_listings
from src.fetch_jp import fetch_jp_auctions
from src.fx import get_fx_rate
from src.cost_model import calculate_landed_cost
from src.generate_report import generate_csv

def main():
    print("Starting Jimny JC74W weekly report...")

    uk_listings = fetch_uk_listings()
    jp_auctions = fetch_jp_auctions()
    fx_rate = get_fx_rate()

    processed = []
    for car in jp_auctions:
        landed = calculate_landed_cost(car, fx_rate)
        processed.append({**car, **landed})

    generate_csv(uk_listings, processed)

    print("Report generated successfully.")

if __name__ == "__main__":
    main()
