def copy_file(command: str) -> None:
    if not command:
        return
    split = command.split()
    if split[0] != "cp" or len(split) != 3:
        return
    source_file = split[1]
    destination_file = split[2]
    if source_file == destination_file:
        return
    try:
        with open(source_file , "r") as file_in, open(destination_file, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    except FileNotFoundError:
        return
