# Task 1

class Artist:
    def __init__(self, name: str):
        self.name = name
        self.albums = {}

    def create_album(self, name):   # -> Type[Album]
        album = Album(name, self)
        self.albums[album] = []
        return album


class Album:
    def __init__(self, name: str, artist: 'Artist'):
        self.name = name
        self.artist = artist
        self.songs = []

    def create_song(self, name: str):
        song = Song(name, self, self.artist)
        self.songs.append(song)
        self.artist.albums[self].append(song)
        return song


class Song:
    def __init__(self, name: str, album: 'Album', artist: 'Artist'):
        self.name = name
        self.artist = artist
        self.album = album


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: 'Song'):
        self.songs.append(song)


slim = Artist('Eminem')
superfast = slim.create_album('Superfast')
superman = superfast.create_song('Superman')
afraid = superfast.create_song('Not Afraid')
# print(superfast.songs)
# for song in superfast.songs:
#     print(song.name)
bijon = Artist('Beyonce')
trip = bijon.create_album('Trip to 2000')
diva = trip.create_song('Diva')
# print('------')
#
# print(diva.name)
# print('------')

topsongs = Playlist('Top Songs')
topsongs.add_song(superman)
topsongs.add_song(afraid)
topsongs.add_song(diva)
# print('------')
# print('Tophit playlist:')
# for hit in topsongs.songs:
#     print(hit.name)
# print('-----')
# print(slim.albums)

# Task 2


class UsernameExists(Exception):
    def __init__(self, username):
        self.username = username
        self.message = f'Username {self.username} already exists!'
        super().__init__(self.message)


class AgeNotPositive(Exception):
    def __init__(self, age):
        self.age = age
        self.message = 'Age is not positive value!'
        super().__init__(self.message)


class UserIsUnderage(Exception):
    def __init__(self, age):
        self.age = age
        self.message = 'User is under 16!'
        super().__init__(self.message)


class InvalidMail(Exception):
    def __init__(self, mail):
        self.mail = mail
        self.message = 'Your mail is invalid. Use name@domain structure!'
        super().__init__(self.message)


data = [('miciorro', 'miciorro@op.pl', 18),
        ('kwaszonek', 'kwaszonek@cos.com', -1),
        ('myszka', 'myszka@', 20),
        ('miciorro', 'miciorro@gowno.com', 20),
        ('zabcia', 'zabcia@onet.pl', 20),
        ('kox', 'kox@op.pl', 15),
        ('bocian', 'bocianos@op.pl', 23),
        ]
valid_usernames = set()


def username_check(username):
    if username in valid_usernames:
        raise UsernameExists(username)


def age_is_positive(age):
    if age < 0:
        raise AgeNotPositive(age)


def age_under_16(age):
    if age < 16:
        raise UserIsUnderage(age)


def mail_check(mail):
    if '@' not in mail:
        raise InvalidMail(mail)
    usr_mail, domain = mail.split('@')
    if usr_mail == '' or domain == '':
        raise InvalidMail(mail)


for username, mail, age in data:
    try:
        username_check(username)
    except UsernameExists as err:
        print(err)
        continue
    try:
        age_is_positive(age)
    except AgeNotPositive as err:
        print(err)
        continue
    try:
        age_under_16(age)
    except UserIsUnderage as err:
        print(err)
        continue
    try:
        mail_check(mail)
    except InvalidMail as err:
        print(err)
        continue
    # finally:        # przy uzyciu finally continue z invalid maila errora nie dziala
    valid_usernames.add(username)

print(valid_usernames)
