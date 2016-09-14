#!/usr/bin/python3

# http://serverfault.com/questions/330069/how-to-create-an-sha-512-hashed-password-for-shadow
# http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
# http://stackoverflow.com/questions/9079036/detect-python-version-at-runtime
# http://security.stackexchange.com/questions/51959/why-are-salted-hashes-more-secure-for-password-storage
# https://pymotw.com/2/getpass/
# https://docs.python.org/2/library/crypt.html

import crypt
import getpass
import random
import string
import sys

if sys.version_info[0] < 3:
  print("Must be using Python 3")
  quit()

pwlength = 14
plainpass1 = getpass.getpass(prompt='Specify new Password: ')
plainpass2 = getpass.getpass(prompt='Verify new Password:  ')

if (not plainpass1) and (not plainpass2):
  print("Got an empty input. Generating random password...")
  plainpass2 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(pwlength)); plainpass1 = plainpass2
  print("\nRandom Password:")
  print(plainpass2)
  print()

if plainpass1 == plainpass2:
  print("Salted SHA512 hash:")
  print(crypt.crypt(plainpass2, crypt.mksalt(crypt.METHOD_SHA512)))
  print()
else:
  print("Password does not match. Please try again.")
