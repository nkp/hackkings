from hackkings import db
from hackkings.constants import ROLES, STATES
from hackkings.models import User,Skill,Project

# Create users
sachin = User.create("sazap10", "sazap10@gmail.com", "password", ROLES.PROPOSER)
andrew = User.create("southrop", "southrop113@gmail.com", "hunter2", ROLES.DEVELOPER)
nic = User.create("nic", "nick@gmail.com", "password", ROLES.DEVELOPER)
Ilija= User.create("Ilija", "Ilija@gmail.com", "letmein", ROLES.DEVELOPER)
Microsoft=User.create("Microsoft", "windows@hotmail.com", "apple", ROLES.PROPOSER)
Microsoft.set_bio("Whether you are creating new code, algorithms or data structures, you are the link between abstract concepts and the technology products used daily by your friends, family and millions of other people around the world. While working on our projects you will improve your technical skills and develop next-generation software!")

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
    project = Project(name, sachin, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eleifend tellus a tortor consequat, sit amet hendrerit massa hendrerit. Mauris nec lacus tortor. Praesent dictum erat at tortor varius gravida. Nulla ac orci eu risus pretium pulvinar. Nam vitae odio orci. Donec elit eros, hendrerit at diam id, eleifend placerat augue. Pellentesque sapien leo, imperdiet eget augue eu, adipiscing placerat urna. Maecenas diam ante, sodales non rhoncus eget, dictum sed libero.", "9000", "0")
    project.add_skill(skillObjects[1])
    if name == "Project":
    	project.add_developer(andrew)
    if name == "Even Awesomer Project":
    	project.add_developer(andrew)
    	project.set_complete()
    db.session.add(project)
db.session.commit()

project = Project("Spreadsheet", Microsoft, "Implement a spreadsheet for entering, modeling and viewing numerical data. Spreadsheet needs to have the ability to represent and evaluate symbolic expressions which are stored in, and can refer to other, cells. Cells are reffered to by a combination of their column and row names. Each cell can contain some text, reffered to as the cell's expression. A user can edit the expression in any cell, and when editing is finished, the expression is interpreted by the cell to produce the value which the cell displays. Feel free to design and structure your classes as you like, however, you may find an attached suggested design useful.", "20", "7")
project.add_skill(skillObjects[0])
db.session.commit()
