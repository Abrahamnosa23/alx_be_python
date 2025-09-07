#!/usr/bin/env python3
"""weather_advice.py
Ask the user about today's weather and print clothing recommendations.
"""

def get_recommendation(weather: str) -> str:
    """Return a clothing recommendation string based on `weather` input.

    Accepts the weather string, strips whitespace, and is case-insensitive.
    """
    w = weather.strip().lower()
    if w == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif w == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif w == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main() -> None:
    """Prompt the user and print the recommendation."""
    # Prompt text follows the project's instruction/example:
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip()
    print(get_recommendation(weather))

if __name__ == "__main__":
    main()
  
