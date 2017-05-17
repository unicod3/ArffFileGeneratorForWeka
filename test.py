from arff_generator import ArffFileGenerator

relation = 'yazarlar'
attribute_list = {'virgul': ',', 'nokta': '.', 've_baglaci': 've'}
folderpath = 'yazarlar'

fg = ArffFileGenerator(relation, attribute_list, folderpath)
filename = fg.generate()
print("File generated successfully at : " + filename)