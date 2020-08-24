class Virus():
    def __init__(self, GenDays: int = 10, StartNum: int = 1):
        self.GenDays = GenDays
        self.StartNum = StartNum

    def Run(self):
        if self.GenDays <= int(100000):
            self.Ks = self.StartNum * 2 ** (self.GenDays - 1)
            self.Smittad = 2 ** (self.GenDays)

            self.Totalt = 2 ** (self.GenDays + 1) - 1

            self.ReturnToUser = self.Totalt

            return self.ReturnToUser
        else:
            return("You need to modifie the code at own riskt to rune this big of a number")
