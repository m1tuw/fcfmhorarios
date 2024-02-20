from important_stuff import *
from solver import *
from solverFindCourse import *

db = Database()
db.load()

sch = Schedule()
sch.add_course(db.searchWithSection("CC3101-2"))
sch.add_course(db.searchWithSection("CC3501-2"))
sch.add_course(db.searchWithSection("MA3403-1"))
sch.add_course(db.searchWithSection("MA3711-1"))

memes = db.searchWithSection("CC3002-2")

memes.printCourse()
sch.printSchedule()

print(sch.check_clash(memes))

