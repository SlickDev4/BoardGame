from kivy.config import Config
from kivy.core.window import Window
from random import randint

p1_pos1_x, p1_pos1_y = 990, 458
p1_pos2_x, p1_pos2_y = 990, 403
p1_pos3_x, p1_pos3_y = 990, 348
p1_pos4_x, p1_pos4_y = 990, 293
p1_pos5_x, p1_pos5_y = 990, 238
p1_pos6_x, p1_pos6_y = 990, 183
p1_pos7_x, p1_pos7_y = 915, 128
p1_pos8_x, p1_pos8_y = 860, 128
p1_pos9_x, p1_pos9_y = 805, 128
p1_pos10_x, p1_pos10_y = 750, 128
p1_pos11_x, p1_pos11_y = 695, 128
p1_pos12_x, p1_pos12_y = 640, 128
p1_pos13_x, p1_pos13_y = 585, 128
p1_pos14_x, p1_pos14_y = 530, 128
p1_pos15_x, p1_pos15_y = 475, 128
p1_pos16_x, p1_pos16_y = 420, 128
p1_pos17_x, p1_pos17_y = 365, 128
p1_pos18_x, p1_pos18_y = 310, 203
p1_pos19_x, p1_pos19_y = 310, 258
p1_pos20_x, p1_pos20_y = 310, 313
p1_pos21_x, p1_pos21_y = 310, 368
p1_pos22_x, p1_pos22_y = 310, 423
p1_pos23_x, p1_pos23_y = 310, 478
p1_pos24_x, p1_pos24_y = 385, 533
p1_pos25_x, p1_pos25_y = 440, 533
p1_pos26_x, p1_pos26_y = 495, 533
p1_pos27_x, p1_pos27_y = 550, 533
p1_pos28_x, p1_pos28_y = 605, 533
p1_pos29_x, p1_pos29_y = 660, 533
p1_pos30_x, p1_pos30_y = 715, 533
p1_pos31_x, p1_pos31_y = 770, 533
p1_pos32_x, p1_pos32_y = 825, 533
p1_pos33_x, p1_pos33_y = 880, 533
p1_pos34_x, p1_pos34_y = 935, 533

p2_pos1_x, p2_pos1_y = 990, 440
p2_pos2_x, p2_pos2_y = 990, 385
p2_pos3_x, p2_pos3_y = 990, 330
p2_pos4_x, p2_pos4_y = 990, 275
p2_pos5_x, p2_pos5_y = 990, 220
p2_pos6_x, p2_pos6_y = 990, 165
p2_pos7_x, p2_pos7_y = 897, 128
p2_pos8_x, p2_pos8_y = 842, 128
p2_pos9_x, p2_pos9_y = 787, 128
p2_pos10_x, p2_pos10_y = 732, 128
p2_pos11_x, p2_pos11_y = 677, 128
p2_pos12_x, p2_pos12_y = 622, 128
p2_pos13_x, p2_pos13_y = 567, 128
p2_pos14_x, p2_pos14_y = 512, 128
p2_pos15_x, p2_pos15_y = 457, 128
p2_pos16_x, p2_pos16_y = 402, 128
p2_pos17_x, p2_pos17_y = 347, 128
p2_pos18_x, p2_pos18_y = 310, 221
p2_pos19_x, p2_pos19_y = 310, 276
p2_pos20_x, p2_pos20_y = 310, 331
p2_pos21_x, p2_pos21_y = 310, 386
p2_pos22_x, p2_pos22_y = 310, 441
p2_pos23_x, p2_pos23_y = 310, 496
p2_pos24_x, p2_pos24_y = 403, 533
p2_pos25_x, p2_pos25_y = 458, 533
p2_pos26_x, p2_pos26_y = 513, 533
p2_pos27_x, p2_pos27_y = 568, 533
p2_pos28_x, p2_pos28_y = 623, 533
p2_pos29_x, p2_pos29_y = 678, 533
p2_pos30_x, p2_pos30_y = 733, 533
p2_pos31_x, p2_pos31_y = 788, 533
p2_pos32_x, p2_pos32_y = 843, 533
p2_pos33_x, p2_pos33_y = 898, 533
p2_pos34_x, p2_pos34_y = 953, 533

player_1_color = (247/255, 7/255, 223/255, 1)
player_2_color = (0, 1, 0, 1)


