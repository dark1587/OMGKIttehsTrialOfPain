import sys

def read_all_the_lines(filename, length):
  try:
    with open(filename, "r") as f:

      lines = f.readlines()
      last_lines = lines[-length:]
    return last_lines
  except FileNotFoundError:
    print("File not found.")
    sys.exit(1)


if __name__ == "__main__":
  try:
    filename = sys.argv[1]
  except IndexError:
    print("Please provide a filename.")
    sys.exit(1)
  try:
    length = int(sys.argv[2])
  except (IndexError, ValueError):
    print("Invalid Length parameter. Using 10 as default.")
    length = 10


  results = read_all_the_lines(filename, length)

  for result in results:
    print(result.strip())
