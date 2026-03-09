def main() -> None:
    file_name = "new_discovery.txt"
    write_file = None
    data = ("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n"
            )
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print(f"Initializing new storage unit: {file_name}")

    try:
        write_file = open(file_name, "w", encoding="utf-8")
        print("Storage unit created successfully...")
        print()
        print("Inscribing preservation data...")
        write_file.write(data)
        print(data)
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except PermissionError: #test this permition error that will raise or not if not change it to FileNotFoundError
        print("ERROR: Permission denied. Cannot create archive.")
    except Exception as e:
        print(f"Error: Unexpected Error ({e})")
    finally:
        if write_file:
            write_file.close()


if __name__ == "__main__":
    main()
