import sys
import os

def safe_exec():
    args = sys.argv
    filePath = args[-1]
    if "safe_exec" in args:
        if os.path.exists(filePath):
            with open(filePath) as f:
                contents = f.read()
                try:
                    exec(contents)
                except Exception as e:
                    print(f"Error: {e}")
                    print(f"Error type: {type(e).__name__}")

                    tb = e.__traceback__
                    while tb.tb_next:
                        tb = tb.tb_next
                    print(f"Error at line: {tb.tb_lineno}")
    else:
        pass