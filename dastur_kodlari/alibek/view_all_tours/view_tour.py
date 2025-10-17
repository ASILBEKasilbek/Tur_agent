tour_packages = [
    {"country": "Turkey", "city": "Istanbul", "days": 7, "price_usd": 850, "hotel": "4-star", "transport": "Flight", "season": "Summer"},
    {"country": "UAE", "city": "Dubai", "days": 6, "price_usd": 920, "hotel": "5-star", "transport": "Flight", "season": "Winter"},
    {"country": "France", "city": "Paris", "days": 8, "price_usd": 1350, "hotel": "4-star", "transport": "Flight", "season": "Spring"},
    {"country": "Italy", "city": "Rome", "days": 7, "price_usd": 1200, "hotel": "4-star", "transport": "Flight", "season": "Autumn"},
    {"country": "Spain", "city": "Barcelona", "days": 6, "price_usd": 1100, "hotel": "3-star", "transport": "Flight", "season": "Summer"},
    {"country": "Thailand", "city": "Bangkok", "days": 5, "price_usd": 780, "hotel": "4-star", "transport": "Flight", "season": "Winter"},
    {"country": "Japan", "city": "Tokyo", "days": 8, "price_usd": 1550, "hotel": "5-star", "transport": "Flight", "season": "Spring"},
    {"country": "Malaysia", "city": "Kuala Lumpur", "days": 5, "price_usd": 700, "hotel": "3-star", "transport": "Flight", "season": "Autumn"},
    {"country": "Indonesia", "city": "Bali", "days": 6, "price_usd": 890, "hotel": "4-star", "transport": "Flight", "season": "Summer"},
    {"country": "Egypt", "city": "Cairo", "days": 7, "price_usd": 950, "hotel": "4-star", "transport": "Flight", "season": "Winter"},
    {"country": "Greece", "city": "Athens", "days": 6, "price_usd": 1000, "hotel": "3-star", "transport": "Flight", "season": "Spring"},
    {"country": "Germany", "city": "Berlin", "days": 7, "price_usd": 1150, "hotel": "4-star", "transport": "Flight", "season": "Autumn"},
    {"country": "Switzerland", "city": "Zurich", "days": 7, "price_usd": 1600, "hotel": "5-star", "transport": "Flight", "season": "Winter"},
    {"country": "USA", "city": "New York", "days": 8, "price_usd": 1850, "hotel": "4-star", "transport": "Flight", "season": "Summer"},
    {"country": "UK", "city": "London", "days": 7, "price_usd": 1450, "hotel": "4-star", "transport": "Flight", "season": "Spring"},
    {"country": "Netherlands", "city": "Amsterdam", "days": 6, "price_usd": 1250, "hotel": "3-star", "transport": "Flight", "season": "Autumn"},
    {"country": "South Korea", "city": "Seoul", "days": 7, "price_usd": 1300, "hotel": "4-star", "transport": "Flight", "season": "Spring"},
    {"country": "China", "city": "Beijing", "days": 7, "price_usd": 950, "hotel": "4-star", "transport": "Flight", "season": "Autumn"},
    {"country": "India", "city": "Delhi", "days": 6, "price_usd": 700, "hotel": "3-star", "transport": "Flight", "season": "Winter"},
    {"country": "Uzbekistan", "city": "Samarkand", "days": 4, "price_usd": 400, "hotel": "3-star", "transport": "Train", "season": "Spring"},
    {"country": "Kazakhstan", "city": "Almaty", "days": 5, "price_usd": 550, "hotel": "3-star", "transport": "Bus", "season": "Summer"},
    {"country": "Russia", "city": "Moscow", "days": 7, "price_usd": 950, "hotel": "4-star", "transport": "Flight", "season": "Winter"},
    {"country": "Morocco", "city": "Marrakech", "days": 6, "price_usd": 980, "hotel": "4-star", "transport": "Flight", "season": "Spring"},
    {"country": "Brazil", "city": "Rio de Janeiro", "days": 8, "price_usd": 1500, "hotel": "4-star", "transport": "Flight", "season": "Summer"},
    {"country": "Australia", "city": "Sydney", "days": 9, "price_usd": 1900, "hotel": "5-star", "transport": "Flight", "season": "Winter"}
]

def view_all_tours():
    # Ichidagi 'tours' bo‘limini olamiz
 for key,value in tour_packages.items():
        print(f"{key}:{value}")
        return "Hamma tourlar kursatildi"