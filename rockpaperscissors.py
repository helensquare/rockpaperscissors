import streamlit as st

import random

favIcons = ["🤜", "✋", "✌️"]

st.set_page_config(page_title="Rock, Paper, Scissors!", page_icon = random.choice(favIcons))

st.title("Rock, Paper, Scissors Game!")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# st.write("Choose Rock, Paper or Scissors")

# col1, col2, col3 = st.columns(3)
# 
# with col1:
    # playerRock = st.button("Rock 🪨")
# 
# with col2:
    # playerPaper = st.button("Paper 📄")
# 
# with col3:
    # playerScissors = st.button("Scissors ✂️")
# 

p1Input = st.number_input("Type 0 for Rock, 1 for Paper or 2 for Scissors.", min_value=0, max_value=2)
  

intToSymbol = [rock, paper, scissors]
p1 = intToSymbol[p1Input]

st.write(p1Input)

st.write(f"Your choice:\n {p1}")


p2Input = random.randint(0, 2)

p2 = intToSymbol[p2Input]

st.write(f"Your opponent's choice: {p2}")

if p1Input == p2Input:
    st.write("It's a tie!")

elif (p1 == rock and p2 == scissors) or (p1 == paper and p2 == rock) or (p1 == scissors and p2 == paper):
    st.success('You win!', icon="🏆")
  
else:
    st.write("You lose...")