# Dictionary for random luck
money_luck = [f"You decided to smoke some weed in the park but you got caught.\nYou pay {'[color=ff0000]'}25 $.",
             f"You won {'[color=09ff00]'}30 ${'[/color]'} from a football bet.",
              f"You made a {'[color=ff0000]'}25 ${'[/color]'} donation for you furry friends.",
             f"Congratz! You just left Tek Experts and for this we personally give you a check "
             f"of {'[color=09ff00]'}50 $.",
            f"You went to the casino and lost {'[color=ff0000]'}40 $.",
              f"Today is Sunday and you decided to order some pizza for {'[color=ff0000]'}30 $.",
            f"While walking on the street you found {'[color=09ff00]'}20 $.",
              f"You helped an old lady and she gave you {'[color=09ff00]'}10 $.",
              f"You went on a trip and paid {'[color=ff0000]'}100 $.",
              f"You won {'[color=09ff00]'}30 ${'[/color]'} from a hot dog monster contest.",
              f"You decided to invest in a small business and made a profit of {'[color=09ff00]'}100 $."]

win_cash = [f"You won the lottery - {'[color=09ff00]'}150 $.", f"Your luck today is {'[color=09ff00]'}100 $.",
            f"The last prize for today is yours - {'[color=09ff00]'}50 $.",
            f"You had an accident but your insurance company gave you {'[color=09ff00]'}70 $.",
            f"Your luck does not suck - {'[color=09ff00]'}25 $.", f"Hop hop, bunny hop - {'[color=09ff00]'}30 $.",
            f"Hurry up and take your {'[color=09ff00]'}15 ${'[/color]'} prize.",
            f"You won a voucher for {'[color=09ff00]'}40 $."]

points_luck = [f"You found an ancient coin and sold it for {'[color=E9F505]'}10 points.",
               f"You didn't stop at red light, you lost {'[color=E9F505]'}10 points.",
               f"There was a rain of points and you managed to collect {'[color=E9F505]'}20.",
               f"You were not careful so you were mugged for {'[color=E9F505]'}20 points.",
               f"You went crazy and won {'[color=E9F505]'}25 points{'[/color]'} in an online contest.",
               f"You did not pay attention at the game so you lost {'[color=E9F505]'}25 points.",
               f"While walking on the beach you found a sea star worth {'[color=E9F505]'}30 points.",
               f"You slipped on the stairs and lost {'[color=E9F505]'}30 points.",
               f"You invested in a points business and made {'[color=E9F505]'}40 points{'[/color]'} on your first day.",
               f"You played some poker and lost {'[color=E9F505]'}40 points."]

card_deck = ["card_deck/2_of_clubs.png", "card_deck/2_of_diamonds.png", "card_deck/2_of_hearts.png",
             "card_deck/2_of_spades.png", "card_deck/3_of_clubs.png", "card_deck/3_of_diamonds.png",
             "card_deck/3_of_hearts.png", "card_deck/3_of_spades.png", "card_deck/4_of_clubs.png",
             "card_deck/4_of_diamonds.png", "card_deck/4_of_hearts.png", "card_deck/4_of_spades.png",
             "card_deck/5_of_clubs.png", "card_deck/5_of_diamonds.png", "card_deck/5_of_hearts.png",
             "card_deck/5_of_spades.png", "card_deck/6_of_clubs.png", "card_deck/6_of_diamonds.png",
             "card_deck/6_of_hearts.png", "card_deck/6_of_spades.png", "card_deck/7_of_clubs.png",
             "card_deck/7_of_diamonds.png", "card_deck/7_of_hearts.png", "card_deck/7_of_spades.png",
             "card_deck/8_of_clubs.png", "card_deck/8_of_diamonds.png", "card_deck/8_of_hearts.png",
             "card_deck/8_of_spades.png", "card_deck/9_of_clubs.png", "card_deck/9_of_diamonds.png",
             "card_deck/9_of_hearts.png", "card_deck/9_of_spades.png", "card_deck/10_of_clubs.png",
             "card_deck/10_of_diamonds.png", "card_deck/10_of_hearts.png", "card_deck/10_of_spades.png",
             "card_deck/jack_of_clubs.png", "card_deck/jack_of_diamonds.png", "card_deck/jack_of_hearts.png",
             "card_deck/jack_of_spades.png", "card_deck/queen_of_clubs.png", "card_deck/queen_of_diamonds.png",
             "card_deck/queen_of_hearts.png", "card_deck/queen_of_spades.png", "card_deck/king_of_clubs.png",
             "card_deck/king_of_diamonds.png", "card_deck/king_of_hearts.png", "card_deck/king_of_spades.png",
             "card_deck/ace_of_clubs.png", "card_deck/ace_of_diamonds.png", "card_deck/ace_of_hearts.png",
             "card_deck/ace_of_spades.png", "card_deck/red_joker.png", "card_deck/black_joker.png"
             ]

