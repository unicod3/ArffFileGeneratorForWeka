#!/usr/bin/python3.5
from collections import Counter
import nltk
import os
from datetime import datetime


class ArffFileGenerator:
    def __init__(self, relation, attribute_list, folderpath):
        """
        Initiate counter and a search list from attribute list
        :param relation: Relation text for arff file
        :param attribute_list: Attribute list for arff file this is dictionary
        :param folderpath: folder path of txt files
        """
        self.relation = relation
        self.attribute_list = attribute_list
        self.folderpath = folderpath
        self.search_list = list(attribute_list.values())

        self.totalCounter = Counter()  # initiate a counter
        for w in self.search_list:  # ensure all keys are exist
            self.totalCounter[w] += 0  # fill them with zero

    def count_words(self, filename):
        """
        Count the words of given search list as attribute list
        :param filename: string name of file
        :return: Counter object
        """
        with open(os.path.join(self.folderpath, filename), encoding="utf-8") as datafile:
            data = datafile.read()
            tokens = nltk.word_tokenize(data)  # populate data with tokens

            filteredwords = [t for t in tokens if t in self.search_list]
            return Counter(filteredwords) # return the counter object of wanted list

    def create_arff(self):
        """
        Create Arff file with a timestamp
        :return: string name of file
        """
        mdate = datetime.now().strftime('%d-%m-%Y_%H_%M_%S')
        my_arff_file = os.path.join(self.folderpath, "arff_file/", mdate + ".arff")

        os.makedirs(os.path.dirname(my_arff_file), exist_ok=True)  # create folder if it does not exist
        with open(my_arff_file, mode='w', encoding='utf-8') as output:
            output.write("@relation " + self.relation + "\n")
            output.write("\n")
            for key, value in self.attribute_list.items():
                output.write("@attribute " + key + " numeric\n")

            output.write("\n")
            output.write("@data\n")
            # populate data part of the file with count of each word
            line = ','.join('{}'.format(self.totalCounter[w]) for w in self.search_list)

            output.write(line + "\n")
        return my_arff_file

    def generate(self):
        """
        Main method of this class it walks in a directory and gets txt files to process
        :return: string name of created arff file.
        """
        # get txt files from folder path
        files = [f for f in os.listdir(self.folderpath) if f.endswith(".txt")]
        for f_name in files:
            self.totalCounter += self.count_words(f_name)  # sum'em up

        arff_file = self.create_arff()  # generate file
        return arff_file


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
