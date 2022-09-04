from models import Users, session, engine

db_session = session(bind=engine)

x = {
    'test' : 1579,
    'tesst' : 2849
}

account = Users(
    id = 7,
    cookie = 'cookielol',
    json = dict(x)
)

#db_session.add(account)
#db_session.commit()

user = db_session.query(Users).get({'id' : 1})
print(user)
#print(user.id)