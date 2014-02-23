from hackkings import db
from hackkings.constants import ROLES, STATES
from hackkings.models import User,Skill,Project

sachin = User("sazap10", "sazap10@gmail.com", "password", ROLES.PROPOSER, "Sachin Pande", "link", "some bio yo")
db.session.add(sachin)
andrew = User("southrop", "southrop113@gmail.com", "hunter2", ROLES.DEVELOPER, "Andrew Li", "link",  "some bio yo")
db.session.add(andrew)
nic = User("nic", "nick@gmail.com", "password", ROLES.DEVELOPER, "Nic", "link", "some bio yo")
db.session.add(nic)
Ilija= User("Ilija", "Ilija@gmail.com", "letmein", ROLES.DEVELOPER, "Ilija Radosavovic", "link", "some bio yo")
db.session.add(Ilija)
db.session.commit()
someSkills = ["java", "c++","js", "c", "python", "web dev"]
skillObjects = map(Skill,someSkills);
map(db.session.add, skillObjects)
db.session.commit()
map(andrew.add_skill, skillObjects)
map(nic.add_skill, skillObjects)
map(Ilija.add_skill, skillObjects)
names = ["Project", "Awesome project", "Even awesomer project", "Super awesome project","Super duper awesomer project"]
for name in names:
    project = Project(name, sachin, "some awesome project description", "9000", "0")
    project.add_skill(skillObjects[1])
    db.session.add(project)
db.session.commit()
