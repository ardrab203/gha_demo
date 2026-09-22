from app.calculator import add, divide


def main() -> None:
    print("GitHub Actions demo app")
    print("2 + 3 =", add(2, 3))
    print("10 / 4 =", divide(10, 4))


if __name__ == "__main__":
    main()
