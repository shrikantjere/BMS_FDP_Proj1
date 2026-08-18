def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main() -> None:
    try:
        s = input("Enter an integer: ").strip()
        n = int(s)
    except Exception:
        print("Invalid input. Please enter an integer.")
        return

    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


if __name__ == "__main__":
    main()
