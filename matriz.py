class Row :
    Me = None

    def __init__(self, data) :
        self.Me = [i for i in data]

    def imprime(self) :
        print(self.Me)

    def add(self, other) :
        for i in range (0, len(self.Me)) :
            self.Me[i] = self.Me[i] + other.Me[i]

    def multiply_by(self, k) :
        size = len(self.Me)
        for i in range (0, size) :
            self.Me[i] = self.Me[i] * k

    def getList(self) :
        return self.Me

class Matrix :
    Me = None

    def __init__(self, data) :
        self.Me = data
        self.imprime()

    def imprime(self) :
        for i in range (0, self.rows()) :
            print(self.Me[i])

    def exchange_rows(self, i, j) :
        tmp = self.Me[i]
        self.Me[i] = self.Me[j]
        self.Me[j] = tmp

    def at_(self, j, i) :
        return self.Me[j][i]

    def at(self, i) :
        return self.Me[i][i]

    def add_i_to_j(self, i, j, k) :
        tmp1 = Row(self.Me[i])
        tmp1.multiply_by(k)
        tmp2 = Row(self.Me[j])
        tmp2.add(tmp1)
        self.Me[j] = tmp2.getList()

    def multiply_i_row_by(self, i, k) :
        tmp = Row(self.Me[i])
        tmp.multiply_by(k)
        self.Me[i] = tmp.getList()
        
    def rows(self) :
        return len(self.Me)

    def columns(self) :
        return len(self.Me[0])
