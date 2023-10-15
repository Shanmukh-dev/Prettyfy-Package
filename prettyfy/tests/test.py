# import msvcrt

# def get_arrow_key():
#     """
#     Capture and return arrow key input.
#     """
#     while True:
#         key = msvcrt.getch()
#         if key == b'\xe0':  # Special keys like arrow keys
#             key = msvcrt.getch()
#             if key == b'H':  # Up arrow
#                 return 'Up'
#             elif key == b'P':  # Down arrow
#                 return 'Down'
#             elif key == b'M':  # Right arrow
#                 return 'Right'
#             elif key == b'K':  # Left arrow
#                 return 'Left'
#         elif key == b'\x03':  # Ctrl+C (Exit on Ctrl+C)
#             raise KeyboardInterrupt

# def main():
#     try:
#         while True:
#             key = get_arrow_key()
#             print(f"Arrow Key Pressed: {key}")
#     except KeyboardInterrupt:
#         print("Ctrl+C Pressed (Exiting)")

# if __name__ == "__main__":
#     main()

import sys

def get_arrow_key():
    while True:
        char = sys.stdin.read(1)
        if char == '\x1b':  # Check for escape key (often the start of an escape sequence)
            sequence = sys.stdin.read(2)  # Read the next two characters (e.g., '[A' for Up arrow)
            if sequence == '[A':
                return 'Up'
            elif sequence == '[B':
                return 'Down'
            elif sequence == '[C':
                return 'Right'
            elif sequence == '[D':
                return 'Left'
        elif char == '\x03':  # Ctrl+C (Exit on Ctrl+C)
            raise KeyboardInterrupt

def main():
    try:
        while True:
            key = get_arrow_key()
            print(f"Arrow Key Pressed: {key}")
    except KeyboardInterrupt:
        print("Ctrl+C Pressed (Exiting)")

if __name__ == "__main__":
    main()