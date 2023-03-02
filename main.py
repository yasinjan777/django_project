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
#     description = 'Wii (スポーツ リゾート Wii Supōtsu Rizōto) is a video game that is a collection of twelve sports mini-games published by Nintendo for its own Wii console; sequel to Wii Sports . The Wii MotionPlus accessory comes with the game.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-11-19',
#     publisher = Publisher.objects.get(id=1), 
#     price = 82.74, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)


# Product.objects.create(
#     title = 'Mario Kart Wii', 
#     description = 'Mario Kart Wii — видеоигра, разработанная компанией Nintendo Entertainment Analysis and Development и выпущенная Nintendo эксклюзивно для платформы Wii. Игра является шестой частью серии Mario Kart и второй игрой из этой серии, использующей сервис Nintendo Wi-Fi Connection.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2008-04-10', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 40.24, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Sports Resort', 
#     description = 'Wii Sports Resort — видеоигра, представляющая собой сборник из двенадцати спортивных мини-игр, выпущенная компанией Nintendo для собственной консоли Wii; сиквел Wii Sports. Вместе с игрой поставляется аксессуар Wii MotionPlus.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2009-06-25', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 33, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Play', 
#     description = 'Wii Play — коллективная видеоигра, разработанная и опубликованная компанией Nintendo для консоли Wii. Игра была выпущена в качестве стартовой игры для консоли в Японии, Европе и Австралии, а также была выпущена в Северной Америке в феврале 2007 года.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-10-02', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 29.02, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'The Legend of Zelda: Skyward Sword', 
#     description = 'The Legend of Zelda: Skyward Sword — игра жанра action-adventure для консоли Wii, разработанная отделом Nintendo Entertainment Analysis and Development.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2011-11-18', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 59.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Donkey Kong Country Returns', 
#     description = 'Donkey Kong Country Returns, в Японии известная под названием Donkey Kong Returns — видеоигра в жанре трехмерного платформера, разработанная компанией Retro Studios.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2010-11-21', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 13.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Mario Party 8', 
#     description = 'Mario Party 8 — видеоигра для вечеринок 2007 года, разработанная Hudson Soft и изданная Nintendo для Wii.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2007-05-29', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 21.99, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Party', 
#     description = 'Wii Party — видеоигра для вечеринок, разработанная и изданная Nintendo для игровой консоли Wii.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2010-07-08', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 40.00, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Wii Fit', 
#     description = 'Wii Fit — спортивный видео-тренажёр, разработанный компанией Nintendo для игровой видео-консоли Wii.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2007-12-01', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 96.84, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'The Legend of Zelda: Twilight Princess', 
#     description = 'The Legend of Zelda: Twilight Princess — видеоигра в жанре Action-adventure из серии The Legend of Zelda, разработанная и изданная компанией Nintendo для платформы GameCube и Wii в 2006 году.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-11-19', 
#     publisher = Publisher.objects.get(id=1), 
#     price = 99.99, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'World of Warcraft', 
#     description = 'World of Warcraft — массовая многопользовательская ролевая онлайн-игра, разработанная и издаваемая компанией Blizzard Entertainment.', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2004-11-23', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 14.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Diablo III', 
#     description = 'Diablo III — компьютерная игра в жанре Action/RPG, разработанная и выпущенная американской компанией Blizzard Entertainment, для платформ Microsoft Windows, Mac OS X, PlayStation 3, PlayStation 4, Xbox 360, Xbox One и Switch.', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2012-05-05', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 59.99, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Guitar Hero III: Legends of Rock', 
#     description = 'Guitar Hero III: Legends of Rock — музыкальная видеоигра, разработанная студией NeverSoft и изданная Aspyr и Activision.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2007-10-28', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 5.90, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Spider-Man: The Movie', 
#     description = 'Spider-Man: The Movie Game, Spider-Man — видеоигра, разработанная компанией Treyarch, и изданная компанией Activision в 2002 году для Xbox, PlayStation 2, GameCube, Microsoft Windows и Game Boy Advance.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2002-04-16', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 14.96, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = "Tony Hawk's Pro Skater 3", 
#     description = "Tony Hawk's Pro Skater 3 — видеоигра из серии Tony Hawk, разработанная компанией Neversoft и изданная Activision в 2001 году для платформ Nintendo GameCube, Game Boy Color, PlayStation и PlayStation 2.", 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2001-10-28', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 35.44, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'World of Warcraft: The Burning Crusade', 
#     description = 'World of Warcraft: The Burning Crusade — первое дополнение к компьютерной игре World of Warcraft', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2007-01-16', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 12.24, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'LEGO Indiana Jones: The Original Adventures', 
#     description = "Lego Indiana Jones: The Original Adventures — компьютерная игра в жанре аркады, разработанная Traveller's Tales и изданная Lucas Arts.", 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2008-06-03', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 19.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = "Tony Hawk's Pro Skater 4", 
#     description = 'Tony Hawk’s Pro Skater 4, четвёртая видеоигра в серии Tony Hawk, разработанная компанией Neversoft и выпущенная Activision в 2002 году для GameCube, Game Boy Advance, PlayStation, PlayStation 2 и Xbox. В 2003 году вышла для Microsoft Windows, Mac OS X и Tapwave Zodiac.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2002-10-23', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 15.00, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Guitar Hero: World Tour', 
#     description = 'Guitar Hero World Tour — видеоигра в жанре музыкальной аркады, разработанная студией Neversoft и изданная RedOctane и Activision. Это четвёртая игра из основной серии Guitar Hero и шестая игра во всей серии. Версии для Microsoft Windows и Apple Macintosh вышли 15 июля 2009 года.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2008-11-26', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 10.45, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Kung Fu Panda', 
#     description = 'Kung Fu Panda — компьютерная игра, основанная на одноимённом анимационном фильме. Разработанная совместными усилиями Luxoflux, XPEC Entertainment, Beenox и Vicarious Visions и изданная Activision, игра была выпущена для PlayStation 3, Xbox 360, Windows, macOS, PlayStation 2, Wii и Nintendo DS в июне 2008 года.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2008-06-03', 
#     publisher = Publisher.objects.get(id=2), 
#     price = 25.00, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Kinect Adventures!', 
#     description = 'Kinect Adventures! — это спортивная видеоигра для Xbox 360, использующая возможности контроллера Kinect и входящая в комплект поставки контроллера. Игра была представлена на выставке Electronic Entertainment Expo 2010 в Лос-Анджелесе.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2010-11-04', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 2.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Minecraft', 
#     description = 'компьютерная инди-игра в жанре песочницы, созданная шведским программистом Маркусом Перссоном и выпущенная его студией Mojang AB.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2011-11-18', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 29.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Forza Motorsport 3', 
#     description = 'Forza Motorsport 3 — компьютерная игра в жанре гоночного симулятора, разработанная студией Turn 10 Studios и изданная на Xbox 360. Игра вышла в октябре 2009 года и является третьей игрой в серии Forza Motorsport.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2009-10-22', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 7.58, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Mass Effect', 
#     description = 'Mass Effect — научно-фантастическая медиафраншиза, созданная Кейси Хадсоном, Дрю Карпишином и Престоном Ватаманюком. Франшиза рассказывает о далёком будущем, в котором люди и инопланетяне колонизировали Млечный Путь с помощью технологий древних цивилизаций.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2007-11-16', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 29.99, 
#     contentRating = ContentRating.objects.get(id=5),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'PGR4 - Project Gotham Racing 4', 
#     description = 'Project Gotham Racing 4 — видеоигра в жанре аркадных авто- и мотогонок, разработанная студией Bizarre Creations и изданная компанией Microsoft Game Studios эксклюзивно для консоли Xbox 360 в октябре 2007 года. За локализацию была ответственна компания «Софт Клаб», которая выпустила игру на русском языке.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2007-10-02', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 19.95, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Kinect Star Wars', 
#     description = 'Kinect Star Wars — видеоигра по вселенной «Звездных войн», разработанная Terminal Reality и опубликованная LucasArts и Microsoft Studios для Xbox 360, в которой используется периферийное устройство движения Kinect.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2012-04-03', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 6.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Alan Wake', 
#     description = 'Alan Wake — компьютерная игра 2010 года, разработанная финской студией Remedy Entertainment и изданная Microsoft Game Studios. Разработчики определяли жанр игры как «психологический экшен-триллер».', 
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
#     description = 'Lost Odyssey — японская ролевая игра, разработанная студией Mistwalker и feelplus, которая была издана Microsoft Game Studios эксклюзивно для Xbox 360. Игрок управляет персонажем по имени Каим, человеком, который живёт уже тысячу лет и ничего не помнит о своём прошлом.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2007-10-06', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 4.28, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=4), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Dance Central 3', 
#     description = 'Dance Central 3 — музыкальная видеоигра, разработанная и изданная Harmonix в сообществе с Backbone Entertainment. Это третья игра в серии Dance Central. Она была анонсирована на игровыставке E3 2012 во время пресс конференции Microsoft.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2012-10-16', 
#     publisher = Publisher.objects.get(id=3), 
#     price = 58.00, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Gran Turismo 3: A-Spec', 
#     description = 'Gran Turismo 3: A-Spec — видеоигра в жанре гоночного симулятора, первая игра из серии Gran Turismo, которая вышла на приставке Sony PlayStation 2. Gran Turismo 2000 было рабочим названием игры, когда она демонстрировалась на выставке Е3 в 2000—2001 годах.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2001-04-28', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 7.90, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = "Uncharted 3: Drake's Deception", 
#     description = "Uncharted 3: Drake's Deception, в России была издана под названием «Uncharted 3: Иллюзии Дрейка» — компьютерная игра в жанре приключенческого боевика с видом от третьего лица, разработанная американской компанией Naughty Dog.", 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2011-11-01', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 4.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'God of War III', 
#     description = 'God of War III — компьютерная игра в жанре hack and slash, выпущенная американской компанией Santa Monica Studio эксклюзивно для платформы PlayStation 3. В России игра вышла 17 марта 2010 года.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2010-03-16', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 19.99, 
#     contentRating = ContentRating.objects.get(id=5),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'EyeToy Play', 
#     description = 'EyeToy: Play - это видеоигра-сборник мини-игр для PlayStation 2, выпущенная в 2003 году. Это была первая игра, в которой использовалась видеокамера PlayStation 2, EyeToy. Игра изначально поставлялась с EyeToy, когда аксессуар был впервые выпущен.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2003-02-04', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 14.03, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sports Champions', 
#     description = 'Праздник Спорта — компьютерная игра 2010 года, разработанная San Diego Studio и Zindagi Games и издана Sony Computer Entertainment для PlayStation 3, в которой используется PlayStation Move. Она была официально представлена на конференции Game Developers Conference в San Francisco.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2010-09-07', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 29.99, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'inFAMOUS', 
#     description = 'inFamous — видеоигра в жанре приключенческого боевика, разработанная Sucker Punch Productions и изданная Sony Computer Entertainment. Игра была издана только для PlayStation 3: 26 мая 2009 года — в США, а 29 мая — в Европе.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2009-05-26', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 9.99, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Hot Shots Golf 3', 
#     description = "Everyone's Golf 3, известная в Северной Америке как Hot Shots Golf 3, является третьей игрой в серии Everyone's Golf и первой игрой, выпущенной для PlayStation 2.", 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2001-07-26', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 2.81, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'God of War Collection', 
#     description = 'God of War Collection — сборник, состоящий из обновлённых и портированных версий God of War и God of War II для PlayStation 3 на одном диске Blu-ray.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2009-11-17', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 13.99, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'SingStar', 
#     description = 'SingStar — серия соревновательных музыкальных игр для игровых приставок PlayStation. Игры серии разработаны компанией London Studio и изданы Sony Interactive Entertainment. Наибольшее число игр предназначено для приставок PlayStation 2 и PlayStation 3.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2004-05-03', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 54.98, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Buzz! The BIG Quiz', 
#     description = 'Buzz!: The BIG Quiz — вторая в Buzz! Серия игр для PlayStation 2, разработанная Relentless Software. Первоначальный рекламный материал назывался Buzz! Uber Quiz, однако Sony Computer Entertainment Europe объявила об изменении после запуска игры. Формат, по сути, тот же, что и у оригинала: Buzz!: Музыкальная викторина.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2006-03-17', 
#     publisher = Publisher.objects.get(id=4), 
#     price = 6.80, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Mario & Sonic at the Olympic Games', 
#     description = 'спортивная видеоигра, разработанная подразделением Sega Sports Japan и выпущенная Nintendo (в Японии) и Sega (в остальных регионах) в ноябре 2007 года (в России вышла в январе 2008 года) для Nintendo Wii и в январе и феврале 2008 года для Nintendo DS.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2007-11-06', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 33.25, 
#     contentRating = ContentRating.objects.get(id=3),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'MadWorld', 
#     description = "MadWorld — это игра в жанре beat 'em up hack and slash, разработанная PlatinumGames, изданная Sega, спродюсированная Ацуши Инаба и режиссером которой является Сигенори Нишикава. Он был выпущен во всем мире для Wii в марте 2009 года и в Японии в феврале 2010 года.", 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2009-03-10', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 12.80, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sega Superstars Tennis', 
#     description = 'Sega Superstars Tennis — теннисная видеоигра, разработанная Sumo Digital и изданная Sega. Является второй игрой в серии-кроссовере Sega Superstars. Она была выпущена на консоли Xbox 360, PlayStation 2, PlayStation 3, Wii и Nintendo DS 18 марта 2008 года в США, 20 марта в Европе и 25 марта в России.', 
#     platform = Platform.objects.get(id=2), 
#     releaseDate = '2006-03-17', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 5.73, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sonic Mega Collection Plus', 
#     description = 'Sonic Mega Collection Plus - сборник видеоигр сониковской серии с консолей Sega Mega Drive и Game Gear. Sonic Mega Collection Plus является усовершенствованной версией Sonic Mega Collection для Nintendo GameCube. Сборник вышел для Sony PlayStation 2, XBOX и PC.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2004-10-04', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 17.68, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'ESPN NFL 2K5', 
#     description = 'ESPN NFL 2K5 — видеоигра в американский футбол, разработанная Visual Concepts для консолей PlayStation 2 и Xbox. Изданная 2K Sports и Sega Corporation, это шестая часть серии NFL 2K и последняя, ​​в которой используется официальная лицензия NFL.', 
#     platform = Platform.objects.get(id=3), 
#     releaseDate = '2004-06-20', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 24.12, 
#     contentRating = ContentRating.objects.get(id=1),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Super Monkey Ball: Banana Blitz', 
#     description = 'Super Monkey Ball: Banana Blitz, в Японии известная как Super Monkey Ball: Exciting Party Collection — компьютерная игра из серии Super Monkey Ball, выпущенная эксклюзивно для игровой консоли Wii в 2006 году.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2006-11-14', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 24.69, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Sonic & Sega All-Stars Racing', 
#     description = 'Sonic & Sega All-Stars Racing, в версии для Xbox 360 известная как Sonic & Sega All-Stars Racing with Banjo-Kazooie — гоночная игра с участием персонажей из игр Sonic the Hedgehog, а также персонажами компании Sega. Игра была анонсирована 28 мая 2009 года.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '2010-02-23', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 10.63, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=1), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Football Manager 2012', 
#     description = 'Football Manager 2012 — компьютерная игра, симулятор футбольного менеджмента, часть серии Football Manager. Игра разработана компанией Sports Interactive на платформы Microsoft Windows и Mac OS X. Игра поступила в продажу 21 октября 2011 года. В России издаётся компанией 1С-СофтКлаб.', 
#     platform = Platform.objects.get(id=5), 
#     releaseDate = '2011-10-20', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 17.80, 
#     contentRating = ContentRating.objects.get(id=4),
#     genre = Genre.objects.get(id=2), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Yakuza 3', 
#     description = 'Yakuza 3 — компьютерная игра, разработанная и изданная компанией Sega. Часть серии Yakuza. Изначально игра была выпущена для игровой приставки PlayStation 3 в 2009 году и в последующем переиздана для платформ PlayStation 4, Xbox One и Windows.', 
#     platform = Platform.objects.get(id=4), 
#     releaseDate = '2009-02-26', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 35.63, 
#     contentRating = ContentRating.objects.get(id=5),
#     genre = Genre.objects.get(id=3), 
#     isAvailable = True)

# Product.objects.create(
#     title = 'Samba De Amigo', 
#     description = 'Samba de Amigo — компьютерная игра, разработанная командой Sonic Team и выпущенная Sega для аркадного автомата и консоли Dreamcast, в 1999 и 2000 годах. В 2008 году игра была выпущена для Wii. Портированием игры для Wii занималась компания Gearbox Software.', 
#     platform = Platform.objects.get(id=1), 
#     releaseDate = '1999-12-17', 
#     publisher = Publisher.objects.get(id=5), 
#     price = 16.50, 
#     contentRating = ContentRating.objects.get(id=2),
#     genre = Genre.objects.get(id=5), 
#     isAvailable = True)

price2 = Product.objects.filter(price>30)
pprint(Product)





