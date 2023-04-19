import pandas as pd

#source: https://ftp.esat.kuleuven.be/pub/SISTA/data/mechanical/ballbeam.dat.gz
class Ballbeam:
    @staticmethod
    def loadDataFrame():
        measures = Ballbeam.loadFile()
        dataframe = pd.DataFrame(measures)
        dataframe.rename(columns={'0': 'input', '1': 'output'}, inplace=True)
        dataframe.columns = ['input', 'output']
        return dataframe


    @staticmethod
    def loadFile():
        with open('ballbeam.dat') as file:
            return [list(map(float, line.split())) for line in file]
