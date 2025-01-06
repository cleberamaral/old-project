
#contents = ["Content 1111" , "Content 2222" , "Content 333333"]
#filenames = ["file 1.txt", "file 2.txt", "file 3.txt"]

#for contents , filenames in zip(contents,filenames) :
#    file = open(f"Files/{filenames}",'w')
#    file.write(contents)


countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for filename, countries in zip(countries,countries):
    file = open(f"{filename}.txt" , 'w')
    file.write(countries)
file.close()