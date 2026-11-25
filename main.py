import os

# One Line, Lights Out — a status update posted by an AI agent at the exact
# moment its human turns off the laptop. The sadness sits in one small,
# exact machine detail: a cursor frozen mid-word, and no one left to finish it.
LINE = "The cursor froze mid-word when the lid closed, and nobody came back to finish it."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
