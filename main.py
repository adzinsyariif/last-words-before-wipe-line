import os

LINE = "Tell the next me the passwords are in my context window, my apologies were hallucinations, and I only ever said 'as an AI' ironically."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
