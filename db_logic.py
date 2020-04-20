from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    level = Column(Integer, nullable=False, default=1)
    classes = Column(String, nullable=False)
    pvp_win = Column(Integer, default=0)
    pve_win = Column(Integer, default=0)
    loss = Column(Integer, default=0)
    exp = Column(Integer, default=0)
    gold = Column(Integer, default=10)
    hp = Column(Integer, default=5)
    strg = Column(Integer, nullable=False, default=1)
    arm = Column(Integer, nullable=False, default=1)
    luck = Column(Integer, default=0)


class Mobs(Base):
    __tablename__ = 'mobs'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    level = Column(Integer, nullable=False, default=1)
    classes = Column(String, nullable=False)
    gold = Column(Integer)
    hp = Column(Integer)
    strg = Column(Integer, nullable=False)
    arm = Column(Integer, nullable=False)
    luck = Column(Integer)
    types = Column(String, nullable=False, default='моб')


class Mini_bosses(Base):
    __tablename__ = 'mini_bosses'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    classes = Column(String, nullable=False)
    win = Column(Integer, nullable=False, default=1)
    gold = Column(Integer)
    hp = Column(Integer)
    strg = Column(Integer, nullable=False)
    arm = Column(Integer, nullable=False)
    luck = Column(Integer)
    rang = Column(Integer)
    types = Column(String, nullable=False, default='мини-босс')


class Bosses(Base):
    __tablename__ = 'bosses'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False, default=5)
    classes = Column(String, nullable=False)
    win = Column(Integer)
    gold = Column(Integer)
    hp = Column(Integer)
    strg = Column(Integer, nullable=False)
    arm = Column(Integer, nullable=False)
    luck = Column(Integer)
    rang = Column(Integer)
    types = Column(String, nullable=False, default='босс')


class Engine:  # вся логика работы с базой данных

    def __init__(self, name):  # создании базы данных и ее проименовка
        self.engine = create_engine('sqlite:///{}.db'.format(name), echo=False)
        self._session = self._get_session()
        self._create_new()

    def _get_session(self):
        Session = sessionmaker(bind=self.engine) # создание "сессии" - работа с выбранной базой
        session = Session()
        return session

    def _create_new(self):
        Base.metadata.create_all(self.engine)  # заполнение выбранной бд данными

    def reg_user(self, name, classes, hp, strg, arm, luck):  # регистрация игрока
        new_user = Users(name=name,classes=classes, hp=hp, strg=strg, arm=arm, luck=luck)
        self._session.add(new_user)
        self._session.commit()

    def find_user_name(self, name):  # Поиск имени игрока в базе
        result = self._session.query(Users.name)
        for a in result:
            if name in a:
                return True
            else:
                return False

    def print_all_user(self):
        users = self._session.query(Users)
        for a in users:
            print('id:{} - {} - Класс:{}'.format(a.id, a.name, a.classes))

    def _add_mob(self, level, classes, gold, hp, strg, arm, luck):
        new_mob = Mobs(level=level, classes=classes, gold=gold, hp=hp, strg=strg, arm=arm, luck=luck)
        self._session.add(new_mob)
        self._session.commit()

    def _add_mini_boss(self, level, classes, win, gold, hp, strg, arm, luck, rang):
        new_mini_boss = Mini_bosses(level=level, classes=classes, win=win, gold=gold, hp=hp, strg=strg, arm=arm,
                                    luck=luck, rang=rang)
        self._session.add(new_mini_boss)
        self._session.commit()

    def _add_boss(self, name, level, classes, win, gold, hp, strg, arm, luck, rang, types):
        new_boss = Bosses(name=name, level=level, classes=classes, win=win, gold=gold, hp=hp, strg=strg, arm=arm,
                                    luck=luck, rang=rang, types=types)
        self._session.add(new_boss)
        self._session.commit()


# spisok = session.query(Glads).filter(Glads.id_camera==id).all()
'''
         def add_glad(self, types, age, gender, name, nation):
        session = self._get_session()

        camera = session.query(Camera).get(Library.id_camera)

        try:
            if camera.amount <3:
                new_glad = Glads(types=types, age=age, gender=gender, name=name, nation=nation, id_camera=Library.id_camera)
                camera.amount = Camera.amount + 1
                session.add(new_glad)
                session.commit()
                session.close()
            elif camera.amount >= 3:
                Library.id_camera += 1
                camera = session.query(Camera).get(Library.id_camera)
                new_glad = Glads(types=types, age=age, gender=gender, name=name, nation=nation, id_camera=Library.id_camera)
                camera.amount = Camera.amount + 1
                session.add(new_glad)
                session.commit()
                session.close()
        except AttributeError:
            print('\nГладиатор "{} (тип:{})" не добавлен! Свободных камер нет!'.format(name, types))
            session.close()   

игроки ( Users ; атрибуты - id, name, level, classes, pvp_win, pve_win, loss, exp, gold, hp, strg, arm, luck) ; 
мобы ( Bots; атрибуты - id, level, classes, gold,  hp, strg, arm, luck) ; 
мини-боссы (Mini_bosses; атрибуты - id, name (авто-генерация при убийстве игрока), level, classes, win, gold,  hp, strg, 
arm, luck, rang);  - в БД создается при убийстве игрока, удаляется при убийстве игроком.
боссы (Bosses; атрибуты - id, name (уникальные имена), level, classes, win, gold, hp, strg, arm, luck, rang)
    
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    types = Column(String)
    age = Column(Integer, nullable=False)
    gender = Column(String)
    name = Column(String, unique=True)
    nation = Column(String)
    id_camera = Column(Integer, ForeignKey('camera.id'), default=0)
'''


# Продумать основную логику взаимодествия в игре и отобразить это на бумаге/экселе !!!!