# Fields Main Labels - On Step
tax_fields = f"Time for taxes my friend !\n\nYou pay {'[color=ff0000]'}50 ${'[/color]'}."
tax_fields_2 = f"Time for taxes my friend !\n\nYou pay {'[color=ff0000]'}150 ${'[/color]'}."
move_three_fields = f"You move {'[color=ffaf03]'}3 fields ahead{'[/color]'}.\n\nTime for crypto baby ! :D"
big_ben_fields = f"{'[color=ffaf03]'}Big Ben Property!{'[/color]'}\n\nThis spot costs " \
                                 f"{'[color=ff0000]'}120 ${'[/color]'} and when owned, every time " \
                                 f"{'[color=ff0000]'}Player 2{'[/color]'} steps on your property, they will" \
                                 f" pay {'[color=09ff00]'}30 ${'[/color]'}.\n\nDo you want to buy it?"
crypto_fields = f"{'[color=ffaf03]'}Crypto Market{'[/color]'}\n\nIf you invest, you will {'[color=09ff00]'}gain" \
                f"{'[/color]'} or {'[color=ff0000]'}lose{'[/color]'} from {'[color=09ff00]'}1 to 20%" \
                f"{'[/color]'}every turn. If your assets reach {'[color=E9F505]'}+ or - 50%{'[/color]'}, " \
                f"they will be automatically sold!"
thief_fields = f"{'[color=ffaf03]'}Money Thief{'[/color]'}\n\nChoose one of the bags and you will steal " \
               f"{'[color=ff0000]'}5 %, 10 % or 15 %{'[/color]'} from {'[color=ff0000]'}Player 2's{'[/color]'} money!"
eiffel_fields = f"{'[color=ffaf03]'}Eiffel Tower Property!{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}200 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}50 $" \
                f"{'[/color]'} every time they visit you.\n\nDo you want to buy it?"
duck_fields = f"{'[color=ffaf03]'}Duck of Luck Property!{'[/color]'}\n\nIf you have this duck, you will " \
              f"receive {'[color=E9F505]'}15 points{'[/color]'} every turn.\nThe property costs " \
              f"{'[color=ff0000]'}150 ${'[/color]'}.\n\nDo you want to buy it?"
brain_fields = f"Brain Memory - You have to memorize the pattern and then complete it exactly the same " \
               f"in about {'[color=ff0000]'}20{'[/color]'} seconds!\n If you do it correctly, " \
               f"you will receive {'[color=E9F505]'}40 points{'[/color]'}, " \
               f"if not you will loose {'[color=ff0000]'}15 points!"
brain_money_fields = f"Brain Memory - You have to memorize the pattern and then complete it exactly the same " \
               f"in about {'[color=ff0000]'}20{'[/color]'} seconds!\n If you do it correctly, " \
               f"you will receive {'[color=09ff00]'}150 ${'[/color]'}, " \
               f"if not you will loose {'[color=ff0000]'}75 $!"
brain_successful = f"Congratulations, you completed the pattern successfully.\n\nYou receive " \
                   f"{'[color=E9F505]'}40 Points!"
brain_unsuccessful = f"Too bad, you suck at this!\n\nYou lose {'[color=ff0000]'}15 points!"
brain_money_successful = f"Congratulations, you completed the pattern successfully.\n\nYou receive " \
                   f"{'[color=09ff00]'}150 $!"
brain_money_unsuccessful = f"Too bad, you suck at this!\n\nYou lose {'[color=ff0000]'}75 $!"
hospital_fields = f"You had an accident and went to the hospital :(\nYou have to choose how to pay the doctor - " \
                   f"with {'[color=ff0000]'}money{'[/color]'} or {'[color=E9F505]'}points{'[/color]'} ?"
coliseum_fields = f"{'[color=ffaf03]'}Coliseum Property!{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}280 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}70 $" \
                f"{'[/color]'} every time they visit you.\n\nDo you want to buy it?"

hospital_1_text = f"-25 $ or\n-50 $ or\n-75 $ or\n-100 $."

