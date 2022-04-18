"""
Notes and Directions from dev (Max Heltzel, 2022):

Any data encrypted in this tool can be decrypted on another computer using the same tool or cipher.
You are able to implement a file edit command within the code if you'd like, but it is not already there.
Vigenere cipher is used to encrypt your data. To learn more on how it works, refer to the following link -
https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html
Your selected file data using is hashed using sha256 and is printed after you finish the encryption process.


Directions:

Make sure your text file data is in all caps (you can use the ".upper" command to do this if not already done).
Your key should also be in all caps (write your key down, it is not saved anywhere)



"""

#Data Encryption
import hashlib
import random
import sys
from termcolor import colored
#Vigenere Cipher and Hashing Encryption

# I used this to verify that the file input function was working
# with open(file_input, 'r') as file:
#       print(file.read())


print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Welcome to 'Ruby'! Your advanced text and number terminal encryption tool. Make sure any text file you encrypt is in all caps")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")



#mostly from codespeedy
#genKey takes the input from the user and turns it into a key which is used to encrypt the text
def genKey(string, key):
        key = list(key)
        if len(string) == len(key):
                return (key)
        else:
                for i in range(len(string) - len(key)):
                                key.append(key[i % len(key)])
        return ("".join(key))

#mostly from codespeedy
def encrypt(string, key):
        encrypt_text = []
        for i in range(len(string)):
                x = (ord(string[i]) + ord(key[i])) % 26
                x += ord('A')
                encrypt_text.append(chr(x))
        return ("".join(encrypt_text))

#mostly from codespeedy
def decrypt(encrypt_text, key):
        orig_text = []
        for i in range(len(encrypt_text)):
                x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
                x += ord('A')
                orig_text.append(chr(x))
        return ("".join(orig_text))


"""
This function takes the users data that was extracted into the 'new_txt_string' and uses the encrypt function to encrypt it
with the users chosen keyword in all caps. For another level of security, the decrypted version uses the capital letter T 
instead of spaces so it is harder for a computer to read.
"""
def runprogram():
        file_input = str(input('What file would you like to encrypt?: ')) + ".txt"
        file = open(file_input)

        #This function takes the file data and inputs it into a list which can then be encrypted using the algo (mostly from geeksforgeeks.org)
        fileopen = open(file_input, 'r')
        fileopen = file.read().replace("\n", " ")
        new_txt_string = "".join(fileopen)
        new_txt_string.upper()


        if __name__ == "__main__":
                string = new_txt_string
                keyword = input("Enter the keyword: ")
                print("  ")
                key = genKey(string, keyword)
                encrypt_text = encrypt(string, key)
                print("Encrypted message:", encrypt_text)
                print("  ")
                hash_object = hashlib.sha256(new_txt_string.encode())
                hex_dig = hash_object.hexdigest()
                print(colored("                       ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈", "blue"))
                print(colored("                      ┊   " + hex_dig + "  ┊", "blue"))
                print(colored("                      ┊                                                                     ┊   ", "blue"))
                print(colored("                      ┊  ^  Above is a sha256 hash encrypted version of your file data.  ^  ┊", "blue"))
                print(colored("                       ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈","blue"))



def print_decrypt():
        file_input = str(input('What file would you like to decrypt?: ')) + ".txt"
        print(" ")
        file = open(file_input)
        fileopen = open(file_input, 'r')
        fileopen = file.read().replace("\n", " ")
        new_txt_string = "".join(fileopen)
        string = new_txt_string
        keyword = input("Enter the keyword that you used: ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        key = genKey(string, keyword)
        encrypt_text = encrypt(string, key)
        print("Decrypted message:", decrypt(encrypt_text, key))
        print("  ")
        print("Above is your decrypted original text in all caps with the letter 'T' in replace of the spaces to mitigate bot understanding")
        print("  ")
        print(fileopen)
        print("^^ This is your original text file data ^^")
        print("  ")

antibot_veri = [837492, 289248, 398382, 839284]
value = random.randint(250, 1000)
rand_veri = random.choice(antibot_veri)
av = rand_veri + value

verification = int(input( f"To prove that you are human, please input the following phrase: '{av}'" + " -  "))

if verification == av:
        runprogram()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

else:
        print("Please input a valid response")
        sys.exit()


print(" ")
print(" ")
print("Above is your encrypted text. Would you like to decrypt it?")
decryptresponse = input("Y or N: ")
print(" ")



if decryptresponse == "Y" or "y":
        print_decrypt()

elif decryptresponse == "N" or "n":
        print("Finished")
        sys.exit()







