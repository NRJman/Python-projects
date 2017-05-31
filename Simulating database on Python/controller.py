import pickle


class MyData:

    def __init__(self):
        try:
            self.ever = {}
            self.file1 = open("fac.pkl", "rb")
            self.file2 = open("grp.pkl", "rb")
            self.faculties = pickle.load(self.file1)
            self.groups = pickle.load(self.file2)
            self.ever['faculties'] = self.faculties
            self.ever['groups'] = self.groups
            self.n = len(self.groups)
            self.file1.close()
            self.file2.close()
        except:
            self.n = 1
            self.faculties = {}
            self.groups = {}
            self.ever = {}
            self.ever['faculties'] = self.faculties
            self.ever['groups'] = self.groups
        #self.faculties = self.ever['faculties']
        #self.groups = self.ever['groups']

    def exit(self):
            self.file1 = open("fac.pkl", "wb")
            self.file2 = open("grp.pkl", "wb")
            pickle.dump(self.ever['faculties'], self.file1)
            pickle.dump(self.ever['groups'], self.file2)
            self.file1.close()
            self.file2.close()

    def newfac(self):
        print('Write the name of new faculty.')
        name = str(input())
        self.faculties[self.n] = name
        self.n += 1
        print('There must be at least one group.')
        print('Write the number of groups you wanna see there, now!')
        num = int(input())
        self.newnum(name, num)

    def newnum(self, name, num):
        self.groups[name] = num

    def delfac(self, name):
        for k, v in list(self.faculties.items()):
            if name == v or isinstance(v, list) and name in v:
                del self.faculties[k]
        self.delnum(name)

    def delnum(self, name):
        try:
            del self.groups[name]
        except KeyError:
            print('Man, I need to know faculty in order to delete the number of groups. You wrote the wrong faculty!')

    def changenum(self, name, newnum):
        if name in self.groups:
            self.groups[name] = newnum
        else:
            print('Bro, I don`t see there this faculty')

    def changefac(self, name, newname):
        for key, val in list(self.faculties.items()):
            if val == name:
                self.faculties[key] = newname
            else:
                print('I don`t see this faculty in database. Maybe you see it?')
