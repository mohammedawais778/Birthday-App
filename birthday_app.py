import streamlit as st
import time
import random
import os

# Set page configuration
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

# Birthday message
st.title("🎉 Happy Birthday to Someone Special! 🎉")
st.markdown(
    """
    <h2 style='text-align: center; color: white;'>
        🎂 Aasiya Sanober! 🎂
    </h2>
    <p style='text-align: center; font-size: 23px; color: white;'>
        Wishing you a year filled with love, laughter, and countless successes in your medical journey! 🩺💖
    </p>
    """,
    unsafe_allow_html=True,
)

# Play Birthday Song in the Background
if os.path.exists("birthday_mp3.mp3"):
    st.markdown(
        """
        <audio autoplay loop style="display:none;">
            <source src="birthday_mp3.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning("Birthday song not found!")

# Birthday Note with Pastel Background
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding: 20px; border: 2px solid #FFD700; border-radius: 10px; background-color: #FFDEE9;">
        <h3 style="color: #4B0082;">🎉 A Special Note for You 🎉</h3>
        <p style="font-size: 18px; color: #4B0082;">
            Dear Aasiya Sanober,<br><br>
            On this special day, we celebrate the amazing person you are. Your kindness, dedication, and passion inspire everyone around you. 
            May this year bring you endless joy, success, and cherished memories.<br><br>
            Here's to a future as bright as your smile and as wonderful as your heart. Keep shining and making the world a better place!<br>
            Pehli baar banaya don't forget to give feedback 😅😅<br>
            🎂 Happy Birthday! 🎂<br><br>
            With love and best wishes,<br>
             
    </div>
    """,
    unsafe_allow_html=True,
)

# Trigger Surprise and Fun Fact actions
if st.button("Surprise 🎊"):
    st.balloons()  # Show balloons
    time.sleep(1)  # Add a delay for better effect
    st.snow()  # Simulate rose petals

if st.button("Fun Fact 🏥"):
    fun_facts = [
        "Did you know? The average human body has enough iron to make a small nail. 🧲",
        "Fun fact: Your stomach gets a new lining every 3 to 4 days to prevent it from digesting itself. 🍔",
        "Medical students are like red blood cells—they carry knowledge everywhere but are always under pressure. 🩸",
        "Did you know? The human brain generates enough electricity to power a small light bulb. 💡",
        "Fun fact: The left lung is smaller than the right lung to make room for the heart. ❤️",
        "Doctors write so many prescriptions that their handwriting is now considered a secret code. 📝",
        "Did you know? Your body has more bacteria than human cells. You’re basically a walking ecosystem! 🦠",
        "Fun fact: The average person produces enough saliva in a lifetime to fill two swimming pools. 🏊",
        "Medical school is the only place where coffee is considered a food group. ☕",
        "Did you know? The human body contains about 60,000 miles of blood vessels. That’s enough to circle the Earth twice! 🌍",
        "Fun fact: The strongest muscle in the body is the masseter (jaw muscle). So keep chewing! 😄",
        "Medical students don’t need sleep—they run on caffeine and deadlines. ⏰",
        "Did you know? Your bones are about five times stronger than steel of the same density. 🦴",
        "Fun fact: The human nose can detect over 1 trillion different scents. 👃",
        "Medical students are proof that stress can be turned into degrees. 🎓",
    ]
    st.info(random.choice(fun_facts))

# Footer
st.markdown(
    """
    <h4 style='text-align: center; color: white;'>
        🎈 Wishing you an incredible birthday and an amazing journey ahead! 🎈
    </h4>
    """,
    unsafe_allow_html=True,
)