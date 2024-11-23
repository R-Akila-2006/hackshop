import streamlit as st
import random

st.title("Guessing Game: You vs Machine!")
st.markdown("In this game, both you and the machine try to guess a number between 1 and 100.")


target_number = random.randint(1, 100)
user_guess = st.number_input("Guess the number (between 1 and 100):", min_value=1, max_value=100, step=1)

if user_guess:
    if user_guess < target_number:
        st.write("Your guess is too low. Try again!")
    elif user_guess > target_number:
        st.write("Your guess is too high. Try again!")
    else:
        st.write("Congratulations! You guessed the number correctly!")


st.subheader("Now it's time for the machine to guess the number!")
low, high = 1, 100
machine_guess = None
attempts = 0

def machine_guesses():
    global low, high, attempts, machine_guess
    machine_guess = (low + high) // 2
    attempts += 1

    if machine_guess < target_number:
        low = machine_guess + 1
        st.write(f"Machine guessed {machine_guess}. Too low! The range is now {low}-{high}.")
    elif machine_guess > target_number:
        high = machine_guess - 1
        st.write(f"Machine guessed {machine_guess}. Too high! The range is now {low}-{high}.")
    else:
        st.write(f"Machine guessed {machine_guess}. The machine got it right in {attempts} attempts!")


if st.button("Let the machine guess"):
    while machine_guess != target_number:
        machine_guesses()
