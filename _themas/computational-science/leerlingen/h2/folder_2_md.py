import os

output_file = "files.md"
relative_path = "leerlingen/h2/"

def folder_2_md(path, output, prefix=None):
    for file_name in os.listdir(path):
        base_name, extension = os.path.splitext(file_name)
        if prefix is None:
            prefix = extension
        file_location = relative_path + file_name
        output.write("* %s [%s](%s)\n" % (prefix, base_name, file_location))


with open("files.md", 'w+') as output:
    folder_2_md("./NetLogo_opdrachten/", output)
    output.write("\n")
    folder_2_md("./video/", output, "VID")
 
