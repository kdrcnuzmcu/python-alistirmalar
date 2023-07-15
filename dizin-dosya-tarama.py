from os import walk


def names_of_files_in_folder(path=".", extract=False):
    """
    This function brings the names of files and folders.
    Parameters
    ----------
    path: string
        The path of the folder.
    extract: bool
        Default value is False, when extract is True the names of your want will be extracted to a text file.

    Returns
    -------
    list, list
    """

    names = walk(path).__next__()
    folders = names[1]
    files = names[2]

    if extract:
        with open("./File-Folder-Names.txt", "a") as output_file:
            output_file.write("\n---FOLDERS--- \n\n")
            for name in folders:
                output_file.writelines(f"{name}\n")
            output_file.write("\n---FILES--- \n\n")
            for name in files:
                output_file.writelines(f"{name}\n")
        output_file.close()

    return folders, files


names_of_files_in_folder(extract=True)
