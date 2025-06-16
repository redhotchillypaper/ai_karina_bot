import os
import time

matrix = [['r','n','r','o','o'],
          ['u','p','a','m','s'],
          ['s','i','s','a','h'],
          ['l','d','a','n','o'],
          ['a','o','r','l','k']]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    for i in range(len(matrix)):          # рядки
        for j in range(len(matrix[0])):      # стовпці
            clear()
            # Друк пробілів і нових рядків, щоб поставити літеру на місце
            print("\n" * j + "  " * i + matrix[j][i])
            time.sleep(0.5)

if __name__ == "__main__":
    main()
