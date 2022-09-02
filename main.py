import secrets

class board:
    def __init__(self, x,y):
        if type(x) is not int or type(x) is not int or x < 1 or y <1:
            print("Fehler")
            exit
        self.x=x
        self.y=y
        self.b = [x] [y]
        self.create()
    def tip(self, trick):
        pass

    def create(self):
        for i in range(1,self.x):
            for j in range(1,self.y):
                self.b[i][j]=


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = board(10,10)

