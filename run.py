import Virus

Test = Virus.Virus(10)

f = open("numbers.txt", "a")
f.truncate(0)

f.write(str(Test.Run()))
f.close()
