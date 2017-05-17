from arff_generator import ArffFileGenerator

if __name__ == "__main__":
    print("")
    print("*** Weka ARFF File Generator ***")
    print("This app only generates numeric fields and looks for value's frequency \non a given txt files.")
    print("--------------------------------")
    print("")

    print("### RELATION ###")
    relation = input("Enter Relation Name: ")
    print("--------------------------------")
    print("")
    print("### ATTRIBUTES ###")
    print("Enter q on Attribute name to finish entering attributes")
    print("")
    attribute_list = {}
    while True:
        attr_name = input("Enter Attribute Name: ")
        if attr_name.strip() == 'q':
            break
        attr_value = input("Enter Value to Search: ")
        attribute_list[attr_name] = attr_value.strip()
        print("")
    print("--------------------------------")
    print("")
    print("### FILES ###")

    folderpath = input("Enter Folder Path for Data Files: ")

    fg = ArffFileGenerator(relation, attribute_list, folderpath)
    filename = fg.generate()
    print("")
    print("File generated successfully at : " + filename)