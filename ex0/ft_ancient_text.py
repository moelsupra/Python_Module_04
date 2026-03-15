def main() -> None:
    filename = "ancient_fragment.txt"
    read_file = None

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {filename}")

    try:
        read_file = open(filename, "r")
        print("Connection established...")
        print()
        content = read_file.read()
        print("RECOVERED DATA:")
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if read_file:
            read_file.close()


if __name__ == "__main__":
    main()
