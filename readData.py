import csv
class ReadData:
    
    def __init__(self, file):
        self.file = file
    
    '''
    This method reads the data and returns an array of data 
    @return 2D array
    '''
    def read(self):
        
        s = []
        with open(self.file, 'r') as csvfile:
            csv_object = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csv_object:
                t = []
                t.append(row[0])
                t.append(row[1])
                s.append(t)
        s.pop(0)
        k = []
        for lst in s:
            c = [float(i) for i in lst]
            k.append(c)
        return (k)
    

## Test the class
# r = ReadData('exercise-1.csv')
# data = r.read()
# print (data)
