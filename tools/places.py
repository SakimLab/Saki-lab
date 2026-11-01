"""Content for every place on the site.

Each place has its story (PT and EN) and its curated photos, in the order they
appear on the page. A photo is (original upload number, file name, alt PT, alt EN).
Curated photos live in assets/img/lugares/<slug>/<name>.jpg; everything else
that was uploaded for a place is kept in assets/img/lugares/<slug>/arquivo/.
"""

PLACES = [
    {
        "slug": "sakim",
        "name": "Sakim",
        "where": {"pt": "Lisboa", "en": "Lisbon"},
        "kind": {"pt": "Gastro bar", "en": "Gastro bar"},
        "range": (506, 535),
        "cover": "sala-comprida",
        "line": {
            "pt": "A minha própria casa. Uma sala comprida, um chão aos quadrados e uma mesa onde estranhos acabam a partilhar o jantar.",
            "en": "My own house. A long room, a chequered floor and a table where strangers end up sharing dinner.",
        },
        "question": {
            "pt": "O que acontece quando quem desenha lugares para os outros abre um para si? Fiz o que sempre defendi: poucos elementos, todos com intenção — as garrafas na parede, a luz baixa, pratos que chegam como pequenas surpresas.",
            "en": "What happens when someone who designs places for others opens one of his own? I did what I've always preached: few elements, all of them deliberate — bottles on the wall, low light, plates that arrive like small surprises.",
        },
        "did": {
            "pt": "Conceito, espaço, carta — e a casa a funcionar todas as noites.",
            "en": "Concept, space, menu — and running the house every night.",
        },
        "photos": [
            (535, "rua-a-noite", "A porta do Sakim numa rua de Lisboa à noite", "Sakim's door on a Lisbon street at night"),
            (508, "fachada", "A fachada do Sakim com a esplanada", "Sakim's façade and terrace"),
            (509, "pela-porta", "A sala vista da porta, com o chão aos quadrados", "The room seen from the door, chequered floor"),
            (513, "candeeiros", "Candeeiros de papel sobre as mesas", "Paper lamps over the tables"),
            (521, "lustre", "Um lustre de vidro cor de âmbar", "An amber glass chandelier"),
            (517, "sala-comprida", "A sala comprida, pronta para a noite", "The long room, set for the night"),
            (520, "garrafas", "Garrafas de vinho presas à parede", "Wine bottles mounted on the wall"),
            (526, "prato-vermelho", "Um prato vermelho com flores", "A red dish with flowers"),
            (529, "tartaro", "Tártaro sobre pão, molho laranja", "Tartare on bread with an orange sauce"),
            (530, "sobremesa", "Sobremesa com figo e amor-perfeito", "Dessert with fig and a pansy"),
            (519, "mesa-longa", "Uma mesa longa cheia de gente a sorrir", "A long table full of smiling people"),
            (525, "noite-cheia", "Mesas e bancos sobre o chão aos quadrados", "Tables and stools on the chequered floor"),
            (534, "sala-e-bancos", "A sala com bancos altos e o chão aos quadrados", "The room with high stools and the chequered floor"),
            (516, "parede-de-garrafas", "Garrafas na parede ao longo da sala", "Bottles on the wall along the room"),
            (515, "entrada", "A entrada com espelho e lavatório dourado", "The entrance with a mirror and a golden basin"),
            (524, "mesa-para-o-jantar", "Uma mesa comprida posta para o jantar", "A long table laid for dinner"),
            (510, "bancos", "Bancos de madeira no chão vermelho e branco", "Wooden stools on a red and white floor"),
            (522, "garrafas-de-perto", "Garrafas presas à parede, de perto", "Bottles mounted on the wall, close up"),
        ],
    },
    {
        "slug": "so-what",
        "name": "So What",
        "where": {"pt": "Santos", "en": "Santos"},
        "kind": {"pt": "Clube de jazz & restaurante", "en": "Jazz club & restaurant"},
        "range": (458, 505),
        "logo": 458,
        "cover": "abobada-acesa",
        "line": {
            "pt": "Uma abóbada vazia que hoje tem fila à porta e um contrabaixo ao fundo.",
            "en": "An empty vault that now has a queue at the door and a double bass at the back.",
        },
        "question": {
            "pt": "Como se faz uma cave parecer que sempre teve jazz? Recuperámos móveis antigos, pintámos de vermelho o túnel de entrada e deixámos a música decidir o resto: o palco, a luz, a distância entre as mesas.",
            "en": "How do you make a cellar feel as if it has always had jazz? We rescued old cabinets, painted the entrance tunnel red and let the music decide the rest: the stage, the light, the distance between tables.",
        },
        "did": {
            "pt": "Conceito, transformação do espaço, mobiliário recuperado, bar, cozinha e música ao vivo.",
            "en": "Concept, transformation of the space, rescued furniture, bar, kitchen and live music.",
        },
        "photos": [
            (483, "fila-a-porta", "Fila à porta do So What", "A queue outside So What"),
            (466, "antes", "A abóbada vazia, antes das obras", "The empty vault, before the works"),
            (492, "movel-recuperado", "Um móvel antigo recuperado para o bar", "An old cabinet rescued for the bar"),
            (497, "abobada-acesa", "A abóbada pronta, com o bar aceso", "The finished vault with the bar lit"),
            (481, "tunel-vermelho", "O túnel de entrada pintado de vermelho", "The entrance tunnel painted red"),
            (480, "telefone-vermelho", "A abóbada vista da cabine de DJ", "The vault seen from the DJ booth"),
            (463, "mesa-posta", "Copos e uma vela na mesa", "Glasses and a candle on the table"),
            (472, "prato", "Um prato da cozinha", "A dish from the kitchen"),
            (476, "contrabaixo", "A mesa de DJ virada para a sala e o palco", "The DJ decks facing the room and the stage"),
            (474, "voz", "Um lustre de vidro sobre o balcão", "A glass chandelier over the bar"),
            (489, "bateria", "Dois telefones antigos no balcão", "Two old telephones on the bar"),
            (485, "sala-cheia", "Candeeiros antigos sobre o balcão", "Old lamps over the bar"),
            (486, "piano", "O piano depois do último tema", "The piano after the last tune"),
            (465, "esplanada", "A esplanada à noite", "The terrace at night"),
            (500, "armario-de-garrafas", "O móvel antigo cheio de garrafas, em luz vermelha", "The old cabinet full of bottles, lit in red"),
            (505, "panorama", "A sala inteira em panorâmica, com o balcão ao fundo", "The whole room in a panorama, the bar at the back"),
            (503, "palco", "O palco com cortinas vermelhas, cadeirões e piano", "The stage with red curtains, armchairs and a piano"),
            (499, "corredor", "O corredor da abóbada com bancos vermelhos", "The vaulted corridor with red benches"),
            (473, "bateria-no-tapete", "Uma bateria num tapete, à espera do concerto", "A drum kit on a rug, waiting for the show"),
            (482, "cadeiroes-na-calcada", "A esplanada na calçada, com cadeirões antigos", "The terrace on the pavement with old armchairs"),
        ],
    },
    {
        "slug": "social-b",
        "name": "Social B",
        "where": {"pt": "Cais do Sodré", "en": "Cais do Sodré"},
        "kind": {"pt": "Bar & clube", "en": "Bar & club"},
        "range": (131, 174),
        "extra": [1],
        "cover": "bar-violeta",
        "line": {
            "pt": "Uma cave abobadada no centro de Lisboa, feita para quando a noite já vai longa.",
            "en": "A vaulted cellar in central Lisbon, made for when the night is already long.",
        },
        "question": {
            "pt": "Como dar a uma cave antiga a energia de um clube sem lhe roubar a memória? Luz violeta nas abóbadas, cinema projectado na parede, um canto de biblioteca — e um balcão onde o chá também se serve em bule.",
            "en": "How do you give an old cellar the energy of a club without stealing its memory? Violet light on the vaults, films projected on the wall, a library corner — and a bar where tea also comes in a teapot.",
        },
        "did": {
            "pt": "Conceito e design de atmosfera.",
            "en": "Concept and atmosphere design.",
        },
        "photos": [
            (1, "letreiro", "O letreiro do Social B na rua, à noite", "The Social B sign on the street at night"),
            (131, "entrada", "A entrada abobadada", "The vaulted entrance"),
            (133, "bar-violeta", "O bar sob luz violeta", "The bar under violet light"),
            (152, "sofa-redondo", "Um sofá redondo debaixo da abóbada", "A round sofa under the vault"),
            (144, "balcao-rosas", "Rosas vermelhas num balcão aos quadrados", "Red roses on a chequered bar"),
            (164, "bules", "Bules e torneiras de cerveja", "Teapots and beer taps"),
            (146, "petiscos", "Croquetes com molho", "Croquettes with sauce"),
            (160, "copo-canela", "Uma bebida com canela e anis", "A drink with cinnamon and star anise"),
            (139, "cinema", "Um filme projectado sobre a sala", "A film projected over the room"),
            (150, "biblioteca", "O canto da biblioteca", "The library corner"),
            (147, "dj", "DJ e pista cheia", "A DJ and a full floor"),
            (156, "logo-azul", "O logo projectado em azul no tecto", "The logo projected in blue on the ceiling"),
            (132, "sala-comprida", "A sala comprida sob os arcos, com candeeiros acesos", "The long room under the arches, lamps lit"),
            (134, "balcao-de-madeira", "O balcão de madeira com bancos altos", "The wooden bar with high stools"),
            (154, "bancada", "A bancada de trás, com frascos, chávenas e máquina de café", "The back counter with jars, cups and a coffee machine"),
            (136, "arco", "O bar visto do fundo, sob o arco", "The bar from the back, under the arch"),
            (174, "torneiras", "Torneiras de cerveja e bules de porcelana", "Beer taps and porcelain teapots"),
            (172, "chavena", "Uma chávena e um bule com flores no balcão", "A cup and a flowered teapot on the bar"),
            (155, "tunel-violeta", "O túnel iluminado de violeta", "The tunnel lit in violet"),
            (168, "lustre", "Um lustre de arame sob a abóbada", "A wire chandelier under the vault"),
        ],
    },
    {
        "slug": "a-tabacaria",
        "name": "A Tabacaria",
        "where": {"pt": "Cais do Sodré", "en": "Cais do Sodré"},
        "kind": {"pt": "Bar de rum", "en": "Rum bar"},
        "range": (4, 81),
        "cover": "balcao",
        "line": {
            "pt": "Uma tabacaria de 1885 que nunca deixou de vender pequenos prazeres. Só mudou de horário.",
            "en": "An 1885 tobacconist that never stopped selling small pleasures. It just changed its hours.",
        },
        "question": {
            "pt": "Como abrir um bar sem apagar mais de um século de história? Não escondendo nada: o balcão de madeira, os letreiros da lotaria, o Totobola, os frascos de boticário. O rum e os cocktails entraram como mais um produto da casa.",
            "en": "How do you open a bar without erasing more than a century of history? By hiding nothing: the wooden counter, the lottery signs, the football-pools sign, the apothecary jars. Rum and cocktails simply became one more thing the shop sells.",
        },
        "did": {
            "pt": "Conceito completo, programa de bar, direção de cocktails e estratégia de lançamento.",
            "en": "Full concept, bar programme, cocktail direction and launch strategy.",
        },
        "photos": [
            (30, "fachada", "A fachada de azulejo verde", "The green-tiled façade"),
            (12, "porta-a-noite", "A porta d'A Tabacaria à noite", "A Tabacaria's door at night"),
            (5, "balcao", "O balcão de madeira de 1885", "The 1885 wooden counter"),
            (45, "janela-electrico", "Um eléctrico visto da janela", "A tram seen through the window"),
            (27, "candeeiro", "Candeeiro esmaltado sobre as garrafas", "An enamel lamp over the bottles"),
            (16, "totobola", "O letreiro antigo do Totobola", "The old football-pools sign"),
            (29, "gramofone", "Um gramofone entre a fruta", "A gramophone among the fruit"),
            (35, "boticario", "Frascos de boticário na penumbra", "Apothecary jars in the half-light"),
            (48, "frasco", "Um frasco com o rótulo da casa", "A jar with the house label"),
            (34, "torneiras", "Torneiras antigas de cerveja", "Old beer taps"),
            (55, "tabua", "Uma tábua de petiscos e um cocktail", "A board of snacks and a cocktail"),
            (58, "macarico", "Carne a ser maçaricada", "Meat being torched"),
            (72, "espuma", "Um cocktail com espuma", "A cocktail with foam"),
            (74, "petalas", "Um cocktail com pétalas", "A cocktail with petals"),
            (76, "vermelho", "Um cocktail vermelho com lima", "A red cocktail with lime"),
            (78, "janela-gramofone", "O gramofone à janela, com o eléctrico lá fora", "The gramophone at the window, a tram outside"),
            (44, "sala-a-noite", "A sala à noite", "The room at night"),
            (15, "ultima-luz", "O bar com a última luz acesa", "The bar with the last light on"),
        ],
    },
    {
        "slug": "velha-senhora",
        "name": "O Bar da Velha Senhora",
        "where": {"pt": "Cais do Sodré", "en": "Cais do Sodré"},
        "kind": {"pt": "Restaurante, bar & clube", "en": "Restaurant, bar & club"},
        "range": (386, 457),
        "logo": 386,
        "cover": "porta",
        "line": {
            "pt": "Burlesco, música de câmara e jantar na mesma noite — às vezes na mesma mesa.",
            "en": "Burlesque, chamber music and dinner on the same night — sometimes at the same table.",
        },
        "question": {
            "pt": "Como se cria um palco onde tudo pode acontecer? Uma sala de candeeiros antigos e corações na parede, mesas feitas à medida, e uma programação que vai do quarteto de cordas ao cabaré.",
            "en": "How do you build a stage where anything can happen? A room of old lamps and hearts on the wall, tables made to measure, and a programme that runs from string quartet to cabaret.",
        },
        "did": {
            "pt": "Conceito, construção do espaço, restaurante, bar e música ao vivo.",
            "en": "Concept, building the space, restaurant, bar and live music.",
        },
        "photos": [
            (392, "porta", "A porta à noite, com gente cá fora", "The door at night, people outside"),
            (457, "rua-rosa", "A rua cor-de-rosa", "The pink street"),
            (416, "mesas-em-obra", "Mesas de ferro a ser feitas", "Iron tables being made"),
            (450, "arco-verde", "O arco verde em construção", "The green arch being built"),
            (433, "candeeiros", "Candeeiros antigos e luzes", "Old lamps and string lights"),
            (410, "coracoes", "O bar com a parede de corações", "The bar with its wall of hearts"),
            (455, "candeeiros-velhos", "Uma colecção de candeeiros antigos", "A collection of old lamps"),
            (434, "jantar", "Jantar visto de cima", "Dinner from above"),
            (414, "quarteto", "Quarteto de cordas sob o mural", "A string quartet under the mural"),
            (393, "danca", "Uma bailarina em palco", "A dancer on stage"),
            (396, "leque", "A entrada do bar, com um cocktail na mesa da rua", "The entrance, with a cocktail on the street table"),
            (399, "cantora", "A sala decorada para o Halloween", "The room dressed for Halloween"),
            (412, "mascaras", "Convidados mascarados", "Masked guests"),
            (445, "festa", "Painéis pintados e chão cor-de-rosa", "Painted panels and a pink floor"),
            (448, "chao-xadrez", "Uma estrutura de ferro sobre o chão aos quadrados", "An iron frame on the chequered floor"),
            (451, "cocktail", "Um cocktail na mesa da rua, à porta do bar", "A cocktail on the street table by the door"),
            (401, "abobada", "O bar comprido sob a abóbada de tijolo", "The long bar under the brick vault"),
            (419, "nicho-verde", "Um nicho verde-água na parede de tijolo", "A turquoise niche in the brick wall"),
            (420, "mural", "Um mural de uma mulher deitada sobre a sala", "A mural of a reclining woman above the room"),
            (421, "piano", "Um piano vermelho com plumas e luzes", "A red piano with feathers and lights"),
        ],
    },
    {
        "slug": "clube-ferroviario",
        "name": "Clube Ferroviário",
        "where": {"pt": "Santa Apolónia", "en": "Santa Apolónia"},
        "kind": {"pt": "Terraço", "en": "Rooftop"},
        "range": (271, 322),
        "logo": 271,
        "cover": "navio",
        "line": {
            "pt": "Um terraço sobre o Tejo onde os navios de cruzeiro passam a fazer parte da decoração.",
            "en": "A terrace over the Tagus where cruise ships become part of the décor.",
        },
        "question": {
            "pt": "Como se devolve a vida a um clube histórico dos ferroviários? De dia, relva, espreguiçadeiras e o rio à frente. À noite, concertos, bailes e cinema ao ar livre.",
            "en": "How do you bring a historic railway workers' club back to life? By day, grass, deckchairs and the river in front. By night, concerts, dances and open-air cinema.",
        },
        "did": {
            "pt": "Conceito, programa de bar, agenda cultural e lançamento.",
            "en": "Concept, bar programme, cultural programme and launch.",
        },
        "photos": [
            (276, "navio", "O terraço vazio sob um céu nublado", "The empty terrace under a cloudy sky"),
            (279, "relva", "Mesas do terraço sob o toldo", "Terrace tables under the awning"),
            (283, "mesas-e-navio", "Sofás laranja e um navio de cruzeiro atrás", "Orange sofas with a cruise ship behind"),
            (281, "bar", "O bar ao ar livre", "The open-air bar"),
            (295, "baile", "Espreguiçadeiras na relva com o Tejo ao fundo", "Loungers on the grass with the Tagus behind"),
            (318, "cinema-mudo", "Sofás azuis e espreguiçadeiras junto ao rio", "Blue sofas and loungers by the river"),
            (285, "concerto", "Multidão num concerto", "A crowd at a concert"),
            (304, "ecra", "O ecrã de cinema ao ar livre", "The open-air cinema screen"),
            (289, "contrabaixo", "Contrabaixo ao anoitecer", "A double bass at dusk"),
            (287, "candeeiro", "O terraço com plantas ao fim do dia", "The terrace with plants at dusk"),
            (303, "anoitecer", "O terraço ao anoitecer, com um navio iluminado", "The terrace at dusk with a lit ship"),
            (272, "2009-e-2014", "O terraço em 2009 e em 2014", "The terrace in 2009 and in 2014"),
            (277, "plantas-e-rio", "Mesas entre plantas, com o Tejo ao fundo", "Tables among plants, the Tagus behind"),
            (311, "musica-ao-vivo", "Música ao vivo sob luz azul", "Live music under blue light"),
            (298, "candeeiros-de-palha", "Candeeiros de palha sobre as mesas, com o rio ao fundo", "Wicker lamps over the tables, the river behind"),
            (292, "mesa-comprida", "Uma mesa comprida posta junto ao rio", "A long table laid by the river"),
            (293, "toalhas-brancas", "Mesas com toalhas brancas sobre a relva", "Tables with white cloths on the grass"),
            (308, "panorama", "O terraço inteiro em panorâmica", "The whole terrace in a panorama"),
            (321, "relva-e-ceu", "A relva e o céu azul sobre o rio", "The lawn under a blue sky by the river"),
            (320, "anoitecer-azul", "O terraço sob um céu azul ao anoitecer", "The terrace under a blue evening sky"),
        ],
    },
    {
        "slug": "o-terraco",
        "name": "O Terraço",
        "where": {"pt": "Lisboa", "en": "Lisbon"},
        "kind": {"pt": "Bar de terraço", "en": "Rooftop bar"},
        "range": (82, 101),
        "cover": "por-do-sol",
        "line": {
            "pt": "Um telhado no centro histórico, uma rede de sombra e Lisboa inteira a mudar de cor.",
            "en": "A rooftop in the old centre, a canopy of shade and the whole of Lisbon changing colour.",
        },
        "question": {
            "pt": "Como fazer as pessoas ficarem do pôr do sol até à noite? Sofás em vez de cadeiras, lanternas que se acendem devagar, música ao vivo quando o céu escurece.",
            "en": "How do you get people to stay from sunset into the night? Sofas instead of chairs, lanterns that come on slowly, live music as the sky goes dark.",
        },
        "did": {
            "pt": "Direção de conceito e design de atmosfera.",
            "en": "Concept direction and atmosphere design.",
        },
        "photos": [
            (90, "tarde", "Amigas num sofá ao fim da tarde", "Friends on a sofa in the late afternoon"),
            (85, "gente", "O terraço cheio ao sol", "The terrace full in the sun"),
            (93, "sesta", "Alguém a dormir num sofá sobre Lisboa", "Someone asleep on a sofa above Lisbon"),
            (88, "guitarra", "Guitarra sob a sombra colorida", "A guitar under the coloured canopy"),
            (100, "por-do-sol", "O pôr do sol debaixo da rede", "Sunset under the canopy"),
            (95, "lanternas", "Lanternas acesas ao anoitecer", "Lanterns lit at dusk"),
            (101, "hora-azul", "A hora azul sobre o rio", "Blue hour over the river"),
            (86, "sofas-a-sombra", "Sofás sob a rede de sombra, com gente a descansar", "Sofas under the shade net, people lounging"),
            (84, "sofa-branco", "Um sofá branco no terraço, com o rio ao fundo", "A white sofa on the terrace, the river behind"),
            (94, "espreguicadeiras", "Espreguiçadeiras de madeira viradas para a cidade", "Wooden loungers facing the city"),
            (83, "cinema", "Uma projecção no terraço à noite", "A projection on the terrace at night"),
            (82, "almofadas-vermelhas", "Gente sentada em almofadas vermelhas", "People sitting on red floor cushions"),
            (96, "vista-ao-anoitecer", "O terraço ao anoitecer, com Lisboa ao fundo", "The terrace at dusk, Lisbon behind"),
        ],
    },
    {
        "slug": "o-larguinho",
        "name": "O Larguinho",
        "where": {"pt": "Alfama", "en": "Alfama"},
        "kind": {"pt": "Bar de tapas", "en": "Tapas bar"},
        "range": (175, 196),
        "cover": "largo-ao-anoitecer",
        "line": {
            "pt": "“A alegria é a coisa mais séria da vida” — está escrito na parede, e o resto do bar leva isso a sério.",
            "en": "“Joy is the most serious thing in life” — it's written on the wall, and the rest of the bar takes it seriously.",
        },
        "question": {
            "pt": "Como se faz um bar de bairro onde o bairro se sente em casa? Uma esplanada no largo, o eléctrico a passar, tapas para partilhar e a porta sempre aberta.",
            "en": "How do you make a neighbourhood bar where the neighbourhood feels at home? A terrace on the little square, the tram going by, tapas to share and the door always open.",
        },
        "did": {
            "pt": "Conceito, carta de tapas e estratégia de abertura.",
            "en": "Concept, tapas menu and opening strategy.",
        },
        "photos": [
            (179, "electrico", "O eléctrico a passar pela esplanada", "The tram passing the terrace"),
            (188, "largo-ao-anoitecer", "O largo ao anoitecer", "The little square at dusk"),
            (175, "mural", "O mural: a alegria é a coisa mais séria da vida", "The mural: joy is the most serious thing in life"),
            (181, "porta-aberta", "Poltronas junto à porta aberta, sob o tecto decorado", "Armchairs by the open door, under the decorated ceiling"),
            (183, "parede-amarela", "Uma parede amarela com grafitti", "A yellow wall with graffiti"),
            (178, "lata", "Um candeeiro feito de lata de sopa", "A lamp made from a soup can"),
            (190, "chapeus", "Dois amigos de chapéu à mesa", "Two friends in hats at a table"),
            (189, "noite", "O balcão e a sala por dentro", "The bar counter and the room inside"),
            (176, "mural-alegria", "Cadeiras sob um mural: «A alegria é a coisa mais séria da vida»", "Seats under a mural: 'Joy is the most serious thing in life'"),
            (193, "tecto-de-luzes", "Uma sala com tecto de luzes e um móvel antigo", "A room with a ceiling of lights and an old cabinet"),
            (180, "porta-estreita", "Uma porta estreita aberta para a sala", "A narrow door open onto the room"),
        ],
    },
    {
        "slug": "bica-me",
        "name": "Bica-me",
        "where": {"pt": "Bica", "en": "Bica"},
        "kind": {"pt": "Mercearia & bar", "en": "Grocery & bar"},
        "range": (102, 121),
        "logo": 102,
        "cover": "velas",
        "line": {
            "pt": "Uma mercearia de dia, um bar à luz das velas à noite.",
            "en": "A grocery by day, a candlelit bar by night.",
        },
        "question": {
            "pt": "Como fazer uma loja de produtos artesanais onde apetece ficar? Prateleiras que se lêem como uma despensa, enchidos e queijos ao balcão, vinhos naturais e velas nas mesas quando a rua escurece.",
            "en": "How do you make a shop of artisan products where people want to stay? Shelves that read like a pantry, charcuterie and cheese at the counter, natural wines, and candles on the tables when the street gets dark.",
        },
        "did": {
            "pt": "Conceito, identidade e programa de comida.",
            "en": "Concept, identity and food programme.",
        },
        "photos": [
            (103, "entrada", "A entrada da Bica-me", "The Bica-me entrance"),
            (110, "prateleiras", "Prateleiras e luzes suspensas", "Shelves and hanging lights"),
            (107, "despensa", "Frascos e garrafas na despensa", "Jars and bottles in the pantry"),
            (114, "vitrine", "A vitrine de queijos e doces", "The cheese and pastry counter"),
            (105, "tabua", "Enchidos, queijo e um copo de vinho", "Charcuterie, cheese and a glass of wine"),
            (120, "vinhos", "Paredes de vinho", "Walls of wine"),
            (119, "velas", "Prateleiras de produtos e o balcão ao fundo", "Shelves of goods and the counter at the back"),
            (121, "mesa-e-vinhos", "Uma mesa de madeira diante das prateleiras de vinho", "A wooden table in front of the wine shelves"),
            (111, "mercearia", "A mercearia com prateleiras cheias e o balcão ao fundo", "The grocery with full shelves and the counter behind"),
            (115, "sala-a-noite", "A sala à noite vista de cima, com a porta aberta", "The room at night from above, the door open"),
            (113, "escada", "Mesas junto às prateleiras e à escada", "Tables by the shelves and the stairs"),
            (106, "movel-antigo", "A sala com velas e um móvel antigo", "The room with candles and an old cabinet"),
        ],
    },
    {
        "slug": "bicaense",
        "name": "Bicaense",
        "where": {"pt": "Bica", "en": "Bica"},
        "kind": {"pt": "Bar & clube", "en": "Bar & club"},
        "range": (122, 130),
        "cover": "jardim-de-luz",
        "line": {
            "pt": "Luz de cor, um balcão curvo e um jardim a crescer pelas paredes.",
            "en": "Coloured light, a curved bar and a garden growing up the walls.",
        },
        "question": {
            "pt": "Como fazer um bar mudar de humor ao longo da noite? Com luz cromática que pinta as paredes, um balcão que convida a dar a volta e uma instalação botânica que suaviza tudo.",
            "en": "How do you make a bar change mood through the night? With chromatic light that paints the walls, a bar you want to walk around, and a botanical installation that softens everything.",
        },
        "did": {
            "pt": "Conceito, programa de bar e design de atmosfera.",
            "en": "Concept, bar programme and atmosphere design.",
        },
        "photos": [
            (122, "jardim-de-luz", "Ramos e luz colorida na parede", "Branches and coloured light on the wall"),
            (123, "ramos", "A instalação botânica sob luz rosa", "The botanical installation under pink light"),
            (124, "balcao-curvo", "O balcão curvo", "The curved bar"),
            (129, "balcao-comprido", "O balcão comprido com bancos vermelhos e a porta para o pátio", "The long bar with red stools and the door to the courtyard"),
            (130, "garrafeira-acesa", "O balcão à noite, com a garrafeira iluminada", "The bar at night with the lit bottle shelves"),
            (127, "projeccao", "Luzes coloridas e uma projecção na parede", "Coloured lights and a projection on the wall"),
        ],
    },
    {
        "slug": "ricucu",
        "name": "Ricucu",
        "where": {"pt": "Praia Verde, Algarve", "en": "Praia Verde, Algarve"},
        "kind": {"pt": "Bar de praia", "en": "Beach bar"},
        "range": (323, 385),
        "cover": "porta-roxa",
        "line": {
            "pt": "Um deck branco nas dunas, redes ao vento e uma porta roxa aberta para a lua.",
            "en": "A white deck in the dunes, hammocks in the wind and a purple door open to the moon.",
        },
        "question": {
            "pt": "Como se desenha um bar de praia que não compete com a paisagem? Madeira branca, colmo, redes para ficar — e uma única cor forte, para lembrar que aqui também é noite.",
            "en": "How do you design a beach bar that doesn't compete with the landscape? White wood, thatch, hammocks to linger in — and a single strong colour, to remind you that night happens here too.",
        },
        "did": {
            "pt": "Conceito completo, identidade, programa de bar e estratégia de abertura.",
            "en": "Full concept, identity, bar programme and opening strategy.",
        },
        "photos": [
            (384, "porta-roxa", "O deck com mesas brancas debaixo da palapa", "The deck with white tables under the palapa"),
            (347, "deck", "O deck com a parede rosa e o mar", "The deck with the pink wall and the sea"),
            (323, "rede", "Uma rede debaixo do colmo", "A hammock under the thatch"),
            (340, "rede-e-mar", "Rede com o mar ao fundo", "A hammock with the sea behind"),
            (343, "espreguicadeiras", "Espreguiçadeiras no deck", "Loungers on the deck"),
            (349, "bar-a-noite", "O bar aceso à noite", "The bar lit at night"),
            (348, "lanterna", "Uma lanterna sobre as mesas", "A lantern over the tables"),
            (383, "dunas", "As dunas ao anoitecer", "The dunes at dusk"),
            (385, "fim-do-dia", "A estrutura de madeira ao fim do dia", "The wooden structure at the end of the day"),
            (324, "deck-branco", "O deck branco sob o colmo, com mesas", "The white deck under the thatch, with tables"),
            (325, "rede-vermelha", "Uma rede vermelha junto à parede roxa", "A red hammock by the purple wall"),
            (329, "almofadas", "Almofadas e uma rede no deck", "Cushions and a hammock on the deck"),
            (336, "garrafas-sob-o-colmo", "O bar à noite, com garrafas sob o colmo", "The bar at night, bottles under the thatch"),
            (337, "luz-vermelha", "Mesas em luz vermelha à noite", "Tables in red light at night"),
            (334, "candeeiro-de-palha", "Um candeeiro de palha aceso sobre as mesas", "A wicker lamp lit over the tables"),
            (361, "redes-e-dunas", "Redes e mesas brancas junto às dunas", "Hammocks and white tables by the dunes"),
            (363, "esplanada", "A esplanada branca sob o colmo", "The white terrace under the thatch"),
            (377, "espreguicadeiras-pretas", "Espreguiçadeiras pretas no deck", "Black loungers on the deck"),
            (366, "palapa", "Uma rede debaixo da palapa, com o mar ao longe", "A hammock under the palapa, the sea far off"),
        ],
    },
    {
        "slug": "monte-da-lua",
        "name": "Monte da Lua",
        "where": {"pt": "Moçambique", "en": "Mozambique"},
        "kind": {"pt": "Retiro", "en": "Retreat"},
        "range": (261, 270),
        "cover": "cabana-a-noite",
        "line": {
            "pt": "Cabanas de colmo na costa de Moçambique, sem rede eléctrica e sem pressa.",
            "en": "Thatched huts on the coast of Mozambique, off the grid and in no hurry.",
        },
        "question": {
            "pt": "Como se recebe alguém onde não há nada — quando é exactamente isso que procura? Luz de lanterna, camas viradas para o pôr do sol, caminhos de areia e só o indispensável.",
            "en": "How do you welcome someone where there is nothing — when that's exactly what they came for? Lantern light, beds facing the sunset, sand paths and only what's essential.",
        },
        "did": {
            "pt": "Conceito de hospitalidade, experiência de hóspede e estratégia de F&B.",
            "en": "Hospitality concept, guest experience and F&B strategy.",
        },
        "photos": [
            (263, "cabana-a-noite", "Uma cabana iluminada à noite", "A hut lit up at night"),
            (261, "cabana", "Uma cabana de colmo", "A thatched hut"),
            (264, "caminho", "Um caminho de areia entre a vegetação", "A sand path through the bush"),
            (265, "interior", "O interior de madeira", "The wooden interior"),
            (262, "por-do-sol", "Uma cama virada para o pôr do sol", "A bed facing the sunset"),
            (266, "varanda", "A varanda ao fim da tarde", "The veranda at the end of the day"),
            (267, "sala-de-madeira", "Uma sala de madeira com cortinas laranja", "A wooden room with orange curtains"),
        ],
    },
    {
        "slug": "house-4",
        "name": "House 4",
        "where": {"pt": "Bairro Alto", "en": "Bairro Alto"},
        "kind": {"pt": "Alojamento local", "en": "Guesthouse"},
        "range": (202, 260),
        "logo": 202,
        "cover": "corredor-rosa",
        "line": {
            "pt": "Uma casa de hóspedes onde cada corredor tem a sua cor.",
            "en": "A guesthouse where every corridor has its own colour.",
        },
        "question": {
            "pt": "Como se faz um alojamento de que alguém se lembra depois de fazer a mala? Corredores rosa e violeta, uma parede de cobre, peças mid-century e pequenos detalhes com humor.",
            "en": "How do you make a guesthouse someone remembers after packing their bag? Pink and violet corridors, a copper wall, mid-century pieces and small details with a sense of humour.",
        },
        "did": {
            "pt": "Conceito de interior e experiência de hóspede.",
            "en": "Interior concept and guest experience.",
        },
        "photos": [
            (203, "fachada", "Um quarto com cama de casal e candeeiro", "A bedroom with a double bed and a lamp"),
            (212, "corredor-rosa", "O corredor com luzes no tecto como estrelas", "The corridor with star-like ceiling lights"),
            (207, "porta-rosa", "Uma porta aberta no corredor rosa", "A door open off the pink corridor"),
            (229, "luz-violeta", "Um quarto branco com janela para a rua", "A white bedroom with a window onto the street"),
            (214, "cadeira", "Uma cadeira mid-century à janela", "A mid-century chair by the window"),
            (226, "algemas", "A casa de banho com lavatório vermelho", "The bathroom with a red basin"),
            (237, "lavatorio", "Lavatório de aço", "A steel washbasin"),
            (225, "sofa", "Um sofá branco e um candeeiro aceso", "A white sofa and a lit lamp"),
            (232, "bar-branco", "Um bar branco com garrafas, em duas imagens", "A white bar with bottles, in two pictures"),
            (245, "cama-castanha", "Uma cama com colcha castanha e parede dourada", "A bed with a brown cover and a golden wall"),
            (248, "toalhas", "Um quarto com toalhas dobradas na cama", "A bedroom with folded towels on the bed"),
            (238, "candeeiro-vermelho", "Um quarto com um candeeiro vermelho", "A bedroom with a red lamp"),
            (252, "parede-dourada", "Almofadas brancas contra uma parede de cobre", "White pillows against a copper wall"),
            (256, "casa-de-banho", "Uma casa de banho com banheira vermelha", "A bathroom with a red bathtub"),
            (257, "secretaria", "Um quarto branco com secretária e porta rosa", "A white bedroom with a desk and a pink door"),
            (259, "candeeiro-de-mesa", "Uma secretária com candeeiro, junto à porta rosa", "A desk with a lamp by the pink door"),
        ],
    },
    {
        "slug": "afro-taska",
        "name": "Afro Taska",
        "where": {"pt": "Lisboa", "en": "Lisbon"},
        "kind": {"pt": "Tasca africana", "en": "African tasca"},
        "range": (197, 201),
        "cover": "mesas",
        "line": {
            "pt": "Uma tasca onde a cozinha da África Ocidental se senta à mesa portuguesa.",
            "en": "A tasca where West African cooking sits down at a Portuguese table.",
        },
        "question": {
            "pt": "Como se juntam duas tradições de mesa sem as transformar em decoração? Murais geométricos, tecido wax — e a comida como ponto de partida.",
            "en": "How do you bring two table traditions together without turning them into decoration? Geometric murals, wax fabric — and the food as the starting point.",
        },
        "did": {
            "pt": "Conceito completo e montagem do restaurante.",
            "en": "Full concept and restaurant setup.",
        },
        "photos": [
            (197, "sala", "A sala com murais geométricos", "The room with geometric murals"),
            (198, "mesas", "Gente à mesa ao fim do dia", "People at the table in the evening"),
            (199, "bolo", "Um bolo com velas sob o mural", "A cake with candles under the mural"),
            (200, "bolos", "Bolos sob uma campânula de vidro, velas e maçãs", "Cakes under a glass dome, candles and apples"),
        ],
    },
]