hospital_2_text = f"-6 points or\n-12 points or\n-18 points or\n-24 points."
sticky_fields = f"The floor was wet and you fell down, now you won't be able to move the next 2 turns."

math_fields = f"{'[color=ffaf03]'}Welcome to the Maths contest!{'[/color]'}\nYou will be given simple maths " \
              f"equations, you will have {'[color=ff0000]'}30 seconds{'[/color]'} to answer as much questions " \
              f"as you can. For every correct answer you will receive {'[color=E9F505]'}3 points."

counterfeit_cash_fields = f"{'[color=ffaf03]'}Counterfeit Cash Factory!{'[/color]'}\n\nIf you own this property," \
                          f"you will have a progress bar, which will load by a % determined from your dice. If you " \
                          f"roll 1, you will load 1% and etc. If you roll a 6, you will be given 10%. At 100% you " \
                          f"will receive {'[color=09ff00]'}200 ${'[/color]'} reward.\nWould you like to buy it for" \
                          f"{'[color=ff0000]'}350 ${'[/color]'} ?"

pisa_fields = f"{'[color=ffaf03]'}Leaning Pisa Tower Property!{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}400 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}100 $" \
                f"{'[/color]'} every time they visit you.\n\nDo you want to buy it?"

star_points_fields = f"{'[color=ffaf03]'}Falling Star Property!{'[/color]'}\n\nThis spot costs " \
                     f"{'[color=ff0000]'}300 ${'[/color]'} and it will give you between " \
                     f"{'[color=E9F505]'}30 and 45 points{'[/color]'} each time the bar above fills up to 100 % !"

move_back_fields = f"Unlucky brother!\n\nYou have to either pay {'[color=ff0000]'}100 ${'[/color]'}" \
                   f" or you will move back to the {'[color=ffaf03]'}Sticky Floor{'[/color]'} and miss 2 more " \
                   f"turns :(\nDo you pay or do you stay? :D"

sydney_fields = f"{'[color=ffaf03]'}Sydney Opera Property!{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}520 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}130 $" \
                f"{'[/color]'} every time they visit you.\n\nDo you want to buy it?"

black_friday = f"{'[color=ffaf03]'}Black Friday!{'[/color]'}\n\nYou have {'[color=09ff00]'}50 %{'[/color]'} " \
               f"discount on everything in the store while on this field."

cards_war = f"{'[color=ffaf03]'}Cards War!{'[/color]'}\n\nBoth players will draw cards 3 times. For 3-0 score, the" \
            f" winner will take {'[color=09ff00]'}250 ${'[/color]'} and for 2-1 score, the winner will " \
            f"take {'[color=09ff00]'}150 $."

skip_danger = f"You may be skipping the danger or an opportunity..Who knows?\n\nBoth ways, you are going to Start!"

tower_1 = f"{'[color=ffaf03]'}Almighty Tower 1{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}400 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}10 %" \
                f"{'[/color]'} every time they visit you.\nFor every tower owned, the percentage will go up!\n" \
          f"Do you want to buy it?"

tower_2 = f"{'[color=ffaf03]'}Almighty Tower 2{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}600 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}15 %" \
                f"{'[/color]'} every time they visit you.\nFor every tower owned, the percentage will go up!\n" \
          f"Do you want to buy it?"

tower_3 = f"{'[color=ffaf03]'}Almighty Tower 3{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}800 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}20 %" \
                f"{'[/color]'} every time they visit you.\nFor every tower owned, the percentage will go up!\n" \
          f"Do you want to buy it?"

salary_building_fields = f"{'[color=ffaf03]'}Increased Salary Property{'[/color]'}\n\n" \
                         f"This spot costs {'[color=ff0000]'}500 " \
                f"${'[/color]'} and you will receive a bonus of {'[color=09ff00]'}150 ${'[/color]'} on every salary."

louvre = f"{'[color=ffaf03]'}Le Louvre Property!{'[/color]'}\n\nThis spot costs {'[color=ff0000]'}600 " \
                f"${'[/color]'} and {'[color=ff0000]'}Player 2{'[/color]'} will pay you {'[color=09ff00]'}150 $" \
                f"{'[/color]'} every time they visit you.\n\nDo you want to buy it?"


def configuration():
    Config.set('graphics', 'resizable', False)
    Config.write()
    Window.size = (1330, 675)
    Window.top = 40
    Window.left = 20
    Window.resize = False
