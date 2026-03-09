def main() -> None:
    filename = "ancient_fragment.txt"
    read_file = None

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {filename}")

    try:
        read_file = open(filename, "r", encoding="utf-8") #read about utf-8 and encoding
        print("Connection established...")
        print()
        content = read_file.read()
        print("RECOVERED DATA:")
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError: # ask if i should except an other errors PermissionError... ?
        print("ERROR: Storage vault not found. Run data generator first.") #check this message was asked ? 
    finally:
        if read_file:
            read_file.close()


if __name__ == "__main__":
    main()
