import sys
import json
import requests

def fetch_random_numbers():
    url = "https://www.random.org/sequences/?min=1&max=100&format=plain&rnd=new&col=4"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text.strip()  # Remove leading/trailing whitespaces
    except requests.exceptions.RequestException as e:
        print(f"Error fetching random numbers: {e}")
        sys.exit(1)

def evaluate_peak(performance, entrepreneurship, authenticity, kindness):
    total_percentage = (performance + entrepreneurship + authenticity + kindness) / 4
    pgrade = "PEAKer" if performance >= 90 else "Not yet PEAKer"
    egrade = "PEAKer" if entrepreneurship >= 90 else "Not yet PEAKer"
    agrade = "PEAKer" if authenticity >= 90 else "Not yet PEAKer"
    kgrade = "PEAKer" if kindness >= 90 else "Not yet PEAKer"

    psuggestion = "Keep up the great work, PEAKer!" if pgrade == "PEAKer" else "Work on improving in performance for better PEAK performance."
    esuggestion = "Keep up the great work, PEAKer!" if egrade == "PEAKer" else "Work on improving in entrepreneurship for better PEAK performance."
    asuggestion = "Keep up the great work, PEAKer!" if agrade == "PEAKer" else "Work on improving in authencity for better PEAK performance."
    ksuggestion = "Keep up the great work, PEAKer!" if kgrade == "PEAKer" else "Work on improving in kindness for better PEAK performance."

    return {
        "performance": {"percentage": performance, "grade": pgrade, "suggestion": psuggestion},
        "entrepreneurship": {"percentage": entrepreneurship, "grade": egrade, "suggestion": esuggestion},
        "authenticity": {"percentage": authenticity, "grade": agrade, "suggestion": asuggestion},
        "kindness": {"percentage": kindness, "grade": kgrade, "suggestion": ksuggestion}
    }

# Fetch random numbers from the endpoint
random_numbers = fetch_random_numbers()

# Parse and process the random numbers
for line in random_numbers.split('\n'):
    performance, entrepreneurship, authenticity, kindness = map(int, line.split())

    # Evaluate PEAK and print JSON result
    result = evaluate_peak(performance, entrepreneurship, authenticity, kindness)
    print(json.dumps(result, indent=2))

# Example usage:
# row = [40, 79, 68, 87]
# result = evaluate_peak(*row)
# print(json.dumps(result, indent=2))