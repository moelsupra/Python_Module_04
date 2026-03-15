def crisis_handler(file_name: str, routine: bool = False) -> None:
    if routine:
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        with open(file_name, "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - {data.strip()}")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly ({e})")
        print("STATUS: Crisis handled, damage contained\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt", routine=True)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
