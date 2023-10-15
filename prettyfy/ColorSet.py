class ColorSet():
    WIN7_COLOR_SET = {
        "FOREGROUND": {
            "BLACK": 0x0000,
            "BLUE": 0x0001,
            "GREEN": 0x0002,
            "CYAN": 0x0003,
            "RED": 0x0004,
            "MAGENTA": 0x0005,
            "YELLOW": 0x0006,
            "WHITE": 0x0007,
            "INTENSITY": 0x0008  # foreground color is intensified.
        },

        "BACKGROUND": {
            "BLACK": 0x0000,
            "BLUE": 0x0010,
            "GREEN": 0x0020,
            "CYAN": 0x0030,
            "RED": 0x0040,
            "MAGENTA": 0x0050,
            "YELLOW": 0x0060,
            "WHITE": 0x0070,
            "INTENSITY": 0x0080  # background color is intensified.
        }

    }

    REGULAR_COLOR_SET = {
        "FOREGROUND": {
            "BLACK": "30",
            "RED": "31",
            "GREEN": "32",
            "YELLOW": "33",
            "BLUE": "34",
            "MAGENTA": "35",
            "CYAN": "36",
            "WHITE": "37",
            
            "BRIGHT_BLACK": "90",
            "BRIGHT_RED": "91",
            "BRIGHT_GREEN": "92",
            "BRIGHT_YELLOW": "93",
            "BRIGHT_BLUE": "94",
            "BRIGHT_MAGENTA": "95",
            "BRIGHT_CYAN": "96",
            "BRIGHT_WHITE": "97",
        },

        "BACKGROUND": {
            "BLACK": "40",
            "RED": "41",
            "GREEN": "42",
            "YELLOW": "43",
            "BLUE": "44",
            "MAGENTA": "45",
            "CYAN": "46",
            "WHITE": "47",

            "BRIGHT_BLACK": "100",
            "BRIGHT_RED": "101",
            "BRIGHT_GREEN": "102",
            "BRIGHT_YELLOW": "103",
            "BRIGHT_BLUE": "104",
            "BRIGHT_MAGENTA": "105",
            "BRIGHT_CYAN": "106",
            "BRIGHT_WHITE": "107",
        }


    }
