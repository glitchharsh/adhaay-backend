from django.db import models

# Create your models here.
EVENTS = (

)

# const events = [
#   {
#     name: "Voice of HBTU",
#     des: "Calling all musical mavens, lyrical legends, and vocal virtuosos - HBTU's annual cultural fest, Adhyaay, is proud to present The Voice of HBTU, the ultimate musical competition of the year! As the legendary Bob Marley once said, One good thing about music, when it hits you, you feel no pain.And that's exactly what we're aiming for - to make you feel the rhythm, to move your body and your soul, and to create an unforgettable experience that you'll cherish for years to come.So, whether you're into pop, rock, R&B, or any other genre, we invite you to join us and show the world what you've got. The Voice of HBTU is not just a competition - it's a celebration of music, creativity, and the power of the human voice. Are you ready to raise the roof and make some noise? Then come and join us at Adhyaay, and let your voice be heard!",
#     img: voice,
#   },
#   {
#     name: "Beat The Street",
#     des: "Step Up and Own the Floor! Let the Rhythm Flow with 'Beat the Street' Dance Battle at Adhyaay!Get ready to unleash your inner dancing sensation as HBTU presents Beat the Street dance battle - the ultimate showdown of style and skill! This is your chance to show off your moves, take on the competition, and claim your place in the spotlight.From breakdancing to hip-hop, contemporary to jazz, this is where creativity and expression meet. As the great Martha Graham once said, Dance is the hidden language of the soul.Let your soul speak and your body move to the beatSo,lace up your shoes, gather your crew, and get ready to own the floor",

