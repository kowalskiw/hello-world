import csv


class ChosenOne:
    def __init__(self, p):
        file = open(p, 'r')
        self.month = csv.DictReader(file)
        self.sd = {}

    def get_my_row(self):
        for row in self.month:
            self.sd = dict(row)
            if self.sd['Nazwisko'] == 'Kowalski':
                break
        return self.sd

    def wolne(self):
        free = []
        for i in self.sd:
            if self.sd[i] == "":
                free.append(i)
        return free


class Changes:
    def __init__(self, p1, p2, p3, cls):
        self.months = []
        self.months.append(csv.DictReader(open(p1)))
        self.months.append(csv.DictReader(open(p2)))
        self.months.append(csv.DictReader(open(p3)))
        self.my_row = cls
        self.day = 8  # int(input("insert the day when you wanna make some change: "))

    def find_cng(self):
        chgs_list = []
        if self.my_row[str(self.day)] == 'O':
            for i in self.months:
                for row in i:
                    if row[str(self.day)] == '' and row[str(self.day-1)] == '' and row[str(self.day+1)] != 'O':
                        chgs_list.append(row['Nazwisko'] + " " + row['Imię'])
        elif self.my_row[str(self.day)] != ('O', ''):
            for i in self.months:
                for row in i:
                    if row[str(self.day)] == '' and row[str(self.day - 1)] == ('O' or '') and row[str(self.day + 1)] == '':
                        chgs_list.append(row['Nazwisko'] + " " + row['Imię'])
        return chgs_list


pth1 = "C:\pliki_py\czerwiec_1.csv"
pth2 = "C:\pliki_py\czerwiec_2.csv"
pth3 = "C:\pliki_py\czerwiec_3.csv"
me = ChosenOne(pth1)
my_chgs = Changes(pth1, pth2, pth3, me.get_my_row())
ex_list = my_chgs.find_cng()
print("your free days: ", *me.wolne())
print("you can make {} change with: {}".format(len(ex_list), ex_list))
