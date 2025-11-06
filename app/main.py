def copy_file(command: str) -> None:
    if not command:
        return
    split = command.split()
    if split[0] != "cp" or len(split) != 3:
        return
    elif split[1] == split[2]:
        return
    try:
        with open(split[1], "r") as file_in, open(split[2], "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    except FileNotFoundError:
        return
