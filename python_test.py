print("Problem 1") 
market_name = "Balogun Market"
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False 
print(f"Market: {market_name} Type: {type(market_name)}")
print(f"Traders: {num_traders} Type: {type(num_traders)} ")
print(f"Coordinates: {location_coords} Type: {type(location_coords)}")
print(f"Open Sundays:  {is_open_sundays} Type: {type(is_open_sundays)}")
total_revenue = 25_000_000
average_revenue = total_revenue / num_traders 
print(f"Average Daily Revenue Per Trader: {average_revenue} Naira ")


print("PROBLEM 2")
host_countries = ["Ghana", "Eygpt", "Nigeria", "Senegal", "Cameroon"]
host_countries.append("Ivory Coast")
host_countries.insert(1, "Morocco")
host_countries.remove("Senegal")
print(f"Total Countries: {len(host_countries)}")
sorted_countries = sorted(host_countries)
print(f"Alphabetical Order: {sorted_countries}")
print(f"Every Second Country: {host_countries[::2]}")

print("PROBLEM3")
river_data = {
    "Nile": {"length_km": 6650, "countries": 11},
    "Congo": {"length_km": 4700, "countries": 9},
    "Niger": {"length_km": 4180, "countries": 5}
}
river_data["Zambezi"] = {"length_km": 2574, "countries": 6}
river_data["Niger"]["countries"] = 6
print("River names:", list(river_data.keys()))
print(f"Congo flows through: {river_data['Congo']['countries']} countries")

total_length = 0
for river in river_data: total_length += river_data[river]["length_km"]
print(f"Total combined length: {total_length} km")

print("PROBLEM 4")
print("Multiplication of 7")
for i in range(1,11): 
 print(f"7*[i] = {7*i} ")
 print("LETTERS IN AFRICA")
 for letter in "Africa": 
   print("Letter")
print("Sum Of Even Numbers (1 to 50)")
even_sum = 0
for number in range (1,51):
 if number % 2 == 0:
    even_sum += number     
print(f"Sum of even numbers 1 to 50: {even_sum}")
print("COUNTDOWN LOOP")
COUNT = 20
while COUNT >= 1:
    print(COUNT)
    COUNT -= 1
    print("First number > 500 divisible by 3 and 7")
    number = 501
    while True: 
        if number % 3 == 0 and number % 7 == 0:
            print(f"First number greater than 500 divisible by 3 and 7: {number}")
            break
        number -= 1 
        
        
print("PROBLEM 5")
def classify_rainfall(mm):
 if mm > 300:
        return "Flood Risk"
 elif mm >= 200:
        return "Heavy Rain"
 elif mm >= 100:
        return "Moderate Rain"
 elif mm >= 1:
        return "Light Rain"
 else:
        return "Dry"
test_values = [350, 250, 150, 50, 0]
for value in test_values:
    print(f"{value}mm: {classify_rainfall(value)}")
    
    print("PROBLEM 6")


def calculate_exchange (amount, rate):
       return amount*rate   
result_amount = calculate_exchange (100, 1508)
print(f"100 USD = {result_amount} NGN")
def format_price(amount, currency="NGN"):
     return f"{currency} {amount:,}"
print(format_price(5000))
print(format_price(200, "GHS"))
def analyize_scores(scores):
       lowest = min(scores)
       highest = max(scores)
       average = sum(scores) / len(scores)
       return lowest,highest,average
scores =  [55, 72, 88, 61, 94, 47, 79]
low, high, aver = analyize_scores (scores)
print(f"lowest: {low}, highest: {high}, average: {aver:.2f }")

 