#     img: bts,
#   },
#   {
#     name: "[EXTICT] Fandom Quiz",
#     des: "Do you know everything from the fun facts about infinity war to the intricacies of OTT Platform  ? Do you love Web series? How well do you know about these most popular web series? Are you generally shunned among peers for being a 'know-it-all'?  Or does information unintentionally comes blurting out whenever you open your mouth?Can you beat your friends at this quiz?Well, here you can actually win prizes for that! So come and embrace the chance to showthe ignoramuses that information is the real wealth!  Dare to pass these quizzes and prove your fandom for your favorite web series.",
#     img: fandom,
#   },
#   {
#     name: "Bollywood Night",
#     des: "The Perfect Collection of music relaxes us like nothing else. Sinking into the ocean of songs filled with emotion and warmth, listening to the best songs that touch you hear.    ADHYAAY'22 is thrilled to announce the Bollywood Night.        Be it bashy or heart-melting romantic Bollywood lyricism, it helps us take our special moments in life to the skies.        This is your chance to witness the magic of the music industry's finest and sing and dance along to the chart-topping hits.        Amidst the dazzling lights and pulsing rhythms, Get ready to be swept away by the duo's unmatched talent and passion, as they deliver a performance that is sure to be etched in your memories forever.        You'll be required to mark your presence in an outrightly Bollywood attire.         #Adhyaay'22 #htbukanpur #collegefest #bollywoodnight #hbtu_fest #PartyNight #LiveConcert #FunNightOut #MusicalEvening #LiveMusic #Culturalevent",
#     img: night,
#   },
#   {
#     name: "Roadies",
#     des: "Its your time to redeem yourself and a chance to experience the  pleasure of accomplishment and appreciation by everyone.Get ready for the ultimate adrenaline rush as we gear up for the HBTU ROADIES !  Are you tough enough to conquer the challenges ahead? From strenuous tasks to unfavorable situations, solo-ing to teaming up, only those who are obstinate not to give up, can become Roadie Stay tuned for more updates and join us as we hit the road towards an adventure of a lifetim ADHYAAY'22",
#     img: Roadies,
#   },
#   {
#     name: "Vogue",
#     des: "Step into the world of haute couture and witness the magic of fashion unfold at the Vogue Fashion Event. From stunning runway shows to exclusive designer collections, this event is a celebration of style and creativity  Join us as we showcase the latest trends and designs from the world's most renowned fashion houses Get ready to be inspired, dazzled, and captivated by the glamour and elegance of the Vogue Fashion Event ADHYAAY'22",
#     img: vogue,
#   },
#   {
#     name: "[EXTICT] 60 Seconds To Fame",
#     des: "Hello Everyone!  Desperate for a chance to show the world what you are capable of doing   Worry not! We bring your stage where you get a chance to showcase your talent. But , here's a catch..60 seconds is all you have!   Adhyaay'22 brings you 60 Seconds to Fame.So, buckle up and be ready to put in all you have, as the game is gonna be of courage and talent ! Do you have what it takes to be a conqueror?...we will get to know soon.",
#     img: sec,
#   },
#   {
#     name: "Masquerade Party",
#     des: "Ready to scare up some fun?  Grab your little goblins, ghouls, and jack-o-lanterns. Come have some fun at our “Masquerade PARTY”  with a theme of Halloween bash!!!  Celebrate with us at a spooktacular Gothic party complete with finger foods, mocktail potions, and trick-or-treating at the end of the night.Show off your best costume and get creative with creepy-fun foods and decor. Join us for a haunted house crawl where we’ll hit all the spooky sites in town !!!  Are you a budding musician or a spoken word artist or an ambivert personality looking for an opportunity to showcase your talent? Look no further than an open mic night!",
#     img: mask,
#   },
#   {
#     name: "Open Mic",
#     des: "A Fun Night of Showcasing Talent and Joy The coolest part about open mic  is that they are open to everyone, with boundless opportunities regardless of skill level or experience.   But open mic nights aren't just for performers. They are  fun-filled nights full of extravaganza and spectacular performance out for anyone who loves leisure activity and regalement.  'You never know what kind of talent you will encounter at an open mic night.So don't miss this chance to witness an adorable and joyful evening.Because The joy of open mic nights is contagious.",
#     img: openmic,
#   },
#   {
#     name: "Sufi Night",
#     des: "Welcome to the enchanting night of Sufi music and mysticism!   We are delighted to invite you to our sufi night event, where you can immerse yourself in the magical melodies and captivating rhythms of Sufi music.     Sufi night will give you different touch and flavour of sensation of music that touches the soul, connecting us with the divine and igniting a sense of inner peace and tranquility.     ' Our sufi night event promises to be truly cherishful and unforgettable experience.'     We summon you to join us on this special night to celebrate the timeless beauty and sufi music. Come and experience the transformative power of this ancient art form,and let it transport you to a world of spiritual bliss.",
#     img: sufi,
#   },
#   {
#     name: "Face Painting",
#     des: "Face Painting,by cultural sub council of course will be setting and breaking all boundaries free at BE/FT Lawn with an open theme face painting event which we all dreamt for",
#     img: face,
#   },
#   {
#     name: "Talent-Fiesta",
#     des: "Adhyaay is bringing this very unique and A FEST WITHIN A FEST concept of Talent Fiesta! So come and show them all what you got ...!! Be a part of this Cultural event and you would never regret an ultimate show like this",
#     img: talent,
#   },
#   {
#     name: "Soda Pop",
#     des: "-It's too hot out there right? In this blazing heat and very dramaƟc summer, we ain't got any escapes though... Adhyaay however never disappoints,we at Adhyaay have pulled this very enthralling event called Soda Pop which will be serving as a restoring force of interests of every Harcourtian ! ",
#     img: soda,
#   },
#   {
#     name: "Best Engineer",
#     des: "It comprise of inter-branch competition. Students participating would be representing their particular branch.They would go through different rounds each round would be unique in its own kind like some would be having quizzes,some would be to show case their talent by performing their artistry(dance,acting,singing),mimicking of their branch professors and some set of questions would be asked to know to evaluate them wholly.At the end we would be judging them on the basis of all the rounds",
#     img: enginner,
#   },
#   {
#     name: "Food Without Fire",
#     des: "To provide a platform for students to foster their creativity and decision making skills and also help them explore their hidden talents and discover new areas of interest. The event gave a platform to the students to demonstrate their culinary knowledge skills related to: developing and following a recipe,preparation of a dish, and displaying the dish before a judging panel where it will be evaluated on flavour,taste and palatability.Their efforts were evaluated on the basis of five parameters: a)Dish Name, b)Taste, c)Presentation, d)Calorie content, e)Hygiene. Participants infused lots of creativity and served delicious etables to enhance the taste buds.Here the participant had to prepare an etable without using the fire.Example Bhel puri,Chaat,sandwiches,shakes,Mojito,Choclate Lollypop,Aamavat mouthfresner and many more",
#     img: foodz,
#   },
#   {
#     name: "High Fives",
#     des: "From bursting ballons,goal post,blindman Swag,identify me to He-me it's a total variety of fun and super cool events by cultural sub council!",
#     img: high,
#   },
#   {
#     name: "Gothic Party",
#     des: "looking for a totally different way of entertaining then step back 160 years to the Victoric Gothic Period and entertain with a flamboyant gothic party,a gothic inspired menu of cocktails and more,gothic party games having a radium neon dust and masquerade mask will be provide for entering the gothic party venue,gothic ball dance,performance would be held.everyone can dress beautifully in vintage styled attire to enjoy an evening of decadence and frivolity",
#     img: gothic,
#   },
#   {
#     name: "Documentary",
#     des: "An event where each participant has to make a documentary on ADHYAAY and the best of them will be shared on the official sub council page as official documentary of Adhyaay",
#     img: adhyaayp,
#   },
#   {
#     name: "Battle of Bands",
#     des: "Competition Between Musical Bands",
#     img:,
#   },
#   {
#     name: "Student of the year",
#     des:"The mega event consists of competitions like Dance, Singing, etc.",
#     img:,
#   },
#   {
#     name: "Awakenings DJ",
#     des: "DJ",
#     img:,
#   },
#   {
#     name: "Guess the Name",
#     des: "Game to guess the name of the movie with the help of given clues",
#     img:,
#   },
#   {
#     name: "Murder Mystery",
#     des: "Treasure Hunt to solve a Murder Mystery.",
#     img:,
#   },
#   {
#     name: "Vogue",
#     des: "Fashion Show",
#     img:,
#   },
#   {
#     name: "Stage performances",
#     des: "Dance, Singing, Rap, etc",
#     img:,
#   },
#   {
#     name: "EDM Night",
#     des: "Electronic Dance Music Night",
#     img:,
#   },
#   {
#     name: "Quiz Marvel",
#     des: "Quiz-based for Marvel fans",
#     img:,
#   },
#   {
#     name: "Celebrity Night",
#     des: "Concert with Artist",
#     img:,
#   },
#   {

#   }
# ];