class TempoEntity():
    def __init__(self, data, probabilidade, precipitacao, max_temp, min_temp, cidade):
        self.__data = data
        self.__probabilidade = probabilidade
        self.__precipitacao = precipitacao
        self.__max_temp = max_temp
        self.__min_temp = min_temp
        self.__cidade = cidade


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def probabilidade(self):
        return self.__probabilidade

    @probabilidade.setter
    def probabilidade(self, probabilidade):
        self.__probabilidade = probabilidade

    @property
    def precipitacao(self):
        return self.__precipitacao

    @precipitacao.setter
    def precipitacao(self, precipitacao):
        self.__precipitacao = precipitacao

    @property
    def max_temp(self):
        return self.__max_temp

    @max_temp.setter
    def max_temp(self, max_temp):
        self.__max_temp = max_temp

    @property
    def min_temp(self):
        return self.__min_temp

    @min_temp.setter
    def min_temp(self, min_temp):
        self.__min_temp = min_temp

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
