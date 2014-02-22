userprojectlink = db.Table('userprojectlink',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

skill_projects_link = db.Table('skill_project_link',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

skill_users_link = db.Table('skill_user_link',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)