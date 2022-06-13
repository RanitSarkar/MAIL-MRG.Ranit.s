PLACEHOLDER = "[name]"
with open(r".\Input\Names\invited_names.txt") as start:
    cont = start.readlines()
with open(r".\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in cont:
        n_name = name.strip()
        n_letter=letter_contents.replace(PLACEHOLDER, n_name)
        with open(f"letter for {n_name}", mode="w") as data:
            data.write(n_letter)