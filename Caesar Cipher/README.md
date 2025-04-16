# 🔐 Caesar Cipher – Python Implementation

This is a beginner-friendly Python implementation of the **Caesar Cipher**, a classic substitution cipher used historically by Julius Caesar to encrypt military messages. The script allows users to encrypt and decrypt messages interactively, with a default or custom shift value.

## ✨ Features

- Encrypt or decrypt any text
- Choose your own shift (default is 3)
- Handles both uppercase and lowercase letters
- Keeps punctuation, numbers, and spaces unchanged
- Input validation for direction and shift amount

## 🚀 How to Run

Make sure you have Python 3 installed.

1. Open a terminal or command prompt
2. Navigate to the project folder
3. Run the script:  _python caesar_cyper.py_

## 🧠 How It Works

Each letter in the text is shifted by a certain number of positions down the alphabet:
	•	A shift of 3 turns "A" into "D", "B" into "E", and so on.
	•	It wraps around the alphabet (e.g., "Z" with shift 1 → "A").
	•	Non-letter characters (spaces, punctuation, etc.) are preserved as-is.

## 🙌 Author

Created by **Yaser** as part of my learning journey into cryptography and cybersecurity.
