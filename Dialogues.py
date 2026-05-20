languages = {
    "ru": {
        "gen_desc_main_locations": [("Мой дорогой друг, ты оказался достаточно храбр, чтобы добраться сюда.\n"
                                     "Наше путешествие начинается отсюда, мой дорогой гость — от холодного костра.\n"
                                     "Ты идешь навстречу новым приключениям и уже обнаружил \n"
                                     "первое из них. Перед тобой пещера, но ты не совсем уверен, что \n"
                                     "находится внутри. Тебе интересно исследовать её, но в то же время ты странно \n"
                                     "озадачен этой пещерой. Ты пытаешься подойти к ней осторожно...")],

        "gen_desc_quests": [("\"Здесь темно, и я слышу кого-то там, глубоко в пещере\", \n"
                             "— говоришь ты. Ты думаешь о нескольких способах справиться с этим:\n"
                             "\t1. Ты можешь проигнорировать пещеру и пойти дальше по дороге рядом с ней.\n"
                             "\t2. Тем не менее, ты не знаешь, что внутри пещеры, но \n"
                             "\tчто если прокрасться внутрь, забрать всё ценное и выбраться оттуда?\n"
                             "\t3. Потому что там может быть что-то очень опасное, и ты \n"
                             "\tможешь начать бой с мобами")],

        "quest_get_option": "Какую опцию ты хочешь выбрать? (Введи номер из списка выше) ",

        "quest1": (
            "КВЕСТ 1",
            {
                "fight": {
                    "kill": "К сожалению, ты был убит",
                    "success": "Это было тяжело, но ты отлично сражался и выиграл битву за Пещеру"
                },

                "end_of_quest": {
                    "1": "\nТеперь ты снаружи пещеры и идешь дальше по дороге."
                         "\nНа улице темно, поэтому ты решил немного отдохнуть",
                    "2": "\nТы смотришь на себя в реку, как в зеркало, и удивляешься этому магическому эффекту...",
                },

                "options": {
                    "1": "Ну, иногда лучше избежать возможной проблемы.\nТем не менее, ты не получаешь приз",
                    "2": {
                        "successful": "Хе-е-ей! Ты пробрался внутрь незаметно и нашел там кое-что действительно интересное",
                        "fail": "Тебя заметили, пока ты пробирался в пещеру.\nБой начался"
                    },
                    "3": {
                        "successful": "Ты начал действительно жестокую битву с монстрами",
                        "fail": "Там было два гигантских зомби, которые, к сожалению, убили тебя..."
                    }
                }
            }
        ),
        "game_save": "Хочешь ли ты сохранить свой игровой прогресс? ",
        "saver_save": "Как бы ты хотел назвать файл сохранения? ",
        "death": "К сожалению, ты был убит",
        "greeting": ("Добро пожаловать в игру D&D Light\n"
                     "Концепция игры такая же, как и в D&D\n"
                     "Игра состоит из некоторого количества квестов, которые тебе нужно выполнить\n"
                     "Затем ты переходишь на стадию босса, и это всё\n"
                     "Довольно просто, не так ли?\n"
                     "Так что давай попробуем эту игру!"),

        "print_player_classes": ("Вот классы, за которые ты можешь играть в этой игре:\n"
                                 "1. Archer\n"
                                 "2. Wizard\n"
                                 "3. Gnome\n"
                                 "4. Ogre\n"
                                 "5. Knight\n"),

        "print_player_classes_description": ("У каждого персонажа своя особенность\n"
                                             "1. Archer\n"
                                             "\tТы владеешь луком, из которого можешь поражать врагов с большого расстояния. Здоровье: {hp_arch}\n"
                                             "2. Wizard\n"
                                             "\tТы владеешь волшебной палочкой, из которой можешь поражать врагов с большого расстояния. Здоровье: {hp_wiz}\n"
                                             "3. Gnome\n"
                                             "\tТы владеешь золотой киркой, которой можешь поражать врагов с короткого расстояния. Здоровье: {hp_gn}\n"
                                             "4. Ogre\n"
                                             "\tТы владеешь булавой, которой можешь поражать врагов со среднего расстояния. Здоровье: {hp_og}\n"
                                             "5. Knight\n"
                                             "\tТы владеешь серебряным мечом, которым можешь поражать врагов с короткого расстояния. Здоровье: {hp_kn}\n"),

        "read_player_name": "Как тебя зовут? ",
        "read_player_class": "Каким классом ты хочешь играть? (Введи номер из списка выше) ",
        "class_choice": {
            "character": "Вот твой персонаж -> ",
            "accept_or_not?": "Это то, чего ты хотел? (Y/N) ",
            "not_accept": "\nХорошо, тогда давай начнем наше путешествие в мир D&D Light!"
        },

        "next_thing": {
            "question": "Готов ли ты идти дальше?: (Y/N) ",
            "additional_time": "Хорошо, не торопись, дорогой мой гость"
        }
    },
    "ua": {
        "gen_desc_main_locations": [("Мій дорогий друже, ти виявився досить хоробрим, щоб дістатися сюди.\n"
                                     "Наша подорож починається звідси, мій любий гостю — від холодного багаття.\n"
                                     "Ти йдеш назустріч новим пригодам і вже виявив \n"
                                     "першу з них. Перед тобою печера, но ти не зовсім упевнений, що \n"
                                     "всередині. Тобі цікаво дослідити її, але водночас ти дивно \n"
                                     "занепокоєний цією печерою. Тобі намагаєшся підійти до неї обережно...")],

        "gen_desc_quests": [("\"Тут темно, і я чую когось там, глибоко в печері\", \n"
                             "— кажеш ти. Ти думаєш про кілька способів впоратися з цим:\n"
                             "\t1. Ти можеш проігнорувати печеру і піти далі дорогою поруч із нею.\n"
                             "\t2. Менше з тим, ти не знаєш, що всередині печери, але \n"
                             "\tщо якщо прокрастися всередину, забрати все цінне і вибратися звідти?\n"
                             "\t3. Тому що там може бути щось дуже небезпечне, і ти \n"
                             "\tможеш почати бій з мобами")],

        "quest_get_option": "Яку опцію ти хочеш обрати? (Введи номер зі списку вище) ",

        "quest1": (
            "КВЕСТ 1",
            {
                "fight": {
                    "kill": "На жаль, тебе було вбито",
                    "success": "Це було важко, але ти чудово бився і виграв битву за Печеру"
                },

                "end_of_quest": {
                    "1": "\nТепер ты зовні печери і йдеш далі дорогою."
                         "\nНа вулиці темно, тому ти вирішив трохи відпочити",
                    "2": "\nТи дивишся на себе в річку, як у дзеркало, і дивуєшся цьому магічному ефекту...",
                },

                "options": {
                    "1": "Ну, іноді краще уникнути можливої проблеми.\nПроте ти не отримуєш приз",
                    "2": {
                        "successful": "Хе-е-ей! Ти пробрався всередину непомітно і знайшов там дещо дійсно цікаве",
                        "fail": "Тебе помітили, поки ти пробирався до печери.\nБій розпочався"
                    },
                    "3": {
                        "successful": "Ти розпочав дійсно жорстоку битву з монстрами",
                        "fail": "Там було два гігантських зомбі, які, на жаль, убили тебе..."
                    }
                }
            },
        ),
        "game_save": "Чи хочеш ти зберегти свій ігровий прогрес? ",
        "saver_save": "Як би ти хотів назвати файл збереження? ",
        "death": "На жаль, тебе було вбито",
        "greeting": ("Ласкаво просимо до гри D&D Light\n"
                     "Концепція гри така ж сама, як і в D&D\n"
                     "Гра складається з деякої кількості квестів, які тобі потрібно виконати\n"
                     "Потім ти переходиш на стадію боса, і це все\n"
                     "Досить просто, чи не так?\n"
                     "Тож давай спробуємо цю гру!"),

        "print_player_classes": ("Ось класи, за які ти можеш грати в цій грі:\n"
                                 "1. Archer\n"
                                 "2. Wizard\n"
                                 "3. Gnome\n"
                                 "4. Ogre\n"
                                 "5. Knight\n"),

        "print_player_classes_description": ("У кожного персонажа є своя особливість\n"
                                             "1. Archer\n"
                                             "\tТи володієш луком, з якого можеш уражати ворогів з великої відстані. Здоров'я: {hp_arch}\n"
                                             "2. Wizard\n"
                                             "\tТи володієш чарівною паличкою, з якої можеш уражати ворогів з великої відстані. Здоров'я: {hp_wiz}\n"
                                             "3. Gnome\n"
                                             "\tТи володієш золотою киркою, якою можеш уражати ворогів з короткої відстані. Здоров'я: {hp_gn}\n"
                                             "4. Ogre\n"
                                             "\tТи володієш булавою, якою можеш уражати ворогів з середньої відстані. Здоров'я: {hp_og}\n"
                                             "5. Knight\n"
                                             "\tТи володієш срібним мечем, яким можеш уражати ворогів з короткої відстані. Здоров'я: {hp_kn}\n"),

        "read_player_name": "Як тебе звати? ",
        "read_player_class": "Яким класом ти хочеш грати? (Введи номер зі списку вище) ",
        "class_choice": {
            "character": "Ось твій персонаж -> ",
            "accept_or_not?": "Це те, чого ти хотів? (Y/N) ",
            "not_accept": "\nДобре, тоді почнімо нашу подорож у світ D&D Light!"
        },

        "next_thing": {
            "question": "Чи готовий ти йти далі?: (Y/N) ",
            "additional_time": "Добре, не поспішай, мій любий гостю"
        }
    },
    "en": {
        "gen_desc_main_locations": [("My dear friend, you have appeared to be brave enough to get here.\n"
                                     "Our journey starts from here, my lovely guest - from a cold campfire.\n"
                                     "You are going towards to new adventures and you have already discovered \n"
                                     "the first one. There is the cave, but you are not really sure what is \n"
                                     "in there. You feel interested about discovering it, but also strangely \n"
                                     "confused of the cave. You are trying to approach it carefully...")],

        "gen_desc_quests": [("\"It is dark here and I hear somebody there, deep in the cave\", \n"
                             "you say. You think of a few ways of coping with it:\n"
                             "\t1. You can ignore the cave and go ahead the road near the cave.\n"
                             "\t2. Nevertheless you are not aware of what is inside the cave, but \n"
                             "\tif you sneak inside, take all the valuable and get out of there?\n"
                             "\t3. Because there might be something that is very dangerous and you\n"
                             "\tmight start the fight with the mobs")],

        "quest_get_option": "Which option would you like to pick? (Enter a number from a list above) ",

        "quest1": (
            "QUEST 1",
            {
                "fight": {
                    "kill": "Unfortunately you have been killed",
                    "success": "It was tough, but you have perfectly fought and won the battle of the Cave"
                },

                "end_of_quest": {
                    "1": "\nNow you are outside the cave and going further the road."
                         "\nIt is dark outside so you decided to rest for a little bit",
                    "2": "\nYou look at yourself in a river as in the mirror and wonder about this magical effect...",
                },

                "options": {
                    "1": "Well, sometimes it is better to omit possible problem.\nNevertheless you don't get the prize",
                    "2": {
                        "successful": "Heeeah! You got inside sneakily and found there something really interesting",
                        "fail": "You have been noticed while sneaking into the cave.\nThe fight has started"
                    },
                    "3": {
                        "successful": "You have started really cruel fight with the monsters",
                        "fail": "There were two giant zombies that, unfortunately, killed you..."
                    }
                }
            },
        ),
        "game_save": "Would you like to save your ingame progress? ",
        "saver_save": "How would you like to name the save file? ",
        "death": "Unfortunately you have been killed",
        "greeting": ("Welcome to the game of D&D Light\n"
                     "The concept of the game is the same as in the D&D\n"
                     "The game consists of some amount of quest that you have to complete\n"
                     "Pretty simple, isn't it?\n"
                     "So let's try this game out!"),

        "print_player_classes": ("Here are the classes that you can play in this game:\n"
                                 "1. Archer\n"
                                 "2. Wizard\n"
                                 "3. Gnome\n"
                                 "4. Ogre\n"
                                 "5. Knight\n"),

        "print_player_classes_description": ("Each character has its own speciality\n"
                                             "1. Archer\n"
                                             "\tYou posses a bow with which you can hit enemies from long distance. Health: {hp_arch}\n"
                                             "2. Wizard\n"
                                             "\tYou posses a magic wand with which you can hit enemies from long distance. Health: {hp_wiz}\n"
                                             "3. Gnome\n"
                                             "\tYou posses a golden pickaxe with which you can hit enemies from short distance. Health: {hp_gn}\n"
                                             "4. Ogre\n"
                                             "\tYou posses a mace with which you can hit enemies from medium distance. Health: {hp_og}\n"
                                             "5. Knight\n"
                                             "\tYou posses a silver sword  with which you can hit enemies from short distance. Health: {hp_kn}\n"),

        "read_player_name": "What is your name? ",
        "read_player_class": "What class do you want to play? (Enter a number from a list above) ",
        "class_choice": {
            "character": "Here is your character -> ",
            "accept_or_not?": "Is that what you wanted? (Y/N) ",
            "not_accept": "\nAlright, then let's start our journey into the world of D&D Light!"
        },

        "next_thing": {
            "question": "Are you ready to go further?: (Y/N) ",
            "additional_time": "Alright, take your time, dear guest of mine"
        }
    },
    "pl": {
        "gen_desc_main_locations": [("Mój drogi przyjacielu, okazałeś się dość odważny, aby tutaj dotrzeć.\n"
                                     "Nasza podróż zaczyna się stąd, mój drogi gościu — od zimnego ogniska.\n"
                                     "Idziesz w stronę nowych przygód i zdążyłeś już odkryć \n"
                                     "pierwszą z nich. Przed Tobą jaskinia, ale nie jesteś do końca pewien, co \n"
                                     "jest w środku. Czujesz zainteresowanie jej odkrywaniem, ale jednocześnie dziwne \n"
                                     "zdezorientowanie tą jaskinią. Próbujesz podejść do niej ostrożnie...")],

        "gen_desc_quests": [("\"Jest tutaj ciemno i słyszę kogoś tam, głęboko w jaskini\", \n"
                             "mówisz. Myślisz o kilku sposobach poradzenia sobie z tym:\n"
                             "\t1. Możesz zignorować jaskinię i iść dalej drogą obok niej.\n"
                             "\t2. Niemniej jednak nie jesteś świadomy tego, co jest w środku, ale \n"
                             "\tco jeśli wślizgniesz się ukradkiem, zabierzesz wszystko, co cenne i się stamtąd wydostaniesz?\n"
                             "\t3. Ponieważ może tam być coś bardzo niebezpiecznego i możesz \n"
                             "\trozpocząć walkę z potworami")],

        "quest_get_option": " Którą opcję chciałbyś wybrać? (Wprowadź numer z listy powyżej) ",

        "quest1": (
            "ZADANIE 1",
            {
                "fight": {
                    "kill": "Niestety zostałeś zabity",
                    "success": "To było trudne, ale doskonale walczyłeś i wygrałeś bitwę o Jaskinię"
                },

                "end_of_quest": {
                    "1": "\nTeraz jesteś na zewnątrz jaskini i idziesz dalej drogą."
                         "\nNa zewnątrz jest ciemno, więc zdecydowałeś się trochę odpocząć",
                    "2": "\nPrzeglądasz się w rzece jak w lustrze i zastanawiasz się nad tym magicznym efektem...",
                },

                "options": {
                    "1": "Cóż, czasami lepiej pominąć potencjalny problem.\nNiemniej jednak nie otrzymujesz nagrody",
                    "2": {
                        "successful": "Heeeah! Wślizgnąłeś się ukradkiem do środka i znalazłeś tam coś naprawdę ciekawego",
                        "fail": "Zostałeś zauważony podczas wślizgiwania się do jaskini.\nWalka się rozpoczęła"
                    },
                    "3": {
                        "successful": "Rozpocząłeś naprawdę okrutną walkę z potworami",
                        "fail": "Były tam dwa gigantyczne zombie, które, niestety, cię zabiły..."
                    }
                }
            },
        ),
        "game_save": "Czy chciałbyś zapisać swój postęp w grze? ",
        "saver_save": "Jak chciałbyś nazwać plik zapisu? ",
        "death": "Niestety zostałeś zabity",
        "greeting": ("Witaj w grze D&D Light\n"
                     "Koncepcja gry jest taka sama jak w D&D\n"
                     "Gra składa się z pewnej ilości zadań, które musisz ukończyć\n"
                     "Następnie wkraczasz w etap bossa i to wszystko\n"
                     "Całkiem proste, prawda?\n"
                     "Więc wypróbujmy tę grę!"),

        "print_player_classes": ("Oto klasy, którymi możesz grać w tej grze:\n"
                                 "1. Archer\n"
                                 "2. Wizard\n"
                                 "3. Gnome\n"
                                 "4. Ogre\n"
                                 "5. Knight\n"),

        "print_player_classes_description": ("Każda postać ma swoją specjalność\n"
                                             "1. Archer\n"
                                             "\tPosiadasz łuk, z którego możesz trafiać wrogów z dużej odległości. Zdrowie: {hp_arch}\n"
                                             "2. Wizard\n"
                                             "\tPosiadasz magiczną różdżkę, z której możesz trafiać wrogów z dużej odległości. Zdrowie: {hp_wiz}\n"
                                             "3. Gnome\n"
                                             "\tPosiadasz złoty kilof, którym możesz trafiać wrogów z bliskiej odległości. Zdrowie: {hp_gn}\n"
                                             "4. Ogre\n"
                                             "\tPosiadasz maczugę, którą możesz trafiać wrogów ze średniej odległości. Zdrowie: {hp_og}\n"
                                             "5. Knight\n"
                                             "\tPosiadasz srebrny miecz, którym możesz trafiać wrogów z bliskiej odległości. Zdrowie: {hp_kn}\n"),

        "read_player_name": "Jak masz na imię? ",
        "read_player_class": "Którą klasą chcesz grać? (Wprowadź numer z listy powyżej) ",
        "class_choice": {
            "character": "Oto Twoja postać -> ",
            "accept_or_not?": "Czy tego właśnie chciałeś? (Y/N) ",
            "not_accept": "\nW porządku, w takim razie zacznijmy naszą podróż do świata D&D Light!"
        },

        "next_thing": {
            "question": "Czy jesteś gotów iść dalej?: (Y/N) ",
            "additional_time": "W porządku, nie spiesz się, mój drogi gościu"
        },
        "ua++": {
            "gen_desc_main_locations": [
                ("МІЙ ДОРОГИЙ ДРУЖЕ, ТИ ПОТУЖНО ВИЯВИВСЯ ДОСИТЬ ХОРОБРИМ, ЩОБ ПОТУЖНО ДІСТАТИСЯ СЮДИ.\n"
                 "НАША ПОДОРОЖ ПОТУЖНО ПОЧИНАЄТЬСЯ ЗВІДСИ, МІЙ ЛЮБИЙ ГОСТЮ — ВІД ХОЛОДНОГО БАГАТТЯ.\n"
                 "ТИ ПОТУЖНО ЙДЕШ НАЗУСТРІЧ НОВИМ ПРИГОДАМ І ВЖЕ ПОТУЖНО ВИЯВИВ \n"
                 "ПЕРШУ З НИХ. ПЕРЕД ТОБОЮ ПЕЧЕРА, АЛЕ ТИ НЕ ЗОВСІМ УПЕВНЕНИЙ, ЩО \n"
                 "ВСЕРЕДИНІ. ТОБІ ЦІКАВО ПОТУЖНО ДОСЛІДИТИ ЇЇ, АЛЕ ВОДНОЧАС ТИ ДИВНО \n"
                 "ЗАНЕПОКОЄНИЙ ЦІЄЮ ПЕЧЕРОЮ. ТИ ПОТУЖНО НАМАГАЄШСЯ ПОТУЖНО ПІДІЙТИ ДО НЕЇ ОБЕРЕЖНО...")],

            "gen_desc_quests": [("\"ТУТ ТЕМНО, І Я ПОТУЖНО ЧУЮ КОГОСЬ ТАМ, ГЛИБОКО В ПЕЧЕРІ\", \n"
                                 "— ПОТУЖНО КАЖЕШ ТИ. ТИ ПОТУЖНО ДУМАЕШ ПРО КІЛЬКА СПОСОБІВ ПОТУЖНО ВПОРАТИСЯ З ЦИМ:\n"
                                 "\t1. ТИ ПОТУЖНО МОЖЕШ ПОТУЖНО ПРОІГНОРУВАТИ ПЕЧЕРУ І ПОТУЖНО ПІТИ ДАЛІ ДОРОГОЮ ПОРУЧ ІЗ НЕЮ.\n"
                                 "\t2. МЕНШЕ З ТИМ, ТИ НЕ ПОТУЖНО ЗНАЄШ, ЩО ВСЕРЕДИНІ ПЕЧЕРИ, АЛЕ \n"
                                 "\tЩО ЯКЩО ПОТУЖНО ПРОКРАСТИСЯ ВСЕРЕДИНУ, ПОТУЖНО ЗАБРАТИ ВСЕ ЦІННЕ І ПОТУЖНО ВИБРАТИСЯ ЗВІДТИ?\n"
                                 "\t3. ТОМУ ЩО ТАМ ПОТУЖНО МОЖЕ ПОТУЖНО БУТИ ЩОСТЬ ДУЖЕ НЕБЕЗПЕЧНЕ, І ТИ \n"
                                 "\tПОТУЖНО МОЖЕШ ПОТУЖНО РОЗПОЧАТИ БІЙ З МОБАМИ")],

            "quest_get_option": "ЯКУ ОПЦІЮ ТИ ПОТУЖНО ХОЧЕШ ПОТУЖНО ОБРАТИ? (ВВЕДИ НОМЕР ЗІ СПИСКУ ВИЩЕ) ",

            "quest1": (
                "КВЕСТ 1",
                {
                    "fight": {
                        "kill": "НА ЖАЛЬ, ТЕБЕ ПОТУЖНО БУЛО ПОТУЖНО ВБИТО",
                        "success": "ЦЕ ПОТУЖНО БУЛО ВАЖКО, АЛЕ ТИ ЧУДОВО ПОТУЖНО БИВСЯ І ПОТУЖНО ВИГРАВ БИТВУ ЗА ПЕЧЕРУ"
                    },

                    "end_of_quest": {
                        "1": "\nТЕПЕР ТИ ЗОВНІ ПЕЧЕРИ І ПОТУЖНО ЙДЕШ ДАЛІ ДОРОГОЮ."
                             "\nНА ВУЛИЦІ ТЕМНО, ТОМУ ТИ ПОТУЖНО ВИРІШИВ ТРОХИ ПОТУЖНО ВІДПОЧИТИ",
                        "2": "\nТИ ПОТУЖНО ДИВИШСЯ НА СЕБЕ В РІЧКУ, ЯК У ДЗЕРКАЛО, І ПОТУЖНО ДИВУЄШСЯ ЦЬОМУ МАГІЧНОМУ ЕФЕКТУ...",
                    },

                    "options": {
                        "1": "ЦÓЖ, ІНОДІ КРАЩЕ ПОТУЖНО УНИКНУТИ МОЖЛИВОЇ ПРОБЛЕМИ.\nПРОТЕ ТИ НЕ ПОТУЖНО ОТРИМУЄШ ПРИЗ",
                        "2": {
                            "successful": "ХЕ-Е-ЕЙ! ТИ ПОТУЖНО ПРОБРАВСЯ ВСЕРЕДИНУ НЕПОМІТНО І ПОТУЖНО ЗНАЙШОВ ТАМ ДЕЩО ДІЙСНО ЦІКАВЕ",
                            "fail": "ТЕБЕ ПОТУЖНО ПОМІТИЛИ, ПОКИ ТИ ПОТУЖНО ПРОБИРАВСЯ ДО ПЕЧЕРИ.\nБІЙ ПОТУЖНО РОЗПОЧАВСЯ"
                        },
                        "3": {
                            "successful": "ТИ ПОТУЖНО РОЗПОЧАВ ДІЙСНО ЖОРСТОКУ БИТВУ З МОНСТРАМИ",
                            "fail": "ТАМ ПОТУЖНО БУЛО ДВА ГІГАНТСЬКИХ ЗОМБІ, ЯКІ, НА ЖАЛЬ, ПОТУЖНО УБИЛИ ТЕБЕ..."
                        }
                    }
                },
            ),
            "game_save": "ЧИ ПОТУЖНО ХОЧЕШ ТИ ПОТУЖНО ЗБЕРЕГТИ СВІЙ ІГРОВИЙ ПРОГРЕС? ",
            "saver_save": "ЯК БИ ТИ ПОТУЖНО ХОТІВ ПОТУЖНО НАЗВАТИ ФАЙЛ ЗБЕРЕЖЕННЯ? ",
            "death": "НА ЖАЛЬ, ТЕБЕ ПОТУЖНО БУЛО ПОТУЖНО ВБИТО",
            "greeting": ("ЛАСКАВО ПОТУЖНО ПРОСИМО ДО ГРИ D&D LIGHT\n"
                         "КОНЦЕПЦІЯ ГРИ ТАКА Ж САМА, ЯК І В D&D\n"
                         "ГРА ПОТУЖНО СКЛАДАЄТЬСЯ З ДЕЯКОЇ КІЛЬКОСТІ КВЕСТІВ, ЯКІ ТОБІ ПОТУЖНО ПОТРІБНО ПОТУЖНО ВИКОНАТИ\n"
                         "ПОТІМ ТИ ПОТУЖНО ПЕРЕХОДИШ НА СТАДІЮ БОССА, І ЦЕ ВСЕ\n"
                         "ДОСИТЬ ПРОСТО, ЧИ НЕ ТАК?\n"
                         "ТОЖ ДАВАЙ ПОТУЖНО СПРОБУЄМО ЦЮ ГРУ!"),

            "print_player_classes": ("ОСЬ КЛАСИ, ЗА ЯКІ ТИ ПОТУЖНО МОЖЕШ ПОТУЖНО ГРАТИ В ЦІЙ ГРІ:\n"
                                     "1. ARCHER\n"
                                     "2. WIZARD\n"
                                     "3. GNOME\n"
                                     "4. OGRE\n"
                                     "5. KNIGHT\n"),

            "print_player_classes_description": ("У КОЖНОГО ПЕРСОНАЖА ПОТУЖНО Є СВОЯ ОСОБЛИВІСТЬ\n"
                                                 "1. ARCHER\n"
                                                 "\tТИ ПОТУЖНО ВОЛОДІЄШ ЛУКОМ, З ЯКОГО ПОТУЖНО МОЖЕШ ПОТУЖНО УРАЖАТИ ВОРОГІВ З ВЕЛИКОЇ ВІДСТАНІ. ЗДОРОВ'Я: {hp_arch}\n"
                                                 "2. WIZARD\n"
                                                 "\tТИ ПОТУЖНО ВОЛОДІЄШ ЧАРІВНОЮ ПАЛИЧКОЮ, З ЯКОЇ ПОТУЖНО МОЖЕШ ПОТУЖНО УРАЖАТИ ВОРОГІВ З ВЕЛИКОЇ ВІДСТАНІ. ЗДОРОВ'Я: {hp_wiz}\n"
                                                 "3. GNOME\n"
                                                 "\tТИ ПОТУЖНО ВОЛОДІЄШ ЗОЛОТОЮ КИРКОЮ, ЯКОЮ ПОТУЖНО МОЖЕШ ПОТУЖНО УРАЖАТИ ВОРОГІВ З КОРОТКОЇ ВІДСТАНІ. ЗДОРОВ'Я: {hp_gn}\n"
                                                 "4. OGRE\n"
                                                 "\tТИ ПОТУЖНО ВОЛОДІЄШ БУЛАВОЮ, ЯКОЮ ПОТУЖНО МОЖЕШ ПОТУЖНО УРАЖАТИ ВОРОГІВ З СЕРЕДНЬОЇ ВІДСТАНІ. ЗДОРОВ'Я: {hp_og}\n"
                                                 "5. KNIGHT\n"
                                                 "\tТИ ПОТУЖНО ВОЛОДІЄШ СРІБНИМ МЕЧЕМ, ЯКИМ ПОТУЖНО МОЖЕШ ПОТУЖНО УРАЖАТИ ВОРОГІВ З КОРОТКОЇ ВІДСТАНІ. ЗДОРОВ'Я: {hp_kn}\n"),

            "read_player_name": "ЯК ТЕБЕ ПОТУЖНО ЗВАТЬ? ",
            "read_player_class": "ЯКИМ КЛАСОМ ТИ ПОТУЖНО ХОЧЕШ ПОТУЖНО ГРАТИ? (ВВЕДИ НОМЕР ЗІ СПИСКУ ВИЩЕ) ",
            "class_choice": {
                "character": "ОСЬ ТВІЙ ПЕРСОНАЖ -> ",
                "accept_or_not?": "ЦЕ ТЕ, ЧОГО ТИ ПОТУЖНО ХОТІВ? (Y/N) ",
                "not_accept": "\nДОБРЕ, ТОДІ ПОТУЖНО ПОЧНІМО НАШУ ПОДОРОЖ У СВІТ D&D LIGHT!"
            },

            "next_thing": {
                "question": "ЧИ ГОТОВИЙ ТИ ПОТУЖНО ЙТИ ДАЛІ?: (Y/N) ",
                "additional_time": "ДОБРЕ, НЕ ПОТУЖНО ПОСПІШАЙ, МІЙ ЛЮБИЙ ГОСТЮ"
            }
        }
    }
}