
import streamlit as st
import matplotlib.pyplot as plt

# Sample ticket data
events = [
    {
        "name": "Taylor Swift – Wembley",
        "date": "2025-08-21",
        "face_value": 110,
        "resale_prices": [150, 175, 200, 250, 275, 300],
    },
    {
        "name": "BBC Radio 1 Big Weekend",
        "date": "2025-05-25",
        "face_value": 37.5,
        "resale_prices": [60, 70, 85, 100, 110, 120],
    }
]

def analyze_event(event):
    prices = event["resale_prices"]
    face_value = event["face_value"]
    peak_price = max(prices)
    profit = peak_price - face_value
    optimal_day = prices.index(peak_price)
    return {
        "peak_price": peak_price,
        "estimated_profit": profit,
        "sell_advice": f"Sell {len(prices) - optimal_day} day(s) before event"
    }

# Streamlit UI
st.title("TicketFlip AI – Profit Dashboard")

for event in events:
    st.subheader(event["name"])
    st.write(f"Date: {event['date']}")
    st.write(f"Face Value: £{event['face_value']}")
    result = analyze_event(event)
    st.write(f"**Predicted Peak Price:** £{result['peak_price']}")
    st.write(f"**Estimated Profit:** £{result['estimated_profit']}")
    st.write(f"**Advice:** {result['sell_advice']}")
    st.line_chart(event["resale_prices"])
    st.markdown("---")
