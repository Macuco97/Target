def fibonacci_sequence(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        if a == n:
            print(f"{n} pertence à sequência de Fibonacci.")
            return
    print(f"{n} não pertence à sequência de Fibonacci.")

quantidade = input("Escolha quantos números você deseja na sequência de fibonacci")
quantidade = int(quantidade)
fibonacci_sequence(quantidade)
