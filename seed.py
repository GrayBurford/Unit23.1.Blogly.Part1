"""Sample data to populate User and Post tables in Blogly database."""

from models import db, User, Post
from app import app

# Drop all and recreate all tables
db.drop_all()
db.create_all()

# If tables aren't empty, empty them
User.query.delete()
Post.query.delete()

# Add some sample Users:
gray = User(first_name='Gray', last_name='Burford', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")
tina = User(first_name='Tiange', last_name='Burford', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")
tracy = User(first_name='Tracy', last_name='Gasiewicz', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")
pete = User(first_name='Peter', last_name='Gasiewicz', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")
ren = User(first_name='Ren', last_name='Ffan', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")
jiaji = User(first_name='Jiaji', last_name='Wu', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")
bob = User(first_name='Robert', last_name='Burford', image_url="https://image.shutterstock.com/image-vector/anonymous-vector-icon-incognito-sign-260nw-1850222983.jpg")

# add and commit new Users to session database
db.session.add_all([gray, tina, tracy, pete, ren, jiaji, bob])
db.session.commit()

# Add some sample Posts for Users:
post1 = Post(title="Mistborn Triology", content="Mistborn is a series of epic fantasy novels written by American author Brandon Sanderson and published by Tor Books. The first trilogy, published between 2006 and 2008, consists of The Final Empire, The Well of Ascension, and The Hero of Ages. A second series was released between 2011 and 2022, and consists of The Alloy of Law, Shadows of Self, The Bands of Mourning and The Lost Metal. A third series will follow them, which is likely to be released yearly from 2025 to 2027. A fourth trilogy is also planned. Brandon also released a novella in 2016, Mistborn: Secret History. The first Mistborn trilogy chronicles the efforts of a secret group of Allomancers who attempt to overthrow a dystopian empire and establish themselves in a world covered by ash and gods. The first trilogy received a huge success and it made Sanderson develop his fictional universe, the Cosmere, which also includes The Stormlight Archive. Set about 300 years after Era 1, the second series is about the exploits of Waxillium Ladrian, a 'wild-west Deputy' forced to move into the big city, and starts investigating kidnappings and robberies. The third series will be set in the early computer age with 1980s technology. The main character is planned as a Terris woman who is a computer programmer and Nicroburst; her brother is also planned to be a character. The fourth series is going to be a space-opera", user_id=1)

post2 = Post(title="A Song of Ice and Fire", content="HISTORY, PURPOSE AND USAGE Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with: “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.” The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content. The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.", user_id=2)

post3 = Post(title="Testing123", content="Test test test", user_id=1)

db.session.add_all([post1, post2, post3])
db.session.commit()