import random

# zakodowanie wartosci na bity
def encode_binary (x, num_bits) :
  """Encode a decimal value into a binary string representation."""
  binary_string = ""
  if x < min_range or x > max_range:
    print(f"Wartosc spoza dozwolonego zakresu [{min_range},{max_range}]!")
    if x < min_range:
      return "0" * num_bits
    else:
      return "1" * num_bits

  # wielkosc pojedynczego kroku w danym zakresie
  step = (2**num_bits - 1) / (max_range - min_range)
  # x w rozwazanej skali (np. 6.5 to 65% maks wartosci) - to warunkuje dokladnosc wyniku
  scaled_x = round(x * step)
  binary_string = bin(scaled_x)[2:].zfill(num_bits)
  return binary_string

# odkodowanie wartosci z bitow
def decode_binary (binary_string, num_bits) :
  """Decode a binary string representation into a decimal value."""
  # zamiana na wartosc w systemie 10
  x = int(binary_string, 2)
  # wielkosc pojedynczego kroku w danym zakresie
  step = (2**num_bits - 1) / (max_range - min_range)
  # odkodowanie zgodnie z naszym zakresem
  x /= step
  return x

# przedział od min_range do max_range jest dozwolony do zakodowania
min_range = 0
max_range = 10

# Example usage
num_bits = 8 # Number of bits to represent x
x = 6.5 # Decimal value of x

# Encoding
binary_string = encode_binary (x, num_bits)
print (f"Binary representation of x: {binary_string}")

# Decoding
decoded_x = decode_binary (binary_string, num_bits)
print (f"Decoded value of x: {decoded_x}")