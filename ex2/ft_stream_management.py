import sys


def main() -> None:
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")
        print()
        if not archivist_id and not status_report:
            print("Error: No Archivist ID And No Status Report Provided !!!")
            return
        if not archivist_id:
            print("Error: No Archivist ID Provided !!!")
            return
        if not status_report:
            print("Error: No Status Report Provided !!!")
            return
        print(f"[STANDARD] Archive status from {archivist_id}: "
              f"{status_report}", file=sys.stdout)
        print("[ALERT] System diagnostic: Communication "
              "channels verified", file=sys.stderr)
        print("[STANDARD] Data transmission complete", file=sys.stdout)
        print()
        print("Three-channel communication test successful.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
