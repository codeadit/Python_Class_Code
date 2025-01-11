def shiftletter(letter, shift):
  if letter.isupper():
    return chr(((ord(letter) + shift - ord("A")) % 26) + ord("A"))
  elif letter.islower():
    return chr(((ord(letter) + shift - ord("a")) % 26) + ord("a"))
  else:
    return letter

def encrypting(phrase, shift):
  encrypt = ""
  for i in phrase:
    encrypt += shiftletter(i, shift)
  return encrypt

def fancy(phrase, codeword):
  for i in range(26):
    p_msg = encrypting(phrase, -int(i))
    if codeword in p_msg:
      print("Here is the shift value: " + str(i))
      print("Here is the shifted phrase: " + str(p_msg))

def vigenere(phrase, codeword, dir):
  codewordindex = 0
  messageindex = 0
  encryptedmessage = ""
  for i in phrase:
    if i.isalpha():
      shift = ord(codeword[codewordindex % len(codeword)]) - ord("a")
      encryptedmessage += shiftletter(i, shift * dir)
      messageindex += 1
      codewordindex += 1
    else:
      encryptedmessage += i
      messageindex += 1
  return encryptedmessage

cipher = input("What cipher do you want to select Vigenere or Ceasar." +
               " Please type C for Ceasar and V for Vigenere: ")
phrase = input("Type a phrase: ")
encryption = input("Do you want to decode or encode your your code." +
                   "Type D for decode and E for encode: ")

if cipher == "C":
  if encryption == "E":
    shift = int(input("How much do you want to shift the letter by: "))
    print(encrypting(phrase, shift))
  elif encryption == "D":
    decodefancy = input("Do want to decrypt the code fancily. Y or N: ")
    if decodefancy == "Y":
      codeword = str(input("Enter a word in the encrypted phrase: "))
      fancy(phrase, codeword)
    elif decodefancy == "N":
      shift = int(input("How much do you want to shift the letter by: "))
      print(encrypting(phrase, -shift))

if cipher == "V":
  codeword = input("What is your code word to encrypt or decrypt: ")
  if encryption == "E":
    dir = 1
    print(vigenere(phrase, codeword, dir))
  elif encryption == "D":
    dir = -1
    print(vigenere(phrase, codeword, dir))