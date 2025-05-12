def calculate_future_value(principal, rate_percent, years):
    return principal * (1 + rate_percent / 100) ** years

def main():
    principal = 1000  # Initial investment in dollars
    rate = 3.93  # Annual interest rate in percent (as of March 3, 2025)
    years = 3  # Investment duration in years

    future_value = calculate_future_value(principal, rate, years)

    print(f"Initial amount: ${principal}")
    print(f"Interest rate: {rate}% per year")
    print(f"Amount after {years} years: ${future_value:.2f}")

if __name__ == "__main__":
    main()