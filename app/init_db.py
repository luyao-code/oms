from app import app, db, User

app.app_context().push()
db.create_all()

""""
# Data Seeding
user1 = User(name='chen')
user2 = User(name='lu')
db.session.add_all([user1, user2])
db.session.commit()
"""

users = User.query.all()
for user in users:
    print(user.name)