def main() -> None:
    read_file_name = "classified_data.txt"
    write_file_name = "secure_vault.txt"
    data = "[CLASSIFIED] New security protocols archived\n"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")

    try:
        with open(read_file_name, "r") as read_file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = read_file.read()
            print(content)

        with open(write_file_name, "w") as write_file:
            print("SECURE PRESERVATION:")
            write_file.write(data)
            print(data, end="")

        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")

    except FileNotFoundError:
        print("ERROR: Classified vault not found.")
    except Exception as e:
        print(f"ERROR: Unexpected Error ({e})")


if __name__ == "__main__":
    main()
