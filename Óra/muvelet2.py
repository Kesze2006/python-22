import gyakorlas0418 as m

class muv(m.muvelet):
    def __inint__(self,szam1,szam2):
        super().__init__(szam1,szam2)

    def p(self):
        return super().osszeadas()



w=m.muvelet(12,13)
print(w.osszeadas())

e=muv(12,13)
print(e.p())
