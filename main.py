from db.models import *

# product = Product(title='Product 1', price=10)
# product.save()

# product = Product.objects.get(id=1)
# product.delete()


# ContentRating.objects.create(title = 'PEGI 3', ageLimit = 3, description = 'The content of apps with this rating is considered suitable for all age groups. Some violence in a comical context (typically cartoonlike - Bugs Bunny or Tom & Jerry - forms of violence) is acceptable. A child should not be able to associate the character on the screen with real life characters, they should be distinctly fantasy. The app should not contain any sounds or pictures that are likely to scare young children. No bad language should be heard.')
# ContentRating.objects.create(title = 'PEGI 7', ageLimit = 7, description = 'Any app that would normally be rated at 3 but contains some scenes or sounds that can possibly be frightening for children may be considered suitable in this category. There can only be very mild violence in a PEGI 7 app, like implied violence or non-detailed, non-realistic violence.')
# ContentRating.objects.create(title = 'PEGI 12', ageLimit = 12, description = 'Games or apps that show violence of a slightly more graphic nature towards fantasy characters, or non-graphic violence towards human-looking characters or animals would fall in this age category, as well as nudity of a slightly more graphic nature and simulated gambling. Any bad language in this category must be mild and fall short of sexual expletives.')
# ContentRating.objects.create(title = 'PEGI 16', ageLimit = 16, description = 'Once the depiction of violence or sexual activity reaches a stage that looks the same as would be expected in real life, this rating is applied. Stronger inappropriate language, encouraging the use of tobacco or drugs and depicting criminal activities can be content of apps that are rated 16.')
# ContentRating.objects.create(title = 'PEGI 18', ageLimit = 18, description = 'The adult classification is applied when the level of violence reaches a stage where it becomes a depiction of gross violence and/or includes elements of specific types of violence (motiveless killing, violence towards defenceless characters or sexual violence). It may also include graphic sexual content, discrimination or the glamorisation of illegal drugs use.')

# Publisher.objects.create(title = 'Nintendo')
# Publisher.objects.create(title = 'Activision')
# Publisher.objects.create(title = 'Microsoft Game Studios')
# Publisher.objects.create(title = 'Sony Computer Entertainment')
# Publisher.objects.create(title = 'Sega')

# Platform.objects.create(title = 'Wii')
# Platform.objects.create(title = 'X360')
# Platform.objects.create(title = 'PS2')
# Platform.objects.create(title = 'PS3')
# Platform.objects.create(title = 'PC')

# Genre.objects.create(title = 'Racing')
# Genre.objects.create(title = 'Sports')
# Genre.objects.create(title = 'Action')
# Genre.objects.create(title = 'Role-Playing')
# Genre.objects.create(title = 'Misc')

# Product.objects.create(
#     title = 'Wii Sports', 
#     description = 'Wii (???????????? ???????????? Wii Sup??tsu Riz??to) is a video game that is a collection of twelve sports mini-games published by Nintendo for its own Wii console; sequel to Wii Sports . The Wii MotionPlus accessory comes with the game.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-11-19',
#     publisher = Publisher.objects.get(id=1), 
#     price = 82.74, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)


