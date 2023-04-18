import random
class muvelet:
    szam1=0
    szam2=0
    def __init__(self,szam1,szam2):
        self.szam1=szam1
        self.szam2=szam2

    def osszeadas(self):
        return self.szam1 + self.szam2
    def kivonas(self):
        return self.szam1 - self.szam2
    def szorzas(self):
        return self.szam1 * self.szam2
    def osztas(self):
        return self.szam1 / self.szam2




if __name__ == '__main__':
    #tesztelés
    q=muvelet(13,6)
    print(q.osszeadas())

    q=muvelet(13,6)
    print(q.osztas())

    q=muvelet(13,6)
    print(q.kivonas())

    q=muvelet(13,6)
    print(q.szorzas())
