filenames = ["1.doc", "1.report", "1.presentantion"]

filenames = [filename.replace('.','-')+".txt" for filename in filenames] 

print(filenames)


temperatures = [10, 12, 14]

temperatures = [str(i)+'\n' for i in temperatures]
 
file = open("file.txt", 'w')
 
file.writelines(temperatures)