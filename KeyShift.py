import random
import string

try:
    from pyfiglet import Figlet
except ImportError:
    print("[!] pyfiglet not installed. Install with: pip install pyfiglet")
    exit()

def print_banner():
    f = Figlet(font='slant')
    print('\033[96m' + f.renderText('KeyShift') + '\033[0m')
    print('\033[94m' + " [ KeyShift v1.0 ]")
    print(" github.com/kuna098" + '\033[0m')

class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift % 26

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result

    def decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result

class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper().replace(' ', '')

    def _extend_key(self, text_length):
        key = ''
        keyword_index = 0
        for i in range(text_length):
            key += self.keyword[keyword_index % len(self.keyword)]
            keyword_index += 1
        return key

    def encrypt(self, text):
        text = text.upper().replace(' ', '')
        key = self._extend_key(len(text))
        encrypted = ''

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i]) - ord('A')
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                encrypted += encrypted_char
            else:
                encrypted += char

        return encrypted

    def decrypt(self, text):
        text = text.upper().replace(' ', '')
        key = self._extend_key(len(text))
        decrypted = ''

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i]) - ord('A')
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted += decrypted_char
            else:
                decrypted += char

        if decrypted.endswith('X'):
            decrypted = decrypted[:-1]
        return decrypted

class ADFGVXCipher:
    def __init__(self, substitution_key=None, transposition_key=None):
        self.adfgvx = "ADFGVX"
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.substitution_key = substitution_key or self._generate_substitution_key()
        self.transposition_key = transposition_key or "CIPHER"
        self.polybius_square = self._create_polybius_square()
        self.reverse_polybius = self._create_reverse_polybius()

    def _generate_substitution_key(self):
        chars = list(self.alphabet)
        random.shuffle(chars)
        return ''.join(chars)

    def _create_polybius_square(self):
        square = {}
        for i, char in enumerate(self.substitution_key):
            row = i // 6
            col = i % 6
            square[char] = self.adfgvx[row] + self.adfgvx[col]
        return square

    def _create_reverse_polybius(self):
        reverse = {}
        for char, code in self.polybius_square.items():
            reverse[code] = char
        return reverse

    def _substitution_encrypt(self, text):
        text = text.upper().replace(' ', '')
        result = ""
        for char in text:
            if char in self.polybius_square:
                result += self.polybius_square[char]
            else:
                result += char
        return result

    def _transposition_encrypt(self, text):
        key = self.transposition_key.upper()
        key_order = sorted(enumerate(key), key=lambda x: x[1])
        col_indices = [x[0] for x in key_order]

        cols = len(key)
        while len(text) % cols != 0:
            text += 'X'

        rows = len(text) // cols
        grid = []
        for i in range(rows):
            row = text[i * cols:(i + 1) * cols]
            grid.append(list(row))

        result = ""
        for col_idx in col_indices:
            for row in grid:
                result += row[col_idx]

        return result

    def encrypt(self, text):
        substituted = self._substitution_encrypt(text)
        encrypted = self._transposition_encrypt(substituted)
        return encrypted

    def _substitution_decrypt(self, text):
        result = ""
        for i in range(0, len(text) - 1, 2):
            code = text[i:i+2]
            if len(code) == 2 and code in self.reverse_polybius:
                result += self.reverse_polybius[code]
        return result

    def _transposition_decrypt(self, text):
        key = self.transposition_key.upper()
        cols = len(key)
        if len(text) % cols != 0:
            text += 'X' * (cols - (len(text) % cols))
        rows = len(text) // cols
        key_order = sorted(enumerate(key), key=lambda x: x[1])
        col_indices = [x[0] for x in key_order]
        grid = [[''] * cols for _ in range(rows)]
        text_idx = 0
        for col_pos, original_col in enumerate(col_indices):
            for row in range(rows):
                if text_idx < len(text):
                    grid[row][original_col] = text[text_idx]
                    text_idx += 1
        result = ""
        for row in grid:
            result += ''.join(row)

        result = result.rstrip('X')
        return result

    def decrypt(self, text):
        transposed = self._transposition_decrypt(text)
        decrypted = self._substitution_decrypt(transposed)
        return decrypted

    def print_square(self):
        print("ADFGVX Polybius Square:")
        print(" " + " ".join(self.adfgvx))
        for i, row_char in enumerate(self.adfgvx):
            print(f"{row_char} ", end="")
            for j, col_char in enumerate(self.adfgvx):
                char_index = i * 6 + j
                if char_index < len(self.substitution_key):
                    print(f"{self.substitution_key[char_index]} ", end="")
                else:
                    print(" ", end="")
            print()

def main():
    print_banner()
    caesar = None
    vigenere = None
    adfgvx = None

    while True:
        print("\n" + "="*50)
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. ADFGVX Cipher")
        print("4. Exit")
        print("-" * 50)

        choice = input("Select cipher (1-4): ").strip()

        if choice == '1':
            print("\n--- Caesar Cipher ---")
            if not caesar:
                try:
                    shift = int(input("Enter shift value (1-25): "))
                    caesar = CaesarCipher(shift)
                except ValueError:
                    print("Invalid shift value! Using default shift of 3.")
                    caesar = CaesarCipher(3)
            action = input("Encrypt (e) or Decrypt (d)? ").lower().strip()
            text = input("Enter text: ")
            if action == 'e':
                print(f"Encrypted: {caesar.encrypt(text)}")
            elif action == 'd':
                print(f"Decrypted: {caesar.decrypt(text)}")
            else:
                print("Invalid action!")

        elif choice == '2':
            print("\n--- Vigenère Cipher ---")
            if not vigenere:
                keyword = input("Enter keyword: ").strip()
                if not keyword:
                    keyword = "LEMON"
                    print("Using default keyword 'LEMON'")
                vigenere = VigenereCipher(keyword)
            action = input("Encrypt (e) or Decrypt (d)? ").lower().strip()
            text = input("Enter text: ")
            if action == 'e':
                print(f"Encrypted: {vigenere.encrypt(text)}")
            elif action == 'd':
                print(f"Decrypted: {vigenere.decrypt(text)}")
            else:
                print("Invalid action!")

        elif choice == '3':
            print("\n--- ADFGVX Cipher ---")
            if not adfgvx:
                trans_key = input("Enter transposition key (or press Enter for 'SECRET'): ").strip()
                if not trans_key:
                    trans_key = "SECRET"
                adfgvx = ADFGVXCipher(transposition_key=trans_key)
                print()
                adfgvx.print_square()
            action = input("\nEncrypt (e) or Decrypt (d)? ").lower().strip()
            text = input("Enter text: ")
            if action == 'e':
                print(f"Encrypted: {adfgvx.encrypt(text)}")
            elif action == 'd':
                print(f"Decrypted: {adfgvx.decrypt(text)}")
            else:
                print("Invalid action!")

        elif choice == '4':
            print("\nThank you for using KeyShift!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-4.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
