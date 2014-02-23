from hackkings import db
from hackkings.constants import ROLES, STATES
from hackkings.models import User,Skill,Project

# Create users
sachin = User.create("sazap10", "sazap10@gmail.com", "password", ROLES.PROPOSER)
andrew = User.create("southrop", "southrop113@gmail.com", "hunter2", ROLES.DEVELOPER)
nic = User.create("nic", "nick@gmail.com", "password", ROLES.DEVELOPER)
Ilija= User.create("Ilija", "Ilija@gmail.com", "letmein", ROLES.DEVELOPER)

# Create Skills
someSkills = ["Java", "C++","JavaScript", "C", "Python", "Web Dev"]
skillObjects = map(Skill,someSkills);
map(db.session.add, skillObjects)
db.session.commit()

# Add skills to users
map(andrew.add_skill, skillObjects)
map(nic.add_skill, skillObjects)
map(Ilija.add_skill, skillObjects)

# Create Projects
names = ["Project", "Awesome Project", "Even Awesomer Project", "Super Awesome Project", "Super Duper Awesomer Project"]
for name in names:
    project = Project(name, sachin, "An awesome project description", "9000", "0")
    project.add_skill(skillObjects[1])
    if name == "Project":
    	project.add_developer(andrew)
    if name == "Even Awesomer Project":
    	project.add_developer(andrew)
    	project.set_complete()
    db.session.add(project)
db.session.commit()
