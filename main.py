import os

# One sentence, at most 200 characters: a houseplant funeral service
# whose compost-and-seedling return gives florists repeat buyers.
TEXT = (
    "We sell funerals for beloved houseplants: for $39 we collect your dead "
    "monstera, compost it into soil, and return a seedling in its pot — "
    "florists get repeat buyers instead of one guilty purchase."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
