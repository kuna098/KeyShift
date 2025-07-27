# KeyShift

**KeyShift** is a Python-based command-line tool for encrypting and decrypting text using classic ciphers: Caesar, Vigenère, and ADFGVX. It's simple, extensible, and built for learning, experimenting, or basic encryption needs.

---

## 🔐 Features

* Caesar Cipher (configurable shift)
* Vigenère Cipher (custom keyword)
* ADFGVX Cipher (random Polybius square & transposition)
* Terminal-based interactive UI
* Stylized ASCII banner with version info

---

## 🚀 Installation

```bash
git clone https://github.com/kuna098/KeyShift.git
cd KeyShift
pip install pyfiglet
```

---

## 🧪 Usage

Run the tool using Python:

```bash
python KeyShift.py
```

You'll be prompted to:

* Choose a cipher (Caesar, Vigenère, ADFGVX)
* Choose to encrypt or decrypt
* Enter your input text

### Example Output:

```bash
Select cipher (1-4): 1
--- Caesar Cipher ---
Encrypt (e) or Decrypt (d)? e
Enter text: hello world
Encrypted: khoor zruog
```

---

## 📂 Project Structure

```
KeyShift/
├── encrypt.py      # Main CLI tool
├── README.md       # You're reading it
```

---

## 🛠 Dependencies

* Python 3.x
* [pyfiglet](https://pypi.org/project/pyfiglet/) (for the banner)

Install with:

```bash
pip install pyfiglet
```

---

## 🧠 Cipher Overview

* **Caesar Cipher**: Shifts each character by a fixed number.
* **Vigenère Cipher**: Uses a keyword to apply multiple Caesar shifts.
* **ADFGVX Cipher**: Combines a Polybius square substitution with columnar transposition.

---

## 🤝 Contributing

Pull requests and issues are welcome. Feel free to fork and improve it.

---

## 📄 License

MIT License

---

## 🔗 Author

Made with ❤️ by [@kuna098](https://github.com/kuna098)
