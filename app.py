import streamlit as st
import ephem
from datetime import datetime as dt
from datetime import timedelta
import math

st.title("Moon phases calculator using PyEphem")
# Get the current date
date = ephem.now() # Convert to datetime object
st.write(f"Current date: {str(date).split(' ')[0]}")  # Display only the date part
# st.write(type(date))
  # Convert to ephem.Date object
# From string
# td=dt.today().utcnow()+timedelta(days=1)
# st.write(td.strftime("%Y-%m-%d %H:%M"))
# st.write("Current date:", ephem.Date(td))
# d1 = ephem.Date("2025/08/24 12:00")
# st.write("Ephem Date:", d1)
# st.write(ephem.Date(date))


def phase_id(phase, moon):
    #st.write(f"Phase: {phase:.2f}%")
    if phase < 1:
        return "New Moon","🌑"
    elif 1 <= phase < 49 and moon.elong > 0:  # elongation >0 → waxing
        return "Waxing Crescent","🌒"
    elif 49 <= phase < 52 and moon.elong > 0:
        return "First Quarter","🌓"
    elif 52 <= phase < 99 and moon.elong > 0:
        return "Waxing Gibbous", "🌔"
    elif 99 <= phase <= 100:
        return "Full Moon", "🌕"
    elif 49 <= phase < 52 and moon.elong < 0:
        return "Last Quarter", "🌗"
    elif 1 <= phase < 49 and moon.elong < 0:  # elongation <0 → waning
        return "Waning Crescent", "🌘"
    else:
        return "Waning Gibbous", "🌖"

# Calculate moon phase
moon_phase = ephem.Moon(date).phase
print(f"Moon phase: {moon_phase:.2f}% illuminated")
text,emoji=phase_id(moon_phase,ephem.Moon(date))
st.write(f"Moon phase: {text}")
st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{emoji}</h1>", unsafe_allow_html=True)
st.progress(round(moon_phase)/100)

if st.button("Next 7 days"):
    st.subheader("Next 7 days:")
    # with st.columns(7) as cols:
    cols=st.columns(7)# , gap="small",vertical_alignment="center")
    for i, col in enumerate(cols):
        next_date = dt.today().utcnow()+timedelta(days=i+1)
        moon = ephem.Moon(next_date)
        phase = moon.phase
        col.write(round(phase)/100)  # Convert phase to degrees
        text, emoji = phase_id(phase, moon)
        col.progress(round(phase)/100)
        #st.write(next_date)
        col.write(f"{next_date.strftime("%Y-%m-%d")} {text}")
        col.write(f"{emoji}")
    # for i in range(1, 8):
    #     next_date = date + i
    #     moon = ephem.Moon(next_date)
    #     phase = moon.phase
    #     text, emoji = phase_id(phase, moon)
    #     st.write(f"{next_date.datetime().strftime('%Y-%m-%d')}: {text} {emoji}")