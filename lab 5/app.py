from utils import process_item

while True:
    x = input()
    if x == 'q':
        break
    x = int(x)
    print(process_item(x))