# Product.objects.create(
#     title = 'Mario Kart Wii', 
#     description = 'Mario Kart Wii ??? ??????????????????, ?????????????????????????? ?????????????????? Nintendo Entertainment Analysis and Development ?? ???????????????????? Nintendo ?????????????????????? ?????? ?????????????????? Wii. ???????? ???????????????? ???????????? ???????????? ?????????? Mario Kart ?? ???????????? ?????????? ???? ???????? ??????????, ???????????????????????? ???????????? Nintendo Wi-Fi Connection.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2008-04-10', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 40.24, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Sports Resort', 
#     description = 'Wii Sports Resort ??? ??????????????????, ???????????????????????????? ?????????? ?????????????? ???? ???????????????????? ???????????????????? ????????-??????, ???????????????????? ?????????????????? Nintendo ?????? ?????????????????????? ?????????????? Wii; ???????????? Wii Sports. ???????????? ?? ?????????? ???????????????????????? ?????????????????? Wii MotionPlus.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2009-06-25', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 33, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Play', 
#     description = 'Wii Play ??? ???????????????????????? ??????????????????, ?????????????????????????? ?? ???????????????????????????? ?????????????????? Nintendo ?????? ?????????????? Wii. ???????? ???????? ???????????????? ?? ???????????????? ?????????????????? ???????? ?????? ?????????????? ?? ????????????, ???????????? ?? ??????????????????, ?? ?????????? ???????? ???????????????? ?? ???????????????? ?????????????? ?? ?????????????? 2007 ????????.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-10-02', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 29.02, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'The Legend of Zelda: Skyward Sword', 
#     description = 'The Legend of Zelda: Skyward Sword ??? ???????? ?????????? action-adventure ?????? ?????????????? Wii, ?????????????????????????? ?????????????? Nintendo Entertainment Analysis and Development.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2011-11-18', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 59.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Donkey Kong Country Returns', 
#     description = 'Donkey Kong Country Returns, ?? ???????????? ?????????????????? ?????? ?????????????????? Donkey Kong Returns ??? ?????????????????? ?? ?????????? ?????????????????????? ??????????????????????, ?????????????????????????? ?????????????????? Retro Studios.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2010-11-21', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 13.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Mario Party 8', 
#     description = 'Mario Party 8 ??? ?????????????????? ?????? ?????????????????? 2007 ????????, ?????????????????????????? Hudson Soft ?? ???????????????? Nintendo ?????? Wii.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2007-05-29', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 21.99, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Party', 
#     description = 'Wii Party ??? ?????????????????? ?????? ??????????????????, ?????????????????????????? ?? ???????????????? Nintendo ?????? ?????????????? ?????????????? Wii.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2010-07-08', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 40.00, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Fit', 
#     description = 'Wii Fit ??? ???????????????????? ??????????-????????????????, ?????????????????????????? ?????????????????? Nintendo ?????? ?????????????? ??????????-?????????????? Wii.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2007-12-01', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 96.84, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'The Legend of Zelda: Twilight Princess', 
#     description = 'The Legend of Zelda: Twilight Princess ??? ?????????????????? ?? ?????????? Action-adventure ???? ?????????? The Legend of Zelda, ?????????????????????????? ?? ???????????????? ?????????????????? Nintendo ?????? ?????????????????? GameCube ?? Wii ?? 2006 ????????.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-11-19', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 99.99, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'World of Warcraft', 
#     description = 'World of Warcraft ??? ???????????????? ?????????????????????????????????????????? ?????????????? ????????????-????????, ?????????????????????????? ?? ???????????????????? ?????????????????? Blizzard Entertainment.', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2004-11-23', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 14.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Diablo III', 
#     description = 'Diablo III ??? ???????????????????????? ???????? ?? ?????????? Action/RPG, ?????????????????????????? ?? ???????????????????? ???????????????????????? ?????????????????? Blizzard Entertainment, ?????? ???????????????? Microsoft Windows, Mac OS X, PlayStation 3, PlayStation 4, Xbox 360, Xbox One ?? Switch.', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2012-05-05', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 59.99, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Guitar Hero III: Legends of Rock', 
#     description = 'Guitar Hero III: Legends of Rock ??? ?????????????????????? ??????????????????, ?????????????????????????? ?????????????? NeverSoft ?? ???????????????? Aspyr ?? Activision.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2007-10-28', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 5.90, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Spider-Man: The Movie', 
#     description = 'Spider-Man: The Movie Game, Spider-Man ??? ??????????????????, ?????????????????????????? ?????????????????? Treyarch, ?? ???????????????? ?????????????????? Activision ?? 2002 ???????? ?????? Xbox, PlayStation 2, GameCube, Microsoft Windows ?? Game Boy Advance.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2002-04-16', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 14.96, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = "Tony Hawk's Pro Skater 3", 
#     description = "Tony Hawk's Pro Skater 3 ??? ?????????????????? ???? ?????????? Tony Hawk, ?????????????????????????? ?????????????????? Neversoft ?? ???????????????? Activision ?? 2001 ???????? ?????? ???????????????? Nintendo GameCube, Game Boy Color, PlayStation ?? PlayStation 2.", 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2001-10-28', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 35.44, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'World of Warcraft: The Burning Crusade', 
#     description = 'World of Warcraft: The Burning Crusade ??? ???????????? ???????????????????? ?? ???????????????????????? ???????? World of Warcraft', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2007-01-16', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 12.24, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'LEGO Indiana Jones: The Original Adventures', 
#     description = "Lego Indiana Jones: The Original Adventures ??? ???????????????????????? ???????? ?? ?????????? ????????????, ?????????????????????????? Traveller's Tales ?? ???????????????? Lucas Arts.", 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2008-06-03', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 19.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = "Tony Hawk's Pro Skater 4", 
#     description = 'Tony Hawk???s Pro Skater 4, ?????????????????? ?????????????????? ?? ?????????? Tony Hawk, ?????????????????????????? ?????????????????? Neversoft ?? ???????????????????? Activision ?? 2002 ???????? ?????? GameCube, Game Boy Advance, PlayStation, PlayStation 2 ?? Xbox. ?? 2003 ???????? ?????????? ?????? Microsoft Windows, Mac OS X ?? Tapwave Zodiac.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2002-10-23', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 15.00, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Guitar Hero: World Tour', 
#     description = 'Guitar Hero World Tour ??? ?????????????????? ?? ?????????? ?????????????????????? ????????????, ?????????????????????????? ?????????????? Neversoft ?? ???????????????? RedOctane ?? Activision. ?????? ?????????????????? ???????? ???? ???????????????? ?????????? Guitar Hero ?? ???????????? ???????? ???? ???????? ??????????. ???????????? ?????? Microsoft Windows ?? Apple Macintosh ?????????? 15 ???????? 2009 ????????.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2008-11-26', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 10.45, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Kung Fu Panda', 
#     description = 'Kung Fu Panda ??? ???????????????????????? ????????, ???????????????????? ???? ?????????????????????? ???????????????????????? ????????????. ?????????????????????????? ?????????????????????? ???????????????? Luxoflux, XPEC Entertainment, Beenox ?? Vicarious Visions ?? ???????????????? Activision, ???????? ???????? ???????????????? ?????? PlayStation 3, Xbox 360, Windows, macOS, PlayStation 2, Wii ?? Nintendo DS ?? ???????? 2008 ????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2008-06-03', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 25.00, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Kinect Adventures!', 
#     description = 'Kinect Adventures! ??? ?????? ???????????????????? ?????????????????? ?????? Xbox 360, ???????????????????????? ?????????????????????? ?????????????????????? Kinect ?? ???????????????? ?? ???????????????? ???????????????? ??????????????????????. ???????? ???????? ???????????????????????? ???? ???????????????? Electronic Entertainment Expo 2010 ?? ??????-??????????????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2010-11-04', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 2.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Minecraft', 
#     description = '???????????????????????? ????????-???????? ?? ?????????? ??????????????????, ?????????????????? ???????????????? ?????????????????????????? ???????????????? ?????????????????? ?? ???????????????????? ?????? ?????????????? Mojang AB.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2011-11-18', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 29.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Forza Motorsport 3', 
#     description = 'Forza Motorsport 3 ??? ???????????????????????? ???????? ?? ?????????? ?????????????????? ????????????????????, ?????????????????????????? ?????????????? Turn 10 Studios ?? ???????????????? ???? Xbox 360. ???????? ?????????? ?? ?????????????? 2009 ???????? ?? ???????????????? ?????????????? ?????????? ?? ?????????? Forza Motorsport.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2009-10-22', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 7.58, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Mass Effect', 
#     description = 'Mass Effect ??? ????????????-???????????????????????????? ??????????????????????????, ?????????????????? ?????????? ????????????????, ?????? ???????????????????? ?? ?????????????????? ??????????????????????. ???????????????? ???????????????????????? ?? ?????????????? ??????????????, ?? ?????????????? ???????? ?? ???????????????????????? ???????????????????????????? ?????????????? ???????? ?? ?????????????? ???????????????????? ?????????????? ??????????????????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2007-11-16', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 29.99, 
#     contentRating = ContentRating.objects.get(id=5),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'PGR4 - Project Gotham Racing 4', 
#     description = 'Project Gotham Racing 4 ??? ?????????????????? ?? ?????????? ???????????????? ????????- ?? ??????????????????, ?????????????????????????? ?????????????? Bizarre Creations ?? ???????????????? ?????????????????? Microsoft Game Studios ?????????????????????? ?????? ?????????????? Xbox 360 ?? ?????????????? 2007 ????????. ???? ?????????????????????? ???????? ???????????????????????? ???????????????? ?????????? ??????????, ?????????????? ?????????????????? ???????? ???? ?????????????? ??????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2007-10-02', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 19.95, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Kinect Star Wars', 
#     description = 'Kinect Star Wars ??? ?????????????????? ???? ?????????????????? ?????????????????? ??????????, ?????????????????????????? Terminal Reality ?? ???????????????????????????? LucasArts ?? Microsoft Studios ?????? Xbox 360, ?? ?????????????? ???????????????????????? ???????????????????????? ???????????????????? ???????????????? Kinect.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2012-04-03', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 6.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Alan Wake', 
#     description = 'Alan Wake ??? ???????????????????????? ???????? 2010 ????????, ?????????????????????????? ?????????????? ?????????????? Remedy Entertainment ?? ???????????????? Microsoft Game Studios. ???????????????????????? ???????????????????? ???????? ???????? ?????? ???????????????????????????????? ??????????-????????????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2010-05-14', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 14.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Blue Dragon', 
#     description = 'At maturity G. atlanticus can be up to 3 cm (1.2 in) in length,[6] though larger specimens have been found.[7] It can live up to a year under the right conditions.[8] It is silvery grey on its dorsal side and dark and pale blue ventrally. It has dark blue stripes on its head. It has a flat, tapering body and six appendages that branch out into rayed, finger-like cerata.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2006-12-07', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 9.50, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Lost Odyssey', 
#     description = 'Lost Odyssey ??? ???????????????? ?????????????? ????????, ?????????????????????????? ?????????????? Mistwalker ?? feelplus, ?????????????? ???????? ???????????? Microsoft Game Studios ?????????????????????? ?????? Xbox 360. ?????????? ?????????????????? ???????????????????? ???? ?????????? ????????, ??????????????????, ?????????????? ?????????? ?????? ???????????? ?????? ?? ???????????? ???? ???????????? ?? ?????????? ??????????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2007-10-06', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 4.28, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Dance Central 3', 
#     description = 'Dance Central 3 ??? ?????????????????????? ??????????????????, ?????????????????????????? ?? ???????????????? Harmonix ?? ???????????????????? ?? Backbone Entertainment. ?????? ???????????? ???????? ?? ?????????? Dance Central. ?????? ???????? ???????????????????????? ???? ???????????????????????? E3 2012 ???? ?????????? ?????????? ?????????????????????? Microsoft.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2012-10-16', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 58.00, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Gran Turismo 3: A-Spec', 
#     description = 'Gran Turismo 3: A-Spec ??? ?????????????????? ?? ?????????? ?????????????????? ????????????????????, ???????????? ???????? ???? ?????????? Gran Turismo, ?????????????? ?????????? ???? ?????????????????? Sony PlayStation 2. Gran Turismo 2000 ???????? ?????????????? ?????????????????? ????????, ?????????? ?????? ?????????????????????????????????? ???? ???????????????? ??3 ?? 2000???2001 ??????????.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2001-04-28', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 7.90, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = "Uncharted 3: Drake's Deception", 
#     description = "Uncharted 3: Drake's Deception, ?? ???????????? ???????? ???????????? ?????? ?????????????????? ??Uncharted 3: ?????????????? ?????????????? ??? ???????????????????????? ???????? ?? ?????????? ???????????????????????????????? ?????????????? ?? ?????????? ???? ???????????????? ????????, ?????????????????????????? ???????????????????????? ?????????????????? Naughty Dog.", 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2011-11-01', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 4.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'God of War III', 
#     description = 'God of War III ??? ???????????????????????? ???????? ?? ?????????? hack and slash, ???????????????????? ???????????????????????? ?????????????????? Santa Monica Studio ?????????????????????? ?????? ?????????????????? PlayStation 3. ?? ???????????? ???????? ?????????? 17 ?????????? 2010 ????????.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2010-03-16', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 19.99, 
#     contentRating = ContentRating.objects.get(id=5),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'EyeToy Play', 
#     description = 'EyeToy: Play - ?????? ??????????????????-?????????????? ????????-?????? ?????? PlayStation 2, ???????????????????? ?? 2003 ????????. ?????? ???????? ???????????? ????????, ?? ?????????????? ???????????????????????????? ?????????????????????? PlayStation 2, EyeToy. ???????? ???????????????????? ???????????????????????? ?? EyeToy, ?????????? ?????????????????? ?????? ?????????????? ??????????????.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2003-02-04', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 14.03, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sports Champions', 
#     description = '???????????????? ???????????? ??? ???????????????????????? ???????? 2010 ????????, ?????????????????????????? San Diego Studio ?? Zindagi Games ?? ???????????? Sony Computer Entertainment ?????? PlayStation 3, ?? ?????????????? ???????????????????????? PlayStation Move. ?????? ???????? ???????????????????? ???????????????????????? ???? ?????????????????????? Game Developers Conference ?? San Francisco.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2010-09-07', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 29.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'inFAMOUS', 
#     description = 'inFamous ??? ?????????????????? ?? ?????????? ???????????????????????????????? ??????????????, ?????????????????????????? Sucker Punch Productions ?? ???????????????? Sony Computer Entertainment. ???????? ???????? ???????????? ???????????? ?????? PlayStation 3: 26 ?????? 2009 ???????? ??? ?? ??????, ?? 29 ?????? ??? ?? ????????????.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2009-05-26', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 9.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Hot Shots Golf 3', 
#     description = "Everyone's Golf 3, ?????????????????? ?? ???????????????? ?????????????? ?????? Hot Shots Golf 3, ???????????????? ?????????????? ?????????? ?? ?????????? Everyone's Golf ?? ???????????? ??????????, ???????????????????? ?????? PlayStation 2.", 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2001-07-26', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 2.81, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'God of War Collection', 
#     description = 'God of War Collection ??? ??????????????, ?????????????????? ???? ?????????????????????? ?? ?????????????????????????? ???????????? God of War ?? God of War II ?????? PlayStation 3 ???? ?????????? ?????????? Blu-ray.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2009-11-17', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 13.99, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'SingStar', 
#     description = 'SingStar ??? ?????????? ???????????????????????????????? ?????????????????????? ?????? ?????? ?????????????? ?????????????????? PlayStation. ???????? ?????????? ?????????????????????? ?????????????????? London Studio ?? ???????????? Sony Interactive Entertainment. ???????????????????? ?????????? ?????? ?????????????????????????? ?????? ?????????????????? PlayStation 2 ?? PlayStation 3.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2004-05-03', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 54.98, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Buzz! The BIG Quiz', 
#     description = 'Buzz!: The BIG Quiz ??? ???????????? ?? Buzz! ?????????? ?????? ?????? PlayStation 2, ?????????????????????????? Relentless Software. ???????????????????????????? ?????????????????? ???????????????? ?????????????????? Buzz! Uber Quiz, ???????????? Sony Computer Entertainment Europe ???????????????? ???? ?????????????????? ?????????? ?????????????? ????????. ????????????, ???? ????????, ?????? ????, ?????? ?? ?? ??????????????????: Buzz!: ?????????????????????? ??????????????????.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2006-03-17', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 6.80, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Mario & Sonic at the Olympic Games', 
#     description = '???????????????????? ??????????????????, ?????????????????????????? ???????????????????????????? Sega Sports Japan ?? ???????????????????? Nintendo (?? ????????????) ?? Sega (?? ?????????????????? ????????????????) ?? ???????????? 2007 ???????? (?? ???????????? ?????????? ?? ???????????? 2008 ????????) ?????? Nintendo Wii ?? ?? ???????????? ?? ?????????????? 2008 ???????? ?????? Nintendo DS.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2007-11-06', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 33.25, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'MadWorld', 
#     description = "MadWorld ??? ?????? ???????? ?? ?????????? beat 'em up hack and slash, ?????????????????????????? PlatinumGames, ???????????????? Sega, ???????????????????????????????? ?????????? ?????????? ?? ???????????????????? ?????????????? ???????????????? ???????????????? ????????????????. ???? ?????? ?????????????? ???? ???????? ???????? ?????? Wii ?? ?????????? 2009 ???????? ?? ?? ???????????? ?? ?????????????? 2010 ????????.", 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2009-03-10', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 12.80, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sega Superstars Tennis', 
#     description = 'Sega Superstars Tennis ??? ?????????????????? ??????????????????, ?????????????????????????? Sumo Digital ?? ???????????????? Sega. ???????????????? ???????????? ?????????? ?? ??????????-???????????????????? Sega Superstars. ?????? ???????? ???????????????? ???? ?????????????? Xbox 360, PlayStation 2, PlayStation 3, Wii ?? Nintendo DS 18 ?????????? 2008 ???????? ?? ??????, 20 ?????????? ?? ???????????? ?? 25 ?????????? ?? ????????????.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2006-03-17', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 5.73, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sonic Mega Collection Plus', 
#     description = 'Sonic Mega Collection Plus - ?????????????? ???????????????? ?????????????????????? ?????????? ?? ???????????????? Sega Mega Drive ?? Game Gear. Sonic Mega Collection Plus ???????????????? ?????????????????????????????????????? ?????????????? Sonic Mega Collection ?????? Nintendo GameCube. ?????????????? ?????????? ?????? Sony PlayStation 2, XBOX ?? PC.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2004-10-04', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 17.68, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'ESPN NFL 2K5', 
#     description = 'ESPN NFL 2K5 ??? ?????????????????? ?? ???????????????????????? ????????????, ?????????????????????????? Visual Concepts ?????? ???????????????? PlayStation 2 ?? Xbox. ???????????????? 2K Sports ?? Sega Corporation, ?????? ???????????? ?????????? ?????????? NFL 2K ?? ??????????????????, ???????? ?????????????? ???????????????????????? ?????????????????????? ???????????????? NFL.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2004-06-20', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 24.12, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Super Monkey Ball: Banana Blitz', 
#     description = 'Super Monkey Ball: Banana Blitz, ?? ???????????? ?????????????????? ?????? Super Monkey Ball: Exciting Party Collection ??? ???????????????????????? ???????? ???? ?????????? Super Monkey Ball, ???????????????????? ?????????????????????? ?????? ?????????????? ?????????????? Wii ?? 2006 ????????.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-11-14', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 24.69, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sonic & Sega All-Stars Racing', 
#     description = 'Sonic & Sega All-Stars Racing, ?? ???????????? ?????? Xbox 360 ?????????????????? ?????? Sonic & Sega All-Stars Racing with Banjo-Kazooie ??? ???????????????? ???????? ?? ???????????????? ???????????????????? ???? ?????? Sonic the Hedgehog, ?? ?????????? ?????????????????????? ???????????????? Sega. ???????? ???????? ???????????????????????? 28 ?????? 2009 ????????.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2010-02-23', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 10.63, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Football Manager 2012', 
#     description = 'Football Manager 2012 ??? ???????????????????????? ????????, ?????????????????? ?????????????????????? ??????????????????????, ?????????? ?????????? Football Manager. ???????? ?????????????????????? ?????????????????? Sports Interactive ???? ?????????????????? Microsoft Windows ?? Mac OS X. ???????? ?????????????????? ?? ?????????????? 21 ?????????????? 2011 ????????. ?? ???????????? ???????????????? ?????????????????? 1??-????????????????.', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2011-10-20', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 17.80, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Yakuza 3', 
#     description = 'Yakuza 3 ??? ???????????????????????? ????????, ?????????????????????????? ?? ???????????????? ?????????????????? Sega. ?????????? ?????????? Yakuza. ???????????????????? ???????? ???????? ???????????????? ?????? ?????????????? ?????????????????? PlayStation 3 ?? 2009 ???????? ?? ?? ?????????????????????? ???????????????????? ?????? ???????????????? PlayStation 4, Xbox One ?? Windows.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2009-02-26', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 35.63, 
#     contentRating = ContentRating.objects.get(id=5),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Samba De Amigo', 
#     description = 'Samba de Amigo ??? ???????????????????????? ????????, ?????????????????????????? ???????????????? Sonic Team ?? ???????????????????? Sega ?????? ?????????????????? ???????????????? ?? ?????????????? Dreamcast, ?? 1999 ?? 2000 ??????????. ?? 2008 ???????? ???????? ???????? ???????????????? ?????? Wii. ?????????????????????????? ???????? ?????? Wii ???????????????????? ???????????????? Gearbox Software.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '1999-12-17', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 16.50, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

price2 = Product.objects.filter(price>30)
pprint(Product)





