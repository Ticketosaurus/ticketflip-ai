import streamlit as st
import datetime
import matplotlib.pyplot as plt

# Sample ticket data (this would be replaced by scraped/live data)
events = [
    {
        "event": "Taylor Swift – Wembley",
        "date": "2025-08-21",
        "face_value": 110,
        "peak_price": 300,
    },
    {
        "event": "BBC Radio 1 Big Weekend",
        "date": "2025-05-25",
        "face_value": 37.50,
        "peak_price": 120,
    }
]

# Streamlit UI
st.set_page_config(page_title="TicketFlip AI – Profit Dashboard", layout="wide")
st.title("TicketFlip AI – Profit Dashboard")

for event in events:
    st.subheader(event["event"])
    st.write(f"**Date:** {event['date']}")
    st.write(f"**Face Value:** £{event['face_value']}")
    st.write(f"**Predicted Peak Price:** £{event['peak_price']}")

    profit = event["peak_price"] - event["face_value"]
    st.write(f"**Estimated Profit:** £{profit}")

    st.write("**Advice:** Sell 1 day(s) before event")

    # Simulated price growth chart
    days = [0, 1, 2, 3, 4, 5]
    prices = [
        event["face_value"] * 1.35,
        event["face_value"] * 1.5,
        event["face_value"] * 1.82,
        event["face_value"] * 2.25,
        event["face_value"] * 2.5,
        event["peak_price"],
    ]

    fig, ax = plt.subplots()
    ax.plot(days, prices, marker="o")
    ax.set_xlabel("Weeks Before Event")
    ax.set_ylabel("Resale Price (£)")
    ax.set_title("Projected Price Trend")
    st.pyplot(fig)

st.markdown("---")
st.caption("This is an early version. Data is simulated.")

# --- Optional Sidebar ---
st.sidebar.header("Filters & Tools")
show_live = st.sidebar.checkbox("Show Sample Ticket Listings", value=True)

if show_live:
    st.sidebar.markdown("### Example Listings (Simulated)")
    st.sidebar.write("**StubHub** – Taylor Swift – £295 (VIP)")
    st.sidebar.write("**Viagogo** – BBC Radio 1 – £115 (Standard)")
    st.sidebar.write("**StubHub** – Taylor Swift – £270 (Upper Tier)")

    st.sidebar.markdown("---")
    st.sidebar.markdown("More live listings coming soon...")

# --- Auto Opportunity Detector ---
st.header("Flip Recommendations")

sample_market = [
    {"event": "Taylor Swift – Wembley", "face_value": 110, "resale_price": 290},
    {"event": "BBC Radio 1 Big Weekend", "face_value": 37.5, "resale_price": 85},
    {"event": "Coldplay – Cardiff", "face_value": 95, "resale_price": 105},
    {"event": "The Killers – Manchester", "face_value": 70, "resale_price": 135},
    {"event": "Elton John – Birmingham", "face_value": 120, "resale_price": 115},  # No profit
]

profitable = [
    item for item in sample_market if item["resale_price"] > item["face_value"] * 1.2
]

if profitable:
    for item in profitable:
        profit = item["resale_price"] - item["face_value"]
        st.success(f"**{item['event']}**: Buy at £{item['face_value']} → Sell for £{item['resale_price']} → Profit: £{profit}")
else:
    st.warning("No strong flips currently detected.")