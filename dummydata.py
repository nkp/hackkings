from hackkings import db
from hackkings.constants import ROLES, STATES
from hackkings.models import User,Skill,Project

sachin = User("sazap10", "sazap10@gmail.com", "Sachin Pande", "link", ROLES.PROPOSER , "some bio yo")
db.session.add(sachin)
andrew = User("southrop", "southrop113@gmail.com", "Andrew Li", "link", ROLES.DEVELOPER , "some bio yo")
db.session.add(andrew)
nic = User("nic", "nick@gmail.com", "Nic", "link", ROLES.DEVELOPER , "some bio yo")
db.session.add(nic)
Ilija= User("Ilija", "Ilija@gmail.com", "Ilija Radosavovic", "link", ROLES.DEVELOPER , "some bio yo")
db.session.add(Ilija)
db.session.commit()
someSkills = ["java", "c++","js", "c", "python", "web dev"]
skillObjects = map(Skill,someSkills);
map(db.session.add, skillObjects)
db.session.commit()
map(andrew.add_skill, skillObjects)
map(nic.add_skill, skillObjects)
map(Ilija.add_skill, skillObjects)
names = ["project", "awesome project", "even awesomer project", "super awesome project","super duper awesomer project"]
for name in names:
    project = Project(name, False, STATES.ONGOING, sachin, "some awesome project description", "9000", "0")
    db.session.add(project)
db.session.commit()