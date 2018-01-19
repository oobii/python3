def main():
    print("This is a script")
    egg()


print("This line printed before one in main()")


def egg():
    print("egg")


if __name__ == "__main__":
    main()
