import time
import random

def get_random_sentence():
    # Replace this function with your own logic to get sentences
    sentences = ["The quick brown fox jumps over the lazy dog.",
                 "Programming is fun and rewarding.",
                 "Practice makes perfect."]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_words):
    minutes = (end_time - start_time) / 60
    words_per_minute = len(typed_words) / minutes
    return words_per_minute

def main():
    print("Welcome to the Typing Speed Calculator!")
    
    input("Press Enter to start typing...")

    sentence_to_type = get_random_sentence()
    print(f"\nType the following:\n'{sentence_to_type}'")

    start_time = time.time()
    user_input = input("Your typing: ")
    end_time = time.time()

    typed_words = user_input.split()
    speed = calculate_typing_speed(start_time, end_time, typed_words)

    print(f"\nYour typing speed: {speed:.2f} words per minute")

    # Additional feedback logic can be added based on accuracy, errors, etc.

if __name__ == "__main__":
    main()

