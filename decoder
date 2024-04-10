def decoder(num):
  decoded = ""
  try:
    for digit in num:
      if digit <= 2:
        digit += 10
      digit -= 3
      decoded = decoded + str(digit)
    decoded = int(decoded)
    return decoded 
  except:
    print("Invalid Input. Enter Intergers only.")
    return None