# Photos used outside a single place
SITE_PHOTOS = {
    2: "assets/img/marca/sakim-logo.jpg",
    3: "assets/img/lisboa/janela-sobre-o-rio.jpg",
}


def photo_path(place, i):
    """Path of a curated photo, relative to the site root."""
    _, name, _, _ = place["photos"][i]
    return f"assets/img/lugares/{place['slug']}/{name}.jpg"


def cover_path(place):
    """The place's main photo, or None while it has no photos."""
    if not place.get("cover"):
        return None
    return f"assets/img/lugares/{place['slug']}/{place['cover']}.jpg"


# Where each project is, for the map on its page.
# geo:  (latitude, longitude) the map is centred on
# zoom: map zoom (16 a street, 15 a neighbourhood, 12 a town, 5 a country)
# mark: "pin" for a confirmed address, "area" when only the neighbourhood or town is known,
#       None when the place is not yet known (the map then just shows the city or country)
# addr: what is written under the map
# Addresses found online (Time Out Lisboa, Observador, The Infatuation, listings), October 2026.
GEO = {
    "a-tabacaria":       {"geo": (38.7078, -9.1468), "zoom": 16, "mark": "pin", "addr": "Rua de São Paulo, 75 · Cais do Sodré"},
    "o-terraco":         {"geo": (38.7139, -9.1394), "zoom": 13, "mark": None, "addr": "Lisboa"},          # address to confirm
    "bica-me":           {"geo": (38.7103, -9.1472), "zoom": 15, "mark": "area", "addr": "Bica"},
    "bicaense":          {"geo": (38.7097, -9.1465), "zoom": 16, "mark": "pin", "addr": "Rua da Bica de Duarte Belo · Bica"},
    "social-b":          {"geo": (38.7084, -9.1497), "zoom": 16, "mark": "pin", "addr": "Rua da Boavista, 116 · Santos"},
    "o-larguinho":       {"geo": (38.7115, -9.1305), "zoom": 15, "mark": "area", "addr": "Alfama"},
    "afro-taska":        {"geo": (38.7139, -9.1394), "zoom": 13, "mark": None, "addr": "Lisboa"},          # address to confirm
    "house-4":           {"geo": (38.7146, -9.1449), "zoom": 16, "mark": "pin", "addr": "Travessa de São Pedro, 9 · Bairro Alto"},
    "monte-da-lua":      {"geo": (-18.6, 35.5), "zoom": 5, "mark": None, "addr": "Moçambique"},           # place to confirm
    "clube-ferroviario": {"geo": (38.7140, -9.1228), "zoom": 16, "mark": "pin", "addr": "Rua de Santa Apolónia, 59"},
    "ricucu":            {"geo": (37.1795, -7.4870), "zoom": 13, "mark": "area", "addr": "Praia Verde · Algarve"},
    "velha-senhora":     {"geo": (38.7069, -9.1440), "zoom": 16, "mark": "pin", "addr": "Rua Nova do Carvalho, 40 · Cais do Sodré"},
    "so-what":           {"geo": (38.7076, -9.1552), "zoom": 15, "mark": "area", "addr": "Santos"},
    "sakim":             {"geo": (38.7139, -9.1394), "zoom": 13, "mark": None, "addr": "Lisboa"},          # address to confirm
}

# Which of the four service areas (A-D, see content.SERVICES) each project had. All four unless listed.
SERVICES_DONE = {}


def services_done(slug):
    return SERVICES_DONE.get(slug, ["A", "B", "C", "D"])
