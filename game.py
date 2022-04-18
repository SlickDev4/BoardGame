from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from config import *
from kivy.animation import Animation
from kivy.clock import Clock

global random_thief, math_answer, add_result, math_reset

# Player 1 - General Functions


def player_1_cash_count_g():
    get = App.get_running_app()
    cash_anim = Animation(opacity=0, duration=0.01)
    cash_anim += Animation(pos=(dp(175), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
    cash_anim += Animation(opacity=1, duration=0.05)
    cash_anim += Animation(color=(0, 1, 0, 1))
    cash_anim.start(get.root.ids.board.ids.cash_count)


def player_1_cash_count_r():
    get = App.get_running_app()
    cash_anim = Animation(opacity=0, duration=0.01)
    cash_anim += Animation(pos=(dp(175), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
    cash_anim += Animation(opacity=1, duration=0.05)
    cash_anim += Animation(color=(1, 0, 0, 1))
    cash_anim.start(get.root.ids.board.ids.cash_count)


def player_1_points_count():
    get = App.get_running_app()
    points_anim = Animation(opacity=0, duration=0.01)
    points_anim += Animation(pos=(dp(175), dp(508)), size=(dp(100), dp(50)), font_size=22, duration=0.2)
    points_anim += Animation(opacity=1, duration=0.25)
    points_anim += Animation(color=(233 / 255, 245 / 255, 5 / 255, 1), duration=0.25)
    points_anim.start(get.root.ids.board.ids.points_count)


# Player 2 - General Functions

def player_2_cash_count_g():
    get = App.get_running_app()
    cash_anim = Animation(opacity=0, duration=0.01)
    cash_anim += Animation(pos=(dp(1055), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
    cash_anim += Animation(opacity=1, duration=0.05)
    cash_anim += Animation(color=(0, 1, 0, 1))
    cash_anim.start(get.root.ids.board.ids.cash_count)


def player_2_cash_count_r():
    get = App.get_running_app()
    cash_anim = Animation(opacity=0, duration=0.01)
    cash_anim += Animation(pos=(dp(1055), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
    cash_anim += Animation(opacity=1, duration=0.05)
    cash_anim += Animation(color=(1, 0, 0, 1))
    cash_anim.start(get.root.ids.board.ids.cash_count)


def player_2_points_count():
    get = App.get_running_app()
    points_anim = Animation(opacity=0, duration=0.01)
    points_anim += Animation(pos=(dp(1055), dp(508)), size=(dp(100), dp(50)), font_size=22, duration=0.2)
    points_anim += Animation(opacity=1, duration=0.25)
    points_anim += Animation(color=(233 / 255, 245 / 255, 5 / 255, 1), duration=0.25)
    points_anim.start(get.root.ids.board.ids.points_count)


# Both Players - General Functions

def hide_cash_count(*args):
    get = App.get_running_app()
    get.root.ids.board.ids.cash_count.text = ""
    anim = Animation(opacity=0, duration=0.05)
    anim += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)
    anim.start(get.root.ids.board.ids.cash_count)


def hide_points_count(*args):
    get = App.get_running_app()
    get.root.ids.board.ids.points_count.text = ""
    points_reset_anim = Animation(opacity=0, duration=0.05)
    points_reset_anim += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)
    points_reset_anim.start(get.root.ids.board.ids.points_count)


def money_update(*args):
    get = App.get_running_app()

    get.root.ids.p1.ids.player_1_money.text = f'{int(get.root.ids.p1.ids.p1_money_stash.text):,} $'
    get.root.ids.p1.ids.player_1_points.text = f'{int(get.root.ids.p1.ids.p1_points_stash.text):,} pts.'
    get.root.ids.p1.ids.p1_crypto.text = f'{float(get.root.ids.p1.ids.p1_crypto_stash.text):,}'

    get.root.ids.p2.ids.player_2_money.text = f'{int(get.root.ids.p2.ids.p2_money_stash.text):,} $'
    get.root.ids.p2.ids.player_2_points.text = f'{int(get.root.ids.p2.ids.p2_points_stash.text):,} pts.'
    get.root.ids.p2.ids.p2_crypto.text = f'{float(get.root.ids.p2.ids.p2_crypto_stash.text):,}'

    if int(get.root.ids.p1.ids.p1_money_stash.text) <= 0:
        get.root.ids.board.ids.big.text = "Player 1 has lost all their money :(\n\nPlayer 2 is the WINNER!"
        get.root.ids.p1.ids.player_1_money.text = f"{0:,} $"
    if int(get.root.ids.p2.ids.p2_money_stash.text) <= 0:
        get.root.ids.board.ids.big.text = "Player 2 has lost all their money :(\n\nPlayer 1 is the WINNER!"
        get.root.ids.p2.ids.player_2_money.text = f"{0:,} $"


def unblock_roll(*args):
    get = App.get_running_app()

    if get.root.ids.p1.ids.turn_1.active:
        if not get.root.ids.board.ids.dice.text == "6":
            get.root.ids.p1.ids.player_1_roll.disabled = True
            get.root.ids.p2.ids.player_2_roll.disabled = False
        else:
            get.root.ids.p1.ids.player_1_roll.disabled = False
            get.root.ids.p2.ids.player_2_roll.disabled = True
    if get.root.ids.p2.ids.turn_2.active:
        if not get.root.ids.board.ids.dice.text == "6":
            get.root.ids.p1.ids.player_1_roll.disabled = False
            get.root.ids.p2.ids.player_2_roll.disabled = True
        else:
            get.root.ids.p1.ids.player_1_roll.disabled = True
            get.root.ids.p2.ids.player_2_roll.disabled = False


class Shop(Widget):

    # Player 1 - Shop

    @staticmethod
    def show_main(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.opacity = 0

        get.root.ids.f_shop.ids.player_1_shop.disabled = False
        get.root.ids.f_shop.ids.player_1_shop_image.opacity = 1
        get.root.ids.f_shop.ids.player_1_shop_image.size = dp(200), dp(200)
        get.root.ids.f_shop.ids.player_1_shop.opacity = 1
        get.root.ids.f_shop.ids.player_1_shop.size = dp(200), dp(200)
        get.root.ids.f_shop.ids.player_1_shop.pos = dp(415), dp(235)

        get.root.ids.f_shop.ids.player_1_inventory.disabled = False
        get.root.ids.f_shop.ids.player_1_inventory_image.opacity = 1
        get.root.ids.f_shop.ids.player_1_inventory_image.size = dp(200), dp(230)
        get.root.ids.f_shop.ids.player_1_inventory.opacity = 1
        get.root.ids.f_shop.ids.player_1_inventory.size = dp(200), dp(200)
        get.root.ids.f_shop.ids.player_1_inventory.pos = dp(700), dp(235)

        get.root.ids.f_shop.ids.shop_main_exit.opacity = 1
        get.root.ids.f_shop.ids.shop_main_exit.size = dp(70), dp(25)
        get.root.ids.f_shop.ids.shop_main_exit.pos = dp(625), dp(210)
        get.root.ids.f_shop.ids.shop_main_exit.text = "Exit"
        get.root.ids.f_shop.ids.shop_main_exit.disabled = False

        get.root.ids.p1.ids.player_1_roll.disabled = True
        get.root.ids.p2.ids.player_2_roll.disabled = True

    @staticmethod
    def hide_buttons():
        get = App.get_running_app()
        get.root.ids.f_shop.ids.player_1_shop.disabled = True
        get.root.ids.f_shop.ids.player_1_shop_image.opacity = 0
        get.root.ids.f_shop.ids.player_1_shop_image.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_1_shop.opacity = 0
        get.root.ids.f_shop.ids.player_1_shop.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_1_shop.pos = dp(0), dp(0)

        get.root.ids.f_shop.ids.player_1_inventory.disabled = True
        get.root.ids.f_shop.ids.player_1_inventory_image.opacity = 0
        get.root.ids.f_shop.ids.player_1_inventory_image.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_1_inventory.opacity = 0
        get.root.ids.f_shop.ids.player_1_inventory.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_1_inventory.pos = dp(0), dp(0)

    @staticmethod
    def show_main_sh_in():
        get = App.get_running_app()
        get.root.ids.f_shop.ids.shop_inventory_background.size = dp(545), dp(270)
        get.root.ids.f_shop.ids.shop_inventory_background.pos = dp(385), dp(203)
        get.root.ids.f_shop.ids.shop_inventory_background.opacity = 1

        get.root.ids.f_shop.ids.building_upgrades.size = dp(175), dp(45)
        get.root.ids.f_shop.ids.building_upgrades.pos = dp(390), dp(423)
        get.root.ids.f_shop.ids.building_upgrades.opacity = 1

        get.root.ids.f_shop.ids.anti_field_cards.size = dp(175), dp(45)
        get.root.ids.f_shop.ids.anti_field_cards.pos = dp(570), dp(423)
        get.root.ids.f_shop.ids.anti_field_cards.opacity = 1

        get.root.ids.f_shop.ids.attack_others.size = dp(175), dp(45)
        get.root.ids.f_shop.ids.attack_others.pos = dp(750), dp(423)
        get.root.ids.f_shop.ids.attack_others.opacity = 1

    def show_shop(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos
        self.hide_buttons()
        self.show_main_sh_in()
        get.root.ids.f_shop.ids.shop_main_exit.text = "Back"

        def big_ben():
            count = int(get.root.ids.f_shop.ids.big_ben_count.text)
            count_2 = int(get.root.ids.f_shop.ids.big_ben_count_2.text)
            get.root.ids.f_shop.ids.big_ben_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.big_ben_shop_image.pos = dp(390), dp(390)
            get.root.ids.f_shop.ids.big_ben_shop_image.opacity = 1

            get.root.ids.f_shop.ids.big_ben_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.big_ben_label.pos = dp(420), dp(390)
            get.root.ids.f_shop.ids.big_ben_label.text = "Property not owned"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_label.halign = "center"
            get.root.ids.f_shop.ids.big_ben_label.font_size = 15
            get.root.ids.f_shop.ids.big_ben_label.opacity = 1

            get.root.ids.f_shop.ids.big_ben_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.big_ben_upgrade.pos = dp(521), dp(390)
            get.root.ids.f_shop.ids.big_ben_upgrade.opacity = 1

            if get.root.ids.f_shop.ids.big_ben_upgrade.text == "N/A":
                get.root.ids.f_shop.ids.big_ben_upgrade.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_5.text == "purple":
                get.root.ids.f_shop.ids.big_ben_label.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.big_ben_label.text = "Rent goes from 30 $ to 50 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.big_ben_upgrade.text = "40 $"
                    else:
                        get.root.ids.f_shop.ids.big_ben_upgrade.text = "80 $"
                    get.root.ids.f_shop.ids.big_ben_upgrade.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.big_ben_label.text = "Rent goes from 50 $ to 85 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.big_ben_upgrade.text = "50 $"
                    else:
                        get.root.ids.f_shop.ids.big_ben_upgrade.text = "100 $"
                    get.root.ids.f_shop.ids.big_ben_upgrade.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.big_ben_label.text = "Rent goes from 85 $ to 120 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.big_ben_upgrade.text = "60 $"
                    else:
                        get.root.ids.f_shop.ids.big_ben_upgrade.text = "120 $"
                    get.root.ids.f_shop.ids.big_ben_upgrade.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.big_ben_label.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.big_ben_upgrade.text = "Max"

        def eiffel():
            count = int(get.root.ids.f_shop.ids.eiffel_count.text)
            count_2 = int(get.root.ids.f_shop.ids.eiffel_count_2.text)
            get.root.ids.f_shop.ids.eiffel_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.eiffel_shop_image.pos = dp(390), dp(357)
            get.root.ids.f_shop.ids.eiffel_shop_image.opacity = 1

            get.root.ids.f_shop.ids.eiffel_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.eiffel_label.pos = dp(420), dp(357)
            get.root.ids.f_shop.ids.eiffel_label.text = "Property not owned"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_label.halign = "center"
            get.root.ids.f_shop.ids.eiffel_label.font_size = 15
            get.root.ids.f_shop.ids.eiffel_label.opacity = 1

            get.root.ids.f_shop.ids.eiffel_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.eiffel_upgrade.pos = dp(521), dp(357)
            get.root.ids.f_shop.ids.eiffel_upgrade.opacity = 1

            if get.root.ids.f_shop.ids.eiffel_upgrade.text == "N/A":
                get.root.ids.f_shop.ids.eiffel_upgrade.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_9.text == "purple":
                get.root.ids.f_shop.ids.eiffel_label.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.eiffel_label.text = "Rent goes from 50 $ to 80 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.eiffel_upgrade.text = "45 $"
                    else:
                        get.root.ids.f_shop.ids.eiffel_upgrade.text = "90 $"
                    get.root.ids.f_shop.ids.eiffel_upgrade.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.eiffel_label.text = "Rent goes from 80 $ to 115 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.eiffel_upgrade.text = "60 $"
                    else:
                        get.root.ids.f_shop.ids.eiffel_upgrade.text = "120 $"
                    get.root.ids.f_shop.ids.eiffel_upgrade.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.eiffel_label.text = "Rent goes from 115 $ to 150 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.eiffel_upgrade.text = "75 $"
                    else:
                        get.root.ids.f_shop.ids.eiffel_upgrade.text = "150 $"
                    get.root.ids.f_shop.ids.eiffel_upgrade.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.eiffel_label.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.eiffel_upgrade.text = "Max"

        def coliseum():
            count = int(get.root.ids.f_shop.ids.coliseum_count.text)
            count_2 = int(get.root.ids.f_shop.ids.coliseum_count_2.text)
            get.root.ids.f_shop.ids.coliseum_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.coliseum_shop_image.pos = dp(390), dp(324)
            get.root.ids.f_shop.ids.coliseum_shop_image.opacity = 1

            get.root.ids.f_shop.ids.coliseum_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.coliseum_label.pos = dp(420), dp(324)
            get.root.ids.f_shop.ids.coliseum_label.text = "Property not owned"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_label.halign = "center"
            get.root.ids.f_shop.ids.coliseum_label.font_size = 15
            get.root.ids.f_shop.ids.coliseum_label.opacity = 1

            get.root.ids.f_shop.ids.coliseum_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.coliseum_upgrade.pos = dp(521), dp(324)
            get.root.ids.f_shop.ids.coliseum_upgrade.opacity = 1

            if get.root.ids.f_shop.ids.coliseum_upgrade.text == "N/A":
                get.root.ids.f_shop.ids.coliseum_upgrade.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_13.text == "purple":
                get.root.ids.f_shop.ids.coliseum_label.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.coliseum_label.text = "Rent goes from 70 $ to 110 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.coliseum_upgrade.text = "55 $"
                    else:
                        get.root.ids.f_shop.ids.coliseum_upgrade.text = "110 $"
                    get.root.ids.f_shop.ids.coliseum_upgrade.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.coliseum_label.text = "Rent goes from 110 $ to 150 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.coliseum_upgrade.text = "70 $"
                    else:
                        get.root.ids.f_shop.ids.coliseum_upgrade.text = "140 $"
                    get.root.ids.f_shop.ids.coliseum_upgrade.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.coliseum_label.text = "Rent goes from 150 $ to 190 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.coliseum_upgrade.text = "85 $"
                    else:
                        get.root.ids.f_shop.ids.coliseum_upgrade.text = "170 $"
                    get.root.ids.f_shop.ids.coliseum_upgrade.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.coliseum_label.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.coliseum_upgrade.text = "Max"

        def pisa():
            count = int(get.root.ids.f_shop.ids.pisa_count.text)
            count_2 = int(get.root.ids.f_shop.ids.pisa_count_2.text)
            get.root.ids.f_shop.ids.pisa_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.pisa_shop_image.pos = dp(390), dp(291)
            get.root.ids.f_shop.ids.pisa_shop_image.opacity = 1

            get.root.ids.f_shop.ids.pisa_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.pisa_label.pos = dp(420), dp(291)
            get.root.ids.f_shop.ids.pisa_label.text = "Property not owned"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_label.halign = "center"
            get.root.ids.f_shop.ids.pisa_label.font_size = 15
            get.root.ids.f_shop.ids.pisa_label.opacity = 1

            get.root.ids.f_shop.ids.pisa_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.pisa_upgrade.pos = dp(521), dp(291)
            get.root.ids.f_shop.ids.pisa_upgrade.opacity = 1

            if get.root.ids.f_shop.ids.pisa_upgrade.text == "N/A":
                get.root.ids.f_shop.ids.pisa_upgrade.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_17.text == "purple":
                get.root.ids.f_shop.ids.pisa_label.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.pisa_label.text = "Rent goes from 100 $ to 150 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.pisa_upgrade.text = "75 $"
                    else:
                        get.root.ids.f_shop.ids.pisa_upgrade.text = "150 $"
                    get.root.ids.f_shop.ids.pisa_upgrade.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.pisa_label.text = "Rent goes from 150 $ to 200 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.pisa_upgrade.text = "100 $"
                    else:
                        get.root.ids.f_shop.ids.pisa_upgrade.text = "200 $"
                    get.root.ids.f_shop.ids.pisa_upgrade.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.pisa_label.text = "Rent goes from 200 $ to 250 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.pisa_upgrade.text = "125 $"
                    else:
                        get.root.ids.f_shop.ids.pisa_upgrade.text = "250 $"
                    get.root.ids.f_shop.ids.pisa_upgrade.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.pisa_label.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.pisa_upgrade.text = "Max"

        def sydney():
            count = int(get.root.ids.f_shop.ids.sydney_count.text)
            count_2 = int(get.root.ids.f_shop.ids.sydney_count_2.text)
            get.root.ids.f_shop.ids.sydney_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.sydney_shop_image.pos = dp(390), dp(258)
            get.root.ids.f_shop.ids.sydney_shop_image.opacity = 1

            get.root.ids.f_shop.ids.sydney_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.sydney_label.pos = dp(420), dp(258)
            get.root.ids.f_shop.ids.sydney_label.text = "Property not owned"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_label.halign = "center"
            get.root.ids.f_shop.ids.sydney_label.font_size = 15
            get.root.ids.f_shop.ids.sydney_label.opacity = 1

            get.root.ids.f_shop.ids.sydney_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.sydney_upgrade.pos = dp(521), dp(258)
            get.root.ids.f_shop.ids.sydney_upgrade.opacity = 1

            if get.root.ids.f_shop.ids.sydney_upgrade.text == "N/A":
                get.root.ids.f_shop.ids.sydney_upgrade.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_22.text == "purple":
                get.root.ids.f_shop.ids.sydney_label.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.sydney_label.text = "Rent goes from 130 $ to 200 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.sydney_upgrade.text = "100 $"
                    else:
                        get.root.ids.f_shop.ids.sydney_upgrade.text = "200 $"
                    get.root.ids.f_shop.ids.sydney_upgrade.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.sydney_label.text = "Rent goes from 200 $ to 250 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.sydney_upgrade.text = "125 $"
                    else:
                        get.root.ids.f_shop.ids.sydney_upgrade.text = "250 $"
                    get.root.ids.f_shop.ids.sydney_upgrade.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.sydney_label.text = "Rent goes from 250 $ to 300 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.sydney_upgrade.text = "150 $"
                    else:
                        get.root.ids.f_shop.ids.sydney_upgrade.text = "300 $"
                    get.root.ids.f_shop.ids.sydney_upgrade.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.sydney_label.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.sydney_upgrade.text = "Max"

        def le_louvre():
            count = int(get.root.ids.f_shop.ids.louvre_count.text)
            count_2 = int(get.root.ids.f_shop.ids.louvre_count_2.text)
            get.root.ids.f_shop.ids.louvre_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.louvre_shop_image.pos = dp(390), dp(225)
            get.root.ids.f_shop.ids.louvre_shop_image.opacity = 1

            get.root.ids.f_shop.ids.louvre_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.louvre_label.pos = dp(420), dp(225)
            get.root.ids.f_shop.ids.louvre_label.text = "Property not owned"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_label.halign = "center"
            get.root.ids.f_shop.ids.louvre_label.font_size = 15
            get.root.ids.f_shop.ids.louvre_label.opacity = 1

            get.root.ids.f_shop.ids.louvre_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.louvre_upgrade.pos = dp(521), dp(225)
            get.root.ids.f_shop.ids.louvre_upgrade.opacity = 1

            if get.root.ids.f_shop.ids.louvre_upgrade.text == "N/A":
                get.root.ids.f_shop.ids.louvre_upgrade.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_33.text == "purple":
                get.root.ids.f_shop.ids.louvre_label.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.louvre_label.text = "Rent goes from 150 $ to 230 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.louvre_upgrade.text = "120 $"
                    else:
                        get.root.ids.f_shop.ids.louvre_upgrade.text = "240 $"
                    get.root.ids.f_shop.ids.louvre_upgrade.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.louvre_label.text = "Rent goes from 230 $ to 300 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.louvre_upgrade.text = "150 $"
                    else:
                        get.root.ids.f_shop.ids.louvre_upgrade.text = "300 $"
                    get.root.ids.f_shop.ids.louvre_upgrade.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.louvre_label.text = "Rent goes from 300 $ to 350 $"
                    if x == p1_pos23_x and y == p1_pos23_y:
                        get.root.ids.f_shop.ids.louvre_upgrade.text = "175 $"
                    else:
                        get.root.ids.f_shop.ids.louvre_upgrade.text = "350 $"
                    get.root.ids.f_shop.ids.louvre_upgrade.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.louvre_label.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.louvre_upgrade.text = "Max"

        def thief():
            get.root.ids.f_shop.ids.anti_thief_image.size = dp(30), dp(30)
            get.root.ids.f_shop.ids.anti_thief_image.pos = dp(570), dp(390)
            get.root.ids.f_shop.ids.anti_thief_image.opacity = 1

            get.root.ids.f_shop.ids.anti_steal_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.anti_steal_label.pos = dp(600), dp(390)
            get.root.ids.f_shop.ids.anti_steal_label.text = "Blocks the Thief"
            get.root.ids.f_shop.ids.anti_steal_label.halign = "left"
            get.root.ids.f_shop.ids.anti_steal_label.font_size = 13
            get.root.ids.f_shop.ids.anti_steal_label.opacity = 1

            get.root.ids.f_shop.ids.anti_thief_buy.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.anti_thief_buy.pos = dp(701), dp(390)
            get.root.ids.f_shop.ids.anti_thief_buy.opacity = 1
            if x == p1_pos23_x and y == p1_pos23_y:
                get.root.ids.f_shop.ids.anti_thief_buy.text = "15 pts"
                if int(get.root.ids.p1.ids.p1_points_stash.text) < 15:
                    get.root.ids.f_shop.ids.anti_thief_buy.disabled = True
                else:
                    get.root.ids.f_shop.ids.anti_thief_buy.disabled = False
            else:
                get.root.ids.f_shop.ids.anti_thief_buy.text = "30 pts"
                if int(get.root.ids.p1.ids.p1_points_stash.text) < 30:
                    get.root.ids.f_shop.ids.anti_thief_buy.disabled = True
                else:
                    get.root.ids.f_shop.ids.anti_thief_buy.disabled = False

        big_ben()
        eiffel()
        coliseum()
        pisa()
        sydney()
        le_louvre()

        thief()

    @staticmethod
    def hide_shop():
        get = App.get_running_app()
        get.root.ids.f_shop.ids.shop_inventory_background.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.shop_inventory_background.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.shop_inventory_background.opacity = 0

        get.root.ids.f_shop.ids.building_upgrades.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.building_upgrades.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.building_upgrades.opacity = 0

        get.root.ids.f_shop.ids.anti_field_cards.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.anti_field_cards.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.anti_field_cards.opacity = 0

        get.root.ids.f_shop.ids.attack_others.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.attack_others.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.attack_others.opacity = 0

        def big_ben():
            get.root.ids.f_shop.ids.big_ben_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_shop_image.opacity = 0

            get.root.ids.f_shop.ids.big_ben_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_label.font_size = 13
            get.root.ids.f_shop.ids.big_ben_label.opacity = 0

            get.root.ids.f_shop.ids.big_ben_upgrade.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_upgrade.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_upgrade.opacity = 0
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        def eiffel():
            get.root.ids.f_shop.ids.eiffel_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_shop_image.opacity = 0

            get.root.ids.f_shop.ids.eiffel_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_label.font_size = 13
            get.root.ids.f_shop.ids.eiffel_label.opacity = 0

            get.root.ids.f_shop.ids.eiffel_upgrade.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_upgrade.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_upgrade.opacity = 0
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        def coliseum():
            get.root.ids.f_shop.ids.coliseum_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_shop_image.opacity = 0

            get.root.ids.f_shop.ids.coliseum_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_label.font_size = 13
            get.root.ids.f_shop.ids.coliseum_label.opacity = 0

            get.root.ids.f_shop.ids.coliseum_upgrade.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_upgrade.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_upgrade.opacity = 0
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        def pisa():
            get.root.ids.f_shop.ids.pisa_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_shop_image.opacity = 0

            get.root.ids.f_shop.ids.pisa_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_label.font_size = 13
            get.root.ids.f_shop.ids.pisa_label.opacity = 0

            get.root.ids.f_shop.ids.pisa_upgrade.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_upgrade.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_upgrade.opacity = 0
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        def sydney():
            get.root.ids.f_shop.ids.sydney_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_shop_image.opacity = 0

            get.root.ids.f_shop.ids.sydney_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_label.font_size = 13
            get.root.ids.f_shop.ids.sydney_label.opacity = 0

            get.root.ids.f_shop.ids.sydney_upgrade.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_upgrade.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_upgrade.opacity = 0
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        def le_louvre():
            get.root.ids.f_shop.ids.louvre_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_shop_image.opacity = 0

            get.root.ids.f_shop.ids.louvre_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_label.font_size = 13
            get.root.ids.f_shop.ids.louvre_label.opacity = 0

            get.root.ids.f_shop.ids.louvre_upgrade.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_upgrade.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_upgrade.opacity = 0
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        def thief():
            get.root.ids.f_shop.ids.anti_thief_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_image.opacity = 0

            get.root.ids.f_shop.ids.anti_steal_label.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_steal_label.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_steal_label.opacity = 0

            get.root.ids.f_shop.ids.anti_thief_buy.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_buy.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_buy.opacity = 0
            get.root.ids.f_shop.ids.anti_thief_buy.disabled = True

        big_ben()
        eiffel()
        coliseum()
        pisa()
        sydney()
        le_louvre()

        thief()

    @staticmethod
    def big_ben_upgrade(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.big_ben_count.text)
        count_2 = int(get.root.ids.f_shop.ids.big_ben_count_2.text)

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "80 $":
            get.root.ids.board.ids.cash_count.text = "-80 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 80}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "40 $":
            get.root.ids.board.ids.cash_count.text = "-40 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 40}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "100 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 100}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "50 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-50 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 50}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "120 $":
            get.root.ids.board.ids.cash_count.text = "-120 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 120}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"No more upgrades"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "Max"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "60 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-60 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 60}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.big_ben_upgrade.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.big_ben_label.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.big_ben_count_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.big_ben_label.text = f"Max Level"

    @staticmethod
    def eiffel_upgrade(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.eiffel_count.text)
        count_2 = int(get.root.ids.f_shop.ids.eiffel_count_2.text)

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "90 $":
            get.root.ids.board.ids.cash_count.text = "-90 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 90}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "45 $":
            get.root.ids.board.ids.cash_count.text = "-45 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 45}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "120 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-120 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 120}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "60 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-60 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 60}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "150 $":
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label.text = f"No more upgrades"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "Max"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "75 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-75 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 75}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.eiffel_upgrade.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.eiffel_label.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.eiffel_count_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.eiffel_label.text = f"Max Level"

    @staticmethod
    def coliseum_upgrade(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.coliseum_count.text)
        count_2 = int(get.root.ids.f_shop.ids.coliseum_count_2.text)

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "110 $":
            get.root.ids.board.ids.cash_count.text = "-110 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 110}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "55 $":
            get.root.ids.board.ids.cash_count.text = "-55 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 55}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "140 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-140 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 140}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "70 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-70 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 70}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "170 $":
            get.root.ids.board.ids.cash_count.text = "-170 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 170}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label.text = f"No more upgrades"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "Max"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "85 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-85 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 85}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.coliseum_upgrade.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.coliseum_label.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.coliseum_count_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.coliseum_label.text = f"Max Level"

    @staticmethod
    def pisa_upgrade(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.pisa_count.text)
        count_2 = int(get.root.ids.f_shop.ids.pisa_count_2.text)

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "150 $":
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "75 $":
            get.root.ids.board.ids.cash_count.text = "-75 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 75}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "200 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-200 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 200}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "100 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 100}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "250 $":
            get.root.ids.board.ids.cash_count.text = "-250 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 250}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label.text = f"No more upgrades"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "Max"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "125 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-125 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 125}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.pisa_upgrade.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.pisa_label.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.pisa_count_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.pisa_label.text = f"Max Level"

    @staticmethod
    def sydney_upgrade(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.sydney_count.text)
        count_2 = int(get.root.ids.f_shop.ids.sydney_count_2.text)

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "200 $":
            get.root.ids.board.ids.cash_count.text = "-200 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 200}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "100 $":
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 100}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "250 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-250 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 250}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "125 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-125 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 125}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "300 $":
            get.root.ids.board.ids.cash_count.text = "-300 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 300}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label.text = f"No more upgrades"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "Max"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "150 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.sydney_upgrade.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.sydney_label.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.sydney_count_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.sydney_label.text = f"Max Level"

    @staticmethod
    def le_louvre_upgrade(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.louvre_count.text)
        count_2 = int(get.root.ids.f_shop.ids.louvre_count_2.text)

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "240 $":
            get.root.ids.board.ids.cash_count.text = "-240 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 240}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "120 $":
            get.root.ids.board.ids.cash_count.text = "-120 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 120}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "300 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-300 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 300}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "150 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "350 $":
            get.root.ids.board.ids.cash_count.text = "-350 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 350}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label.text = f"No more upgrades"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "Max"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "175 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-175 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 175}"
            player_1_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.louvre_upgrade.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.louvre_label.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.louvre_count_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.louvre_label.text = f"Max Level"

    @staticmethod
    def anti_thief_buy(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.anti_steal_count.text)

        if get.root.ids.f_shop.ids.anti_thief_buy.text == "30 pts":
            get.root.ids.board.ids.points_count.text = "-30 pts."
            get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 30}"
            player_1_points_count()
            count += 1
            get.root.ids.f_shop.ids.anti_steal_count.text = f"{count}"
            get.root.ids.f_shop.ids.anti_thief_buy.disabled = True

        if get.root.ids.f_shop.ids.anti_thief_buy.text == "15 pts":
            get.root.ids.board.ids.points_count.text = "-15 pts."
            get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 15}"
            player_1_points_count()
            count += 1
            get.root.ids.f_shop.ids.anti_steal_count.text = f"{count}"
            get.root.ids.f_shop.ids.anti_thief_buy.disabled = True

        Clock.schedule_once(hide_points_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.anti_thief_buy.text == "Use":
            count -= 1
            get.root.ids.f_shop.ids.anti_steal_count.text = f"{count}"
            get.root.ids.f_shop.ids.anti_steal_label.text = f"x {get.root.ids.f_shop.ids.anti_steal_count.text}"
            get.root.ids.f_shop.ids.anti_thief_active.size = dp(30), dp(30)
            get.root.ids.f_shop.ids.anti_thief_active.pos = dp(15), dp(310)
            get.root.ids.f_shop.ids.anti_thief_active.opacity = 1
            if count == 0 or get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.f_shop.ids.anti_thief_buy.disabled = True

    def show_inventory(self):
        get = App.get_running_app()
        get.root.ids.f_shop.ids.shop_main_exit.text = "Back"

        self.hide_buttons()
        self.show_main_sh_in()

        def big_ben():
            count = int(get.root.ids.f_shop.ids.big_ben_count.text)
            count_2 = int(get.root.ids.f_shop.ids.big_ben_count_2.text)
            get.root.ids.f_shop.ids.big_ben_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.big_ben_shop_image.pos = dp(390), dp(390)
            get.root.ids.f_shop.ids.big_ben_shop_image.opacity = 1
            get.root.ids.f_shop.ids.big_ben_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.big_ben_label.pos = dp(420), dp(390)
            get.root.ids.f_shop.ids.big_ben_label.text = f"Property not owned"
            get.root.ids.f_shop.ids.big_ben_label.halign = "center"
            get.root.ids.f_shop.ids.big_ben_label.font_size = 15
            get.root.ids.f_shop.ids.big_ben_label.opacity = 1
            get.root.ids.f_shop.ids.big_ben_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.big_ben_upgrade.pos = dp(521), dp(390)
            get.root.ids.f_shop.ids.big_ben_upgrade.opacity = 1
            get.root.ids.f_shop.ids.big_ben_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade.disabled = True

            if get.root.ids.board.ids.field_5.text == "purple":
                get.root.ids.f_shop.ids.big_ben_label.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.big_ben_upgrade.disabled = False
                    get.root.ids.f_shop.ids.big_ben_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.big_ben_upgrade.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.big_ben_upgrade.disabled = False
                    get.root.ids.f_shop.ids.big_ben_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.big_ben_upgrade.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.big_ben_upgrade.disabled = False
                    get.root.ids.f_shop.ids.big_ben_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.big_ben_upgrade.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.big_ben_label.text = f"Max Level"

        def eiffel():
            count = int(get.root.ids.f_shop.ids.eiffel_count.text)
            count_2 = int(get.root.ids.f_shop.ids.eiffel_count_2.text)
            get.root.ids.f_shop.ids.eiffel_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.eiffel_shop_image.pos = dp(390), dp(357)
            get.root.ids.f_shop.ids.eiffel_shop_image.opacity = 1
            get.root.ids.f_shop.ids.eiffel_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.eiffel_label.pos = dp(420), dp(357)
            get.root.ids.f_shop.ids.eiffel_label.text = f"Property not owned"
            get.root.ids.f_shop.ids.eiffel_label.halign = "center"
            get.root.ids.f_shop.ids.eiffel_label.font_size = 15
            get.root.ids.f_shop.ids.eiffel_label.opacity = 1
            get.root.ids.f_shop.ids.eiffel_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.eiffel_upgrade.pos = dp(521), dp(357)
            get.root.ids.f_shop.ids.eiffel_upgrade.opacity = 1
            get.root.ids.f_shop.ids.eiffel_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade.disabled = True

            if get.root.ids.board.ids.field_9.text == "purple":
                get.root.ids.f_shop.ids.eiffel_label.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.eiffel_upgrade.disabled = False
                    get.root.ids.f_shop.ids.eiffel_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.eiffel_upgrade.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.eiffel_upgrade.disabled = False
                    get.root.ids.f_shop.ids.eiffel_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.eiffel_upgrade.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.eiffel_upgrade.disabled = False
                    get.root.ids.f_shop.ids.eiffel_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.eiffel_upgrade.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.eiffel_label.text = f"Max Level"

        def coliseum():
            count = int(get.root.ids.f_shop.ids.coliseum_count.text)
            count_2 = int(get.root.ids.f_shop.ids.coliseum_count_2.text)
            get.root.ids.f_shop.ids.coliseum_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.coliseum_shop_image.pos = dp(390), dp(324)
            get.root.ids.f_shop.ids.coliseum_shop_image.opacity = 1
            get.root.ids.f_shop.ids.coliseum_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.coliseum_label.pos = dp(420), dp(324)
            get.root.ids.f_shop.ids.coliseum_label.text = f"Property not owned"
            get.root.ids.f_shop.ids.coliseum_label.halign = "center"
            get.root.ids.f_shop.ids.coliseum_label.font_size = 15
            get.root.ids.f_shop.ids.coliseum_label.opacity = 1
            get.root.ids.f_shop.ids.coliseum_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.coliseum_upgrade.pos = dp(521), dp(324)
            get.root.ids.f_shop.ids.coliseum_upgrade.opacity = 1
            get.root.ids.f_shop.ids.coliseum_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade.disabled = True

            if get.root.ids.board.ids.field_13.text == "purple":
                get.root.ids.f_shop.ids.coliseum_label.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.coliseum_upgrade.disabled = False
                    get.root.ids.f_shop.ids.coliseum_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.coliseum_upgrade.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.coliseum_upgrade.disabled = False
                    get.root.ids.f_shop.ids.coliseum_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.coliseum_upgrade.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.coliseum_upgrade.disabled = False
                    get.root.ids.f_shop.ids.coliseum_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.coliseum_upgrade.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.coliseum_label.text = f"Max Level"

        def pisa():
            count = int(get.root.ids.f_shop.ids.pisa_count.text)
            count_2 = int(get.root.ids.f_shop.ids.pisa_count_2.text)
            get.root.ids.f_shop.ids.pisa_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.pisa_shop_image.pos = dp(390), dp(291)
            get.root.ids.f_shop.ids.pisa_shop_image.opacity = 1
            get.root.ids.f_shop.ids.pisa_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.pisa_label.pos = dp(420), dp(291)
            get.root.ids.f_shop.ids.pisa_label.text = f"Property not owned"
            get.root.ids.f_shop.ids.pisa_label.halign = "center"
            get.root.ids.f_shop.ids.pisa_label.font_size = 15
            get.root.ids.f_shop.ids.pisa_label.opacity = 1
            get.root.ids.f_shop.ids.pisa_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.pisa_upgrade.pos = dp(521), dp(291)
            get.root.ids.f_shop.ids.pisa_upgrade.opacity = 1
            get.root.ids.f_shop.ids.pisa_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade.disabled = True

            if get.root.ids.board.ids.field_17.text == "purple":
                get.root.ids.f_shop.ids.pisa_label.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.pisa_upgrade.disabled = False
                    get.root.ids.f_shop.ids.pisa_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.pisa_upgrade.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.pisa_upgrade.disabled = False
                    get.root.ids.f_shop.ids.pisa_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.pisa_upgrade.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.pisa_upgrade.disabled = False
                    get.root.ids.f_shop.ids.pisa_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.pisa_upgrade.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.pisa_label.text = f"Max Level"

        def sydney():
            count = int(get.root.ids.f_shop.ids.sydney_count.text)
            count_2 = int(get.root.ids.f_shop.ids.sydney_count_2.text)
            get.root.ids.f_shop.ids.sydney_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.sydney_shop_image.pos = dp(390), dp(258)
            get.root.ids.f_shop.ids.sydney_shop_image.opacity = 1
            get.root.ids.f_shop.ids.sydney_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.sydney_label.pos = dp(420), dp(258)
            get.root.ids.f_shop.ids.sydney_label.text = f"Property not owned"
            get.root.ids.f_shop.ids.sydney_label.halign = "center"
            get.root.ids.f_shop.ids.sydney_label.font_size = 15
            get.root.ids.f_shop.ids.sydney_label.opacity = 1
            get.root.ids.f_shop.ids.sydney_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.sydney_upgrade.pos = dp(521), dp(258)
            get.root.ids.f_shop.ids.sydney_upgrade.opacity = 1
            get.root.ids.f_shop.ids.sydney_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade.disabled = True

            if get.root.ids.board.ids.field_33.text == "purple":
                get.root.ids.f_shop.ids.sydney_label.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.sydney_upgrade.disabled = False
                    get.root.ids.f_shop.ids.sydney_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.sydney_upgrade.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.sydney_upgrade.disabled = False
                    get.root.ids.f_shop.ids.sydney_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.sydney_upgrade.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.sydney_upgrade.disabled = False
                    get.root.ids.f_shop.ids.sydney_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.sydney_upgrade.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.sydney_label.text = f"Max Level"

        def le_louvre():
            count = int(get.root.ids.f_shop.ids.louvre_count.text)
            count_2 = int(get.root.ids.f_shop.ids.louvre_count_2.text)
            get.root.ids.f_shop.ids.louvre_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.louvre_shop_image.pos = dp(390), dp(225)
            get.root.ids.f_shop.ids.louvre_shop_image.opacity = 1
            get.root.ids.f_shop.ids.louvre_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.louvre_label.pos = dp(420), dp(225)
            get.root.ids.f_shop.ids.louvre_label.text = f"Property not owned"
            get.root.ids.f_shop.ids.louvre_label.halign = "center"
            get.root.ids.f_shop.ids.louvre_label.font_size = 15
            get.root.ids.f_shop.ids.louvre_label.opacity = 1
            get.root.ids.f_shop.ids.louvre_upgrade.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.louvre_upgrade.pos = dp(521), dp(225)
            get.root.ids.f_shop.ids.louvre_upgrade.opacity = 1
            get.root.ids.f_shop.ids.louvre_upgrade.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade.disabled = True

            if get.root.ids.board.ids.field_33.text == "purple":
                get.root.ids.f_shop.ids.louvre_label.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.louvre_upgrade.disabled = False
                    get.root.ids.f_shop.ids.louvre_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.louvre_upgrade.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.louvre_upgrade.disabled = False
                    get.root.ids.f_shop.ids.louvre_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.louvre_upgrade.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.louvre_upgrade.disabled = False
                    get.root.ids.f_shop.ids.louvre_label.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.louvre_upgrade.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.louvre_label.text = f"Max Level"

        def thief():
            count = int(get.root.ids.f_shop.ids.anti_steal_count.text)
            get.root.ids.f_shop.ids.anti_thief_image.size = dp(30), dp(30)
            get.root.ids.f_shop.ids.anti_thief_image.pos = dp(570), dp(390)
            get.root.ids.f_shop.ids.anti_thief_image.opacity = 1

            get.root.ids.f_shop.ids.anti_steal_label.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.anti_steal_label.pos = dp(600), dp(390)
            get.root.ids.f_shop.ids.anti_steal_label.halign = "center"
            get.root.ids.f_shop.ids.anti_steal_label.font_size = 18
            get.root.ids.f_shop.ids.anti_steal_label.text = f"x {get.root.ids.f_shop.ids.anti_steal_count.text}"
            get.root.ids.f_shop.ids.anti_steal_label.opacity = 1

            get.root.ids.f_shop.ids.anti_thief_buy.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.anti_thief_buy.pos = dp(701), dp(390)
            get.root.ids.f_shop.ids.anti_thief_buy.opacity = 1
            get.root.ids.f_shop.ids.anti_thief_buy.text = "Use"
            get.root.ids.f_shop.ids.anti_thief_buy.disabled = False
            get.root.ids.f_shop.ids.shop_main_exit.text = "Back"

            if count == 0 or get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.f_shop.ids.anti_thief_buy.disabled = True

        big_ben()
        eiffel()
        coliseum()
        pisa()
        sydney()
        le_louvre()

        thief()

    def main_exit(self):
        get = App.get_running_app()
        if get.root.ids.f_shop.ids.shop_main_exit.text == "Exit":
            get.root.ids.board.ids.big.opacity = 1
            get.root.ids.f_shop.ids.shop_main_exit.opacity = 0
            get.root.ids.f_shop.ids.shop_main_exit.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.shop_main_exit.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.shop_main_exit.disabled = True
            unblock_roll()
            self.hide_buttons()
            self.hide_shop()
        if get.root.ids.f_shop.ids.shop_main_exit.text == "Back":
            get.root.ids.f_shop.ids.shop_main_exit.text = "Exit"
            self.hide_shop()
            self.show_main()

    def shop_on_press(self):
        self.ids.player_1_shop_image.source = "images/shop_on_press.png"

    def shop_on_release(self):
        self.ids.player_1_shop_image.source = "images/shop.png"

    def inventory_on_press(self):
        self.ids.player_1_inventory_image.source = "images/inventory_on_press.png"

    def inventory_on_release(self):
        self.ids.player_1_inventory_image.source = "images/inventory_button.png"

    # Player 2 - Shop

    @staticmethod
    def show_main_2(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.opacity = 0

        get.root.ids.f_shop.ids.player_2_shop.disabled = False
        get.root.ids.f_shop.ids.player_2_shop_image.opacity = 1
        get.root.ids.f_shop.ids.player_2_shop_image.size = dp(200), dp(200)
        get.root.ids.f_shop.ids.player_2_shop.opacity = 1
        get.root.ids.f_shop.ids.player_2_shop.size = dp(200), dp(200)
        get.root.ids.f_shop.ids.player_2_shop.pos = dp(415), dp(235)

        get.root.ids.f_shop.ids.player_2_inventory.disabled = False
        get.root.ids.f_shop.ids.player_2_inventory_image.opacity = 1
        get.root.ids.f_shop.ids.player_2_inventory_image.size = dp(200), dp(230)
        get.root.ids.f_shop.ids.player_2_inventory.opacity = 1
        get.root.ids.f_shop.ids.player_2_inventory.size = dp(200), dp(200)
        get.root.ids.f_shop.ids.player_2_inventory.pos = dp(700), dp(235)

        get.root.ids.f_shop.ids.shop_main_exit_2.opacity = 1
        get.root.ids.f_shop.ids.shop_main_exit_2.size = dp(70), dp(25)
        get.root.ids.f_shop.ids.shop_main_exit_2.pos = dp(625), dp(210)
        get.root.ids.f_shop.ids.shop_main_exit_2.text = "Exit"
        get.root.ids.f_shop.ids.shop_main_exit_2.disabled = False

    @staticmethod
    def hide_buttons_2():
        get = App.get_running_app()
        get.root.ids.f_shop.ids.player_2_shop.disabled = True
        get.root.ids.f_shop.ids.player_2_shop_image.opacity = 0
        get.root.ids.f_shop.ids.player_2_shop_image.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_2_shop.opacity = 0
        get.root.ids.f_shop.ids.player_2_shop.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_2_shop.pos = dp(0), dp(0)

        get.root.ids.f_shop.ids.player_2_inventory.disabled = True
        get.root.ids.f_shop.ids.player_2_inventory_image.opacity = 0
        get.root.ids.f_shop.ids.player_2_inventory_image.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_2_inventory.opacity = 0
        get.root.ids.f_shop.ids.player_2_inventory.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.player_2_inventory.pos = dp(0), dp(0)

    @staticmethod
    def show_main_sh_in_2():
        get = App.get_running_app()
        get.root.ids.f_shop.ids.shop_inventory_background.size = dp(545), dp(270)
        get.root.ids.f_shop.ids.shop_inventory_background.pos = dp(385), dp(203)
        get.root.ids.f_shop.ids.shop_inventory_background.opacity = 1

        get.root.ids.f_shop.ids.building_upgrades.size = dp(175), dp(45)
        get.root.ids.f_shop.ids.building_upgrades.pos = dp(390), dp(423)
        get.root.ids.f_shop.ids.building_upgrades.opacity = 1

        get.root.ids.f_shop.ids.anti_field_cards.size = dp(175), dp(45)
        get.root.ids.f_shop.ids.anti_field_cards.pos = dp(570), dp(423)
        get.root.ids.f_shop.ids.anti_field_cards.opacity = 1

        get.root.ids.f_shop.ids.attack_others.size = dp(175), dp(45)
        get.root.ids.f_shop.ids.attack_others.pos = dp(750), dp(423)
        get.root.ids.f_shop.ids.attack_others.opacity = 1

    def show_shop_2(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos
        self.hide_buttons_2()
        self.show_main_sh_in_2()
        get.root.ids.f_shop.ids.shop_main_exit_2.text = "Back"

        def big_ben():
            count = int(get.root.ids.f_shop.ids.big_ben_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.big_ben_count_2_2.text)
            get.root.ids.f_shop.ids.big_ben_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.big_ben_shop_image.pos = dp(390), dp(390)
            get.root.ids.f_shop.ids.big_ben_shop_image.opacity = 1

            get.root.ids.f_shop.ids.big_ben_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.big_ben_label_2.pos = dp(420), dp(390)
            get.root.ids.f_shop.ids.big_ben_label_2.text = "Property not owned"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_label_2.halign = "center"
            get.root.ids.f_shop.ids.big_ben_label_2.font_size = 15
            get.root.ids.f_shop.ids.big_ben_label_2.opacity = 1

            get.root.ids.f_shop.ids.big_ben_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.big_ben_upgrade_2.pos = dp(521), dp(390)
            get.root.ids.f_shop.ids.big_ben_upgrade_2.opacity = 1

            if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "N/A":
                get.root.ids.f_shop.ids.big_ben_upgrade_2.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_5.text == "green":
                get.root.ids.f_shop.ids.big_ben_label_2.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.big_ben_label_2.text = "Rent goes from 30 $ to 50 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "40 $"
                    else:
                        get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "80 $"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.big_ben_label_2.text = "Rent goes from 50 $ to 85 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "50 $"
                    else:
                        get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "100 $"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.big_ben_label_2.text = "Rent goes from 85 $ to 120 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "60 $"
                    else:
                        get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "120 $"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.big_ben_label_2.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "Max"

        def eiffel():
            count = int(get.root.ids.f_shop.ids.eiffel_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.eiffel_count_2_2.text)
            get.root.ids.f_shop.ids.eiffel_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.eiffel_shop_image.pos = dp(390), dp(357)
            get.root.ids.f_shop.ids.eiffel_shop_image.opacity = 1

            get.root.ids.f_shop.ids.eiffel_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.eiffel_label_2.pos = dp(420), dp(357)
            get.root.ids.f_shop.ids.eiffel_label_2.text = "Property not owned"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_label_2.halign = "center"
            get.root.ids.f_shop.ids.eiffel_label_2.font_size = 15
            get.root.ids.f_shop.ids.eiffel_label_2.opacity = 1

            get.root.ids.f_shop.ids.eiffel_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.eiffel_upgrade_2.pos = dp(521), dp(357)
            get.root.ids.f_shop.ids.eiffel_upgrade_2.opacity = 1

            if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "N/A":
                get.root.ids.f_shop.ids.eiffel_upgrade_2.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_9.text == "green":
                get.root.ids.f_shop.ids.eiffel_label_2.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.eiffel_label_2.text = "Rent goes from 50 $ to 80 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "45 $"
                    else:
                        get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "90 $"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.eiffel_label_2.text = "Rent goes from 80 $ to 115 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "60 $"
                    else:
                        get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "120 $"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.eiffel_label_2.text = "Rent goes from 115 $ to 150 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "75 $"
                    else:
                        get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "150 $"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.eiffel_label_2.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "Max"

        def coliseum():
            count = int(get.root.ids.f_shop.ids.coliseum_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.coliseum_count_2_2.text)
            get.root.ids.f_shop.ids.coliseum_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.coliseum_shop_image.pos = dp(390), dp(324)
            get.root.ids.f_shop.ids.coliseum_shop_image.opacity = 1

            get.root.ids.f_shop.ids.coliseum_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.coliseum_label_2.pos = dp(420), dp(324)
            get.root.ids.f_shop.ids.coliseum_label_2.text = "Property not owned"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_label_2.halign = "center"
            get.root.ids.f_shop.ids.coliseum_label_2.font_size = 15
            get.root.ids.f_shop.ids.coliseum_label_2.opacity = 1

            get.root.ids.f_shop.ids.coliseum_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.coliseum_upgrade_2.pos = dp(521), dp(324)
            get.root.ids.f_shop.ids.coliseum_upgrade_2.opacity = 1

            if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "N/A":
                get.root.ids.f_shop.ids.coliseum_upgrade_2.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_13.text == "green":
                get.root.ids.f_shop.ids.coliseum_label_2.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.coliseum_label_2.text = "Rent goes from 70 $ to 110 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "55 $"
                    else:
                        get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "110 $"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.coliseum_label_2.text = "Rent goes from 110 $ to 150 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "70 $"
                    else:
                        get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "140 $"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.coliseum_label_2.text = "Rent goes from 150 $ to 190 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "85 $"
                    else:
                        get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "170 $"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.coliseum_label_2.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "Max"

        def pisa():
            count = int(get.root.ids.f_shop.ids.pisa_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.pisa_count_2_2.text)
            get.root.ids.f_shop.ids.pisa_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.pisa_shop_image.pos = dp(390), dp(291)
            get.root.ids.f_shop.ids.pisa_shop_image.opacity = 1

            get.root.ids.f_shop.ids.pisa_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.pisa_label_2.pos = dp(420), dp(291)
            get.root.ids.f_shop.ids.pisa_label_2.text = "Property not owned"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_label_2.halign = "center"
            get.root.ids.f_shop.ids.pisa_label_2.font_size = 15
            get.root.ids.f_shop.ids.pisa_label_2.opacity = 1

            get.root.ids.f_shop.ids.pisa_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.pisa_upgrade_2.pos = dp(521), dp(291)
            get.root.ids.f_shop.ids.pisa_upgrade_2.opacity = 1

            if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "N/A":
                get.root.ids.f_shop.ids.pisa_upgrade_2.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_17.text == "green":
                get.root.ids.f_shop.ids.pisa_label_2.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.pisa_label_2.text = "Rent goes from 100 $ to 150 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.pisa_upgrade_2.text = "75 $"
                    else:
                        get.root.ids.f_shop.ids.pisa_upgrade_2.text = "150 $"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.pisa_label_2.text = "Rent goes from 150 $ to 200 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.pisa_upgrade_2.text = "100 $"
                    else:
                        get.root.ids.f_shop.ids.pisa_upgrade_2.text = "200 $"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.pisa_label_2.text = "Rent goes from 200 $ to 250 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.pisa_upgrade_2.text = "125 $"
                    else:
                        get.root.ids.f_shop.ids.pisa_upgrade_2.text = "250 $"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.pisa_label_2.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.text = "Max"

        def sydney():
            count = int(get.root.ids.f_shop.ids.sydney_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.sydney_count_2_2.text)
            get.root.ids.f_shop.ids.sydney_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.sydney_shop_image.pos = dp(390), dp(258)
            get.root.ids.f_shop.ids.sydney_shop_image.opacity = 1

            get.root.ids.f_shop.ids.sydney_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.sydney_label_2.pos = dp(420), dp(258)
            get.root.ids.f_shop.ids.sydney_label_2.text = "Property not owned"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_label_2.halign = "center"
            get.root.ids.f_shop.ids.sydney_label_2.font_size = 15
            get.root.ids.f_shop.ids.sydney_label_2.opacity = 1

            get.root.ids.f_shop.ids.sydney_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.sydney_upgrade_2.pos = dp(521), dp(258)
            get.root.ids.f_shop.ids.sydney_upgrade_2.opacity = 1

            if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "N/A":
                get.root.ids.f_shop.ids.sydney_upgrade_2.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_22.text == "green":
                get.root.ids.f_shop.ids.sydney_label_2.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.sydney_label_2.text = "Rent goes from 130 $ to 200 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.sydney_upgrade_2.text = "100 $"
                    else:
                        get.root.ids.f_shop.ids.sydney_upgrade_2.text = "200 $"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.sydney_label_2.text = "Rent goes from 200 $ to 250 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.sydney_upgrade_2.text = "125 $"
                    else:
                        get.root.ids.f_shop.ids.sydney_upgrade_2.text = "250 $"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.sydney_label_2.text = "Rent goes from 250 $ to 300 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.sydney_upgrade_2.text = "150 $"
                    else:
                        get.root.ids.f_shop.ids.sydney_upgrade_2.text = "300 $"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.sydney_label_2.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.text = "Max"

        def le_louvre():
            count = int(get.root.ids.f_shop.ids.louvre_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.louvre_count_2_2.text)
            get.root.ids.f_shop.ids.louvre_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.louvre_shop_image.pos = dp(390), dp(225)
            get.root.ids.f_shop.ids.louvre_shop_image.opacity = 1

            get.root.ids.f_shop.ids.louvre_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.louvre_label_2.pos = dp(420), dp(225)
            get.root.ids.f_shop.ids.louvre_label_2.text = "Property not owned"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_label_2.halign = "center"
            get.root.ids.f_shop.ids.louvre_label_2.font_size = 15
            get.root.ids.f_shop.ids.louvre_label_2.opacity = 1

            get.root.ids.f_shop.ids.louvre_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.louvre_upgrade_2.pos = dp(521), dp(225)
            get.root.ids.f_shop.ids.louvre_upgrade_2.opacity = 1

            if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "N/A":
                get.root.ids.f_shop.ids.louvre_upgrade_2.color = (1, 0, 0, 1)
            if get.root.ids.board.ids.field_33.text == "green":
                get.root.ids.f_shop.ids.louvre_label_2.text = "Upgrade in inventory"
                if count == 0 and count_2 == 0:
                    get.root.ids.f_shop.ids.louvre_label_2.text = "Rent goes from 150 $ to 230 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.louvre_upgrade_2.text = "120 $"
                    else:
                        get.root.ids.f_shop.ids.louvre_upgrade_2.text = "240 $"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = False
                if count == 1 and count_2 == 1:
                    get.root.ids.f_shop.ids.louvre_label_2.text = "Rent goes from 230 $ to 300 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.louvre_upgrade_2.text = "150 $"
                    else:
                        get.root.ids.f_shop.ids.louvre_upgrade_2.text = "300 $"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = False
                if count == 2 and count_2 == 2:
                    get.root.ids.f_shop.ids.louvre_label_2.text = "Rent goes from 300 $ to 350 $"
                    if x == p2_pos23_x and y == p2_pos23_y:
                        get.root.ids.f_shop.ids.louvre_upgrade_2.text = "175 $"
                    else:
                        get.root.ids.f_shop.ids.louvre_upgrade_2.text = "350 $"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = False
                if count == 3:
                    get.root.ids.f_shop.ids.louvre_label_2.text = f"No more upgrades"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.text = "Max"

        def thief():
            get.root.ids.f_shop.ids.anti_thief_image.size = dp(30), dp(30)
            get.root.ids.f_shop.ids.anti_thief_image.pos = dp(570), dp(390)
            get.root.ids.f_shop.ids.anti_thief_image.opacity = 1

            get.root.ids.f_shop.ids.anti_steal_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.anti_steal_label_2.pos = dp(600), dp(390)
            get.root.ids.f_shop.ids.anti_steal_label_2.text = "Blocks the Thief"
            get.root.ids.f_shop.ids.anti_steal_label_2.halign = "left"
            get.root.ids.f_shop.ids.anti_steal_label_2.font_size = 13
            get.root.ids.f_shop.ids.anti_steal_label_2.opacity = 1

            get.root.ids.f_shop.ids.anti_thief_buy_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.anti_thief_buy_2.pos = dp(701), dp(390)
            get.root.ids.f_shop.ids.anti_thief_buy_2.opacity = 1
            if x == p2_pos23_x and y == p2_pos23_y:
                get.root.ids.f_shop.ids.anti_thief_buy_2.text = "15 pts"
                if int(get.root.ids.p2.ids.p2_points_stash.text) < 15:
                    get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True
                else:
                    get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = False
            else:
                get.root.ids.f_shop.ids.anti_thief_buy_2.text = "30 pts"
                if int(get.root.ids.p2.ids.p2_points_stash.text) < 30:
                    get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True
                else:
                    get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = False

        big_ben()
        eiffel()
        coliseum()
        pisa()
        sydney()
        le_louvre()

        thief()

    @staticmethod
    def hide_shop_2():
        get = App.get_running_app()
        get.root.ids.f_shop.ids.shop_inventory_background.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.shop_inventory_background.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.shop_inventory_background.opacity = 0

        get.root.ids.f_shop.ids.building_upgrades.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.building_upgrades.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.building_upgrades.opacity = 0

        get.root.ids.f_shop.ids.anti_field_cards.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.anti_field_cards.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.anti_field_cards.opacity = 0

        get.root.ids.f_shop.ids.attack_others.size = dp(0), dp(0)
        get.root.ids.f_shop.ids.attack_others.pos = dp(0), dp(0)
        get.root.ids.f_shop.ids.attack_others.opacity = 0

        def big_ben():
            get.root.ids.f_shop.ids.big_ben_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_shop_image.opacity = 0

            get.root.ids.f_shop.ids.big_ben_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_label_2.font_size = 13
            get.root.ids.f_shop.ids.big_ben_label_2.opacity = 0

            get.root.ids.f_shop.ids.big_ben_upgrade_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_upgrade_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.big_ben_upgrade_2.opacity = 0
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        def eiffel():
            get.root.ids.f_shop.ids.eiffel_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_shop_image.opacity = 0

            get.root.ids.f_shop.ids.eiffel_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_label_2.font_size = 13
            get.root.ids.f_shop.ids.eiffel_label_2.opacity = 0

            get.root.ids.f_shop.ids.eiffel_upgrade_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_upgrade_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.eiffel_upgrade_2.opacity = 0
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        def coliseum():
            get.root.ids.f_shop.ids.coliseum_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_shop_image.opacity = 0

            get.root.ids.f_shop.ids.coliseum_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_label_2.font_size = 13
            get.root.ids.f_shop.ids.coliseum_label_2.opacity = 0

            get.root.ids.f_shop.ids.coliseum_upgrade_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_upgrade_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.coliseum_upgrade_2.opacity = 0
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        def pisa():
            get.root.ids.f_shop.ids.pisa_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_shop_image.opacity = 0

            get.root.ids.f_shop.ids.pisa_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_label_2.font_size = 13
            get.root.ids.f_shop.ids.pisa_label_2.opacity = 0

            get.root.ids.f_shop.ids.pisa_upgrade_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_upgrade_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.pisa_upgrade_2.opacity = 0
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        def sydney():
            get.root.ids.f_shop.ids.sydney_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_shop_image.opacity = 0

            get.root.ids.f_shop.ids.sydney_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_label_2.font_size = 13
            get.root.ids.f_shop.ids.sydney_label_2.opacity = 0

            get.root.ids.f_shop.ids.sydney_upgrade_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_upgrade_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.sydney_upgrade_2.opacity = 0
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        def le_louvre():
            get.root.ids.f_shop.ids.louvre_shop_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_shop_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_shop_image.opacity = 0

            get.root.ids.f_shop.ids.louvre_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_label_2.font_size = 13
            get.root.ids.f_shop.ids.louvre_label_2.opacity = 0

            get.root.ids.f_shop.ids.louvre_upgrade_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_upgrade_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.louvre_upgrade_2.opacity = 0
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        def thief():
            get.root.ids.f_shop.ids.anti_thief_image.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_image.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_image.opacity = 0

            get.root.ids.f_shop.ids.anti_steal_label_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_steal_label_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_steal_label_2.opacity = 0

            get.root.ids.f_shop.ids.anti_thief_buy_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_buy_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.anti_thief_buy_2.opacity = 0
            get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True

        big_ben()
        eiffel()
        coliseum()
        pisa()
        sydney()
        le_louvre()

        thief()

    @staticmethod
    def big_ben_upgrade_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.big_ben_count_22.text)
        count_2 = int(get.root.ids.f_shop.ids.big_ben_count_2_2.text)

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "80 $":
            get.root.ids.board.ids.cash_count.text = "-80 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 80}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "40 $":
            get.root.ids.board.ids.cash_count.text = "-40 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 40}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "100 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 100}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "50 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-50 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 50}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "120 $":
            get.root.ids.board.ids.cash_count.text = "-120 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 120}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label_2.text = f"No more upgrades"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "Max"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "60 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-60 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 60}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.big_ben_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.big_ben_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.big_ben_upgrade_2.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.big_ben_label_2.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.big_ben_count_2_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.big_ben_label_2.text = f"Max Level"

    @staticmethod
    def eiffel_upgrade_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.eiffel_count_22.text)
        count_2 = int(get.root.ids.f_shop.ids.eiffel_count_2_2.text)

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "90 $":
            get.root.ids.board.ids.cash_count.text = "-90 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 90}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "45 $":
            get.root.ids.board.ids.cash_count.text = "-45 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 45}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "120 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-120 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 120}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "60 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-60 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 60}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "150 $":
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"No more upgrades"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "Max"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "75 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-75 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 75}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.eiffel_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.eiffel_upgrade_2.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.eiffel_count_2_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.eiffel_label_2.text = f"Max Level"

    @staticmethod
    def coliseum_upgrade_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.coliseum_count_22.text)
        count_2 = int(get.root.ids.f_shop.ids.coliseum_count_2_2.text)

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "110 $":
            get.root.ids.board.ids.cash_count.text = "-110 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 110}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "55 $":
            get.root.ids.board.ids.cash_count.text = "-55 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 55}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "140 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-140 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 140}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "70 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-70 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 70}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "170 $":
            get.root.ids.board.ids.cash_count.text = "-170 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 170}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"No more upgrades"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "Max"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "85 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-85 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 85}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.coliseum_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.coliseum_upgrade_2.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.coliseum_count_2_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.coliseum_label_2.text = f"Max Level"

    @staticmethod
    def pisa_upgrade_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.pisa_count_22.text)
        count_2 = int(get.root.ids.f_shop.ids.pisa_count_2_2.text)

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "150 $":
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "75 $":
            get.root.ids.board.ids.cash_count.text = "-75 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 75}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "200 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-200 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 200}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "100 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 100}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "250 $":
            get.root.ids.board.ids.cash_count.text = "-250 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 250}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label_2.text = f"No more upgrades"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "Max"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "125 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-125 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 125}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.pisa_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.pisa_upgrade_2.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.pisa_count_2_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.pisa_label_2.text = f"Max Level"

    @staticmethod
    def sydney_upgrade_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.sydney_count_22.text)
        count_2 = int(get.root.ids.f_shop.ids.sydney_count_2_2.text)

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "200 $":
            get.root.ids.board.ids.cash_count.text = "-200 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 200}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "100 $":
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 100}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "250 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-250 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 250}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "125 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-125 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 125}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "300 $":
            get.root.ids.board.ids.cash_count.text = "-300 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 300}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label_2.text = f"No more upgrades"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "Max"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "150 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.sydney_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.sydney_upgrade_2.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.sydney_count_2_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.sydney_label_2.text = f"Max Level"

    @staticmethod
    def le_louvre_upgrade_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.louvre_count_22.text)
        count_2 = int(get.root.ids.f_shop.ids.louvre_count_2_2.text)

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "240 $":
            get.root.ids.board.ids.cash_count.text = "-240 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 240}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "120 $":
            get.root.ids.board.ids.cash_count.text = "-120 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 120}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "300 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-300 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 300}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "150 $" and count_2 == 1:
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "350 $":
            get.root.ids.board.ids.cash_count.text = "-350 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 350}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label_2.text = f"No more upgrades"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "Max"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "175 $" and count_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-175 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 175}"
            player_2_cash_count_r()
            count += 1
            get.root.ids.f_shop.ids.louvre_count_22.text = f"{count}"
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Upgrade in Inventory"
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

        Clock.schedule_once(hide_cash_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.louvre_upgrade_2.text == "Upgr.":
            count_2 += 1
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Level {count_2}"
            get.root.ids.f_shop.ids.louvre_count_2_2.text = f"{count_2}"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True
            if count_2 == 3:
                get.root.ids.f_shop.ids.louvre_label_2.text = f"Max Level"

    @staticmethod
    def anti_thief_buy_2(*args):
        get = App.get_running_app()
        count = int(get.root.ids.f_shop.ids.anti_steal_count_2.text)

        if get.root.ids.f_shop.ids.anti_thief_buy_2.text == "30 pts":
            get.root.ids.board.ids.points_count.text = "-30 pts."
            get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 30}"
            player_2_points_count()
            count += 1
            get.root.ids.f_shop.ids.anti_steal_count_2.text = f"{count}"
            get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True

        if get.root.ids.f_shop.ids.anti_thief_buy_2.text == "15 pts":
            get.root.ids.board.ids.points_count.text = "-15 pts."
            get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 15}"
            player_2_points_count()
            count += 1
            get.root.ids.f_shop.ids.anti_steal_count_2.text = f"{count}"
            get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True

        Clock.schedule_once(hide_points_count, 1.5)
        Clock.schedule_once(money_update, 1.5)

        if get.root.ids.f_shop.ids.anti_thief_buy_2.text == "Use":
            count -= 1
            get.root.ids.f_shop.ids.anti_steal_count_2.text = f"{count}"
            get.root.ids.f_shop.ids.anti_steal_label_2.text = f"x {get.root.ids.f_shop.ids.anti_steal_count_2.text}"
            get.root.ids.f_shop.ids.anti_thief_active_2.size = dp(30), dp(30)
            get.root.ids.f_shop.ids.anti_thief_active_2.pos = dp(1285), dp(310)
            get.root.ids.f_shop.ids.anti_thief_active_2.opacity = 1
            if count == 0 or get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True

    def show_inventory_2(self):
        get = App.get_running_app()
        get.root.ids.f_shop.ids.shop_main_exit_2.text = "Back"

        self.hide_buttons_2()
        self.show_main_sh_in_2()

        def big_ben():
            count = int(get.root.ids.f_shop.ids.big_ben_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.big_ben_count_2_2.text)
            get.root.ids.f_shop.ids.big_ben_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.big_ben_shop_image.pos = dp(390), dp(390)
            get.root.ids.f_shop.ids.big_ben_shop_image.opacity = 1
            get.root.ids.f_shop.ids.big_ben_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.big_ben_label_2.pos = dp(420), dp(390)
            get.root.ids.f_shop.ids.big_ben_label_2.text = f"Property not owned"
            get.root.ids.f_shop.ids.big_ben_label_2.halign = "center"
            get.root.ids.f_shop.ids.big_ben_label_2.font_size = 15
            get.root.ids.f_shop.ids.big_ben_label_2.opacity = 1
            get.root.ids.f_shop.ids.big_ben_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.big_ben_upgrade_2.pos = dp(521), dp(390)
            get.root.ids.f_shop.ids.big_ben_upgrade_2.opacity = 1
            get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = True

            if get.root.ids.board.ids.field_5.text == "green":
                get.root.ids.f_shop.ids.big_ben_label_2.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.big_ben_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.big_ben_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.big_ben_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.big_ben_upgrade_2.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.big_ben_label_2.text = f"Max Level"

        def eiffel():
            count = int(get.root.ids.f_shop.ids.eiffel_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.eiffel_count_2_2.text)
            get.root.ids.f_shop.ids.eiffel_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.eiffel_shop_image.pos = dp(390), dp(357)
            get.root.ids.f_shop.ids.eiffel_shop_image.opacity = 1
            get.root.ids.f_shop.ids.eiffel_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.eiffel_label_2.pos = dp(420), dp(357)
            get.root.ids.f_shop.ids.eiffel_label_2.text = f"Property not owned"
            get.root.ids.f_shop.ids.eiffel_label_2.halign = "center"
            get.root.ids.f_shop.ids.eiffel_label_2.font_size = 15
            get.root.ids.f_shop.ids.eiffel_label_2.opacity = 1
            get.root.ids.f_shop.ids.eiffel_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.eiffel_upgrade_2.pos = dp(521), dp(357)
            get.root.ids.f_shop.ids.eiffel_upgrade_2.opacity = 1
            get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = True

            if get.root.ids.board.ids.field_9.text == "green":
                get.root.ids.f_shop.ids.eiffel_label_2.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.eiffel_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.eiffel_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.eiffel_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.eiffel_upgrade_2.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.eiffel_label_2.text = f"Max Level"

        def coliseum():
            count = int(get.root.ids.f_shop.ids.coliseum_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.coliseum_count_2_2.text)
            get.root.ids.f_shop.ids.coliseum_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.coliseum_shop_image.pos = dp(390), dp(324)
            get.root.ids.f_shop.ids.coliseum_shop_image.opacity = 1
            get.root.ids.f_shop.ids.coliseum_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.coliseum_label_2.pos = dp(420), dp(324)
            get.root.ids.f_shop.ids.coliseum_label_2.text = f"Property not owned"
            get.root.ids.f_shop.ids.coliseum_label_2.halign = "center"
            get.root.ids.f_shop.ids.coliseum_label_2.font_size = 15
            get.root.ids.f_shop.ids.coliseum_label_2.opacity = 1
            get.root.ids.f_shop.ids.coliseum_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.coliseum_upgrade_2.pos = dp(521), dp(324)
            get.root.ids.f_shop.ids.coliseum_upgrade_2.opacity = 1
            get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = True

            if get.root.ids.board.ids.field_13.text == "green":
                get.root.ids.f_shop.ids.coliseum_label_2.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.coliseum_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.coliseum_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.coliseum_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.coliseum_upgrade_2.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.coliseum_label_2.text = f"Max Level"

        def pisa():
            count = int(get.root.ids.f_shop.ids.pisa_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.pisa_count_2_2.text)
            get.root.ids.f_shop.ids.pisa_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.pisa_shop_image.pos = dp(390), dp(291)
            get.root.ids.f_shop.ids.pisa_shop_image.opacity = 1
            get.root.ids.f_shop.ids.pisa_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.pisa_label_2.pos = dp(420), dp(291)
            get.root.ids.f_shop.ids.pisa_label_2.text = f"Property not owned"
            get.root.ids.f_shop.ids.pisa_label_2.halign = "center"
            get.root.ids.f_shop.ids.pisa_label_2.font_size = 15
            get.root.ids.f_shop.ids.pisa_label_2.opacity = 1
            get.root.ids.f_shop.ids.pisa_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.pisa_upgrade_2.pos = dp(521), dp(291)
            get.root.ids.f_shop.ids.pisa_upgrade_2.opacity = 1
            get.root.ids.f_shop.ids.pisa_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = True

            if get.root.ids.board.ids.field_17.text == "green":
                get.root.ids.f_shop.ids.pisa_label_2.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.pisa_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.pisa_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.pisa_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.pisa_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.pisa_upgrade_2.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.pisa_label_2.text = f"Max Level"

        def sydney():
            count = int(get.root.ids.f_shop.ids.sydney_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.sydney_count_2_2.text)
            get.root.ids.f_shop.ids.sydney_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.sydney_shop_image.pos = dp(390), dp(258)
            get.root.ids.f_shop.ids.sydney_shop_image.opacity = 1
            get.root.ids.f_shop.ids.sydney_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.sydney_label_2.pos = dp(420), dp(258)
            get.root.ids.f_shop.ids.sydney_label_2.text = f"Property not owned"
            get.root.ids.f_shop.ids.sydney_label_2.halign = "center"
            get.root.ids.f_shop.ids.sydney_label_2.font_size = 15
            get.root.ids.f_shop.ids.sydney_label_2.opacity = 1
            get.root.ids.f_shop.ids.sydney_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.sydney_upgrade_2.pos = dp(521), dp(258)
            get.root.ids.f_shop.ids.sydney_upgrade_2.opacity = 1
            get.root.ids.f_shop.ids.sydney_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = True

            if get.root.ids.board.ids.field_22.text == "green":
                get.root.ids.f_shop.ids.sydney_label_2.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.sydney_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.sydney_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.sydney_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.sydney_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.sydney_upgrade_2.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.sydney_label_2.text = f"Max Level"

        def le_louvre():
            count = int(get.root.ids.f_shop.ids.louvre_count_22.text)
            count_2 = int(get.root.ids.f_shop.ids.louvre_count_2_2.text)
            get.root.ids.f_shop.ids.louvre_shop_image.size = dp(29), dp(30)
            get.root.ids.f_shop.ids.louvre_shop_image.pos = dp(390), dp(225)
            get.root.ids.f_shop.ids.louvre_shop_image.opacity = 1
            get.root.ids.f_shop.ids.louvre_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.louvre_label_2.pos = dp(420), dp(225)
            get.root.ids.f_shop.ids.louvre_label_2.text = f"Property not owned"
            get.root.ids.f_shop.ids.louvre_label_2.halign = "center"
            get.root.ids.f_shop.ids.louvre_label_2.font_size = 15
            get.root.ids.f_shop.ids.louvre_label_2.opacity = 1
            get.root.ids.f_shop.ids.louvre_upgrade_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.louvre_upgrade_2.pos = dp(521), dp(225)
            get.root.ids.f_shop.ids.louvre_upgrade_2.opacity = 1
            get.root.ids.f_shop.ids.louvre_upgrade_2.text = "N/A"
            get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = True

            if get.root.ids.board.ids.field_33.text == "green":
                get.root.ids.f_shop.ids.louvre_label_2.text = f"Buy an upgrade"
                if count == 1 and count_2 == 0:
                    get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.louvre_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.text = "Upgr."
                if count == 2 and count_2 == 1:
                    get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.louvre_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.text = "Upgr."
                if count == 3 and count_2 == 2:
                    get.root.ids.f_shop.ids.louvre_upgrade_2.disabled = False
                    get.root.ids.f_shop.ids.louvre_label_2.text = f"Level {count_2}"
                    get.root.ids.f_shop.ids.louvre_upgrade_2.text = "Upgr."
                if count_2 == 3:
                    get.root.ids.f_shop.ids.louvre_label_2.text = f"Max Level"

        def thief():
            count = int(get.root.ids.f_shop.ids.anti_steal_count_2.text)
            get.root.ids.f_shop.ids.anti_thief_image.size = dp(30), dp(30)
            get.root.ids.f_shop.ids.anti_thief_image.pos = dp(570), dp(390)
            get.root.ids.f_shop.ids.anti_thief_image.opacity = 1

            get.root.ids.f_shop.ids.anti_steal_label_2.size = dp(100), dp(30)
            get.root.ids.f_shop.ids.anti_steal_label_2.pos = dp(600), dp(390)
            get.root.ids.f_shop.ids.anti_steal_label_2.halign = "center"
            get.root.ids.f_shop.ids.anti_steal_label_2.font_size = 18
            get.root.ids.f_shop.ids.anti_steal_label_2.text = f"x {get.root.ids.f_shop.ids.anti_steal_count_2.text}"
            get.root.ids.f_shop.ids.anti_steal_label_2.opacity = 1

            get.root.ids.f_shop.ids.anti_thief_buy_2.size = dp(44), dp(30)
            get.root.ids.f_shop.ids.anti_thief_buy_2.pos = dp(701), dp(390)
            get.root.ids.f_shop.ids.anti_thief_buy_2.opacity = 1
            get.root.ids.f_shop.ids.anti_thief_buy_2.text = "Use"
            get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = False
            get.root.ids.f_shop.ids.shop_main_exit_2.text = "Back"

            if count == 0 or get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.f_shop.ids.anti_thief_buy_2.disabled = True

        big_ben()
        eiffel()
        coliseum()
        pisa()
        sydney()
        le_louvre()

        thief()

    def main_exit_2(self):
        get = App.get_running_app()
        if get.root.ids.f_shop.ids.shop_main_exit_2.text == "Exit":
            get.root.ids.board.ids.big.opacity = 1
            get.root.ids.f_shop.ids.shop_main_exit_2.opacity = 0
            get.root.ids.f_shop.ids.shop_main_exit_2.size = dp(0), dp(0)
            get.root.ids.f_shop.ids.shop_main_exit_2.pos = dp(0), dp(0)
            get.root.ids.f_shop.ids.shop_main_exit_2.disabled = True
            self.hide_buttons_2()
            self.hide_shop_2()
        if get.root.ids.f_shop.ids.shop_main_exit_2.text == "Back":
            get.root.ids.f_shop.ids.shop_main_exit_2.text = "Exit"
            self.hide_shop_2()
            self.show_main_2()

    def shop_on_press_2(self):
        self.ids.player_2_shop_image.source = "images/shop_on_press.png"

    def shop_on_release_2(self):
        self.ids.player_2_shop_image.source = "images/shop.png"

    def inventory_on_press_2(self):
        self.ids.player_2_inventory_image.source = "images/inventory_on_press.png"

    def inventory_on_release_2(self):
        self.ids.player_2_inventory_image.source = "images/inventory_button.png"


class MovePlayers(Widget):
    @staticmethod
    def player_1(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos
        # get.root.ids.board.ids.dice.text = get.root.ids.p1.ids.p1_input.text
        get.root.ids.board.ids.dice.text = f"{randint(1, 6)}"

        def reposition_1():
            pl_1 = get.root.ids.p1.ids.player_1
            pl_1_animate = Animation(pos=(dp(x), dp(y)), duration=0.2)
            pl_1_animate.start(pl_1)

        def reposition_2():
            pl_1 = get.root.ids.p1.ids.player_1
            pl_1_animate = Animation(pos=(dp(x), dp(y)), duration=0.4)
            pl_1_animate.start(pl_1)

        def reposition_3():
            pl_1 = get.root.ids.p1.ids.player_1
            pl_1_animate = Animation(pos=(dp(x), dp(y)), duration=0.6)
            pl_1_animate.start(pl_1)

        def reposition_4():
            pl_1 = get.root.ids.p1.ids.player_1
            pl_1_animate = Animation(pos=(dp(x), dp(y)), duration=0.8)
            pl_1_animate.start(pl_1)

        def reposition_5():
            pl_1 = get.root.ids.p1.ids.player_1
            pl_1_animate = Animation(pos=(dp(x), dp(y)), duration=1)
            pl_1_animate.start(pl_1)

        def reposition_6():
            pl_1 = get.root.ids.p1.ids.player_1
            pl_1_animate = Animation(pos=(dp(x), dp(y)), duration=1.2)
            pl_1_animate.start(pl_1)

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos1_x and y == p1_pos1_y:
                x, y = p1_pos2_x, p1_pos2_y
                reposition_1()
            elif x == p1_pos2_x and y == p1_pos2_y:
                x, y = p1_pos3_x, p1_pos3_y
                reposition_1()
            elif x == p1_pos3_x and y == p1_pos3_y:
                x, y = p1_pos4_x, p1_pos4_y
                reposition_1()
            elif x == p1_pos4_x and y == p1_pos4_y:
                x, y = p1_pos5_x, p1_pos5_y
                reposition_1()
            elif x == p1_pos5_x and y == p1_pos5_y:
                x, y = p1_pos6_x, p1_pos6_y
                reposition_1()
            elif x == p1_pos6_x and y == p1_pos6_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos6_x, p1_pos6_y - 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos7_x, p1_pos7_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos7_x and y == p1_pos7_y:
                x, y = p1_pos8_x, p1_pos8_y
                reposition_1()
            elif x == p1_pos8_x and y == p1_pos8_y:
                x, y = p1_pos9_x, p1_pos9_y
                reposition_1()
            elif x == p1_pos9_x and y == p1_pos9_y:
                x, y = p1_pos10_x, p1_pos10_y
                reposition_1()
            elif x == p1_pos10_x and y == p1_pos10_y:
                x, y = p1_pos11_x, p1_pos11_y
                reposition_1()
            elif x == p1_pos11_x and y == p1_pos11_y:
                x, y = p1_pos12_x, p1_pos12_y
                reposition_1()
            elif x == p1_pos12_x and y == p1_pos12_y:
                x, y = p1_pos13_x, p1_pos13_y
                reposition_1()
            elif x == p1_pos13_x and y == p1_pos13_y:
                x, y = p1_pos14_x, p1_pos14_y
                reposition_1()
            elif x == p1_pos14_x and y == p1_pos14_y:
                x, y = p1_pos15_x, p1_pos15_y
                reposition_1()
            elif x == p1_pos15_x and y == p1_pos15_y:
                x, y = p1_pos16_x, p1_pos16_y
                reposition_1()
            elif x == p1_pos16_x and y == p1_pos16_y:
                x, y = p1_pos17_x, p1_pos17_y
                reposition_1()
            elif x == p1_pos17_x and y == p1_pos17_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos17_x - 55, p1_pos17_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos18_x, p1_pos18_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos18_x and y == p1_pos18_y:
                x, y = p1_pos19_x, p1_pos19_y
                reposition_1()
            elif x == p1_pos19_x and y == p1_pos19_y:
                x, y = p1_pos20_x, p1_pos20_y
                reposition_1()
            elif x == p1_pos20_x and y == p1_pos20_y:
                x, y = p1_pos21_x, p1_pos21_y
                reposition_1()
            elif x == p1_pos21_x and y == p1_pos21_y:
                x, y = p1_pos22_x, p1_pos22_y
                reposition_1()
            elif x == p1_pos22_x and y == p1_pos22_y:
                x, y = p1_pos23_x, p1_pos23_y
                reposition_1()
            elif x == p1_pos23_x and y == p1_pos23_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos23_x, p1_pos23_y + 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos24_x, p1_pos24_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos24_x and y == p1_pos24_y:
                x, y = p1_pos25_x, p1_pos25_y
                reposition_1()
            elif x == p1_pos25_x and y == p1_pos25_y:
                x, y = p1_pos26_x, p1_pos26_y
                reposition_1()
            elif x == p1_pos26_x and y == p1_pos26_y:
                x, y = p1_pos27_x, p1_pos27_y
                reposition_1()
            elif x == p1_pos27_x and y == p1_pos27_y:
                x, y = p1_pos28_x, p1_pos28_y
                reposition_1()
            elif x == p1_pos28_x and y == p1_pos28_y:
                x, y = p1_pos29_x, p1_pos29_y
                reposition_1()
            elif x == p1_pos29_x and y == p1_pos29_y:
                x, y = p1_pos30_x, p1_pos30_y
                reposition_1()
            elif x == p1_pos30_x and y == p1_pos30_y:
                x, y = p1_pos31_x, p1_pos31_y
                reposition_1()
            elif x == p1_pos31_x and y == p1_pos31_y:
                x, y = p1_pos32_x, p1_pos32_y
                reposition_1()
            elif x == p1_pos32_x and y == p1_pos32_y:
                x, y = p1_pos33_x, p1_pos33_y
                reposition_1()
            elif x == p1_pos33_x and y == p1_pos33_y:
                x, y = p1_pos34_x, p1_pos34_y
                reposition_1()
            elif x == p1_pos34_x and y == p1_pos34_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos34_x + 55, p1_pos34_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos1_x, p1_pos1_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos1_x and y == p1_pos1_y:
                x, y = p1_pos3_x, p1_pos3_y
                reposition_2()
            elif x == p1_pos2_x and y == p1_pos2_y:
                x, y = p1_pos4_x, p1_pos4_y
                reposition_2()
            elif x == p1_pos3_x and y == p1_pos3_y:
                x, y = p1_pos5_x, p1_pos5_y
                reposition_2()
            elif x == p1_pos4_x and y == p1_pos4_y:
                x, y = p1_pos6_x, p1_pos6_y
                reposition_2()
            elif x == p1_pos5_x and y == p1_pos5_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos5_x, p1_pos5_y - 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos7_x, p1_pos7_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos6_x and y == p1_pos6_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos6_x, p1_pos6_y - 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos8_x, p1_pos8_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos7_x and y == p1_pos7_y:
                x, y = p1_pos9_x, p1_pos9_y
                reposition_2()
            elif x == p1_pos8_x and y == p1_pos8_y:
                x, y = p1_pos10_x, p1_pos10_y
                reposition_2()
            elif x == p1_pos9_x and y == p1_pos9_y:
                x, y = p1_pos11_x, p1_pos11_y
                reposition_2()
            elif x == p1_pos10_x and y == p1_pos10_y:
                x, y = p1_pos12_x, p1_pos12_y
                reposition_2()
            elif x == p1_pos11_x and y == p1_pos11_y:
                x, y = p1_pos13_x, p1_pos13_y
                reposition_2()
            elif x == p1_pos12_x and y == p1_pos12_y:
                x, y = p1_pos14_x, p1_pos14_y
                reposition_2()
            elif x == p1_pos13_x and y == p1_pos13_y:
                x, y = p1_pos15_x, p1_pos15_y
                reposition_2()
            elif x == p1_pos14_x and y == p1_pos14_y:
                x, y = p1_pos16_x, p1_pos16_y
                reposition_2()
            elif x == p1_pos15_x and y == p1_pos15_y:
                x, y = p1_pos17_x, p1_pos17_y
                reposition_2()
            elif x == p1_pos16_x and y == p1_pos16_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos16_x - 55 * 2, p1_pos16_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos18_x, p1_pos18_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos17_x and y == p1_pos17_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos17_x - 55, p1_pos17_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos19_x, p1_pos19_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos18_x and y == p1_pos18_y:
                x, y = p1_pos20_x, p1_pos20_y
                reposition_2()
            elif x == p1_pos19_x and y == p1_pos19_y:
                x, y = p1_pos21_x, p1_pos21_y
                reposition_2()
            elif x == p1_pos20_x and y == p1_pos20_y:
                x, y = p1_pos22_x, p1_pos22_y
                reposition_2()
            elif x == p1_pos21_x and y == p1_pos21_y:
                x, y = p1_pos23_x, p1_pos23_y
                reposition_2()
            elif x == p1_pos22_x and y == p1_pos22_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos22_x, p1_pos22_y + 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos24_x, p1_pos24_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos23_x and y == p1_pos23_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos23_x, p1_pos23_y + 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos25_x, p1_pos25_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos24_x and y == p1_pos24_y:
                x, y = p1_pos26_x, p1_pos26_y
                reposition_2()
            elif x == p1_pos25_x and y == p1_pos25_y:
                x, y = p1_pos27_x, p1_pos27_y
                reposition_2()
            elif x == p1_pos26_x and y == p1_pos26_y:
                x, y = p1_pos28_x, p1_pos28_y
                reposition_2()
            elif x == p1_pos27_x and y == p1_pos27_y:
                x, y = p1_pos29_x, p1_pos29_y
                reposition_2()
            elif x == p1_pos28_x and y == p1_pos28_y:
                x, y = p1_pos30_x, p1_pos30_y
                reposition_2()
            elif x == p1_pos29_x and y == p1_pos29_y:
                x, y = p1_pos31_x, p1_pos31_y
                reposition_2()
            elif x == p1_pos30_x and y == p1_pos30_y:
                x, y = p1_pos32_x, p1_pos32_y
                reposition_2()
            elif x == p1_pos31_x and y == p1_pos31_y:
                x, y = p1_pos33_x, p1_pos33_y
                reposition_2()
            elif x == p1_pos32_x and y == p1_pos32_y:
                x, y = p1_pos34_x, p1_pos34_y
                reposition_2()
            elif x == p1_pos33_x and y == p1_pos33_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos33_x + 55 * 2, p1_pos33_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos1_x, p1_pos1_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos34_x and y == p1_pos34_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos34_x + 55, p1_pos34_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos2_x, p1_pos2_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos1_x and y == p1_pos1_y:
                x, y = p1_pos4_x, p1_pos4_y
                reposition_3()
            elif x == p1_pos2_x and y == p1_pos2_y:
                x, y = p1_pos5_x, p1_pos5_y
                reposition_3()
            elif x == p1_pos3_x and y == p1_pos3_y:
                x, y = p1_pos6_x, p1_pos6_y
                reposition_3()
            elif x == p1_pos4_x and y == p1_pos4_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos4_x, p1_pos4_y - 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos7_x, p1_pos7_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos5_x and y == p1_pos5_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos5_x, p1_pos5_y - 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos8_x, p1_pos8_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos6_x and y == p1_pos6_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos6_x, p1_pos6_y - 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos9_x, p1_pos9_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos7_x and y == p1_pos7_y:
                x, y = p1_pos10_x, p1_pos10_y
                reposition_3()
            elif x == p1_pos8_x and y == p1_pos8_y:
                x, y = p1_pos11_x, p1_pos11_y
                reposition_3()
            elif x == p1_pos9_x and y == p1_pos9_y:
                x, y = p1_pos12_x, p1_pos12_y
                reposition_3()
            elif x == p1_pos10_x and y == p1_pos10_y:
                x, y = p1_pos13_x, p1_pos13_y
                reposition_3()
            elif x == p1_pos11_x and y == p1_pos11_y:
                x, y = p1_pos14_x, p1_pos14_y
                reposition_3()
            elif x == p1_pos12_x and y == p1_pos12_y:
                x, y = p1_pos15_x, p1_pos15_y
                reposition_3()
            elif x == p1_pos13_x and y == p1_pos13_y:
                x, y = p1_pos16_x, p1_pos16_y
                reposition_3()
            elif x == p1_pos14_x and y == p1_pos14_y:
                x, y = p1_pos17_x, p1_pos17_y
                reposition_3()
            elif x == p1_pos15_x and y == p1_pos15_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos15_x - 55 * 3, p1_pos15_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos18_x, p1_pos18_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos16_x and y == p1_pos16_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos16_x - 55 * 2, p1_pos16_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos19_x, p1_pos19_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos17_x and y == p1_pos17_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos17_x - 55, p1_pos17_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos20_x, p1_pos20_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos18_x and y == p1_pos18_y:
                x, y = p1_pos21_x, p1_pos21_y
                reposition_3()
            elif x == p1_pos19_x and y == p1_pos19_y:
                x, y = p1_pos22_x, p1_pos22_y
                reposition_3()
            elif x == p1_pos20_x and y == p1_pos20_y:
                x, y = p1_pos23_x, p1_pos23_y
                reposition_3()
            elif x == p1_pos21_x and y == p1_pos21_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos21_x, p1_pos21_y + 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos24_x, p1_pos24_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos22_x and y == p1_pos22_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos22_x, p1_pos22_y + 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos25_x, p1_pos25_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos23_x and y == p1_pos23_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos23_x, p1_pos23_y + 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos26_x, p1_pos26_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos24_x and y == p1_pos24_y:
                x, y = p1_pos27_x, p1_pos27_y
                reposition_3()
            elif x == p1_pos25_x and y == p1_pos25_y:
                x, y = p1_pos28_x, p1_pos28_y
                reposition_3()
            elif x == p1_pos26_x and y == p1_pos26_y:
                x, y = p1_pos29_x, p1_pos29_y
                reposition_3()
            elif x == p1_pos27_x and y == p1_pos27_y:
                x, y = p1_pos30_x, p1_pos30_y
                reposition_3()
            elif x == p1_pos28_x and y == p1_pos28_y:
                x, y = p1_pos31_x, p1_pos31_y
                reposition_3()
            elif x == p1_pos29_x and y == p1_pos29_y:
                x, y = p1_pos32_x, p1_pos32_y
                reposition_3()
            elif x == p1_pos30_x and y == p1_pos30_y:
                x, y = p1_pos33_x, p1_pos33_y
                reposition_3()
            elif x == p1_pos31_x and y == p1_pos31_y:
                x, y = p1_pos34_x, p1_pos34_y
                reposition_3()
            elif x == p1_pos32_x and y == p1_pos32_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos32_x + 55 * 3, p1_pos32_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos1_x, p1_pos1_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos33_x and y == p1_pos33_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos33_x + 55 * 2, p1_pos33_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos2_x, p1_pos2_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos34_x and y == p1_pos34_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos34_x + 55, p1_pos34_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos3_x, p1_pos3_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos1_x and y == p1_pos1_y:
                x, y = p1_pos5_x, p1_pos5_y
                reposition_4()
            elif x == p1_pos2_x and y == p1_pos2_y:
                x, y = p1_pos6_x, p1_pos6_y
                reposition_4()
            elif x == p1_pos3_x and y == p1_pos3_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos3_x, p1_pos3_y - 55 * 4
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos7_x, p1_pos7_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos4_x and y == p1_pos4_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos4_x, p1_pos4_y - 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos8_x, p1_pos8_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos5_x and y == p1_pos5_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos5_x, p1_pos5_y - 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos9_x, p1_pos9_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos6_x and y == p1_pos6_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos6_x, p1_pos6_y - 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos10_x, p1_pos10_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos7_x and y == p1_pos7_y:
                x, y = p1_pos11_x, p1_pos11_y
                reposition_4()
            elif x == p1_pos8_x and y == p1_pos8_y:
                x, y = p1_pos12_x, p1_pos12_y
                reposition_4()
            elif x == p1_pos9_x and y == p1_pos9_y:
                x, y = p1_pos13_x, p1_pos13_y
                reposition_4()
            elif x == p1_pos10_x and y == p1_pos10_y:
                x, y = p1_pos14_x, p1_pos14_y
                reposition_4()
            elif x == p1_pos11_x and y == p1_pos11_y:
                x, y = p1_pos15_x, p1_pos15_y
                reposition_4()
            elif x == p1_pos12_x and y == p1_pos12_y:
                x, y = p1_pos16_x, p1_pos16_y
                reposition_4()
            elif x == p1_pos13_x and y == p1_pos13_y:
                x, y = p1_pos17_x, p1_pos17_y
                reposition_4()
            elif x == p1_pos14_x and y == p1_pos14_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos14_x - 55 * 4, p1_pos14_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos18_x, p1_pos18_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos15_x and y == p1_pos15_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos15_x - 55 * 3, p1_pos15_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos19_x, p1_pos19_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos16_x and y == p1_pos16_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos16_x - 55 * 2, p1_pos16_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos20_x, p1_pos20_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos17_x and y == p1_pos17_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos17_x - 55, p1_pos17_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos21_x, p1_pos21_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos18_x and y == p1_pos18_y:
                x, y = p1_pos22_x, p1_pos22_y
                reposition_4()
            elif x == p1_pos19_x and y == p1_pos19_y:
                x, y = p1_pos23_x, p1_pos23_y
                reposition_4()
            elif x == p1_pos20_x and y == p1_pos20_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos20_x, p1_pos20_y + 55 * 4
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos24_x, p1_pos24_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos21_x and y == p1_pos21_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos21_x, p1_pos21_y + 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos25_x, p1_pos25_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos22_x and y == p1_pos22_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos22_x, p1_pos22_y + 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos26_x, p1_pos26_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos23_x and y == p1_pos23_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos23_x, p1_pos23_y + 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos27_x, p1_pos27_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos24_x and y == p1_pos24_y:
                x, y = p1_pos28_x, p1_pos28_y
                reposition_4()
            elif x == p1_pos25_x and y == p1_pos25_y:
                x, y = p1_pos29_x, p1_pos29_y
                reposition_4()
            elif x == p1_pos26_x and y == p1_pos26_y:
                x, y = p1_pos30_x, p1_pos30_y
                reposition_4()
            elif x == p1_pos27_x and y == p1_pos27_y:
                x, y = p1_pos31_x, p1_pos31_y
                reposition_4()
            elif x == p1_pos28_x and y == p1_pos28_y:
                x, y = p1_pos32_x, p1_pos32_y
                reposition_4()
            elif x == p1_pos29_x and y == p1_pos29_y:
                x, y = p1_pos33_x, p1_pos33_y
                reposition_4()
            elif x == p1_pos30_x and y == p1_pos30_y:
                x, y = p1_pos34_x, p1_pos34_y
                reposition_4()
            elif x == p1_pos31_x and y == p1_pos31_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos31_x + 55 * 4, p1_pos31_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos1_x, p1_pos1_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos32_x and y == p1_pos32_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos32_x + 55 * 3, p1_pos32_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos2_x, p1_pos2_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos33_x and y == p1_pos33_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos33_x + 55 * 2, p1_pos33_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos3_x, p1_pos3_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos34_x and y == p1_pos34_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos34_x + 55, p1_pos34_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos4_x, p1_pos4_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos1_x and y == p1_pos1_y:
                x, y = p1_pos6_x, p1_pos6_y
                reposition_5()
            elif x == p1_pos2_x and y == p1_pos2_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos2_x, p1_pos2_y - 55 * 5
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos7_x, p1_pos7_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos3_x and y == p1_pos3_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos3_x, p1_pos3_y - 55 * 4
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos8_x, p1_pos8_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos4_x and y == p1_pos4_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos4_x, p1_pos4_y - 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos9_x, p1_pos9_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos5_x and y == p1_pos5_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos5_x, p1_pos5_y - 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos10_x, p1_pos10_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos6_x and y == p1_pos6_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos6_x, p1_pos6_y - 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos11_x, p1_pos11_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos7_x and y == p1_pos7_y:
                x, y = p1_pos12_x, p1_pos12_y
                reposition_5()
            elif x == p1_pos8_x and y == p1_pos8_y:
                x, y = p1_pos13_x, p1_pos13_y
                reposition_5()
            elif x == p1_pos9_x and y == p1_pos9_y:
                x, y = p1_pos14_x, p1_pos14_y
                reposition_5()
            elif x == p1_pos10_x and y == p1_pos10_y:
                x, y = p1_pos15_x, p1_pos15_y
                reposition_5()
            elif x == p1_pos11_x and y == p1_pos11_y:
                x, y = p1_pos16_x, p1_pos16_y
                reposition_5()
            elif x == p1_pos12_x and y == p1_pos12_y:
                x, y = p1_pos17_x, p1_pos17_y
                reposition_5()
            elif x == p1_pos13_x and y == p1_pos13_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos13_x - 55 * 5, p1_pos13_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos18_x, p1_pos18_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos14_x and y == p1_pos14_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos14_x - 55 * 4, p1_pos14_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos19_x, p1_pos19_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos15_x and y == p1_pos15_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos15_x - 55 * 3, p1_pos15_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos20_x, p1_pos20_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos16_x and y == p1_pos16_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos16_x - 55 * 2, p1_pos16_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos21_x, p1_pos21_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos17_x and y == p1_pos17_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos17_x - 55, p1_pos17_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos22_x, p1_pos22_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos18_x and y == p1_pos18_y:
                x, y = p1_pos23_x, p1_pos23_y
                reposition_5()
            elif x == p1_pos19_x and y == p1_pos19_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos19_x, p1_pos19_y + 55 * 5
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos24_x, p1_pos24_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos20_x and y == p1_pos20_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos20_x, p1_pos20_y + 55 * 4
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos25_x, p1_pos25_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos21_x and y == p1_pos21_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos21_x, p1_pos21_y + 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos26_x, p1_pos26_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos22_x and y == p1_pos22_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos22_x, p1_pos22_y + 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos27_x, p1_pos27_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos23_x and y == p1_pos23_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos23_x, p1_pos23_y + 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos28_x, p1_pos28_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos24_x and y == p1_pos24_y:
                x, y = p1_pos29_x, p1_pos29_y
                reposition_5()
            elif x == p1_pos25_x and y == p1_pos25_y:
                x, y = p1_pos30_x, p1_pos30_y
                reposition_5()
            elif x == p1_pos26_x and y == p1_pos26_y:
                x, y = p1_pos31_x, p1_pos31_y
                reposition_5()
            elif x == p1_pos27_x and y == p1_pos27_y:
                x, y = p1_pos32_x, p1_pos32_y
                reposition_5()
            elif x == p1_pos28_x and y == p1_pos28_y:
                x, y = p1_pos33_x, p1_pos33_y
                reposition_5()
            elif x == p1_pos29_x and y == p1_pos29_y:
                x, y = p1_pos34_x, p1_pos34_y
                reposition_5()
            elif x == p1_pos30_x and y == p1_pos30_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos30_x + 55 * 5, p1_pos30_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos1_x, p1_pos1_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos31_x and y == p1_pos31_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos31_x + 55 * 4, p1_pos31_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos2_x, p1_pos2_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos32_x and y == p1_pos32_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos32_x + 55 * 3, p1_pos32_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos3_x, p1_pos3_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos33_x and y == p1_pos33_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos33_x + 55 * 2, p1_pos33_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos4_x, p1_pos4_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos34_x and y == p1_pos34_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos34_x + 55, p1_pos34_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos5_x, p1_pos5_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos1_x and y == p1_pos1_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos1_x, p1_pos1_y - 55 * 6
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos7_x, p1_pos7_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos2_x and y == p1_pos2_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos2_x, p1_pos2_y - 55 * 5
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos8_x, p1_pos8_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos3_x and y == p1_pos3_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos3_x, p1_pos3_y - 55 * 4
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos9_x, p1_pos9_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos4_x and y == p1_pos4_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos4_x, p1_pos4_y - 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos10_x, p1_pos10_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos5_x and y == p1_pos5_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos5_x, p1_pos5_y - 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos11_x, p1_pos11_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos6_x and y == p1_pos6_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos6_x, p1_pos6_y - 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos12_x, p1_pos12_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos7_x and y == p1_pos7_y:
                x, y = p1_pos13_x, p1_pos13_y
                reposition_6()
            elif x == p1_pos8_x and y == p1_pos8_y:
                x, y = p1_pos14_x, p1_pos14_y
                reposition_6()
            elif x == p1_pos9_x and y == p1_pos9_y:
                x, y = p1_pos15_x, p1_pos15_y
                reposition_6()
            elif x == p1_pos10_x and y == p1_pos10_y:
                x, y = p1_pos16_x, p1_pos16_y
                reposition_6()
            elif x == p1_pos11_x and y == p1_pos11_y:
                x, y = p1_pos17_x, p1_pos17_y
                reposition_6()
            elif x == p1_pos12_x and y == p1_pos12_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos12_x - 55 * 6, p1_pos12_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos18_x, p1_pos18_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos13_x and y == p1_pos13_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos13_x - 55 * 5, p1_pos13_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos19_x, p1_pos19_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos14_x and y == p1_pos14_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos14_x - 55 * 4, p1_pos14_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos20_x, p1_pos20_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos15_x and y == p1_pos15_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos15_x - 55 * 3, p1_pos15_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos21_x, p1_pos21_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos16_x and y == p1_pos16_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos16_x - 55 * 2, p1_pos16_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos22_x, p1_pos22_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos17_x and y == p1_pos17_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos17_x - 55, p1_pos17_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos23_x, p1_pos23_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos18_x and y == p1_pos18_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos18_x, p1_pos18_y + 55 * 6
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos24_x, p1_pos24_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos19_x and y == p1_pos19_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos19_x, p1_pos19_y + 55 * 5
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos25_x, p1_pos25_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos20_x and y == p1_pos20_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos20_x, p1_pos20_y + 55 * 4
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos26_x, p1_pos26_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos21_x and y == p1_pos21_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos21_x, p1_pos21_y + 55 * 3
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos27_x, p1_pos27_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos22_x and y == p1_pos22_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos22_x, p1_pos22_y + 55 * 2
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos28_x, p1_pos28_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos23_x and y == p1_pos23_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos23_x, p1_pos23_y + 55
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos29_x, p1_pos29_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos24_x and y == p1_pos24_y:
                x, y = p1_pos30_x, p1_pos30_y
                reposition_6()
            elif x == p1_pos25_x and y == p1_pos25_y:
                x, y = p1_pos31_x, p1_pos31_y
                reposition_6()
            elif x == p1_pos26_x and y == p1_pos26_y:
                x, y = p1_pos32_x, p1_pos32_y
                reposition_6()
            elif x == p1_pos27_x and y == p1_pos27_y:
                x, y = p1_pos33_x, p1_pos33_y
                reposition_6()
            elif x == p1_pos28_x and y == p1_pos28_y:
                x, y = p1_pos34_x, p1_pos34_y
                reposition_6()
            elif x == p1_pos29_x and y == p1_pos29_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos29_x + 55 * 6, p1_pos29_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos1_x, p1_pos1_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos30_x and y == p1_pos30_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos30_x + 55 * 5, p1_pos30_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos2_x, p1_pos2_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos31_x and y == p1_pos31_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos31_x + 55 * 4, p1_pos31_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos3_x, p1_pos3_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos32_x and y == p1_pos32_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos32_x + 55 * 3, p1_pos32_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos4_x, p1_pos4_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos33_x and y == p1_pos33_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos33_x + 55 * 2, p1_pos33_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos5_x, p1_pos5_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_1_animated.start(player_1_curve)
            elif x == p1_pos34_x and y == p1_pos34_y:
                player_1_curve = get.root.ids.p1.ids.player_1
                x, y = p1_pos34_x + 55, p1_pos34_y
                player_1_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_1_animated.start(player_1_curve)
                x, y = p1_pos6_x, p1_pos6_y
                player_1_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_1_animated.start(player_1_curve)

    @staticmethod
    def player_2(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos
        # get.root.ids.board.ids.dice.text = get.root.ids.p2.ids.p2_input.text
        get.root.ids.board.ids.dice.text = f"{randint(1, 6)}"

        def reposition_1():
            pl_2 = get.root.ids.p2.ids.player_2
            pl_2_animate = Animation(pos=(dp(x), dp(y)), duration=0.2)
            pl_2_animate.start(pl_2)

        def reposition_2():
            pl_2 = get.root.ids.p2.ids.player_2
            pl_2_animate = Animation(pos=(dp(x), dp(y)), duration=0.4)
            pl_2_animate.start(pl_2)

        def reposition_3():
            pl_2 = get.root.ids.p2.ids.player_2
            pl_2_animate = Animation(pos=(dp(x), dp(y)), duration=0.6)
            pl_2_animate.start(pl_2)

        def reposition_4():
            pl_2 = get.root.ids.p2.ids.player_2
            pl_2_animate = Animation(pos=(dp(x), dp(y)), duration=0.8)
            pl_2_animate.start(pl_2)

        def reposition_5():
            pl_2 = get.root.ids.p2.ids.player_2
            pl_2_animate = Animation(pos=(dp(x), dp(y)), duration=1)
            pl_2_animate.start(pl_2)

        def reposition_6():
            pl_2 = get.root.ids.p2.ids.player_2
            pl_2_animate = Animation(pos=(dp(x), dp(y)), duration=1.2)
            pl_2_animate.start(pl_2)

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos1_x and y == p2_pos1_y:
                x, y = p2_pos2_x, p2_pos2_y
                reposition_1()
            elif x == p2_pos2_x and y == p2_pos2_y:
                x, y = p2_pos3_x, p2_pos3_y
                reposition_1()
            elif x == p2_pos3_x and y == p2_pos3_y:
                x, y = p2_pos4_x, p2_pos4_y
                reposition_1()
            elif x == p2_pos4_x and y == p2_pos4_y:
                x, y = p2_pos5_x, p2_pos5_y
                reposition_1()
            elif x == p2_pos5_x and y == p2_pos5_y:
                x, y = p2_pos6_x, p2_pos6_y
                reposition_1()
            elif x == p2_pos6_x and y == p2_pos6_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos6_x, p2_pos6_y - 37
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos7_x, p2_pos7_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos7_x and y == p2_pos7_y:
                x, y = p2_pos8_x, p2_pos8_y
                reposition_1()
            elif x == p2_pos8_x and y == p2_pos8_y:
                x, y = p2_pos9_x, p2_pos9_y
                reposition_1()
            elif x == p2_pos9_x and y == p2_pos9_y:
                x, y = p2_pos10_x, p2_pos10_y
                reposition_1()
            elif x == p2_pos10_x and y == p2_pos10_y:
                x, y = p2_pos11_x, p2_pos11_y
                reposition_1()
            elif x == p2_pos11_x and y == p2_pos11_y:
                x, y = p2_pos12_x, p2_pos12_y
                reposition_1()
            elif x == p2_pos12_x and y == p2_pos12_y:
                x, y = p2_pos13_x, p2_pos13_y
                reposition_1()
            elif x == p2_pos13_x and y == p2_pos13_y:
                x, y = p2_pos14_x, p2_pos14_y
                reposition_1()
            elif x == p2_pos14_x and y == p2_pos14_y:
                x, y = p2_pos15_x, p2_pos15_y
                reposition_1()
            elif x == p2_pos15_x and y == p2_pos15_y:
                x, y = p2_pos16_x, p2_pos16_y
                reposition_1()
            elif x == p2_pos16_x and y == p2_pos16_y:
                x, y = p2_pos17_x, p2_pos17_y
                reposition_1()
            elif x == p2_pos17_x and y == p2_pos17_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos17_x - 37, p2_pos17_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos18_x, p2_pos18_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos18_x and y == p2_pos18_y:
                x, y = p2_pos19_x, p2_pos19_y
                reposition_1()
            elif x == p2_pos19_x and y == p2_pos19_y:
                x, y = p2_pos20_x, p2_pos20_y
                reposition_1()
            elif x == p2_pos20_x and y == p2_pos20_y:
                x, y = p2_pos21_x, p2_pos21_y
                reposition_1()
            elif x == p2_pos21_x and y == p2_pos21_y:
                x, y = p2_pos22_x, p2_pos22_y
                reposition_1()
            elif x == p2_pos22_x and y == p2_pos22_y:
                x, y = p2_pos23_x, p2_pos23_y
                reposition_1()
            elif x == p2_pos23_x and y == p2_pos23_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos23_x, p2_pos23_y + 37
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos24_x, p2_pos24_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos24_x and y == p2_pos24_y:
                x, y = p2_pos25_x, p2_pos25_y
                reposition_1()
            elif x == p2_pos25_x and y == p2_pos25_y:
                x, y = p2_pos26_x, p2_pos26_y
                reposition_1()
            elif x == p2_pos26_x and y == p2_pos26_y:
                x, y = p2_pos27_x, p2_pos27_y
                reposition_1()
            elif x == p2_pos27_x and y == p2_pos27_y:
                x, y = p2_pos28_x, p2_pos28_y
                reposition_1()
            elif x == p2_pos28_x and y == p2_pos28_y:
                x, y = p2_pos29_x, p2_pos29_y
                reposition_1()
            elif x == p2_pos29_x and y == p2_pos29_y:
                x, y = p2_pos30_x, p2_pos30_y
                reposition_1()
            elif x == p2_pos30_x and y == p2_pos30_y:
                x, y = p2_pos31_x, p2_pos31_y
                reposition_1()
            elif x == p2_pos31_x and y == p2_pos31_y:
                x, y = p2_pos32_x, p2_pos32_y
                reposition_1()
            elif x == p2_pos32_x and y == p2_pos32_y:
                x, y = p2_pos33_x, p2_pos33_y
                reposition_1()
            elif x == p2_pos33_x and y == p2_pos33_y:
                x, y = p2_pos34_x, p2_pos34_y
                reposition_1()
            elif x == p2_pos34_x and y == p2_pos34_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos34_x + 37, p2_pos34_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos1_x, p2_pos1_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos1_x and y == p2_pos1_y:
                x, y = p2_pos3_x, p2_pos3_y
                reposition_2()
            elif x == p2_pos2_x and y == p2_pos2_y:
                x, y = p2_pos4_x, p2_pos4_y
                reposition_2()
            elif x == p2_pos3_x and y == p2_pos3_y:
                x, y = p2_pos5_x, p2_pos5_y
                reposition_2()
            elif x == p2_pos4_x and y == p2_pos4_y:
                x, y = p2_pos6_x, p2_pos6_y
                reposition_2()
            elif x == p2_pos5_x and y == p2_pos5_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos5_x, p2_pos5_y - 92
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos7_x, p2_pos7_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos6_x and y == p2_pos6_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos6_x, p2_pos6_y - 37
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos8_x, p2_pos8_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos7_x and y == p2_pos7_y:
                x, y = p2_pos9_x, p2_pos9_y
                reposition_2()
            elif x == p2_pos8_x and y == p2_pos8_y:
                x, y = p2_pos10_x, p2_pos10_y
                reposition_2()
            elif x == p2_pos9_x and y == p2_pos9_y:
                x, y = p2_pos11_x, p2_pos11_y
                reposition_2()
            elif x == p2_pos10_x and y == p2_pos10_y:
                x, y = p2_pos12_x, p2_pos12_y
                reposition_2()
            elif x == p2_pos11_x and y == p2_pos11_y:
                x, y = p2_pos13_x, p2_pos13_y
                reposition_2()
            elif x == p2_pos12_x and y == p2_pos12_y:
                x, y = p2_pos14_x, p2_pos14_y
                reposition_2()
            elif x == p2_pos13_x and y == p2_pos13_y:
                x, y = p2_pos15_x, p2_pos15_y
                reposition_2()
            elif x == p2_pos14_x and y == p2_pos14_y:
                x, y = p2_pos16_x, p2_pos16_y
                reposition_2()
            elif x == p2_pos15_x and y == p2_pos15_y:
                x, y = p2_pos17_x, p2_pos17_y
                reposition_2()
            elif x == p2_pos16_x and y == p2_pos16_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos16_x - 55 * 2 + 18, p2_pos16_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos18_x, p2_pos18_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos17_x and y == p2_pos17_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos17_x - 55 + 18, p2_pos17_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos19_x, p2_pos19_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos18_x and y == p2_pos18_y:
                x, y = p2_pos20_x, p2_pos20_y
                reposition_2()
            elif x == p2_pos19_x and y == p2_pos19_y:
                x, y = p2_pos21_x, p2_pos21_y
                reposition_2()
            elif x == p2_pos20_x and y == p2_pos20_y:
                x, y = p2_pos22_x, p2_pos22_y
                reposition_2()
            elif x == p2_pos21_x and y == p2_pos21_y:
                x, y = p2_pos23_x, p2_pos23_y
                reposition_2()
            elif x == p2_pos22_x and y == p2_pos22_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos22_x, p2_pos22_y + 55 * 2 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos24_x, p2_pos24_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos23_x and y == p2_pos23_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos23_x, p2_pos23_y + 55 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos25_x, p2_pos25_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos24_x and y == p2_pos24_y:
                x, y = p2_pos26_x, p2_pos26_y
                reposition_2()
            elif x == p2_pos25_x and y == p2_pos25_y:
                x, y = p2_pos27_x, p2_pos27_y
                reposition_2()
            elif x == p2_pos26_x and y == p2_pos26_y:
                x, y = p2_pos28_x, p2_pos28_y
                reposition_2()
            elif x == p2_pos27_x and y == p2_pos27_y:
                x, y = p2_pos29_x, p2_pos29_y
                reposition_2()
            elif x == p2_pos28_x and y == p2_pos28_y:
                x, y = p2_pos30_x, p2_pos30_y
                reposition_2()
            elif x == p2_pos29_x and y == p2_pos29_y:
                x, y = p2_pos31_x, p2_pos31_y
                reposition_2()
            elif x == p2_pos30_x and y == p2_pos30_y:
                x, y = p2_pos32_x, p2_pos32_y
                reposition_2()
            elif x == p2_pos31_x and y == p2_pos31_y:
                x, y = p2_pos33_x, p2_pos33_y
                reposition_2()
            elif x == p2_pos32_x and y == p2_pos32_y:
                x, y = p2_pos34_x, p2_pos34_y
                reposition_2()
            elif x == p2_pos33_x and y == p2_pos33_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos33_x + 55 * 2 - 18, p2_pos33_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos1_x, p2_pos1_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos34_x and y == p2_pos34_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos34_x + 55 - 18, p2_pos34_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos2_x, p2_pos2_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos1_x and y == p2_pos1_y:
                x, y = p2_pos4_x, p2_pos4_y
                reposition_3()
            elif x == p2_pos2_x and y == p2_pos2_y:
                x, y = p2_pos5_x, p2_pos5_y
                reposition_3()
            elif x == p2_pos3_x and y == p2_pos3_y:
                x, y = p2_pos6_x, p2_pos6_y
                reposition_3()
            elif x == p2_pos4_x and y == p2_pos4_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos4_x, p2_pos4_y - 55 * 3 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos7_x, p2_pos7_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos5_x and y == p2_pos5_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos5_x, p2_pos5_y - 55 * 2 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos8_x, p2_pos8_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos6_x and y == p2_pos6_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos6_x, p2_pos6_y - 55 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos9_x, p2_pos9_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos7_x and y == p2_pos7_y:
                x, y = p2_pos10_x, p2_pos10_y
                reposition_3()
            elif x == p2_pos8_x and y == p2_pos8_y:
                x, y = p2_pos11_x, p2_pos11_y
                reposition_3()
            elif x == p2_pos9_x and y == p2_pos9_y:
                x, y = p2_pos12_x, p2_pos12_y
                reposition_3()
            elif x == p2_pos10_x and y == p2_pos10_y:
                x, y = p2_pos13_x, p2_pos13_y
                reposition_3()
            elif x == p2_pos11_x and y == p2_pos11_y:
                x, y = p2_pos14_x, p2_pos14_y
                reposition_3()
            elif x == p2_pos12_x and y == p2_pos12_y:
                x, y = p2_pos15_x, p2_pos15_y
                reposition_3()
            elif x == p2_pos13_x and y == p2_pos13_y:
                x, y = p2_pos16_x, p2_pos16_y
                reposition_3()
            elif x == p2_pos14_x and y == p2_pos14_y:
                x, y = p2_pos17_x, p2_pos17_y
                reposition_3()
            elif x == p2_pos15_x and y == p2_pos15_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos15_x - 55 * 3 + 18, p2_pos15_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos18_x, p2_pos18_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos16_x and y == p2_pos16_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos16_x - 55 * 2 + 18, p2_pos16_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos19_x, p2_pos19_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos17_x and y == p2_pos17_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos17_x - 55 + 18, p2_pos17_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos20_x, p2_pos20_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos18_x and y == p2_pos18_y:
                x, y = p2_pos21_x, p2_pos21_y
                reposition_3()
            elif x == p2_pos19_x and y == p2_pos19_y:
                x, y = p2_pos22_x, p2_pos22_y
                reposition_3()
            elif x == p2_pos20_x and y == p2_pos20_y:
                x, y = p2_pos23_x, p2_pos23_y
                reposition_3()
            elif x == p2_pos21_x and y == p2_pos21_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos21_x, p2_pos21_y + 55 * 3 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos24_x, p2_pos24_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos22_x and y == p2_pos22_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos22_x, p2_pos22_y + 55 * 2 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos25_x, p2_pos25_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos23_x and y == p2_pos23_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos23_x, p2_pos23_y + 55 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos26_x, p2_pos26_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos24_x and y == p2_pos24_y:
                x, y = p2_pos27_x, p2_pos27_y
                reposition_3()
            elif x == p2_pos25_x and y == p2_pos25_y:
                x, y = p2_pos28_x, p2_pos28_y
                reposition_3()
            elif x == p2_pos26_x and y == p2_pos26_y:
                x, y = p2_pos29_x, p2_pos29_y
                reposition_3()
            elif x == p2_pos27_x and y == p2_pos27_y:
                x, y = p2_pos30_x, p2_pos30_y
                reposition_3()
            elif x == p2_pos28_x and y == p2_pos28_y:
                x, y = p2_pos31_x, p2_pos31_y
                reposition_3()
            elif x == p2_pos29_x and y == p2_pos29_y:
                x, y = p2_pos32_x, p2_pos32_y
                reposition_3()
            elif x == p2_pos30_x and y == p2_pos30_y:
                x, y = p2_pos33_x, p2_pos33_y
                reposition_3()
            elif x == p2_pos31_x and y == p2_pos31_y:
                x, y = p2_pos34_x, p2_pos34_y
                reposition_3()
            elif x == p2_pos32_x and y == p2_pos32_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos32_x + 55 * 3 - 18, p2_pos32_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos1_x, p2_pos1_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos33_x and y == p2_pos33_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos33_x + 55 * 2 - 18, p2_pos33_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos2_x, p2_pos2_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos34_x and y == p2_pos34_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos34_x + 55 - 18, p2_pos34_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos3_x, p2_pos3_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos1_x and y == p2_pos1_y:
                x, y = p2_pos5_x, p2_pos5_y
                reposition_4()
            elif x == p2_pos2_x and y == p2_pos2_y:
                x, y = p2_pos6_x, p2_pos6_y
                reposition_4()
            elif x == p2_pos3_x and y == p2_pos3_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos3_x, p2_pos3_y - 55 * 4 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos7_x, p2_pos7_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos4_x and y == p2_pos4_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos4_x, p2_pos4_y - 55 * 3 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos8_x, p2_pos8_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos5_x and y == p2_pos5_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos5_x, p2_pos5_y - 55 * 2 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos9_x, p2_pos9_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos6_x and y == p2_pos6_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos6_x, p2_pos6_y - 55 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos10_x, p2_pos10_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos7_x and y == p2_pos7_y:
                x, y = p2_pos11_x, p2_pos11_y
                reposition_4()
            elif x == p2_pos8_x and y == p2_pos8_y:
                x, y = p2_pos12_x, p2_pos12_y
                reposition_4()
            elif x == p2_pos9_x and y == p2_pos9_y:
                x, y = p2_pos13_x, p2_pos13_y
                reposition_4()
            elif x == p2_pos10_x and y == p2_pos10_y:
                x, y = p2_pos14_x, p2_pos14_y
                reposition_4()
            elif x == p2_pos11_x and y == p2_pos11_y:
                x, y = p2_pos15_x, p2_pos15_y
                reposition_4()
            elif x == p2_pos12_x and y == p2_pos12_y:
                x, y = p2_pos16_x, p2_pos16_y
                reposition_4()
            elif x == p2_pos13_x and y == p2_pos13_y:
                x, y = p2_pos17_x, p2_pos17_y
                reposition_4()
            elif x == p2_pos14_x and y == p2_pos14_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos14_x - 55 * 4 + 18, p2_pos14_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos18_x, p2_pos18_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos15_x and y == p2_pos15_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos15_x - 55 * 3 + 18, p2_pos15_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos19_x, p2_pos19_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos16_x and y == p2_pos16_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos16_x - 55 * 2 + 18, p2_pos16_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos20_x, p2_pos20_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos17_x and y == p2_pos17_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos17_x - 55 + 18, p2_pos17_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos21_x, p2_pos21_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos18_x and y == p2_pos18_y:
                x, y = p2_pos22_x, p2_pos22_y
                reposition_4()
            elif x == p2_pos19_x and y == p2_pos19_y:
                x, y = p2_pos23_x, p2_pos23_y
                reposition_4()
            elif x == p2_pos20_x and y == p2_pos20_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos20_x, p2_pos20_y + 55 * 4 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos24_x, p2_pos24_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos21_x and y == p2_pos21_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos21_x, p2_pos21_y + 55 * 3 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos25_x, p2_pos25_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos22_x and y == p2_pos22_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos22_x, p2_pos22_y + 55 * 2 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos26_x, p2_pos26_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos23_x and y == p2_pos23_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos23_x, p2_pos23_y + 55 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos27_x, p2_pos27_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos24_x and y == p2_pos24_y:
                x, y = p2_pos28_x, p2_pos28_y
                reposition_4()
            elif x == p2_pos25_x and y == p2_pos25_y:
                x, y = p2_pos29_x, p2_pos29_y
                reposition_4()
            elif x == p2_pos26_x and y == p2_pos26_y:
                x, y = p2_pos30_x, p2_pos30_y
                reposition_4()
            elif x == p2_pos27_x and y == p2_pos27_y:
                x, y = p2_pos31_x, p2_pos31_y
                reposition_4()
            elif x == p2_pos28_x and y == p2_pos28_y:
                x, y = p2_pos32_x, p2_pos32_y
                reposition_4()
            elif x == p2_pos29_x and y == p2_pos29_y:
                x, y = p2_pos33_x, p2_pos33_y
                reposition_4()
            elif x == p2_pos30_x and y == p2_pos30_y:
                x, y = p2_pos34_x, p2_pos34_y
                reposition_4()
            elif x == p2_pos31_x and y == p2_pos31_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos31_x + 55 * 4 - 18, p2_pos31_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos1_x, p2_pos1_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos32_x and y == p2_pos32_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos32_x + 55 * 3 - 18, p2_pos32_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos2_x, p2_pos2_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos33_x and y == p2_pos33_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos33_x + 55 * 2 - 18, p2_pos33_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos3_x, p2_pos3_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos34_x and y == p2_pos34_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos34_x + 55 - 18, p2_pos34_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos4_x, p2_pos4_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos1_x and y == p2_pos1_y:
                x, y = p2_pos6_x, p2_pos6_y
                reposition_5()
            elif x == p2_pos2_x and y == p2_pos2_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos2_x, p2_pos2_y - 55 * 5 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos7_x, p2_pos7_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos3_x and y == p2_pos3_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos3_x, p2_pos3_y - 55 * 4 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos8_x, p2_pos8_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos4_x and y == p2_pos4_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos4_x, p2_pos4_y - 55 * 3 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos9_x, p2_pos9_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos5_x and y == p2_pos5_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos5_x, p2_pos5_y - 55 * 2 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos10_x, p2_pos10_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos6_x and y == p2_pos6_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos6_x, p2_pos6_y - 55 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos11_x, p2_pos11_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos7_x and y == p2_pos7_y:
                x, y = p2_pos12_x, p2_pos12_y
                reposition_5()
            elif x == p2_pos8_x and y == p2_pos8_y:
                x, y = p2_pos13_x, p2_pos13_y
                reposition_5()
            elif x == p2_pos9_x and y == p2_pos9_y:
                x, y = p2_pos14_x, p2_pos14_y
                reposition_5()
            elif x == p2_pos10_x and y == p2_pos10_y:
                x, y = p2_pos15_x, p2_pos15_y
                reposition_5()
            elif x == p2_pos11_x and y == p2_pos11_y:
                x, y = p2_pos16_x, p2_pos16_y
                reposition_5()
            elif x == p2_pos12_x and y == p2_pos12_y:
                x, y = p2_pos17_x, p2_pos17_y
                reposition_5()
            elif x == p2_pos13_x and y == p2_pos13_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos13_x - 55 * 5 + 18, p2_pos13_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos18_x, p2_pos18_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos14_x and y == p2_pos14_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos14_x - 55 * 4 + 18, p2_pos14_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos19_x, p2_pos19_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos15_x and y == p2_pos15_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos15_x - 55 * 3 + 18, p2_pos15_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos20_x, p2_pos20_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos16_x and y == p2_pos16_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos16_x - 55 * 2 + 18, p2_pos16_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos21_x, p2_pos21_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos17_x and y == p2_pos17_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos17_x - 55 + 18, p2_pos17_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos22_x, p2_pos22_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos18_x and y == p2_pos18_y:
                x, y = p2_pos23_x, p2_pos23_y
                reposition_5()
            elif x == p2_pos19_x and y == p2_pos19_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos19_x, p2_pos19_y + 55 * 5 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos24_x, p2_pos24_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos20_x and y == p2_pos20_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos20_x, p2_pos20_y + 55 * 4 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos25_x, p2_pos25_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos21_x and y == p2_pos21_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos21_x, p2_pos21_y + 55 * 3 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos26_x, p2_pos26_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos22_x and y == p2_pos22_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos22_x, p2_pos22_y + 55 * 2 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos27_x, p2_pos27_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos23_x and y == p2_pos23_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos23_x, p2_pos23_y + 55 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos28_x, p2_pos28_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos24_x and y == p2_pos24_y:
                x, y = p2_pos29_x, p2_pos29_y
                reposition_5()
            elif x == p2_pos25_x and y == p2_pos25_y:
                x, y = p2_pos30_x, p2_pos30_y
                reposition_5()
            elif x == p2_pos26_x and y == p2_pos26_y:
                x, y = p2_pos31_x, p2_pos31_y
                reposition_5()
            elif x == p2_pos27_x and y == p2_pos27_y:
                x, y = p2_pos32_x, p2_pos32_y
                reposition_5()
            elif x == p2_pos28_x and y == p2_pos28_y:
                x, y = p2_pos33_x, p2_pos33_y
                reposition_5()
            elif x == p2_pos29_x and y == p2_pos29_y:
                x, y = p2_pos34_x, p2_pos34_y
                reposition_5()
            elif x == p2_pos30_x and y == p2_pos30_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos30_x + 55 * 5 - 18, p2_pos30_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos1_x, p2_pos1_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos31_x and y == p2_pos31_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos31_x + 55 * 4 - 18, p2_pos31_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos2_x, p2_pos2_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos32_x and y == p2_pos32_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos32_x + 55 * 3 - 18, p2_pos32_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos3_x, p2_pos3_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos33_x and y == p2_pos33_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos33_x + 55 * 2 - 18, p2_pos33_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos4_x, p2_pos4_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos34_x and y == p2_pos34_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos34_x + 55 - 18, p2_pos34_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos5_x, p2_pos5_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos1_x and y == p2_pos1_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos1_x, p2_pos1_y - 55 * 6 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos7_x, p2_pos7_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos2_x and y == p2_pos2_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos2_x, p2_pos2_y - 55 * 5 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos8_x, p2_pos8_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos3_x and y == p2_pos3_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos3_x, p2_pos3_y - 55 * 4 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos9_x, p2_pos9_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos4_x and y == p2_pos4_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos4_x, p2_pos4_y - 55 * 3 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos10_x, p2_pos10_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos5_x and y == p2_pos5_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos5_x, p2_pos5_y - 55 * 2 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos11_x, p2_pos11_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos6_x and y == p2_pos6_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos6_x, p2_pos6_y - 55 + 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos12_x, p2_pos12_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos7_x and y == p2_pos7_y:
                x, y = p2_pos13_x, p2_pos13_y
                reposition_6()
            elif x == p2_pos8_x and y == p2_pos8_y:
                x, y = p2_pos14_x, p2_pos14_y
                reposition_6()
            elif x == p2_pos9_x and y == p2_pos9_y:
                x, y = p2_pos15_x, p2_pos15_y
                reposition_6()
            elif x == p2_pos10_x and y == p2_pos10_y:
                x, y = p2_pos16_x, p2_pos16_y
                reposition_6()
            elif x == p2_pos11_x and y == p2_pos11_y:
                x, y = p2_pos17_x, p2_pos17_y
                reposition_6()
            elif x == p2_pos12_x and y == p2_pos12_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos12_x - 55 * 6 + 18, p2_pos12_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos18_x, p2_pos18_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos13_x and y == p2_pos13_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos13_x - 55 * 5 + 18, p2_pos13_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos19_x, p2_pos19_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos14_x and y == p2_pos14_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos14_x - 55 * 4 + 18, p2_pos14_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos20_x, p2_pos20_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos15_x and y == p2_pos15_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos15_x - 55 * 3 + 18, p2_pos15_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos21_x, p2_pos21_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos16_x and y == p2_pos16_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos16_x - 55 * 2 + 18, p2_pos16_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos22_x, p2_pos22_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos17_x and y == p2_pos17_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos17_x - 55 + 18, p2_pos17_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos23_x, p2_pos23_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos18_x and y == p2_pos18_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos18_x, p2_pos18_y + 55 * 6 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos24_x, p2_pos24_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos19_x and y == p2_pos19_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos19_x, p2_pos19_y + 55 * 5 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos25_x, p2_pos25_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos20_x and y == p2_pos20_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos20_x, p2_pos20_y + 55 * 4 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos26_x, p2_pos26_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos21_x and y == p2_pos21_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos21_x, p2_pos21_y + 55 * 3 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos27_x, p2_pos27_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos22_x and y == p2_pos22_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos22_x, p2_pos22_y + 55 * 2 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos28_x, p2_pos28_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos23_x and y == p2_pos23_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos23_x, p2_pos23_y + 55 - 18
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos29_x, p2_pos29_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos24_x and y == p2_pos24_y:
                x, y = p2_pos30_x, p2_pos30_y
                reposition_6()
            elif x == p2_pos25_x and y == p2_pos25_y:
                x, y = p2_pos31_x, p2_pos31_y
                reposition_6()
            elif x == p2_pos26_x and y == p2_pos26_y:
                x, y = p2_pos32_x, p2_pos32_y
                reposition_6()
            elif x == p2_pos27_x and y == p2_pos27_y:
                x, y = p2_pos33_x, p2_pos33_y
                reposition_6()
            elif x == p2_pos28_x and y == p2_pos28_y:
                x, y = p2_pos34_x, p2_pos34_y
                reposition_6()
            elif x == p2_pos29_x and y == p2_pos29_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos29_x + 55 * 6 - 18, p2_pos29_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos1_x, p2_pos1_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos30_x and y == p2_pos30_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos30_x + 55 * 5 - 18, p2_pos30_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos2_x, p2_pos2_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos31_x and y == p2_pos31_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos31_x + 55 * 4 - 18, p2_pos31_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos3_x, p2_pos3_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos32_x and y == p2_pos32_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos32_x + 55 * 3 - 18, p2_pos32_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.6)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos4_x, p2_pos4_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=0.8)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos33_x and y == p2_pos33_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos33_x + 55 * 2 - 18, p2_pos33_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.4)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos5_x, p2_pos5_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1)
                player_2_animated.start(player_2_curve)
            elif x == p2_pos34_x and y == p2_pos34_y:
                player_2_curve = get.root.ids.p2.ids.player_2
                x, y = p2_pos34_x + 55 - 18, p2_pos34_y
                player_2_animated = Animation(pos=(dp(x), dp(y)), duration=0.2)
                player_2_animated.start(player_2_curve)
                x, y = p2_pos6_x, p2_pos6_y
                player_2_animated += Animation(pos=(dp(x), dp(y)), duration=1.2)
                player_2_animated.start(player_2_curve)


class Salary(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos34_x and y == p1_pos34_y:
                Clock.schedule_once(self.start_text, 0.5)
                Clock.schedule_once(self.player_1_show_salary, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos33_x and y == p1_pos33_y:
                Clock.schedule_once(self.start_text, 0.7)
                Clock.schedule_once(self.player_1_show_salary, 0.7)

            if x == p1_pos34_x and y == p1_pos34_y:
                Clock.schedule_once(self.tax_text, 0.7)
                Clock.schedule_once(self.player_1_show_salary, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos32_x and y == p1_pos32_y:
                Clock.schedule_once(self.start_text, 0.9)
                Clock.schedule_once(self.player_1_show_salary, 0.9)

            if x == p1_pos33_x and y == p1_pos33_y:
                Clock.schedule_once(self.tax_text, 0.9)
                Clock.schedule_once(self.player_1_show_salary, 0.9)

            if x == p1_pos34_x and y == p1_pos34_y:
                Clock.schedule_once(self.move_text, 0.9)
                Clock.schedule_once(self.player_1_show_salary, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos31_x and y == p1_pos31_y:
                Clock.schedule_once(self.start_text, 1.1)
                Clock.schedule_once(self.player_1_show_salary, 1.1)

            if x == p1_pos32_x and y == p1_pos32_y:
                Clock.schedule_once(self.tax_text, 1.1)
                Clock.schedule_once(self.player_1_show_salary, 1.1)

            if x == p1_pos33_x and y == p1_pos33_y:
                Clock.schedule_once(self.move_text, 1.1)
                Clock.schedule_once(self.player_1_show_salary, 1.1)

            if x == p1_pos34_x and y == p1_pos34_y:
                Clock.schedule_once(self.points_text, 1.1)
                Clock.schedule_once(self.player_1_show_salary, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos30_x and y == p1_pos30_y:
                Clock.schedule_once(self.start_text, 1.3)
                Clock.schedule_once(self.player_1_show_salary, 1.3)

            if x == p1_pos31_x and y == p1_pos31_y:
                Clock.schedule_once(self.tax_text, 1.3)
                Clock.schedule_once(self.player_1_show_salary, 1.3)

            if x == p1_pos32_x and y == p1_pos32_y:
                Clock.schedule_once(self.move_text, 1.3)
                Clock.schedule_once(self.player_1_show_salary, 1.3)

            if x == p1_pos33_x and y == p1_pos33_y:
                Clock.schedule_once(self.points_text, 1.3)
                Clock.schedule_once(self.player_1_show_salary, 1.3)

            if x == p1_pos34_x and y == p1_pos34_y:
                Clock.schedule_once(self.player_1_big_ben_text, 2.5)
                Clock.schedule_once(self.player_1_show_salary, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos29_x and y == p1_pos29_y:
                Clock.schedule_once(self.start_text, 1.5)
                Clock.schedule_once(self.player_1_show_salary, 1.5)

            if x == p1_pos30_x and y == p1_pos30_y:
                Clock.schedule_once(self.tax_text, 1.5)
                Clock.schedule_once(self.player_1_show_salary, 1.5)

            if x == p1_pos31_x and y == p1_pos31_y:
                Clock.schedule_once(self.move_text, 1.5)
                Clock.schedule_once(self.player_1_show_salary, 1.5)

            if x == p1_pos32_x and y == p1_pos32_y:
                Clock.schedule_once(self.points_text, 1.5)
                Clock.schedule_once(self.player_1_show_salary, 1.5)

            if x == p1_pos33_x and y == p1_pos33_y:
                Clock.schedule_once(self.player_1_big_ben_text, 2.5)
                Clock.schedule_once(self.player_1_show_salary, 1.5)

            if x == p1_pos34_x and y == p1_pos34_y:
                Clock.schedule_once(self.crypto_text, 1.5)
                Clock.schedule_once(self.player_1_show_salary, 1.5)

    def player_1_show_salary(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "+200 $"
        if get.root.ids.board.ids.field_32.text == "purple" or get.root.ids.board.ids.field_34.text == "purple":
            get.root.ids.board.ids.cash_count.text = "+350 $"
        player_1_cash_count_g()
        DuckField.player_1_duck_on_turn(f_duck)
        Clock.schedule_once(self.player_1_hide_salary, 2.2)

    def player_1_hide_salary(self, *args):
        hide_cash_count()
        Clock.schedule_once(self.player_1_give_salary, 0.1)

    def player_1_give_salary(self, *args):
        get = App.get_running_app()
        if get.root.ids.board.ids.field_32.text == "purple" or get.root.ids.board.ids.field_34.text == "purple":
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 350}"
        else:
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 200}"
        money_update()
        Clock.schedule_once(self.player_1_callbacks, 0)

    @staticmethod
    def player_1_callbacks(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if x == p1_pos1_x and y == p1_pos1_y:
            unblock_roll()
        if x == p1_pos2_x and y == p1_pos2_y:
            TaxField.player_1_main(f_tax)
            TaxField.player_1_start_anim(f_tax)
        if x == p1_pos3_x and y == p1_pos3_y:
            MoveField.player_1_move_anim(f_move_field)
        if x == p1_pos4_x and y == p1_pos4_y:
            PointsField.player_1_points_anim(f_points)
        if x == p1_pos6_x and y == p1_pos6_y:
            CryptoField.player_1_crypto(f_crypto)

    @staticmethod
    def player_1_big_ben_text(*args):
        BigBenField.player_1_determine_ownership(f_big_ben)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos34_x and y == p2_pos34_y:
                Clock.schedule_once(self.start_text, 0.5)
                Clock.schedule_once(self.player_2_show_salary, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos33_x and y == p2_pos33_y:
                Clock.schedule_once(self.start_text, 0.7)
                Clock.schedule_once(self.player_2_show_salary, 0.7)

            if x == p2_pos34_x and y == p2_pos34_y:
                Clock.schedule_once(self.tax_text, 0.7)
                Clock.schedule_once(self.player_2_show_salary, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos32_x and y == p2_pos32_y:
                Clock.schedule_once(self.start_text, 0.9)
                Clock.schedule_once(self.player_2_show_salary, 0.9)

            if x == p2_pos33_x and y == p2_pos33_y:
                Clock.schedule_once(self.tax_text, 0.9)
                Clock.schedule_once(self.player_2_show_salary, 0.9)

            if x == p2_pos34_x and y == p2_pos34_y:
                Clock.schedule_once(self.move_text, 0.9)
                Clock.schedule_once(self.player_2_show_salary, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos31_x and y == p2_pos31_y:
                Clock.schedule_once(self.start_text, 1.1)
                Clock.schedule_once(self.player_2_show_salary, 1.1)

            if x == p2_pos32_x and y == p2_pos32_y:
                Clock.schedule_once(self.tax_text, 1.1)
                Clock.schedule_once(self.player_2_show_salary, 1.1)

            if x == p2_pos33_x and y == p2_pos33_y:
                Clock.schedule_once(self.move_text, 1.1)
                Clock.schedule_once(self.player_2_show_salary, 1.1)

            if x == p2_pos34_x and y == p2_pos34_y:
                Clock.schedule_once(self.points_text, 1.1)
                Clock.schedule_once(self.player_2_show_salary, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos30_x and y == p2_pos30_y:
                Clock.schedule_once(self.start_text, 1.3)
                Clock.schedule_once(self.player_2_show_salary, 1.3)

            if x == p2_pos31_x and y == p2_pos31_y:
                Clock.schedule_once(self.tax_text, 1.3)
                Clock.schedule_once(self.player_2_show_salary, 1.3)

            if x == p2_pos32_x and y == p2_pos32_y:
                Clock.schedule_once(self.move_text, 1.3)
                Clock.schedule_once(self.player_2_show_salary, 1.3)

            if x == p2_pos33_x and y == p2_pos33_y:
                Clock.schedule_once(self.points_text, 1.3)
                Clock.schedule_once(self.player_2_show_salary, 1.3)

            if x == p2_pos34_x and y == p2_pos34_y:
                Clock.schedule_once(self.player_2_big_ben_text, 2.5)
                Clock.schedule_once(self.player_2_show_salary, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos29_x and y == p2_pos29_y:
                Clock.schedule_once(self.start_text, 1.5)
                Clock.schedule_once(self.player_2_show_salary, 1.5)

            if x == p2_pos30_x and y == p2_pos30_y:
                Clock.schedule_once(self.tax_text, 1.5)
                Clock.schedule_once(self.player_2_show_salary, 1.5)

            if x == p2_pos31_x and y == p2_pos31_y:
                Clock.schedule_once(self.move_text, 1.5)
                Clock.schedule_once(self.player_2_show_salary, 1.5)

            if x == p2_pos32_x and y == p2_pos32_y:
                Clock.schedule_once(self.points_text, 1.5)
                Clock.schedule_once(self.player_2_show_salary, 1.5)

            if x == p2_pos33_x and y == p2_pos33_y:
                Clock.schedule_once(self.player_2_big_ben_text, 2.5)
                Clock.schedule_once(self.player_2_show_salary, 1.5)

            if x == p2_pos34_x and y == p2_pos34_y:
                Clock.schedule_once(self.crypto_text, 1.5)
                Clock.schedule_once(self.player_2_show_salary, 1.5)

    def player_2_show_salary(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "+200 $"
        if get.root.ids.board.ids.field_32.text == "green" or get.root.ids.board.ids.field_34.text == "green":
            get.root.ids.board.ids.cash_count.text = "+350 $"
        player_2_cash_count_g()
        DuckField.player_2_duck_on_turn(f_duck)
        Clock.schedule_once(self.player_2_hide_salary, 2.2)

    def player_2_hide_salary(self, *args):
        hide_cash_count()
        Clock.schedule_once(self.player_2_give_salary, 0.1)

    def player_2_give_salary(self, *args):
        get = App.get_running_app()
        if get.root.ids.board.ids.field_32.text == "green" or get.root.ids.board.ids.field_34.text == "green":
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 350}"
        else:
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 200}"
        money_update()
        Clock.schedule_once(self.player_2_callbacks, 0)

    @staticmethod
    def player_2_callbacks(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if x == p2_pos1_x and y == p2_pos1_y:
            unblock_roll()
        if x == p2_pos2_x and y == p2_pos2_y:
            TaxField.player_2_main(f_tax)
            TaxField.player_2_start_anim(f_tax)
        if x == p2_pos3_x and y == p2_pos3_y:
            MoveField.player_2_move_anim(f_move_field)
        if x == p2_pos4_x and y == p2_pos4_y:
            PointsField.player_2_points_anim(f_points)
        if x == p2_pos6_x and y == p2_pos6_y:
            CryptoField.player_2_crypto(f_crypto)

    @staticmethod
    def player_2_big_ben_text(*args):
        BigBenField.player_2_determine_ownership(f_big_ben)

    # Both Players - General Functions

    @staticmethod
    def start_text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "Taking the Big Money! :D"
        get.root.ids.board.ids.big.valign = "middle"
        get.root.ids.board.ids.big.font_size = 35

    @staticmethod
    def tax_text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = tax_fields
        get.root.ids.board.ids.big.valign = "middle"
        get.root.ids.board.ids.big.font_size = 35

    @staticmethod
    def move_text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = move_three_fields
        get.root.ids.board.ids.big.valign = "middle"
        get.root.ids.board.ids.big.font_size = 35

    @staticmethod
    def crypto_text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = crypto_fields

    @staticmethod
    def points_text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = f"{'[color=ffaf03]'}Points multiplier!{'[/color]'}\n\nDice number " \
                                          f"multiplied by 3!\n\nYou receive {'[color=E9F505]'}" \
                                          f"{int(get.root.ids.board.ids.dice.text) * 3} points{'[/color]'}."


class TaxField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self, *args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos1_x and y == p1_pos1_y:
                Clock.schedule_once(self.player_1_main, 0.3)
                Clock.schedule_once(self.player_1_start_anim, 0.5)

            if x == p1_pos17_x and y == p1_pos17_y:
                Clock.schedule_once(self.player_1_main, 0.5)
                Clock.schedule_once(self.player_1_start_anim, 0.7)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos16_x and y == p1_pos16_y:
                Clock.schedule_once(self.player_1_main, 0.7)
                Clock.schedule_once(self.player_1_start_anim, 0.9)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos15_x and y == p1_pos15_y:
                Clock.schedule_once(self.player_1_main, 0.9)
                Clock.schedule_once(self.player_1_start_anim, 1.1)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos14_x and y == p1_pos14_y:
                Clock.schedule_once(self.player_1_main, 1.1)
                Clock.schedule_once(self.player_1_start_anim, 1.3)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos13_x and y == p1_pos13_y:
                Clock.schedule_once(self.player_1_main, 1.3)
                Clock.schedule_once(self.player_1_start_anim, 1.5)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos12_x and y == p1_pos12_y:
                Clock.schedule_once(self.player_1_main, 1.5)
                Clock.schedule_once(self.player_1_start_anim, 1.7)

    def player_1_start_anim(self, *args):
        player_1_cash_count_r()
        Clock.schedule_once(self.end_anim, 2)

    @staticmethod
    def player_1_main(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if x == p1_pos2_x and y == p1_pos2_y:
            get.root.ids.board.ids.big.text = tax_fields
            get.root.ids.board.ids.cash_count.text = "-50 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 50}"

        if x == p1_pos18_x and y == p1_pos18_y:
            get.root.ids.board.ids.big.text = tax_fields_2
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"

    # Player 2 - Own Functions

    def player_2_trigger(self, *args):
        get = App.get_running_app()

        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos1_x and y == p2_pos1_y:
                Clock.schedule_once(self.player_2_main, 0.3)
                Clock.schedule_once(self.player_2_start_anim, 0.5)

            if x == p2_pos17_x and y == p2_pos17_y:
                Clock.schedule_once(self.player_2_main, 0.5)
                Clock.schedule_once(self.player_2_start_anim, 0.7)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos16_x and y == p2_pos16_y:
                Clock.schedule_once(self.player_2_main, 0.7)
                Clock.schedule_once(self.player_2_start_anim, 0.9)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos15_x and y == p2_pos15_y:
                Clock.schedule_once(self.player_2_main, 0.9)
                Clock.schedule_once(self.player_2_start_anim, 1.1)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos14_x and y == p2_pos14_y:
                Clock.schedule_once(self.player_2_main, 1.1)
                Clock.schedule_once(self.player_2_start_anim, 1.3)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos13_x and y == p2_pos13_y:
                Clock.schedule_once(self.player_2_main, 1.3)
                Clock.schedule_once(self.player_2_start_anim, 1.5)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos12_x and y == p2_pos12_y:
                Clock.schedule_once(self.player_2_main, 1.5)
                Clock.schedule_once(self.player_2_start_anim, 1.7)

    def player_2_start_anim(self, *args):
        player_2_cash_count_r()
        Clock.schedule_once(self.end_anim, 2)

    @staticmethod
    def player_2_main(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if x == p2_pos2_x and y == p2_pos2_y:
            get.root.ids.board.ids.big.text = tax_fields
            get.root.ids.board.ids.cash_count.text = "-50 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 50}"

        if x == p2_pos18_x and y == p2_pos18_y:
            get.root.ids.board.ids.big.text = tax_fields_2
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class MoveField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos2_x and y == p1_pos2_y:
                Clock.schedule_once(self.text, 0.3)
                Clock.schedule_once(self.player_1_move_anim, 2)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos1_x and y == p1_pos1_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.player_1_move_anim, 2.2)

    def player_1_move_anim(self, *args):
        get = App.get_running_app()
        pl_1 = get.root.ids.p1.ids.player_1
        pl_1_anim = Animation(pos=(dp(p1_pos6_x), dp(p1_pos6_y)), duration=0.6)
        pl_1_anim.start(pl_1)

        Clock.schedule_once(self.player_1_crypto, 0.7)

    @staticmethod
    def player_1_crypto(*args):
        CryptoField.player_1_crypto(f_crypto)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos2_x and y == p2_pos2_y:
                Clock.schedule_once(self.text, 0.3)
                Clock.schedule_once(self.player_2_move_anim, 2)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos1_x and y == p2_pos1_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.player_2_move_anim, 2.2)

    def player_2_move_anim(self, *args):
        get = App.get_running_app()
        pl_1 = get.root.ids.p2.ids.player_2
        pl_1_anim = Animation(pos=(dp(p2_pos6_x), dp(p2_pos6_y)), duration=0.6)
        pl_1_anim.start(pl_1)

        Clock.schedule_once(self.player_2_crypto, 0.7)

    @staticmethod
    def player_2_crypto(*args):
        CryptoField.player_2_crypto(f_crypto)

    # Both Players - General Functions

    @staticmethod
    def text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = move_three_fields


class PointsField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos3_x and y == p1_pos3_y:
                Clock.schedule_once(self.text, 0.4)
                Clock.schedule_once(self.player_1_points_anim, 0.6)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos2_x and y == p1_pos2_y:
                Clock.schedule_once(self.text, 0.6)
                Clock.schedule_once(self.player_1_points_anim, 0.8)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos1_x and y == p1_pos1_y:
                Clock.schedule_once(self.text, 0.8)
                Clock.schedule_once(self.player_1_points_anim, 1)

    def player_1_points_anim(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.points_count.text = f"+{int(get.root.ids.board.ids.dice.text) * 3} pts."
        player_1_points_count()
        get.root.ids.p1.ids.p1_points_stash.text = \
            f"{int(get.root.ids.p1.ids.p1_points_stash.text) + int(get.root.ids.board.ids.dice.text) * 3}"
        Clock.schedule_once(self.end_anim, 2)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos3_x and y == p2_pos3_y:
                Clock.schedule_once(self.text, 0.4)
                Clock.schedule_once(self.player_2_points_anim, 0.6)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos2_x and y == p2_pos2_y:
                Clock.schedule_once(self.text, 0.6)
                Clock.schedule_once(self.player_2_points_anim, 0.8)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos1_x and y == p2_pos1_y:
                Clock.schedule_once(self.text, 0.8)
                Clock.schedule_once(self.player_2_points_anim, 1)

    def player_2_points_anim(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.points_count.text = f"+{int(get.root.ids.board.ids.dice.text) * 3} pts."
        player_2_points_count()
        get.root.ids.p2.ids.p2_points_stash.text = \
            f"{int(get.root.ids.p2.ids.p2_points_stash.text) + int(get.root.ids.board.ids.dice.text) * 3}"
        Clock.schedule_once(self.end_anim, 2)

    # Both Players - General Functions

    @staticmethod
    def text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = f"{'[color=ffaf03]'}Points multiplier!{'[/color]'}\n\nDice number " \
                                          f"multiplied by 3!\n\nYou receive {'[color=E9F505]'}" \
                                          f"{int(get.root.ids.board.ids.dice.text) * 3} points{'[/color]'}."

    @staticmethod
    def end_anim(*args):
        hide_points_count()
        money_update()
        unblock_roll()


class BigBenField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos4_x and y == p1_pos4_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos3_x and y == p1_pos3_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos2_x and y == p1_pos2_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos1_x and y == p1_pos1_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_5.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_5.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_5.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = big_ben_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. Big Ben is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-120 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 120}"
        get.root.ids.board.ids.field_5.background_color = player_1_color
        get.root.ids.board.ids.field_5.text = "purple"
        money_update()
        unblock_roll()

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        unblock_roll()

    def player_1_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 0:
            fee = 30
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 1:
            fee = 50
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 2:
            fee = 85
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 3:
            fee = 120
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money, 1.5)

    def player_1_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 0:
            fee = 30
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 1:
            fee = 50
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 2:
            fee = 85
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 3:
            fee = 120
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) - fee)}"
        player_1_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_1_move_label, 1.5)

    def player_1_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money, 1)

    def player_2_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 0:
            fee = 30
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 1:
            fee = 50
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 2:
            fee = 85
        if int(get.root.ids.f_shop.ids.big_ben_count_2_2.text) == 3:
            fee = 120
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)
        Clock.schedule_once(self.end_anim, 1.8)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos4_x and y == p2_pos4_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos3_x and y == p2_pos3_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos2_x and y == p2_pos2_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos1_x and y == p2_pos1_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_5.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_5.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_5.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = big_ben_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. Big Ben is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-120 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 120}"
        get.root.ids.board.ids.field_5.background_color = player_2_color
        get.root.ids.board.ids.field_5.text = "green"
        money_update()
        unblock_roll()

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        unblock_roll()

    def player_2_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 0:
            fee = 30
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 1:
            fee = 50
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 2:
            fee = 85
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 3:
            fee = 120
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money, 1.5)

    def player_2_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 0:
            fee = 30
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 1:
            fee = 50
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 2:
            fee = 85
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 3:
            fee = 120
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) - fee)}"
        player_2_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_2_move_label, 1.5)

    def player_2_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money, 1)

    def player_1_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 0:
            fee = 30
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 1:
            fee = 50
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 2:
            fee = 85
        if int(get.root.ids.f_shop.ids.big_ben_count_2.text) == 3:
            fee = 120
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)
        Clock.schedule_once(self.end_anim, 1.8)

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class CryptoField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos5_x and y == p1_pos5_y:
                Clock.schedule_once(self.player_1_crypto, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos4_x and y == p1_pos4_y:
                Clock.schedule_once(self.player_1_crypto, 0.7)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos2_x and y == p1_pos2_y:
                Clock.schedule_once(self.player_1_crypto, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos1_x and y == p1_pos1_y:
                Clock.schedule_once(self.player_1_crypto, 1.3)

    @staticmethod
    def player_1_crypto(*args):
        get = App.get_running_app()

        if get.root.ids.p1.ids.p1_crypto_stash.text == "0":
            get.root.ids.board.ids.big.text = crypto_fields
            get.root.ids.p1.ids.player_1_yes.disabled = False
            get.root.ids.p1.ids.yes_button_image.opacity = 1
            get.root.ids.p1.ids.player_1_no.disabled = False
            get.root.ids.p1.ids.no_button_image.opacity = 1

        if not get.root.ids.p1.ids.p1_crypto_stash.text == "0":
            get.root.ids.board.ids.big.text = "You can't buy crypto when you already own!"
            unblock_roll()

    @staticmethod
    def player_1_crypto_update(*args):
        get = App.get_running_app()

        def perc_cond():
            if a == 0:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+1 %"
            if a == 1:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+2 %"
            if a == 2:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+3 %"
            if a == 3:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+4 %"
            if a == 4:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+5 %"
            if a == 5:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+6 %"
            if a == 6:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+7 %"
            if a == 7:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+8 %"
            if a == 8:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+9 %"
            if a == 9:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+10 %"
            if a == 10:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+11 %"
            if a == 11:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+12 %"
            if a == 12:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+13 %"
            if a == 13:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+14 %"
            if a == 14:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+15 %"
            if a == 15:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+16 %"
            if a == 16:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+17 %"
            if a == 17:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+18 %"
            if a == 18:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+19 %"
            if a == 19:
                get.root.ids.p1.ids.p1_crypto_percent.text = "+20 %"
            if a == 20:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-1 %"
            if a == 21:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-2 %"
            if a == 22:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-3 %"
            if a == 23:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-4 %"
            if a == 24:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-5 %"
            if a == 25:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-6 %"
            if a == 26:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-7 %"
            if a == 27:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-8 %"
            if a == 28:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-9 %"
            if a == 29:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-10 %"
            if a == 30:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-11 %"
            if a == 31:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-12 %"
            if a == 32:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-13 %"
            if a == 33:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-14 %"
            if a == 34:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-15 %"
            if a == 35:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-16 %"
            if a == 36:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-17 %"
            if a == 37:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-18 %"
            if a == 38:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-19 %"
            if a == 39:
                get.root.ids.p1.ids.p1_crypto_percent.text = "-20 %"

        def animate_sell_profit(*args):
            get.root.ids.p1.ids.p1_crypto_percent.opacity = 0
            res = int(float(get.root.ids.p1.ids.p1_crypto_stash.text))
            res2 = int(float(res) - float(player1))

            get.root.ids.board.ids.cash_count.text = f"+{res} $"
            get.root.ids.board.ids.crypto_count.text = f"+{res2} $"

            player_1_cash_count_g()

            anim2 = Animation(opacity=0, duration=0.01)
            anim2 += Animation(pos=(dp(175), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim2 += Animation(opacity=1, duration=0.05)
            anim2 += Animation(color=(0, 1, 0, 1))
            anim2.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell_profit, 2.5)

        def animate_sell_loss(*args):
            get.root.ids.p1.ids.p1_crypto_percent.opacity = 0
            res = int(float(player1) - float(get.root.ids.p1.ids.p1_crypto_stash.text))
            res2 = int(float(get.root.ids.p1.ids.p1_crypto_stash.text))

            get.root.ids.board.ids.cash_count.text = f"+{res2} $"
            get.root.ids.board.ids.crypto_count.text = f"-{res} $"

            player_1_cash_count_g()

            anim = Animation(opacity=0, duration=0.01)
            anim += Animation(pos=(dp(175), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim += Animation(opacity=1, duration=0.05)
            anim += Animation(color=(1, 0, 0, 1))

            anim.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell_profit, 2.5)

        def sell_profit(*args):
            get.root.ids.board.ids.crypto_count.text = ""
            hide_cash_count()

            crypto_anim = Animation(opacity=0, duration=0.05)
            crypto_anim += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)
            crypto_anim.start(get.root.ids.board.ids.crypto_count)

            all_money = int(get.root.ids.p1.ids.p1_money_stash.text) + float(get.root.ids.p1.ids.p1_crypto_stash.text)
            all_money = int(all_money)

            get.root.ids.p1.ids.p1_money_stash.text = f"{all_money}"
            get.root.ids.p1.ids.p1_crypto_stash.text = "0"
            get.root.ids.p1.ids.p1_sell_crypto.disabled = True
            get.root.ids.p1.ids.crypto_button_image.opacity = 0
            get.root.ids.p1.ids.p1_crypto_percent.opacity = 0

            money_update()

        with open(r"crypto.txt", "r") as f:
            player1 = f.readline().strip()
            f.close()

        if not get.root.ids.p1.ids.p1_crypto_stash.text == "0":
            get.root.ids.p1.ids.p1_crypto_percent.opacity = 1

            my_tuple = 1 / 100, 2 / 100, 3 / 100, 4 / 100, 5 / 100, 6 / 100, 7 / 100, 8 / 100, 9 / 100, 10 / 100, \
                       11 / 100, 12 / 100, 13 / 100, 14 / 100, 15 / 100, 16 / 100, 17 / 100, 18 / 100, 19 / 100, \
                       20 / 100, -1 / 100, -2 / 100, -3 / 100, -4 / 100, -5 / 100, -6 / 100, -7 / 100, -8 / 100, \
                       -9 / 100, -10 / 100, -11 / 100, -12 / 100, -13 / 100, -14 / 100, -15 / 100, -16 / 100, \
                       -17 / 100, -18 / 100, -19 / 100, -20 / 100

            a = randint(0, 39)
            rand = my_tuple[a]

            if a <= 19:
                get.root.ids.p1.ids.p1_crypto_percent.color = (0, 1, 0, 1)
            elif a >= 20:
                get.root.ids.p1.ids.p1_crypto_percent.color = (1, 0, 0, 1)

            result = float(get.root.ids.p1.ids.p1_crypto_stash.text) + \
                     (float(get.root.ids.p1.ids.p1_crypto_stash.text) * rand)
            result = round(result, 2)
            get.root.ids.p1.ids.p1_crypto_stash.text = f"{result}"

            perc_cond()
            money_update()

            sell_crypto_profit = float(player1) + (float(player1) * 50 / 100)
            sell_crypto_loss = float(player1) - (float(player1) * 50 / 100)

            if result > sell_crypto_profit:
                animate_sell_profit()

            elif result <= sell_crypto_loss:
                animate_sell_loss()

        if get.root.ids.p1.ids.p1_crypto_stash.text == "0":
            get.root.ids.p1.ids.p1_sell_crypto.disabled = True
            get.root.ids.p1.ids.crypto_button_image.opacity = 0
            get.root.ids.p1.ids.p1_crypto_percent.opacity = 0

    @staticmethod
    def player_1_buy(*args):
        get = App.get_running_app()

        def buy(*args):
            get.root.ids.p1.ids.p1_sell_crypto.disabled = False
            get.root.ids.p1.ids.crypto_button_image.opacity = 1

            invested = float(get.root.ids.p1.ids.p1_input.text)
            total = int(float(get.root.ids.p1.ids.p1_money_stash.text) - invested)

            get.root.ids.p1.ids.p1_crypto_stash.text = \
                f"{float(get.root.ids.p1.ids.p1_crypto_stash.text) + invested}"

            get.root.ids.p1.ids.p1_money_stash.text = f"{total}"

            with open(r"crypto.txt", "w+") as f:
                f.write(f"{invested}".strip())
                f.close()

            money_update()
            unblock_roll()

        def exchange_money(*args):
            def empty_field_pop_up():
                popup = Popup(title='Invalid entry', content=Label(text="                Empty input field???\n\n"
                                                                        "Please input a valid amount to invest!"),
                              size_hint=(None, None), size=(400, 400))
                popup.open()

            def not_enough_cash_pop_up():
                popup = Popup(title='Invalid entry', content=Label(text="             Not enough cash to invest!"
                                                                        "\n\nPlease enter a number that you have "
                                                                        "available!"),
                              size_hint=(None, None), size=(400, 400))
                popup.open()

            if get.root.ids.p1.ids.p1_input.text == "":
                empty_field_pop_up()
            elif float(get.root.ids.p1.ids.p1_input.text) > float(get.root.ids.p1.ids.p1_money_stash.text):
                not_enough_cash_pop_up()
            else:
                get.root.ids.board.ids.cash_count.text = f"-{get.root.ids.p1.ids.p1_input.text} $"
                get.root.ids.board.ids.crypto_count.text = f"+{get.root.ids.p1.ids.p1_input.text} $"

                player_1_cash_count_r()

                anim2 = Animation(opacity=0, duration=0.01)
                anim2 += Animation(pos=(dp(175), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
                anim2 += Animation(opacity=1, duration=0.05)
                anim2 += Animation(color=(0, 1, 0, 1))

                anim2.start(get.root.ids.board.ids.crypto_count)

                Clock.schedule_once(remove_animation, 3)

        def remove_animation(*args):
            get.root.ids.board.ids.crypto_count.text = ""

            hide_cash_count()

            anim = Animation(opacity=0, duration=0.05)
            anim += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)

            anim.start(get.root.ids.board.ids.crypto_count)

            anim.bind(on_complete=buy)

        Clock.schedule_once(exchange_money, 0.2)

    @staticmethod
    def player_1_sell(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.p1_sell_crypto.disabled = True
        get.root.ids.p1.ids.crypto_button_image.opacity = 0
        get.root.ids.p1.ids.p1_crypto_percent.opacity = 0

        with open(r"crypto.txt", "r") as f:
            player1 = f.readline().strip()
            f.close()

        def animate_sell_profit(*args):
            final = int(float(get.root.ids.p1.ids.p1_crypto_stash.text))
            final2 = int(float(get.root.ids.p1.ids.p1_crypto_stash.text) - float(player1))

            get.root.ids.board.ids.cash_count.text = f"+{final} $"
            get.root.ids.board.ids.crypto_count.text = f"+{final2} $"

            player_1_cash_count_g()

            anim2 = Animation(opacity=0, duration=0.01)
            anim2 += Animation(pos=(dp(175), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim2 += Animation(opacity=1, duration=0.05)
            anim2 += Animation(color=(0, 1, 0, 1))

            anim2.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell, 2.5)

        def animate_sell_loss(*args):
            final = int(float(get.root.ids.p1.ids.p1_crypto_stash.text))
            final2 = int(float(player1) - float(get.root.ids.p1.ids.p1_crypto_stash.text))

            get.root.ids.board.ids.cash_count.text = f"+{final} $"
            get.root.ids.board.ids.crypto_count.text = f"-{final2} $"

            player_1_cash_count_g()

            anim = Animation(opacity=0, duration=0.01)
            anim += Animation(pos=(dp(175), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim += Animation(opacity=1, duration=0.05)
            anim += Animation(color=(1, 0, 0, 1))

            anim.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell, 2.5)

        def sell(*args):
            get.root.ids.board.ids.crypto_count.text = ""
            hide_cash_count()

            anim2 = Animation(opacity=0, duration=0.05)
            anim2 += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)

            anim2.start(get.root.ids.board.ids.crypto_count)

            all_money = int(get.root.ids.p1.ids.p1_money_stash.text) + float(get.root.ids.p1.ids.p1_crypto_stash.text)
            all_money = int(all_money)
            get.root.ids.p1.ids.p1_money_stash.text = f"{all_money}"
            get.root.ids.p1.ids.p1_crypto_stash.text = "0"

            money_update()

        res = round(float(get.root.ids.p1.ids.p1_crypto_stash.text), 0)
        something = float(player1)

        if res >= something:
            animate_sell_profit()
        elif res <= something:
            animate_sell_loss()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos5_x and y == p2_pos5_y:
                Clock.schedule_once(self.player_2_crypto, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos4_x and y == p2_pos4_y:
                Clock.schedule_once(self.player_2_crypto, 0.7)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos2_x and y == p2_pos2_y:
                Clock.schedule_once(self.player_2_crypto, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos1_x and y == p2_pos1_y:
                Clock.schedule_once(self.player_2_crypto, 1.3)

    @staticmethod
    def player_2_crypto(*args):
        get = App.get_running_app()

        if get.root.ids.p2.ids.p2_crypto_stash.text == "0":
            get.root.ids.board.ids.big.text = crypto_fields
            get.root.ids.p2.ids.player_2_yes.disabled = False
            get.root.ids.p2.ids.yes_button_image.opacity = 1
            get.root.ids.p2.ids.player_2_no.disabled = False
            get.root.ids.p2.ids.no_button_image.opacity = 1

        if not get.root.ids.p2.ids.p2_crypto_stash.text == "0":
            get.root.ids.board.ids.big.text = "You can't buy crypto when you already own!"
            unblock_roll()

    @staticmethod
    def player_2_crypto_update(*args):
        get = App.get_running_app()

        def perc_cond():
            if a == 0:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+1 %"
            if a == 1:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+2 %"
            if a == 2:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+3 %"
            if a == 3:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+4 %"
            if a == 4:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+5 %"
            if a == 5:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+6 %"
            if a == 6:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+7 %"
            if a == 7:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+8 %"
            if a == 8:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+9 %"
            if a == 9:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+10 %"
            if a == 10:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+11 %"
            if a == 11:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+12 %"
            if a == 12:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+13 %"
            if a == 13:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+14 %"
            if a == 14:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+15 %"
            if a == 15:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+16 %"
            if a == 16:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+17 %"
            if a == 17:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+18 %"
            if a == 18:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+19 %"
            if a == 19:
                get.root.ids.p2.ids.p2_crypto_percent.text = "+20 %"
            if a == 20:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-1 %"
            if a == 21:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-2 %"
            if a == 22:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-3 %"
            if a == 23:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-4 %"
            if a == 24:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-5 %"
            if a == 25:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-6 %"
            if a == 26:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-7 %"
            if a == 27:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-8 %"
            if a == 28:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-9 %"
            if a == 29:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-10 %"
            if a == 30:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-11 %"
            if a == 31:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-12 %"
            if a == 32:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-13 %"
            if a == 33:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-14 %"
            if a == 34:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-15 %"
            if a == 35:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-16 %"
            if a == 36:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-17 %"
            if a == 37:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-18 %"
            if a == 38:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-19 %"
            if a == 39:
                get.root.ids.p2.ids.p2_crypto_percent.text = "-20 %"

        def animate_sell_profit(*args):
            get.root.ids.p2.ids.p2_crypto_percent.opacity = 0
            res = int(float(get.root.ids.p2.ids.p2_crypto_stash.text))
            res2 = int(float(res) - float(player2))

            get.root.ids.board.ids.cash_count.text = f"+{res} $"
            get.root.ids.board.ids.crypto_count.text = f"+{res2} $"

            player_2_cash_count_g()

            anim2 = Animation(opacity=0, duration=0.01)
            anim2 += Animation(pos=(dp(1055), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim2 += Animation(opacity=1, duration=0.05)
            anim2 += Animation(color=(0, 1, 0, 1))
            anim2.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell_profit, 2.5)

        def animate_sell_loss(*args):
            get.root.ids.p2.ids.p2_crypto_percent.opacity = 0
            res = int(float(player2) - float(get.root.ids.p2.ids.p2_crypto_stash.text))
            res2 = int(float(get.root.ids.p2.ids.p2_crypto_stash.text))

            get.root.ids.board.ids.cash_count.text = f"+{res2} $"
            get.root.ids.board.ids.crypto_count.text = f"-{res} $"

            player_2_cash_count_g()

            anim = Animation(opacity=0, duration=0.01)
            anim += Animation(pos=(dp(1055), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim += Animation(opacity=1, duration=0.05)
            anim += Animation(color=(1, 0, 0, 1))

            anim.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell_profit, 2.5)

        def sell_profit(*args):
            get.root.ids.board.ids.crypto_count.text = ""
            hide_cash_count()

            crypto_anim = Animation(opacity=0, duration=0.05)
            crypto_anim += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)
            crypto_anim.start(get.root.ids.board.ids.crypto_count)

            all_money = int(get.root.ids.p2.ids.p2_money_stash.text) + float(get.root.ids.p2.ids.p2_crypto_stash.text)
            all_money = int(all_money)

            get.root.ids.p2.ids.p2_money_stash.text = f"{all_money}"
            get.root.ids.p2.ids.p2_crypto_stash.text = "0"
            get.root.ids.p2.ids.p2_sell_crypto.disabled = True
            get.root.ids.p2.ids.crypto_button_image.opacity = 0
            get.root.ids.p2.ids.p2_crypto_percent.opacity = 0

            money_update()

        with open(r"crypto_2.txt", "r") as f:
            player2 = f.readline().strip()
            f.close()

        if not get.root.ids.p2.ids.p2_crypto_stash.text == "0":
            get.root.ids.p2.ids.p2_crypto_percent.opacity = 1

            my_tuple = 1 / 100, 2 / 100, 3 / 100, 4 / 100, 5 / 100, 6 / 100, 7 / 100, 8 / 100, 9 / 100, 10 / 100, \
                       11 / 100, 12 / 100, 13 / 100, 14 / 100, 15 / 100, 16 / 100, 17 / 100, 18 / 100, 19 / 100, \
                       20 / 100, -1 / 100, -2 / 100, -3 / 100, -4 / 100, -5 / 100, -6 / 100, -7 / 100, -8 / 100, \
                       -9 / 100, -10 / 100, -11 / 100, -12 / 100, -13 / 100, -14 / 100, -15 / 100, -16 / 100, \
                       -17 / 100, -18 / 100, -19 / 100, -20 / 100

            a = randint(0, 39)
            rand = my_tuple[a]

            if a <= 19:
                get.root.ids.p2.ids.p2_crypto_percent.color = (0, 1, 0, 1)
            elif a >= 20:
                get.root.ids.p2.ids.p2_crypto_percent.color = (1, 0, 0, 1)

            result = float(get.root.ids.p2.ids.p2_crypto_stash.text) + \
                     (float(get.root.ids.p2.ids.p2_crypto_stash.text) * rand)
            result = round(result, 2)
            get.root.ids.p2.ids.p2_crypto_stash.text = f"{result}"

            perc_cond()
            money_update()

            sell_crypto_profit = float(player2) + (float(player2) * 50 / 100)
            sell_crypto_loss = float(player2) - (float(player2) * 50 / 100)

            if result > sell_crypto_profit:
                animate_sell_profit()

            elif result <= sell_crypto_loss:
                animate_sell_loss()

        if get.root.ids.p2.ids.p2_crypto_stash.text == "0":
            get.root.ids.p2.ids.p2_sell_crypto.disabled = True
            get.root.ids.p2.ids.crypto_button_image.opacity = 0
            get.root.ids.p2.ids.p2_crypto_percent.opacity = 0

    @staticmethod
    def player_2_buy(*args):
        get = App.get_running_app()

        def buy(*args):
            get.root.ids.p2.ids.p2_sell_crypto.disabled = False
            get.root.ids.p2.ids.crypto_button_image.opacity = 1

            invested = float(get.root.ids.p2.ids.p2_input.text)
            total = int(float(get.root.ids.p2.ids.p2_money_stash.text) - invested)

            get.root.ids.p2.ids.p2_crypto_stash.text = \
                f"{float(get.root.ids.p2.ids.p2_crypto_stash.text) + invested}"

            get.root.ids.p2.ids.p2_money_stash.text = f"{total}"

            with open(r"crypto_2.txt", "w+") as f:
                f.write(f"{invested}".strip())
                f.close()

            money_update()
            unblock_roll()

        def exchange_money(*args):
            def empty_field_pop_up():
                popup = Popup(title='Invalid entry', content=Label(text="                Empty input field???\n\n"
                                                                        "Please input a valid amount to invest!"),
                              size_hint=(None, None), size=(400, 400))
                popup.open()

            def not_enough_cash_pop_up():
                popup = Popup(title='Invalid entry', content=Label(text="             Not enough cash to invest!"
                                                                        "\n\nPlease enter a number that you have "
                                                                        "available!"),
                              size_hint=(None, None), size=(400, 400))
                popup.open()

            if get.root.ids.p2.ids.p2_input.text == "":
                empty_field_pop_up()
            elif float(get.root.ids.p2.ids.p2_input.text) > float(get.root.ids.p2.ids.p2_money_stash.text):
                not_enough_cash_pop_up()
            else:
                get.root.ids.board.ids.cash_count.text = f"-{get.root.ids.p2.ids.p2_input.text} $"
                get.root.ids.board.ids.crypto_count.text = f"+{get.root.ids.p2.ids.p2_input.text} $"

                player_2_cash_count_r()

                anim2 = Animation(opacity=0, duration=0.01)
                anim2 += Animation(pos=(dp(1055), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
                anim2 += Animation(opacity=1, duration=0.05)
                anim2 += Animation(color=(0, 1, 0, 1))

                anim2.start(get.root.ids.board.ids.crypto_count)

                Clock.schedule_once(remove_animation, 3)

        def remove_animation(*args):
            get.root.ids.board.ids.crypto_count.text = ""

            hide_cash_count()

            anim = Animation(opacity=0, duration=0.05)
            anim += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)

            anim.start(get.root.ids.board.ids.crypto_count)

            anim.bind(on_complete=buy)

        Clock.schedule_once(exchange_money, 0.2)

    @staticmethod
    def player_2_sell(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.p2_sell_crypto.disabled = True
        get.root.ids.p2.ids.crypto_button_image.opacity = 0
        get.root.ids.p2.ids.p2_crypto_percent.opacity = 0

        with open(r"crypto_2.txt", "r") as f:
            player2 = f.readline().strip()
            f.close()

        def animate_sell_profit(*args):
            final = int(float(get.root.ids.p2.ids.p2_crypto_stash.text))
            final2 = int(float(get.root.ids.p2.ids.p2_crypto_stash.text) - float(player2))

            get.root.ids.board.ids.cash_count.text = f"+{final} $"
            get.root.ids.board.ids.crypto_count.text = f"+{final2} $"

            player_2_cash_count_g()

            anim2 = Animation(opacity=0, duration=0.01)
            anim2 += Animation(pos=(dp(1055), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim2 += Animation(opacity=1, duration=0.05)
            anim2 += Animation(color=(0, 1, 0, 1))

            anim2.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell, 2.5)

        def animate_sell_loss(*args):
            final = int(float(get.root.ids.p2.ids.p2_crypto_stash.text))
            final2 = int(float(player2) - float(get.root.ids.p2.ids.p2_crypto_stash.text))

            get.root.ids.board.ids.cash_count.text = f"+{final} $"
            get.root.ids.board.ids.crypto_count.text = f"-{final2} $"

            player_2_cash_count_g()

            anim = Animation(opacity=0, duration=0.01)
            anim += Animation(pos=(dp(1055), dp(457)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            anim += Animation(opacity=1, duration=0.05)
            anim += Animation(color=(1, 0, 0, 1))

            anim.start(get.root.ids.board.ids.crypto_count)

            Clock.schedule_once(sell, 2.5)

        def sell(*args):
            get.root.ids.board.ids.crypto_count.text = ""
            hide_cash_count()

            anim2 = Animation(opacity=0, duration=0.05)
            anim2 += Animation(size=(dp(0), dp(0)), pos=(dp(0), dp(0)), color=(0, 0, 0, 1), duration=0.05)

            anim2.start(get.root.ids.board.ids.crypto_count)

            all_money = int(get.root.ids.p2.ids.p2_money_stash.text) + float(get.root.ids.p2.ids.p2_crypto_stash.text)
            all_money = int(all_money)
            get.root.ids.p2.ids.p2_money_stash.text = f"{all_money}"
            get.root.ids.p2.ids.p2_crypto_stash.text = "0"

            money_update()

        res = round(float(get.root.ids.p2.ids.p2_crypto_stash.text), 0)
        something = float(player2)

        if res >= something:
            animate_sell_profit()
        elif res <= something:
            animate_sell_loss()


class ThiefField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos
        get.root.ids.f_shop.ids.anti_thief_active.opacity = 0

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos6_x and y == p1_pos6_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.player_1_show_buttons, 3.2)
                Clock.schedule_once(self.show_boxes, 3.2)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos5_x and y == p1_pos5_y:
                Clock.schedule_once(self.text, 0.7)
                Clock.schedule_once(self.player_1_show_buttons, 3.4)
                Clock.schedule_once(self.show_boxes, 3.4)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos4_x and y == p1_pos4_y:
                Clock.schedule_once(self.text, 0.9)
                Clock.schedule_once(self.player_1_show_buttons, 3.6)
                Clock.schedule_once(self.show_boxes, 3.6)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos2_x and y == p1_pos2_y:
                Clock.schedule_once(self.text, 1.3)
                Clock.schedule_once(self.player_1_show_buttons, 4)
                Clock.schedule_once(self.show_boxes, 4)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos1_x and y == p1_pos1_y:
                Clock.schedule_once(self.text, 1.5)
                Clock.schedule_once(self.player_1_show_buttons, 4.2)
                Clock.schedule_once(self.show_boxes, 4.2)

    @staticmethod
    def player_1_show_buttons(*args):
        get = App.get_running_app()

        label_anim = Animation(opacity=0, font_size=0, duration=0)
        label_anim.start(get.root.ids.board.ids.big)

        butt_1 = get.root.ids.f_thief.ids.thief_butt1
        butt_2 = get.root.ids.f_thief.ids.thief_butt2
        butt_3 = get.root.ids.f_thief.ids.thief_butt3

        butt_1.disabled = False
        butt_2.disabled = False
        butt_3.disabled = False

        butt_1_anim = Animation(opacity=0, duration=0.01)
        butt_1_anim += Animation(size=(dp(150), dp(40)), pos=(dp(400), dp(212)), duration=0.05)
        butt_1_anim += Animation(opacity=1, duration=1)

        butt_2_anim = Animation(opacity=0, duration=0.01)
        butt_2_anim += Animation(size=(dp(150), dp(40)), pos=(dp(585), dp(212)), duration=0.05)
        butt_2_anim += Animation(opacity=1, duration=1)

        butt_3_anim = Animation(opacity=0, duration=0.01)
        butt_3_anim += Animation(size=(dp(150), dp(40)), pos=(dp(767), dp(212)), duration=0.05)
        butt_3_anim += Animation(opacity=1, duration=1)

        butt_1_anim.start(butt_1)
        butt_2_anim.start(butt_2)
        butt_3_anim.start(butt_3)

    @staticmethod
    def player_1_thief_animations(*args):
        global random_thief

        get = App.get_running_app()

        def animate(*args):
            def drag_money(*args):
                drag_anim = Animation(pos=(dp(615), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=1.5)
                drag_anim.start(get.root.ids.board.ids.cash_count)

                drag_anim.bind(on_complete=subtract_money)

            def subtract_money(*args):
                get.root.ids.board.ids.cash_count.text = f"+{steal} $"
                change_anim = Animation(color=(0, 1, 0, 1), duration=0.05)
                change_anim.start(get.root.ids.board.ids.cash_count)

                change_anim.bind(on_complete=drag_money_2)

                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - steal}"
                money_update()

            def drag_money_2(*args):
                drag2_anim = Animation(pos=(dp(175), dp(559)), duration=1.5)
                drag2_anim.start(get.root.ids.board.ids.cash_count)

                Clock.schedule_once(add_money, 1.7)

            def add_money(*args):
                hide_cash_count()

                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + steal}"
                money_update()
                unblock_roll()
                Clock.schedule_once(reset_animations, 0.3)

            take_anim = Animation(opacity=0, duration=0.01)
            take_anim += Animation(pos=(dp(1055), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            take_anim += Animation(opacity=1, duration=0.05)
            take_anim += Animation(color=(1, 0, 0, 1))
            take_anim.start(get.root.ids.board.ids.cash_count)

            take_anim.bind(on_complete=drag_money)

        def reset_animations(*args):
            box_1 = get.root.ids.f_thief.ids.thief_box1
            box_2 = get.root.ids.f_thief.ids.thief_box2
            box_3 = get.root.ids.f_thief.ids.thief_box3

            butt_1 = get.root.ids.f_thief.ids.thief_butt1
            butt_2 = get.root.ids.f_thief.ids.thief_butt2
            butt_3 = get.root.ids.f_thief.ids.thief_butt3

            box_1.opacity = 0
            box_2.opacity = 0
            box_3.opacity = 0

            box_1.size = dp(0), dp(0)
            box_2.size = dp(0), dp(0)
            box_3.size = dp(0), dp(0)

            box_1.pos = dp(0), dp(0)
            box_2.pos = dp(0), dp(0)
            box_3.pos = dp(0), dp(0)

            butt_1.opacity = 0
            butt_2.opacity = 0
            butt_3.opacity = 0

            butt_1.size = dp(0), dp(0)
            butt_2.size = dp(0), dp(0)
            butt_3.size = dp(0), dp(0)

            butt_1.pos = dp(0), dp(0)
            butt_2.pos = dp(0), dp(0)
            butt_3.pos = dp(0), dp(0)

            get.root.ids.board.ids.big.opacity = 1
            get.root.ids.board.ids.big.font_size = 35

        if random_thief == 1:
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 5 / 100
                steal = round(steal)
                animate()
            else:
                reset_animations()
                unblock_roll()
                get.root.ids.board.ids.big.text = "Player 2 is immune to thief this turn!"

        if random_thief == 2:
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 10 / 100
                steal = round(steal)
                animate()
            else:
                reset_animations()
                unblock_roll()
                get.root.ids.board.ids.big.text = "Player 2 is immune to thief this turn!"

        if random_thief == 3:
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 15 / 100
                steal = round(steal)
                animate()
            else:
                reset_animations()
                unblock_roll()
                get.root.ids.board.ids.big.text = "Player 2 is immune to thief this turn!"

    def player_1_thief_option_1(self, *args):
        global random_thief

        get = App.get_running_app()
        random_thief = randint(1, 3)

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/percent_5.png'
        box_2.source = 'images/percent_10.png'
        box_3.source = 'images/percent_15.png'

        butt_1 = get.root.ids.f_thief.ids.thief_butt1
        butt_2 = get.root.ids.f_thief.ids.thief_butt2
        butt_3 = get.root.ids.f_thief.ids.thief_butt3

        butt_1.disabled = True
        butt_2.disabled = True
        butt_3.disabled = True

        if random_thief == 1:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 5 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(585), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_1.pos = dp(400), dp(282)
            box_2.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(585), dp(282)

        if random_thief == 2:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 10 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(585), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_2.pos = dp(400), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(585), dp(282)

        if random_thief == 3:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 15 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(585), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_3.pos = dp(400), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_2.pos = dp(767), dp(282)
            else:
                box_2.pos = dp(585), dp(282)

        Clock.schedule_once(self.player_1_thief_animations, 0.5)

    def player_1_thief_option_2(self, *args):
        global random_thief

        get = App.get_running_app()
        random_thief = randint(1, 3)

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/percent_5.png'
        box_2.source = 'images/percent_10.png'
        box_3.source = 'images/percent_15.png'

        butt_1 = get.root.ids.f_thief.ids.thief_butt1
        butt_2 = get.root.ids.f_thief.ids.thief_butt2
        butt_3 = get.root.ids.f_thief.ids.thief_butt3

        butt_1.disabled = True
        butt_2.disabled = True
        butt_3.disabled = True

        if random_thief == 1:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 5 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_1.pos = dp(585), dp(282)
            box_2.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 2:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 10 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_2.pos = dp(585), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 3:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 15 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_3.pos = dp(585), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_2.pos = dp(767), dp(282)
            else:
                box_2.pos = dp(400), dp(282)

        Clock.schedule_once(self.player_1_thief_animations, 0.5)

    def player_1_thief_option_3(self, *args):
        global random_thief

        get = App.get_running_app()
        random_thief = randint(1, 3)

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/percent_5.png'
        box_2.source = 'images/percent_10.png'
        box_3.source = 'images/percent_15.png'

        butt_1 = get.root.ids.f_thief.ids.thief_butt1
        butt_2 = get.root.ids.f_thief.ids.thief_butt2
        butt_3 = get.root.ids.f_thief.ids.thief_butt3

        butt_1.disabled = True
        butt_2.disabled = True
        butt_3.disabled = True

        if random_thief == 1:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 5 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(585), dp(282))
            number = randint(0, 1)

            box_1.pos = dp(767), dp(282)
            box_2.pos = position[number]

            if number == 0:
                box_3.pos = dp(585), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 2:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 10 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(585), dp(282))
            number = randint(0, 1)

            box_2.pos = dp(767), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_3.pos = dp(585), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 3:
            steal = int(get.root.ids.p2.ids.p2_money_stash.text) * 15 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active_2.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(585), dp(282))
            number = randint(0, 1)

            box_3.pos = dp(767), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_2.pos = dp(585), dp(282)
            else:
                box_2.pos = dp(400), dp(282)

        Clock.schedule_once(self.player_1_thief_animations, 0.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos
        get.root.ids.f_shop.ids.anti_thief_active_2.opacity = 0

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos6_x and y == p2_pos6_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.player_2_show_buttons, 3.2)
                Clock.schedule_once(self.show_boxes, 3.2)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos5_x and y == p2_pos5_y:
                Clock.schedule_once(self.text, 0.7)
                Clock.schedule_once(self.player_2_show_buttons, 3.4)
                Clock.schedule_once(self.show_boxes, 3.4)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos4_x and y == p2_pos4_y:
                Clock.schedule_once(self.text, 0.9)
                Clock.schedule_once(self.player_2_show_buttons, 3.6)
                Clock.schedule_once(self.show_boxes, 3.6)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos2_x and y == p2_pos2_y:
                Clock.schedule_once(self.text, 1.3)
                Clock.schedule_once(self.player_2_show_buttons, 4)
                Clock.schedule_once(self.show_boxes, 4)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos1_x and y == p2_pos1_y:
                Clock.schedule_once(self.text, 1.5)
                Clock.schedule_once(self.player_2_show_buttons, 4.2)
                Clock.schedule_once(self.show_boxes, 4.2)

    @staticmethod
    def player_2_show_buttons(*args):
        get = App.get_running_app()

        label_anim = Animation(opacity=0, font_size=0, duration=0)
        label_anim.start(get.root.ids.board.ids.big)

        butt_1 = get.root.ids.f_thief.ids.thief_butt4
        butt_2 = get.root.ids.f_thief.ids.thief_butt5
        butt_3 = get.root.ids.f_thief.ids.thief_butt6

        butt_1.disabled = False
        butt_2.disabled = False
        butt_3.disabled = False

        butt_1_anim = Animation(opacity=0, duration=0.01)
        butt_1_anim += Animation(size=(dp(150), dp(40)), pos=(dp(400), dp(212)), duration=0.05)
        butt_1_anim += Animation(opacity=1, duration=1)

        butt_2_anim = Animation(opacity=0, duration=0.01)
        butt_2_anim += Animation(size=(dp(150), dp(40)), pos=(dp(585), dp(212)), duration=0.05)
        butt_2_anim += Animation(opacity=1, duration=1)

        butt_3_anim = Animation(opacity=0, duration=0.01)
        butt_3_anim += Animation(size=(dp(150), dp(40)), pos=(dp(767), dp(212)), duration=0.05)
        butt_3_anim += Animation(opacity=1, duration=1)

        butt_1_anim.start(butt_1)
        butt_2_anim.start(butt_2)
        butt_3_anim.start(butt_3)

    @staticmethod
    def player_2_thief_animations(*args):
        global random_thief

        get = App.get_running_app()

        def animate(*args):
            def drag_money(*args):
                drag_anim = Animation(pos=(dp(615), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=1.5)
                drag_anim.start(get.root.ids.board.ids.cash_count)

                drag_anim.bind(on_complete=subtract_money)

            def subtract_money(*args):
                get.root.ids.board.ids.cash_count.text = f"+{steal} $"
                change_anim = Animation(color=(0, 1, 0, 1), duration=0.05)
                change_anim.start(get.root.ids.board.ids.cash_count)

                change_anim.bind(on_complete=drag_money_2)

                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - steal}"
                money_update()

            def drag_money_2(*args):
                drag2_anim = Animation(pos=(dp(1055), dp(559)), duration=1.5)
                drag2_anim.start(get.root.ids.board.ids.cash_count)

                Clock.schedule_once(add_money, 1.7)

            def add_money(*args):
                hide_cash_count()
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + steal}"
                money_update()
                unblock_roll()
                Clock.schedule_once(reset_animations, 0.3)

            take_anim = Animation(opacity=0, duration=0.01)
            take_anim += Animation(pos=(dp(175), dp(559)), size=(dp(100), dp(50)), font_size=25, duration=0.05)
            take_anim += Animation(opacity=1, duration=0.05)
            take_anim += Animation(color=(1, 0, 0, 1))
            take_anim.start(get.root.ids.board.ids.cash_count)

            take_anim.bind(on_complete=drag_money)

        def reset_animations(*args):
            box_1 = get.root.ids.f_thief.ids.thief_box1
            box_2 = get.root.ids.f_thief.ids.thief_box2
            box_3 = get.root.ids.f_thief.ids.thief_box3

            butt_1 = get.root.ids.f_thief.ids.thief_butt4
            butt_2 = get.root.ids.f_thief.ids.thief_butt5
            butt_3 = get.root.ids.f_thief.ids.thief_butt6

            box_1.opacity = 0
            box_2.opacity = 0
            box_3.opacity = 0

            box_1.size = dp(0), dp(0)
            box_2.size = dp(0), dp(0)
            box_3.size = dp(0), dp(0)

            box_1.pos = dp(0), dp(0)
            box_2.pos = dp(0), dp(0)
            box_3.pos = dp(0), dp(0)

            butt_1.opacity = 0
            butt_2.opacity = 0
            butt_3.opacity = 0

            butt_1.size = dp(0), dp(0)
            butt_2.size = dp(0), dp(0)
            butt_3.size = dp(0), dp(0)

            butt_1.pos = dp(0), dp(0)
            butt_2.pos = dp(0), dp(0)
            butt_3.pos = dp(0), dp(0)

            get.root.ids.board.ids.big.opacity = 1
            get.root.ids.board.ids.big.font_size = 35

        if random_thief == 1:
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 5 / 100
                steal = round(steal)
            else:
                steal = 0
            animate()

        if random_thief == 2:
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 10 / 100
                steal = round(steal)
            else:
                steal = 0
            animate()

        if random_thief == 3:
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 15 / 100
                steal = round(steal)
            else:
                steal = 0
            animate()

    def player_2_thief_option_1(self, *args):
        global random_thief

        get = App.get_running_app()
        random_thief = randint(1, 3)

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/percent_5.png'
        box_2.source = 'images/percent_10.png'
        box_3.source = 'images/percent_15.png'

        butt_1 = get.root.ids.f_thief.ids.thief_butt4
        butt_2 = get.root.ids.f_thief.ids.thief_butt5
        butt_3 = get.root.ids.f_thief.ids.thief_butt6

        butt_1.disabled = True
        butt_2.disabled = True
        butt_3.disabled = True

        if random_thief == 1:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 5 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(585), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_1.pos = dp(400), dp(282)
            box_2.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(585), dp(282)

        if random_thief == 2:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 10 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(585), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_2.pos = dp(400), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(585), dp(282)

        if random_thief == 3:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 15 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(585), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_3.pos = dp(400), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_2.pos = dp(767), dp(282)
            else:
                box_2.pos = dp(585), dp(282)

        Clock.schedule_once(self.player_2_thief_animations, 0.5)

    def player_2_thief_option_2(self, *args):
        global random_thief

        get = App.get_running_app()
        random_thief = randint(1, 3)

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/percent_5.png'
        box_2.source = 'images/percent_10.png'
        box_3.source = 'images/percent_15.png'

        butt_1 = get.root.ids.f_thief.ids.thief_butt4
        butt_2 = get.root.ids.f_thief.ids.thief_butt5
        butt_3 = get.root.ids.f_thief.ids.thief_butt6

        butt_1.disabled = True
        butt_2.disabled = True
        butt_3.disabled = True

        if random_thief == 1:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 5 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_1.pos = dp(585), dp(282)
            box_2.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 2:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 10 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_2.pos = dp(585), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_3.pos = dp(767), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 3:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 15 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(767), dp(282))
            number = randint(0, 1)

            box_3.pos = dp(585), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_2.pos = dp(767), dp(282)
            else:
                box_2.pos = dp(400), dp(282)

        Clock.schedule_once(self.player_2_thief_animations, 0.5)

    def player_2_thief_option_3(self, *args):
        global random_thief

        get = App.get_running_app()
        random_thief = randint(1, 3)

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/percent_5.png'
        box_2.source = 'images/percent_10.png'
        box_3.source = 'images/percent_15.png'

        butt_1 = get.root.ids.f_thief.ids.thief_butt4
        butt_2 = get.root.ids.f_thief.ids.thief_butt5
        butt_3 = get.root.ids.f_thief.ids.thief_butt6

        butt_1.disabled = True
        butt_2.disabled = True
        butt_3.disabled = True

        if random_thief == 1:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 5 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(585), dp(282))
            number = randint(0, 1)

            box_1.pos = dp(767), dp(282)
            box_2.pos = position[number]

            if number == 0:
                box_3.pos = dp(585), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 2:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 10 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(585), dp(282))
            number = randint(0, 1)

            box_2.pos = dp(767), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_3.pos = dp(585), dp(282)
            else:
                box_3.pos = dp(400), dp(282)

        if random_thief == 3:
            steal = int(get.root.ids.p1.ids.p1_money_stash.text) * 15 / 100
            steal = round(steal)
            if not get.root.ids.f_shop.ids.anti_thief_active.opacity == 1:
                get.root.ids.board.ids.cash_count.text = f"-{steal} $"
            else:
                get.root.ids.board.ids.cash_count.text = f"-{0} $"
            get.root.ids.board.ids.big.opacity = 0

            position = (dp(400), dp(282)), (dp(585), dp(282))
            number = randint(0, 1)

            box_3.pos = dp(767), dp(282)
            box_1.pos = position[number]

            if number == 0:
                box_2.pos = dp(585), dp(282)
            else:
                box_2.pos = dp(400), dp(282)

        Clock.schedule_once(self.player_2_thief_animations, 0.5)

    # Both Players - General Functions

    @staticmethod
    def text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = thief_fields

    @staticmethod
    def show_boxes(*args):
        get = App.get_running_app()

        box_1 = get.root.ids.f_thief.ids.thief_box1
        box_2 = get.root.ids.f_thief.ids.thief_box2
        box_3 = get.root.ids.f_thief.ids.thief_box3

        box_1.source = 'images/bag.png'
        box_2.source = 'images/bag.png'
        box_3.source = 'images/bag.png'

        box_1_anim = Animation(opacity=0, duration=0.01)
        box_1_anim += Animation(size=(dp(150), dp(170)), pos=(dp(400), dp(282)), duration=0.05)
        box_1_anim += Animation(opacity=1, duration=1)

        box_2_anim = Animation(opacity=0, duration=0.01)
        box_2_anim += Animation(size=(dp(150), dp(170)), pos=(dp(585), dp(282)), duration=0.05)
        box_2_anim += Animation(opacity=1, duration=1)

        box_3_anim = Animation(opacity=0, duration=0.01)
        box_3_anim += Animation(size=(dp(150), dp(170)), pos=(dp(767), dp(282)), duration=0.05)
        box_3_anim += Animation(opacity=1, duration=1)

        box_1_anim.start(box_1)
        box_2_anim.start(box_2)
        box_3_anim.start(box_3)


class ChanceField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos7_x and y == p1_pos7_y:
                Clock.schedule_once(self.player_1_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos6_x and y == p1_pos6_y:
                Clock.schedule_once(self.player_1_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos5_x and y == p1_pos5_y:
                Clock.schedule_once(self.player_1_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos4_x and y == p1_pos4_y:
                Clock.schedule_once(self.player_1_main, 1.1)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos2_x and y == p1_pos2_y:
                Clock.schedule_once(self.player_1_main, 1.5)

    @staticmethod
    def player_1_main(*args):
        get = App.get_running_app()
        random_luck = randint(0, 10)
        get.root.ids.board.ids.big.font_size = 40
        get.root.ids.board.ids.big.valign = "middle"

        def money(*args):
            if random_luck == 0 or random_luck == 2:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 25}"
            if random_luck == 1 or random_luck == 9:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 30}"
            if random_luck == 3:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 50}"
            if random_luck == 4:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 40}"
            if random_luck == 5:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 30}"
            if random_luck == 6:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 20}"
            if random_luck == 7:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 10}"
            if random_luck == 8:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 100}"
            if random_luck == 10:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 100}"
            unblock_roll()

        if random_luck == 0:
            get.root.ids.board.ids.big.text = money_luck[0]
            get.root.ids.board.ids.cash_count.text = "-25 $"
            player_1_cash_count_r()

        if random_luck == 1:
            get.root.ids.board.ids.big.text = money_luck[1]
            get.root.ids.board.ids.cash_count.text = "+30 $"
            player_1_cash_count_g()

        if random_luck == 2:
            get.root.ids.board.ids.big.text = money_luck[2]
            get.root.ids.board.ids.cash_count.text = "-25 $"
            player_1_cash_count_r()

        if random_luck == 3:
            get.root.ids.board.ids.big.text = money_luck[3]
            get.root.ids.board.ids.cash_count.text = "+50 $"
            player_1_cash_count_g()

        if random_luck == 4:
            get.root.ids.board.ids.big.text = money_luck[4]
            get.root.ids.board.ids.cash_count.text = "-40 $"
            player_1_cash_count_r()

        if random_luck == 5:
            get.root.ids.board.ids.big.text = money_luck[5]
            get.root.ids.board.ids.cash_count.text = "-30 $"
            player_1_cash_count_r()

        if random_luck == 6:
            get.root.ids.board.ids.big.text = money_luck[6]
            get.root.ids.board.ids.cash_count.text = "+20 $"
            player_1_cash_count_g()

        if random_luck == 7:
            get.root.ids.board.ids.big.text = money_luck[7]
            get.root.ids.board.ids.cash_count.text = "+10 $"
            player_1_cash_count_g()

        if random_luck == 8:
            get.root.ids.board.ids.big.text = money_luck[8]
            get.root.ids.board.ids.cash_count.text = "-100 $"
            player_1_cash_count_r()

        if random_luck == 9:
            get.root.ids.board.ids.big.text = money_luck[9]
            get.root.ids.board.ids.cash_count.text = "+30 $"
            player_1_cash_count_g()

        if random_luck == 10:
            get.root.ids.board.ids.big.text = money_luck[10]
            get.root.ids.board.ids.cash_count.text = "+100 $"
            player_1_cash_count_g()

        Clock.schedule_once(hide_cash_count, 2.5)
        Clock.schedule_once(money, 2.5)
        Clock.schedule_once(money_update, 2.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos7_x and y == p2_pos7_y:
                Clock.schedule_once(self.player_2_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos6_x and y == p2_pos6_y:
                Clock.schedule_once(self.player_2_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos5_x and y == p2_pos5_y:
                Clock.schedule_once(self.player_2_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos4_x and y == p2_pos4_y:
                Clock.schedule_once(self.player_2_main, 1.1)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos2_x and y == p2_pos2_y:
                Clock.schedule_once(self.player_2_main, 1.5)

    @staticmethod
    def player_2_main(*args):
        get = App.get_running_app()
        random_luck = randint(0, 10)
        get.root.ids.board.ids.big.font_size = 40
        get.root.ids.board.ids.big.valign = "middle"

        def money(*args):
            if random_luck == 0 or random_luck == 2:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 25}"
            if random_luck == 1 or random_luck == 9:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 30}"
            if random_luck == 3:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 50}"
            if random_luck == 4:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 40}"
            if random_luck == 5:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 30}"
            if random_luck == 6:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 20}"
            if random_luck == 7:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 10}"
            if random_luck == 8:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 100}"
            if random_luck == 10:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 100}"
            unblock_roll()

        if random_luck == 0:
            get.root.ids.board.ids.big.text = money_luck[0]
            get.root.ids.board.ids.cash_count.text = "-25 $"
            player_2_cash_count_r()

        if random_luck == 1:
            get.root.ids.board.ids.big.text = money_luck[1]
            get.root.ids.board.ids.cash_count.text = "+30 $"
            player_2_cash_count_g()

        if random_luck == 2:
            get.root.ids.board.ids.big.text = money_luck[2]
            get.root.ids.board.ids.cash_count.text = "-25 $"
            player_2_cash_count_r()

        if random_luck == 3:
            get.root.ids.board.ids.big.text = money_luck[3]
            get.root.ids.board.ids.cash_count.text = "+50 $"
            player_2_cash_count_g()

        if random_luck == 4:
            get.root.ids.board.ids.big.text = money_luck[4]
            get.root.ids.board.ids.cash_count.text = "-40 $"
            player_2_cash_count_r()

        if random_luck == 5:
            get.root.ids.board.ids.big.text = money_luck[5]
            get.root.ids.board.ids.cash_count.text = "-30 $"
            player_2_cash_count_r()

        if random_luck == 6:
            get.root.ids.board.ids.big.text = money_luck[6]
            get.root.ids.board.ids.cash_count.text = "+20 $"
            player_2_cash_count_g()

        if random_luck == 7:
            get.root.ids.board.ids.big.text = money_luck[7]
            get.root.ids.board.ids.cash_count.text = "+10 $"
            player_2_cash_count_g()

        if random_luck == 8:
            get.root.ids.board.ids.big.text = money_luck[8]
            get.root.ids.board.ids.cash_count.text = "-100 $"
            player_2_cash_count_r()

        if random_luck == 9:
            get.root.ids.board.ids.big.text = money_luck[9]
            get.root.ids.board.ids.cash_count.text = "+30 $"
            player_2_cash_count_g()

        if random_luck == 10:
            get.root.ids.board.ids.big.text = money_luck[10]
            get.root.ids.board.ids.cash_count.text = "+100 $"
            player_2_cash_count_g()

        Clock.schedule_once(hide_cash_count, 2.5)
        Clock.schedule_once(money, 2.5)
        Clock.schedule_once(money_update, 2.5)


class EiffelTowerField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos8_x and y == p1_pos8_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos7_x and y == p1_pos7_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos6_x and y == p1_pos6_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos5_x and y == p1_pos5_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos4_x and y == p1_pos4_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_9.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_9.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_9.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = eiffel_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Eiffel Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-200 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 200}"
        get.root.ids.board.ids.field_9.background_color = player_1_color
        get.root.ids.board.ids.field_9.text = "purple"

        money_update()
        unblock_roll()

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 0:
            fee = 50
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 1:
            fee = 80
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 2:
            fee = 115
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 3:
            fee = 150
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money, 1.5)

    def player_1_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 0:
            fee = 50
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 1:
            fee = 80
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 2:
            fee = 115
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 3:
            fee = 150
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) - fee)}"
        player_1_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_1_move_label, 1.5)

    def player_1_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money, 1)

    def player_2_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 0:
            fee = 50
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 1:
            fee = 80
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 2:
            fee = 115
        if int(get.root.ids.f_shop.ids.eiffel_count_2_2.text) == 3:
            fee = 150
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)
        Clock.schedule_once(self.end_anim, 1.8)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos8_x and y == p2_pos8_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos7_x and y == p2_pos7_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos6_x and y == p2_pos6_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos5_x and y == p2_pos5_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos4_x and y == p2_pos4_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_9.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_9.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_9.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = eiffel_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Eiffel Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-200 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 200}"
        get.root.ids.board.ids.field_9.background_color = player_2_color
        get.root.ids.board.ids.field_9.text = "green"
        money_update()
        unblock_roll()

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        unblock_roll()

    def player_2_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 0:
            fee = 50
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 1:
            fee = 80
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 2:
            fee = 115
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 3:
            fee = 150
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money, 1.5)

    def player_2_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 0:
            fee = 50
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 1:
            fee = 80
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 2:
            fee = 115
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 3:
            fee = 150
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) - fee)}"
        player_2_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_2_move_label, 1.5)

    def player_2_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money, 1)

    def player_1_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 0:
            fee = 50
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 1:
            fee = 80
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 2:
            fee = 115
        if int(get.root.ids.f_shop.ids.eiffel_count_2.text) == 3:
            fee = 150
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)
        Clock.schedule_once(self.end_anim, 1.8)

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class BrainMemoryField(Widget):

    countdown = NumericProperty(33)
    countdown_2 = NumericProperty(23)

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos
        get.root.ids.p1.ids.turn_1.active = True
        get.root.ids.p2.ids.turn_2.active = False

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos9_x and y == p1_pos9_y:
                Clock.schedule_once(self.brain_memory, 0.5)
            if x == p1_pos27_x and y == p1_pos27_y:
                Clock.schedule_once(self.brain_memory, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos8_x and y == p1_pos8_y:
                Clock.schedule_once(self.brain_memory, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos7_x and y == p1_pos7_y:
                Clock.schedule_once(self.brain_memory, 0.9)
            if x == p1_pos25_x and y == p1_pos25_y:
                Clock.schedule_once(self.brain_memory, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos6_x and y == p1_pos6_y:
                Clock.schedule_once(self.brain_memory, 1.1)
            if x == p1_pos24_x and y == p1_pos24_y:
                Clock.schedule_once(self.brain_memory, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos5_x and y == p1_pos5_y:
                Clock.schedule_once(self.brain_memory, 1.3)
            if x == p1_pos23_x and y == p1_pos23_y:
                Clock.schedule_once(self.brain_memory, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos4_x and y == p1_pos4_y:
                Clock.schedule_once(self.brain_memory, 1.5)
            if x == p1_pos22_x and y == p1_pos22_y:
                Clock.schedule_once(self.brain_memory, 1.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos
        get.root.ids.p1.ids.turn_1.active = False
        get.root.ids.p2.ids.turn_2.active = True

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos9_x and y == p2_pos9_y:
                Clock.schedule_once(self.brain_memory, 0.5)
            if x == p2_pos27_x and y == p2_pos27_y:
                Clock.schedule_once(self.brain_memory, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos8_x and y == p2_pos8_y:
                Clock.schedule_once(self.brain_memory, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos7_x and y == p2_pos7_y:
                Clock.schedule_once(self.brain_memory, 0.9)
            if x == p2_pos25_x and y == p2_pos25_y:
                Clock.schedule_once(self.brain_memory, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos6_x and y == p2_pos6_y:
                Clock.schedule_once(self.brain_memory, 1.1)
            if x == p2_pos24_x and y == p2_pos24_y:
                Clock.schedule_once(self.brain_memory, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos5_x and y == p2_pos5_y:
                Clock.schedule_once(self.brain_memory, 1.3)
            if x == p2_pos23_x and y == p2_pos23_y:
                Clock.schedule_once(self.brain_memory, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos4_x and y == p2_pos4_y:
                Clock.schedule_once(self.brain_memory, 1.5)
            if x == p2_pos22_x and y == p2_pos22_y:
                Clock.schedule_once(self.brain_memory, 1.5)

    # Both Players - General Functions

    def brain_memory(self, *args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos
        x1, y1 = get.root.ids.p2.ids.player_2.pos

        self.countdown = 33
        self.countdown_2 = 23

        butt_1 = get.root.ids.f_brain.ids.brain_1
        butt_2 = get.root.ids.f_brain.ids.brain_2
        butt_3 = get.root.ids.f_brain.ids.brain_3
        butt_4 = get.root.ids.f_brain.ids.brain_4
        butt_5 = get.root.ids.f_brain.ids.brain_5
        butt_6 = get.root.ids.f_brain.ids.brain_6
        butt_7 = get.root.ids.f_brain.ids.brain_7
        butt_8 = get.root.ids.f_brain.ids.brain_8
        butt_9 = get.root.ids.f_brain.ids.brain_9
        butt_10 = get.root.ids.f_brain.ids.brain_10
        butt_11 = get.root.ids.f_brain.ids.brain_11
        butt_12 = get.root.ids.f_brain.ids.brain_12
        butt_13 = get.root.ids.f_brain.ids.brain_13
        butt_14 = get.root.ids.f_brain.ids.brain_14
        butt_15 = get.root.ids.f_brain.ids.brain_15
        butt_16 = get.root.ids.f_brain.ids.brain_16
        butt_17 = get.root.ids.f_brain.ids.brain_17
        butt_18 = get.root.ids.f_brain.ids.brain_18
        butt_19 = get.root.ids.f_brain.ids.brain_19
        butt_20 = get.root.ids.f_brain.ids.brain_20
        butt_21 = get.root.ids.f_brain.ids.brain_21
        butt_22 = get.root.ids.f_brain.ids.brain_22
        butt_23 = get.root.ids.f_brain.ids.brain_23
        butt_24 = get.root.ids.f_brain.ids.brain_24
        butt_25 = get.root.ids.f_brain.ids.brain_25
        butt_26 = get.root.ids.f_brain.ids.brain_26
        butt_27 = get.root.ids.f_brain.ids.brain_27
        butt_28 = get.root.ids.f_brain.ids.brain_28
        butt_29 = get.root.ids.f_brain.ids.brain_29
        butt_30 = get.root.ids.f_brain.ids.brain_30
        butt_31 = get.root.ids.f_brain.ids.brain_31
        butt_32 = get.root.ids.f_brain.ids.brain_32
        butt_33 = get.root.ids.f_brain.ids.brain_33
        butt_34 = get.root.ids.f_brain.ids.brain_34
        butt_35 = get.root.ids.f_brain.ids.brain_35
        butt_36 = get.root.ids.f_brain.ids.brain_36
        butt_37 = get.root.ids.f_brain.ids.brain_37
        butt_38 = get.root.ids.f_brain.ids.brain_38
        butt_39 = get.root.ids.f_brain.ids.brain_39
        butt_40 = get.root.ids.f_brain.ids.brain_40

        def show_instructions(*args):
            if x == p1_pos10_x and y == p1_pos10_y:
                if get.root.ids.p1.ids.turn_1.active:
                    get.root.ids.board.ids.big.text = brain_fields
                    get.root.ids.board.ids.big.font_size = 30
                    get.root.ids.board.ids.big.valign = "middle"
                    Clock.schedule_once(show_pattern, 5)
            if x == p1_pos28_x and y == p1_pos28_y:
                if get.root.ids.p1.ids.turn_1.active:
                    get.root.ids.board.ids.big.text = brain_money_fields
                    get.root.ids.board.ids.big.font_size = 30
                    get.root.ids.board.ids.big.valign = "middle"
                    Clock.schedule_once(show_pattern, 5)

            if x1 == p2_pos10_x and y1 == p2_pos10_y:
                if get.root.ids.p2.ids.turn_2.active:
                    get.root.ids.board.ids.big.text = brain_fields
                    get.root.ids.board.ids.big.font_size = 30
                    get.root.ids.board.ids.big.valign = "middle"
                    Clock.schedule_once(show_pattern, 5)
            if x1 == p2_pos28_x and y1 == p2_pos28_y:
                if get.root.ids.p2.ids.turn_2.active:
                    get.root.ids.board.ids.big.text = brain_money_fields
                    get.root.ids.board.ids.big.font_size = 30
                    get.root.ids.board.ids.big.valign = "middle"
                    Clock.schedule_once(show_pattern, 5)

        def show_pattern(*args):
            get.root.ids.board.ids.big.text = "You have          seconds to memorize the pattern!"
            get.root.ids.board.ids.big.pos = dp(385), dp(423)
            get.root.ids.board.ids.big.size = dp(545), dp(50)
            get.root.ids.board.ids.count_down.size = dp(60), dp(50)
            get.root.ids.board.ids.count_down.pos = dp(496), dp(423)
            get.root.ids.board.ids.big.font_size = 25
            Clock.schedule_once(random_pattern, 1)

        def random_pattern(*args):

            num_1 = randint(0, 1)
            num_2 = randint(0, 1)
            num_3 = randint(0, 1)
            num_4 = randint(0, 1)
            num_5 = randint(0, 1)
            num_6 = randint(0, 1)
            num_7 = randint(0, 1)
            num_8 = randint(0, 1)
            num_9 = randint(0, 1)
            num_10 = randint(0, 1)
            num_11 = randint(0, 1)
            num_12 = randint(0, 1)
            num_13 = randint(0, 1)
            num_14 = randint(0, 1)
            num_15 = randint(0, 1)
            num_16 = randint(0, 1)
            num_17 = randint(0, 1)
            num_18 = randint(0, 1)
            num_19 = randint(0, 1)
            num_20 = randint(0, 1)
            num_21 = randint(0, 1)
            num_22 = randint(0, 1)
            num_23 = randint(0, 1)
            num_24 = randint(0, 1)
            num_25 = randint(0, 1)
            num_26 = randint(0, 1)
            num_27 = randint(0, 1)
            num_28 = randint(0, 1)
            num_29 = randint(0, 1)
            num_30 = randint(0, 1)
            num_31 = randint(0, 1)
            num_32 = randint(0, 1)
            num_33 = randint(0, 1)
            num_34 = randint(0, 1)
            num_35 = randint(0, 1)
            num_36 = randint(0, 1)
            num_37 = randint(0, 1)
            num_38 = randint(0, 1)
            num_39 = randint(0, 1)
            num_40 = randint(0, 1)

            butt_1_anim = Animation(pos=(dp(385), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_1_anim += Animation(opacity=1, duration=0.05)
            if num_1 == 0:
                butt_1_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_1_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_2_anim = Animation(pos=(dp(440), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_2_anim += Animation(opacity=1, duration=0.05)
            if num_2 == 0:
                butt_2_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_2_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_3_anim = Animation(pos=(dp(495), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_3_anim += Animation(opacity=1, duration=0.05)
            if num_3 == 0:
                butt_3_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_3_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_4_anim = Animation(pos=(dp(550), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_4_anim += Animation(opacity=1, duration=0.05)
            if num_4 == 0:
                butt_4_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_4_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_5_anim = Animation(pos=(dp(605), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_5_anim += Animation(opacity=1, duration=0.05)
            if num_5 == 0:
                butt_5_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_5_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_6_anim = Animation(pos=(dp(660), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_6_anim += Animation(opacity=1, duration=0.05)
            if num_6 == 0:
                butt_6_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_6_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_7_anim = Animation(pos=(dp(715), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_7_anim += Animation(opacity=1, duration=0.05)
            if num_7 == 0:
                butt_7_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_7_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_8_anim = Animation(pos=(dp(770), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_8_anim += Animation(opacity=1, duration=0.05)
            if num_8 == 0:
                butt_8_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_8_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_9_anim = Animation(pos=(dp(825), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_9_anim += Animation(opacity=1, duration=0.05)
            if num_9 == 0:
                butt_9_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_9_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_10_anim = Animation(pos=(dp(880), dp(203)), size=(dp(50), dp(50)), duration=0.05)
            butt_10_anim += Animation(opacity=1, duration=0.05)
            if num_10 == 0:
                butt_10_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_10_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_11_anim = Animation(pos=(dp(385), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_11_anim += Animation(opacity=1, duration=0.05)
            if num_11 == 0:
                butt_11_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_11_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_12_anim = Animation(pos=(dp(440), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_12_anim += Animation(opacity=1, duration=0.05)
            if num_12 == 0:
                butt_12_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_12_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_13_anim = Animation(pos=(dp(495), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_13_anim += Animation(opacity=1, duration=0.05)
            if num_13 == 0:
                butt_13_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_13_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_14_anim = Animation(pos=(dp(550), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_14_anim += Animation(opacity=1, duration=0.05)
            if num_14 == 0:
                butt_14_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_14_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_15_anim = Animation(pos=(dp(605), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_15_anim += Animation(opacity=1, duration=0.05)
            if num_15 == 0:
                butt_15_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_15_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_16_anim = Animation(pos=(dp(660), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_16_anim += Animation(opacity=1, duration=0.05)
            if num_16 == 0:
                butt_16_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_16_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_17_anim = Animation(pos=(dp(715), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_17_anim += Animation(opacity=1, duration=0.05)
            if num_17 == 0:
                butt_17_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_17_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_18_anim = Animation(pos=(dp(770), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_18_anim += Animation(opacity=1, duration=0.05)
            if num_18 == 0:
                butt_18_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_18_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_19_anim = Animation(pos=(dp(825), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_19_anim += Animation(opacity=1, duration=0.05)
            if num_19 == 0:
                butt_19_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_19_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_20_anim = Animation(pos=(dp(880), dp(258)), size=(dp(50), dp(50)), duration=0.05)
            butt_20_anim += Animation(opacity=1, duration=0.05)
            if num_20 == 0:
                butt_20_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_20_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_21_anim = Animation(pos=(dp(385), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_21_anim += Animation(opacity=1, duration=0.05)
            if num_21 == 0:
                butt_21_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_21_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_22_anim = Animation(pos=(dp(440), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_22_anim += Animation(opacity=1, duration=0.05)
            if num_22 == 0:
                butt_22_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_22_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_23_anim = Animation(pos=(dp(495), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_23_anim += Animation(opacity=1, duration=0.05)
            if num_23 == 0:
                butt_23_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_23_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_24_anim = Animation(pos=(dp(550), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_24_anim += Animation(opacity=1, duration=0.05)
            if num_24 == 0:
                butt_24_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_24_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_25_anim = Animation(pos=(dp(605), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_25_anim += Animation(opacity=1, duration=0.05)
            if num_25 == 0:
                butt_25_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_25_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_26_anim = Animation(pos=(dp(660), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_26_anim += Animation(opacity=1, duration=0.05)
            if num_26 == 0:
                butt_26_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_26_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_27_anim = Animation(pos=(dp(715), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_27_anim += Animation(opacity=1, duration=0.05)
            if num_27 == 0:
                butt_27_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_27_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_28_anim = Animation(pos=(dp(770), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_28_anim += Animation(opacity=1, duration=0.05)
            if num_28 == 0:
                butt_28_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_28_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_29_anim = Animation(pos=(dp(825), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_29_anim += Animation(opacity=1, duration=0.05)
            if num_29 == 0:
                butt_29_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_29_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_30_anim = Animation(pos=(dp(880), dp(313)), size=(dp(50), dp(50)), duration=0.05)
            butt_30_anim += Animation(opacity=1, duration=0.05)
            if num_30 == 0:
                butt_30_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_30_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_31_anim = Animation(pos=(dp(385), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_31_anim += Animation(opacity=1, duration=0.05)
            if num_31 == 0:
                butt_31_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_31_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_32_anim = Animation(pos=(dp(440), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_32_anim += Animation(opacity=1, duration=0.05)
            if num_32 == 0:
                butt_32_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_32_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_33_anim = Animation(pos=(dp(495), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_33_anim += Animation(opacity=1, duration=0.05)
            if num_33 == 0:
                butt_33_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_33_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_34_anim = Animation(pos=(dp(550), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_34_anim += Animation(opacity=1, duration=0.05)
            if num_34 == 0:
                butt_34_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_34_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_35_anim = Animation(pos=(dp(605), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_35_anim += Animation(opacity=1, duration=0.05)
            if num_35 == 0:
                butt_35_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_35_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_36_anim = Animation(pos=(dp(660), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_36_anim += Animation(opacity=1, duration=0.05)
            if num_36 == 0:
                butt_36_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_36_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_37_anim = Animation(pos=(dp(715), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_37_anim += Animation(opacity=1, duration=0.05)
            if num_37 == 0:
                butt_37_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_37_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_38_anim = Animation(pos=(dp(770), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_38_anim += Animation(opacity=1, duration=0.05)
            if num_38 == 0:
                butt_38_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_38_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_39_anim = Animation(pos=(dp(825), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_39_anim += Animation(opacity=1, duration=0.05)
            if num_39 == 0:
                butt_39_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_39_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_40_anim = Animation(pos=(dp(880), dp(368)), size=(dp(50), dp(50)), duration=0.05)
            butt_40_anim += Animation(opacity=1, duration=0.05)
            if num_40 == 0:
                butt_40_anim += Animation(background_color=(0, 1, 0, 1), duration=1.5)
            else:
                butt_40_anim += Animation(background_color=(247 / 255, 7 / 255, 223 / 255, 1), duration=1.5)

            butt_1_anim.start(butt_1)
            butt_2_anim.start(butt_2)
            butt_3_anim.start(butt_3)
            butt_4_anim.start(butt_4)
            butt_5_anim.start(butt_5)
            butt_6_anim.start(butt_6)
            butt_7_anim.start(butt_7)
            butt_8_anim.start(butt_8)
            butt_9_anim.start(butt_9)
            butt_10_anim.start(butt_10)
            butt_11_anim.start(butt_11)
            butt_12_anim.start(butt_12)
            butt_13_anim.start(butt_13)
            butt_14_anim.start(butt_14)
            butt_15_anim.start(butt_15)
            butt_16_anim.start(butt_16)
            butt_17_anim.start(butt_17)
            butt_18_anim.start(butt_18)
            butt_19_anim.start(butt_19)
            butt_20_anim.start(butt_20)
            butt_21_anim.start(butt_21)
            butt_22_anim.start(butt_22)
            butt_23_anim.start(butt_23)
            butt_24_anim.start(butt_24)
            butt_25_anim.start(butt_25)
            butt_26_anim.start(butt_26)
            butt_27_anim.start(butt_27)
            butt_28_anim.start(butt_28)
            butt_29_anim.start(butt_29)
            butt_30_anim.start(butt_30)
            butt_31_anim.start(butt_31)
            butt_32_anim.start(butt_32)
            butt_33_anim.start(butt_33)
            butt_34_anim.start(butt_34)
            butt_35_anim.start(butt_35)
            butt_36_anim.start(butt_36)
            butt_37_anim.start(butt_37)
            butt_38_anim.start(butt_38)
            butt_39_anim.start(butt_39)
            butt_40_anim.start(butt_40)

            with open(r"brain.txt", "w+") as f:
                f.write(str(num_1).strip() + "\n" + str(num_2).strip() + "\n" + str(num_3).strip() + "\n" +
                        str(num_4).strip() + "\n" + str(num_5).strip() + "\n" + str(num_6).strip() + "\n" +
                        str(num_7).strip() + "\n" + str(num_8).strip() + "\n" + str(num_9).strip() + "\n" +
                        str(num_10).strip() + "\n" + str(num_11).strip() + "\n" + str(num_12).strip() + "\n" +
                        str(num_13).strip() + "\n" + str(num_14).strip() + "\n" + str(num_15).strip() + "\n" +
                        str(num_16).strip() + "\n" + str(num_17).strip() + "\n" + str(num_18).strip() + "\n" +
                        str(num_19).strip() + "\n" + str(num_20).strip() + "\n" + str(num_21).strip() + "\n" +
                        str(num_22).strip() + "\n" + str(num_23).strip() + "\n" + str(num_24).strip() + "\n" +
                        str(num_25).strip() + "\n" + str(num_26).strip() + "\n" + str(num_27).strip() + "\n" +
                        str(num_28).strip() + "\n" + str(num_29).strip() + "\n" + str(num_30).strip() + "\n" +
                        str(num_31).strip() + "\n" + str(num_32).strip() + "\n" + str(num_33).strip() + "\n" +
                        str(num_34).strip() + "\n" + str(num_35).strip() + "\n" + str(num_36).strip() + "\n" +
                        str(num_37).strip() + "\n" + str(num_38).strip() + "\n" + str(num_39).strip() + "\n" +
                        str(num_40).strip())
                f.close()

            Clock.schedule_interval(decrement_time, .1)

        def decrement_time(*args):
            get.root.ids.board.ids.count_down.opacity = 1
            get.root.ids.board.ids.count_down.color = (1, 0, 0, 1)
            get.root.ids.board.ids.count_down.text = f"{self.countdown}"
            self.countdown -= .1
            self.countdown = round(self.countdown, 2)

            if self.countdown == 0:
                Clock.schedule_once(unlock_buttons, 0)
                Clock.unschedule(decrement_time)
                get.root.ids.board.ids.big.text = "You have          seconds to complete the pattern!"

        def decrement_time_2(*args):
            get.root.ids.board.ids.count_down.opacity = 1
            get.root.ids.board.ids.count_down.color = (1, 0, 0, 1)
            get.root.ids.board.ids.count_down.text = f"{self.countdown_2}"
            self.countdown_2 -= .1
            self.countdown_2 = round(self.countdown_2, 2)

            if self.countdown_2 == 0:
                Clock.unschedule(decrement_time_2)
                get.root.ids.board.ids.big.text = "Time is out!"
                Clock.schedule_once(check_result, 1)

        def unlock_buttons(*args):
            butt_1.disabled = False
            butt_2.disabled = False
            butt_3.disabled = False
            butt_4.disabled = False
            butt_5.disabled = False
            butt_6.disabled = False
            butt_7.disabled = False
            butt_8.disabled = False
            butt_9.disabled = False
            butt_10.disabled = False
            butt_11.disabled = False
            butt_12.disabled = False
            butt_13.disabled = False
            butt_14.disabled = False
            butt_15.disabled = False
            butt_16.disabled = False
            butt_17.disabled = False
            butt_18.disabled = False
            butt_19.disabled = False
            butt_20.disabled = False
            butt_21.disabled = False
            butt_22.disabled = False
            butt_23.disabled = False
            butt_24.disabled = False
            butt_25.disabled = False
            butt_26.disabled = False
            butt_27.disabled = False
            butt_28.disabled = False
            butt_29.disabled = False
            butt_30.disabled = False
            butt_31.disabled = False
            butt_32.disabled = False
            butt_33.disabled = False
            butt_34.disabled = False
            butt_35.disabled = False
            butt_36.disabled = False
            butt_37.disabled = False
            butt_38.disabled = False
            butt_39.disabled = False
            butt_40.disabled = False

            butt_1_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_2_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_3_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_4_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_5_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_6_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_7_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_8_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_9_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_10_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_11_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_12_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_13_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_14_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_15_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_16_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_17_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_18_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_19_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_20_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_21_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_22_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_23_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_24_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_25_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_26_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_27_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_28_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_29_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_30_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_31_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_32_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_33_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_34_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_35_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_36_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_37_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_38_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_39_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)
            butt_40_reset_anim = Animation(background_color=(0, 1, 0, 1), duration=1.5)

            butt_1_reset_anim.start(butt_1)
            butt_2_reset_anim.start(butt_2)
            butt_3_reset_anim.start(butt_3)
            butt_4_reset_anim.start(butt_4)
            butt_5_reset_anim.start(butt_5)
            butt_6_reset_anim.start(butt_6)
            butt_7_reset_anim.start(butt_7)
            butt_8_reset_anim.start(butt_8)
            butt_9_reset_anim.start(butt_9)
            butt_10_reset_anim.start(butt_10)
            butt_11_reset_anim.start(butt_11)
            butt_12_reset_anim.start(butt_12)
            butt_13_reset_anim.start(butt_13)
            butt_14_reset_anim.start(butt_14)
            butt_15_reset_anim.start(butt_15)
            butt_16_reset_anim.start(butt_16)
            butt_17_reset_anim.start(butt_17)
            butt_18_reset_anim.start(butt_18)
            butt_19_reset_anim.start(butt_19)
            butt_20_reset_anim.start(butt_20)
            butt_21_reset_anim.start(butt_21)
            butt_22_reset_anim.start(butt_22)
            butt_23_reset_anim.start(butt_23)
            butt_24_reset_anim.start(butt_24)
            butt_25_reset_anim.start(butt_25)
            butt_26_reset_anim.start(butt_26)
            butt_27_reset_anim.start(butt_27)
            butt_28_reset_anim.start(butt_28)
            butt_29_reset_anim.start(butt_29)
            butt_30_reset_anim.start(butt_30)
            butt_31_reset_anim.start(butt_31)
            butt_32_reset_anim.start(butt_32)
            butt_33_reset_anim.start(butt_33)
            butt_34_reset_anim.start(butt_34)
            butt_35_reset_anim.start(butt_35)
            butt_36_reset_anim.start(butt_36)
            butt_37_reset_anim.start(butt_37)
            butt_38_reset_anim.start(butt_38)
            butt_39_reset_anim.start(butt_39)
            butt_40_reset_anim.start(butt_40)

            butt_40_reset_anim.bind(on_complete=Clock.schedule_interval(decrement_time_2, .1))

        def check_result(*args):
            with open(r"brain.txt", "r") as f:
                num_1_r = f.readline().strip()
                num_2_r = f.readline().strip()
                num_3_r = f.readline().strip()
                num_4_r = f.readline().strip()
                num_5_r = f.readline().strip()
                num_6_r = f.readline().strip()
                num_7_r = f.readline().strip()
                num_8_r = f.readline().strip()
                num_9_r = f.readline().strip()
                num_10_r = f.readline().strip()
                num_11_r = f.readline().strip()
                num_12_r = f.readline().strip()
                num_13_r = f.readline().strip()
                num_14_r = f.readline().strip()
                num_15_r = f.readline().strip()
                num_16_r = f.readline().strip()
                num_17_r = f.readline().strip()
                num_18_r = f.readline().strip()
                num_19_r = f.readline().strip()
                num_20_r = f.readline().strip()
                num_21_r = f.readline().strip()
                num_22_r = f.readline().strip()
                num_23_r = f.readline().strip()
                num_24_r = f.readline().strip()
                num_25_r = f.readline().strip()
                num_26_r = f.readline().strip()
                num_27_r = f.readline().strip()
                num_28_r = f.readline().strip()
                num_29_r = f.readline().strip()
                num_30_r = f.readline().strip()
                num_31_r = f.readline().strip()
                num_32_r = f.readline().strip()
                num_33_r = f.readline().strip()
                num_34_r = f.readline().strip()
                num_35_r = f.readline().strip()
                num_36_r = f.readline().strip()
                num_37_r = f.readline().strip()
                num_38_r = f.readline().strip()
                num_39_r = f.readline().strip()
                num_40_r = f.readline().strip()
                f.close()

            check_1 = False
            check_2 = False
            check_3 = False
            check_4 = False
            check_5 = False
            check_6 = False
            check_7 = False
            check_8 = False
            check_9 = False
            check_10 = False
            check_11 = False
            check_12 = False
            check_13 = False
            check_14 = False
            check_15 = False
            check_16 = False
            check_17 = False
            check_18 = False
            check_19 = False
            check_20 = False
            check_21 = False
            check_22 = False
            check_23 = False
            check_24 = False
            check_25 = False
            check_26 = False
            check_27 = False
            check_28 = False
            check_29 = False
            check_30 = False
            check_31 = False
            check_32 = False
            check_33 = False
            check_34 = False
            check_35 = False
            check_36 = False
            check_37 = False
            check_38 = False
            check_39 = False
            check_40 = False

            if num_1_r == "1" and butt_1.state == "down" or num_1_r == "0" and butt_1.state == "normal":
                check_1 = True
            if num_2_r == "1" and butt_2.state == "down" or num_2_r == "0" and butt_2.state == "normal":
                check_2 = True
            if num_3_r == "1" and butt_3.state == "down" or num_3_r == "0" and butt_3.state == "normal":
                check_3 = True
            if num_4_r == "1" and butt_4.state == "down" or num_4_r == "0" and butt_4.state == "normal":
                check_4 = True
            if num_5_r == "1" and butt_5.state == "down" or num_5_r == "0" and butt_5.state == "normal":
                check_5 = True
            if num_6_r == "1" and butt_6.state == "down" or num_6_r == "0" and butt_6.state == "normal":
                check_6 = True
            if num_7_r == "1" and butt_7.state == "down" or num_7_r == "0" and butt_7.state == "normal":
                check_7 = True
            if num_8_r == "1" and butt_8.state == "down" or num_8_r == "0" and butt_8.state == "normal":
                check_8 = True
            if num_9_r == "1" and butt_9.state == "down" or num_9_r == "0" and butt_9.state == "normal":
                check_9 = True
            if num_10_r == "1" and butt_10.state == "down" or num_10_r == "0" and butt_10.state == "normal":
                check_10 = True
            if num_11_r == "1" and butt_11.state == "down" or num_11_r == "0" and butt_11.state == "normal":
                check_11 = True
            if num_12_r == "1" and butt_12.state == "down" or num_12_r == "0" and butt_12.state == "normal":
                check_12 = True
            if num_13_r == "1" and butt_13.state == "down" or num_13_r == "0" and butt_13.state == "normal":
                check_13 = True
            if num_14_r == "1" and butt_14.state == "down" or num_14_r == "0" and butt_14.state == "normal":
                check_14 = True
            if num_15_r == "1" and butt_15.state == "down" or num_15_r == "0" and butt_15.state == "normal":
                check_15 = True
            if num_16_r == "1" and butt_16.state == "down" or num_16_r == "0" and butt_16.state == "normal":
                check_16 = True
            if num_17_r == "1" and butt_17.state == "down" or num_17_r == "0" and butt_17.state == "normal":
                check_17 = True
            if num_18_r == "1" and butt_18.state == "down" or num_18_r == "0" and butt_18.state == "normal":
                check_18 = True
            if num_19_r == "1" and butt_19.state == "down" or num_19_r == "0" and butt_19.state == "normal":
                check_19 = True
            if num_20_r == "1" and butt_20.state == "down" or num_20_r == "0" and butt_20.state == "normal":
                check_20 = True
            if num_21_r == "1" and butt_21.state == "down" or num_21_r == "0" and butt_21.state == "normal":
                check_21 = True
            if num_22_r == "1" and butt_22.state == "down" or num_22_r == "0" and butt_22.state == "normal":
                check_22 = True
            if num_23_r == "1" and butt_23.state == "down" or num_23_r == "0" and butt_23.state == "normal":
                check_23 = True
            if num_24_r == "1" and butt_24.state == "down" or num_24_r == "0" and butt_24.state == "normal":
                check_24 = True
            if num_25_r == "1" and butt_25.state == "down" or num_25_r == "0" and butt_25.state == "normal":
                check_25 = True
            if num_26_r == "1" and butt_26.state == "down" or num_26_r == "0" and butt_26.state == "normal":
                check_26 = True
            if num_27_r == "1" and butt_27.state == "down" or num_27_r == "0" and butt_27.state == "normal":
                check_27 = True
            if num_28_r == "1" and butt_28.state == "down" or num_28_r == "0" and butt_28.state == "normal":
                check_28 = True
            if num_29_r == "1" and butt_29.state == "down" or num_29_r == "0" and butt_29.state == "normal":
                check_29 = True
            if num_30_r == "1" and butt_30.state == "down" or num_30_r == "0" and butt_30.state == "normal":
                check_30 = True
            if num_31_r == "1" and butt_31.state == "down" or num_31_r == "0" and butt_31.state == "normal":
                check_31 = True
            if num_32_r == "1" and butt_32.state == "down" or num_32_r == "0" and butt_32.state == "normal":
                check_32 = True
            if num_33_r == "1" and butt_33.state == "down" or num_33_r == "0" and butt_33.state == "normal":
                check_33 = True
            if num_34_r == "1" and butt_34.state == "down" or num_34_r == "0" and butt_34.state == "normal":
                check_34 = True
            if num_35_r == "1" and butt_35.state == "down" or num_35_r == "0" and butt_35.state == "normal":
                check_35 = True
            if num_36_r == "1" and butt_36.state == "down" or num_36_r == "0" and butt_36.state == "normal":
                check_36 = True
            if num_37_r == "1" and butt_37.state == "down" or num_37_r == "0" and butt_37.state == "normal":
                check_37 = True
            if num_38_r == "1" and butt_38.state == "down" or num_38_r == "0" and butt_38.state == "normal":
                check_38 = True
            if num_39_r == "1" and butt_39.state == "down" or num_39_r == "0" and butt_39.state == "normal":
                check_39 = True
            if num_40_r == "1" and butt_40.state == "down" or num_40_r == "0" and butt_40.state == "normal":
                check_40 = True

            if check_1 and check_2 and check_3 and check_4 and check_5 and check_6 and check_7 and check_8 and \
                    check_9 and check_10 and check_11 and check_12 and check_13 and check_14 and check_15 and \
                    check_16 and check_17 and check_18 and check_19 and check_20 and check_21 and check_22 and \
                    check_23 and check_24 and check_25 and check_26 and check_27 and check_28 and check_29 and \
                    check_30 and check_31 and check_32 and check_33 and check_34 and check_35 and check_36 and \
                    check_37 and check_38 and check_39 and check_40:
                Clock.schedule_once(successful, 0.5)
                Clock.schedule_once(reset_buttons, 0)
                get.root.ids.board.ids.count_down.text = ""
                get.root.ids.board.ids.count_down.size = dp(0), dp(0)
                get.root.ids.board.ids.count_down.pos = dp(0), dp(0)
                get.root.ids.board.ids.count_down.opacity = 0
            else:
                Clock.schedule_once(unsuccessful, 0.5)
                Clock.schedule_once(reset_buttons, 0)
                get.root.ids.board.ids.count_down.text = ""
                get.root.ids.board.ids.count_down.size = dp(0), dp(0)
                get.root.ids.board.ids.count_down.pos = dp(0), dp(0)
                get.root.ids.board.ids.count_down.opacity = 0

        def reset_buttons(*args):
            butt_1.size = dp(0), dp(0)
            butt_1.pos = dp(0), dp(0)
            butt_1.opacity = 0
            butt_1.disabled = True
            butt_1.state = "normal"

            butt_2.size = dp(0), dp(0)
            butt_2.pos = dp(0), dp(0)
            butt_2.opacity = 0
            butt_2.disabled = True
            butt_2.state = "normal"

            butt_3.size = dp(0), dp(0)
            butt_3.pos = dp(0), dp(0)
            butt_3.opacity = 0
            butt_3.disabled = True
            butt_3.state = "normal"

            butt_4.size = dp(0), dp(0)
            butt_4.pos = dp(0), dp(0)
            butt_4.opacity = 0
            butt_4.disabled = True
            butt_4.state = "normal"

            butt_5.size = dp(0), dp(0)
            butt_5.pos = dp(0), dp(0)
            butt_5.opacity = 0
            butt_5.disabled = True
            butt_5.state = "normal"

            butt_6.size = dp(0), dp(0)
            butt_6.pos = dp(0), dp(0)
            butt_6.opacity = 0
            butt_6.disabled = True
            butt_6.state = "normal"

            butt_7.size = dp(0), dp(0)
            butt_7.pos = dp(0), dp(0)
            butt_7.opacity = 0
            butt_7.disabled = True
            butt_7.state = "normal"

            butt_8.size = dp(0), dp(0)
            butt_8.pos = dp(0), dp(0)
            butt_8.opacity = 0
            butt_8.disabled = True
            butt_8.state = "normal"

            butt_9.size = dp(0), dp(0)
            butt_9.pos = dp(0), dp(0)
            butt_9.opacity = 0
            butt_9.disabled = True
            butt_9.state = "normal"

            butt_10.size = dp(0), dp(0)
            butt_10.pos = dp(0), dp(0)
            butt_10.opacity = 0
            butt_10.disabled = True
            butt_10.state = "normal"

            butt_11.size = dp(0), dp(0)
            butt_11.pos = dp(0), dp(0)
            butt_11.opacity = 0
            butt_11.disabled = True
            butt_11.state = "normal"

            butt_12.size = dp(0), dp(0)
            butt_12.pos = dp(0), dp(0)
            butt_12.opacity = 0
            butt_12.disabled = True
            butt_12.state = "normal"

            butt_13.size = dp(0), dp(0)
            butt_13.pos = dp(0), dp(0)
            butt_13.opacity = 0
            butt_13.disabled = True
            butt_13.state = "normal"

            butt_14.size = dp(0), dp(0)
            butt_14.pos = dp(0), dp(0)
            butt_14.opacity = 0
            butt_14.disabled = True
            butt_14.state = "normal"

            butt_15.size = dp(0), dp(0)
            butt_15.pos = dp(0), dp(0)
            butt_15.opacity = 0
            butt_15.disabled = True
            butt_15.state = "normal"

            butt_16.size = dp(0), dp(0)
            butt_16.pos = dp(0), dp(0)
            butt_16.opacity = 0
            butt_16.disabled = True
            butt_16.state = "normal"

            butt_17.size = dp(0), dp(0)
            butt_17.pos = dp(0), dp(0)
            butt_17.opacity = 0
            butt_17.disabled = True
            butt_17.state = "normal"

            butt_18.size = dp(0), dp(0)
            butt_18.pos = dp(0), dp(0)
            butt_18.opacity = 0
            butt_18.disabled = True
            butt_18.state = "normal"

            butt_19.size = dp(0), dp(0)
            butt_19.pos = dp(0), dp(0)
            butt_19.opacity = 0
            butt_19.disabled = True
            butt_19.state = "normal"

            butt_20.size = dp(0), dp(0)
            butt_20.pos = dp(0), dp(0)
            butt_20.opacity = 0
            butt_20.disabled = True
            butt_20.state = "normal"

            butt_21.size = dp(0), dp(0)
            butt_21.pos = dp(0), dp(0)
            butt_21.opacity = 0
            butt_21.disabled = True
            butt_21.state = "normal"

            butt_22.size = dp(0), dp(0)
            butt_22.pos = dp(0), dp(0)
            butt_22.opacity = 0
            butt_22.disabled = True
            butt_22.state = "normal"

            butt_23.size = dp(0), dp(0)
            butt_23.pos = dp(0), dp(0)
            butt_23.opacity = 0
            butt_23.disabled = True
            butt_23.state = "normal"

            butt_24.size = dp(0), dp(0)
            butt_24.pos = dp(0), dp(0)
            butt_24.opacity = 0
            butt_24.disabled = True
            butt_24.state = "normal"

            butt_25.size = dp(0), dp(0)
            butt_25.pos = dp(0), dp(0)
            butt_25.opacity = 0
            butt_25.disabled = True
            butt_25.state = "normal"

            butt_26.size = dp(0), dp(0)
            butt_26.pos = dp(0), dp(0)
            butt_26.opacity = 0
            butt_26.disabled = True
            butt_26.state = "normal"

            butt_27.size = dp(0), dp(0)
            butt_27.pos = dp(0), dp(0)
            butt_27.opacity = 0
            butt_27.disabled = True
            butt_27.state = "normal"

            butt_28.size = dp(0), dp(0)
            butt_28.pos = dp(0), dp(0)
            butt_28.opacity = 0
            butt_28.disabled = True
            butt_28.state = "normal"

            butt_29.size = dp(0), dp(0)
            butt_29.pos = dp(0), dp(0)
            butt_29.opacity = 0
            butt_29.disabled = True
            butt_29.state = "normal"

            butt_30.size = dp(0), dp(0)
            butt_30.pos = dp(0), dp(0)
            butt_30.opacity = 0
            butt_30.disabled = True
            butt_30.state = "normal"

            butt_31.size = dp(0), dp(0)
            butt_31.pos = dp(0), dp(0)
            butt_31.opacity = 0
            butt_31.disabled = True
            butt_31.state = "normal"

            butt_32.size = dp(0), dp(0)
            butt_32.pos = dp(0), dp(0)
            butt_32.opacity = 0
            butt_32.disabled = True
            butt_32.state = "normal"

            butt_33.size = dp(0), dp(0)
            butt_33.pos = dp(0), dp(0)
            butt_33.opacity = 0
            butt_33.disabled = True
            butt_33.state = "normal"

            butt_34.size = dp(0), dp(0)
            butt_34.pos = dp(0), dp(0)
            butt_34.opacity = 0
            butt_34.disabled = True
            butt_34.state = "normal"

            butt_35.size = dp(0), dp(0)
            butt_35.pos = dp(0), dp(0)
            butt_35.opacity = 0
            butt_35.disabled = True
            butt_35.state = "normal"

            butt_36.size = dp(0), dp(0)
            butt_36.pos = dp(0), dp(0)
            butt_36.opacity = 0
            butt_36.disabled = True
            butt_36.state = "normal"

            butt_37.size = dp(0), dp(0)
            butt_37.pos = dp(0), dp(0)
            butt_37.opacity = 0
            butt_37.disabled = True
            butt_37.state = "normal"

            butt_38.size = dp(0), dp(0)
            butt_38.pos = dp(0), dp(0)
            butt_38.opacity = 0
            butt_38.disabled = True
            butt_38.state = "normal"

            butt_39.size = dp(0), dp(0)
            butt_39.pos = dp(0), dp(0)
            butt_39.opacity = 0
            butt_39.disabled = True
            butt_39.state = "normal"

            butt_40.size = dp(0), dp(0)
            butt_40.pos = dp(0), dp(0)
            butt_40.opacity = 0
            butt_40.disabled = True
            butt_40.state = "normal"

            get.root.ids.board.ids.big.text = ""
            get.root.ids.board.ids.big.size = dp(545), dp(270)
            get.root.ids.board.ids.big.pos = dp(385), dp(203)
            get.root.ids.board.ids.count_down.size = dp(0), dp(0)
            get.root.ids.board.ids.count_down.pos = dp(0), dp(0)

        def successful(*args):
            def end_anim(*args):
                get.root.ids.board.ids.big.text = ""
                hide_points_count()
                money_update()
                unblock_roll()

            def end_money_anim(*args):
                get.root.ids.board.ids.big.text = ""
                hide_cash_count()
                money_update()
                unblock_roll()

            if x == p1_pos10_x and y == p1_pos10_y:
                if get.root.ids.p1.ids.turn_1.active:
                    get.root.ids.board.ids.big.text = brain_successful
                    get.root.ids.board.ids.big.font_size = 35
                    get.root.ids.board.ids.points_count.text = f"+{40} pts."
                    get.root.ids.p1.ids.p1_points_stash.text = f"{(int(get.root.ids.p1.ids.p1_points_stash.text)) + 40}"
                    player_1_points_count()
                    Clock.schedule_once(end_anim, 3)
            if x == p1_pos28_x and y == p1_pos28_y:
                if get.root.ids.p1.ids.turn_1.active:
                    get.root.ids.board.ids.big.text = brain_money_successful
                    get.root.ids.board.ids.big.font_size = 35
                    get.root.ids.board.ids.cash_count.text = f"+{150} $."
                    get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text)) + 150}"
                    player_1_cash_count_g()
                    Clock.schedule_once(end_money_anim, 3)

            if x1 == p2_pos10_x and y1 == p2_pos10_y:
                if get.root.ids.p2.ids.turn_2.active:
                    get.root.ids.board.ids.big.text = brain_successful
                    get.root.ids.board.ids.big.font_size = 35
                    get.root.ids.board.ids.points_count.text = f"+{40} pts."
                    get.root.ids.p2.ids.p2_points_stash.text = f"{(int(get.root.ids.p2.ids.p2_points_stash.text)) + 40}"
                    player_2_points_count()
                    Clock.schedule_once(end_anim, 3)
            if x1 == p2_pos28_x and y1 == p2_pos28_y:
                if get.root.ids.p2.ids.turn_2.active:
                    get.root.ids.board.ids.big.text = brain_money_successful
                    get.root.ids.board.ids.big.font_size = 35
                    get.root.ids.board.ids.cash_count.text = f"+{150} $."
                    get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text)) + 150}"
                    player_2_cash_count_g()
                    Clock.schedule_once(end_money_anim, 3)

        def unsuccessful(*args):
            def end_anim(*args):
                get.root.ids.board.ids.big.text = ""
                hide_points_count()
                money_update()
                unblock_roll()

            def end_money_anim(*args):
                get.root.ids.board.ids.big.text = ""
                hide_cash_count()
                money_update()
                unblock_roll()

            if x == p1_pos10_x and y == p1_pos10_y:
                if get.root.ids.p1.ids.turn_1.active:
                    get.root.ids.board.ids.big.text = brain_unsuccessful
                    get.root.ids.board.ids.big.font_size = 35
                    if (int(get.root.ids.p1.ids.p1_points_stash.text)) - 15 < 0:
                        get.root.ids.board.ids.points_count.text = \
                            f"-{(int(get.root.ids.p1.ids.p1_points_stash.text))} pts."
                        get.root.ids.p1.ids.p1_points_stash.text = f"{0}"
                    else:
                        get.root.ids.board.ids.points_count.text = f"-{15} pts."
                        get.root.ids.p1.ids.p1_points_stash.text = \
                            f"{(int(get.root.ids.p1.ids.p1_points_stash.text)) - 15}"
                    player_1_points_count()
                    Clock.schedule_once(end_anim, 3)
            if x == p1_pos28_x and y == p1_pos28_y:
                if get.root.ids.p1.ids.turn_1.active:
                    get.root.ids.board.ids.big.text = brain_money_unsuccessful
                    get.root.ids.board.ids.big.font_size = 35
                    get.root.ids.board.ids.cash_count.text = f"-{75} $."
                    get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text)) - 75}"
                    player_1_cash_count_r()
                    Clock.schedule_once(end_money_anim, 3)

            if x1 == p2_pos10_x and y1 == p2_pos10_y:
                if get.root.ids.p2.ids.turn_2.active:
                    get.root.ids.board.ids.big.text = brain_unsuccessful
                    get.root.ids.board.ids.big.font_size = 35
                    if (int(get.root.ids.p2.ids.p2_points_stash.text)) - 15 < 0:
                        get.root.ids.board.ids.points_count.text = \
                            f"-{(int(get.root.ids.p2.ids.p2_points_stash.text))} pts."
                        get.root.ids.p2.ids.p2_points_stash.text = f"{0}"
                    else:
                        get.root.ids.board.ids.points_count.text = f"-{15} pts."
                        get.root.ids.p2.ids.p2_points_stash.text = \
                            f"{(int(get.root.ids.p2.ids.p2_points_stash.text)) - 15}"
                    player_2_points_count()
                    Clock.schedule_once(end_anim, 3)
            if x1 == p2_pos28_x and y1 == p2_pos28_y:
                if get.root.ids.p2.ids.turn_2.active:
                    get.root.ids.board.ids.big.text = brain_money_unsuccessful
                    get.root.ids.board.ids.big.font_size = 35
                    get.root.ids.board.ids.cash_count.text = f"-{75} $."
                    get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text)) - 75}"
                    player_2_cash_count_r()
                    Clock.schedule_once(end_money_anim, 3)

        show_instructions()

    @staticmethod
    def on_press_button_color():
        get = App.get_running_app()

        if get.root.ids.f_brain.ids.brain_1.state == "down":
            get.root.ids.f_brain.ids.brain_1.background_normal = ''
            get.root.ids.f_brain.ids.brain_1.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_1.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_2.state == "down":
            get.root.ids.f_brain.ids.brain_2.background_normal = ''
            get.root.ids.f_brain.ids.brain_2.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_2.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_3.state == "down":
            get.root.ids.f_brain.ids.brain_3.background_normal = ''
            get.root.ids.f_brain.ids.brain_3.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_3.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_4.state == "down":
            get.root.ids.f_brain.ids.brain_4.background_normal = ''
            get.root.ids.f_brain.ids.brain_4.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_4.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_5.state == "down":
            get.root.ids.f_brain.ids.brain_5.background_normal = ''
            get.root.ids.f_brain.ids.brain_5.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_5.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_6.state == "down":
            get.root.ids.f_brain.ids.brain_6.background_normal = ''
            get.root.ids.f_brain.ids.brain_6.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_6.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_7.state == "down":
            get.root.ids.f_brain.ids.brain_7.background_normal = ''
            get.root.ids.f_brain.ids.brain_7.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_7.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_8.state == "down":
            get.root.ids.f_brain.ids.brain_8.background_normal = ''
            get.root.ids.f_brain.ids.brain_8.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_8.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_9.state == "down":
            get.root.ids.f_brain.ids.brain_9.background_normal = ''
            get.root.ids.f_brain.ids.brain_9.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_9.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_10.state == "down":
            get.root.ids.f_brain.ids.brain_10.background_normal = ''
            get.root.ids.f_brain.ids.brain_10.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_10.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_11.state == "down":
            get.root.ids.f_brain.ids.brain_11.background_normal = ''
            get.root.ids.f_brain.ids.brain_11.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_11.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_12.state == "down":
            get.root.ids.f_brain.ids.brain_12.background_normal = ''
            get.root.ids.f_brain.ids.brain_12.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_12.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_13.state == "down":
            get.root.ids.f_brain.ids.brain_13.background_normal = ''
            get.root.ids.f_brain.ids.brain_13.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_13.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_14.state == "down":
            get.root.ids.f_brain.ids.brain_14.background_normal = ''
            get.root.ids.f_brain.ids.brain_14.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_14.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_15.state == "down":
            get.root.ids.f_brain.ids.brain_15.background_normal = ''
            get.root.ids.f_brain.ids.brain_15.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_15.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_16.state == "down":
            get.root.ids.f_brain.ids.brain_16.background_normal = ''
            get.root.ids.f_brain.ids.brain_16.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_16.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_17.state == "down":
            get.root.ids.f_brain.ids.brain_17.background_normal = ''
            get.root.ids.f_brain.ids.brain_17.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_17.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_18.state == "down":
            get.root.ids.f_brain.ids.brain_18.background_normal = ''
            get.root.ids.f_brain.ids.brain_18.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_18.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_19.state == "down":
            get.root.ids.f_brain.ids.brain_19.background_normal = ''
            get.root.ids.f_brain.ids.brain_19.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_19.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_20.state == "down":
            get.root.ids.f_brain.ids.brain_20.background_normal = ''
            get.root.ids.f_brain.ids.brain_20.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_20.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_21.state == "down":
            get.root.ids.f_brain.ids.brain_21.background_normal = ''
            get.root.ids.f_brain.ids.brain_21.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_21.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_22.state == "down":
            get.root.ids.f_brain.ids.brain_22.background_normal = ''
            get.root.ids.f_brain.ids.brain_22.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_22.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_23.state == "down":
            get.root.ids.f_brain.ids.brain_23.background_normal = ''
            get.root.ids.f_brain.ids.brain_23.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_23.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_24.state == "down":
            get.root.ids.f_brain.ids.brain_24.background_normal = ''
            get.root.ids.f_brain.ids.brain_24.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_24.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_25.state == "down":
            get.root.ids.f_brain.ids.brain_25.background_normal = ''
            get.root.ids.f_brain.ids.brain_25.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_25.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_26.state == "down":
            get.root.ids.f_brain.ids.brain_26.background_normal = ''
            get.root.ids.f_brain.ids.brain_26.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_26.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_27.state == "down":
            get.root.ids.f_brain.ids.brain_27.background_normal = ''
            get.root.ids.f_brain.ids.brain_27.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_27.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_28.state == "down":
            get.root.ids.f_brain.ids.brain_28.background_normal = ''
            get.root.ids.f_brain.ids.brain_28.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_28.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_29.state == "down":
            get.root.ids.f_brain.ids.brain_29.background_normal = ''
            get.root.ids.f_brain.ids.brain_29.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_29.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_30.state == "down":
            get.root.ids.f_brain.ids.brain_30.background_normal = ''
            get.root.ids.f_brain.ids.brain_30.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_30.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_31.state == "down":
            get.root.ids.f_brain.ids.brain_31.background_normal = ''
            get.root.ids.f_brain.ids.brain_31.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_31.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_32.state == "down":
            get.root.ids.f_brain.ids.brain_32.background_normal = ''
            get.root.ids.f_brain.ids.brain_32.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_32.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_33.state == "down":
            get.root.ids.f_brain.ids.brain_33.background_normal = ''
            get.root.ids.f_brain.ids.brain_33.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_33.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_34.state == "down":
            get.root.ids.f_brain.ids.brain_34.background_normal = ''
            get.root.ids.f_brain.ids.brain_34.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_34.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_35.state == "down":
            get.root.ids.f_brain.ids.brain_35.background_normal = ''
            get.root.ids.f_brain.ids.brain_35.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_35.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_36.state == "down":
            get.root.ids.f_brain.ids.brain_36.background_normal = ''
            get.root.ids.f_brain.ids.brain_36.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_36.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_37.state == "down":
            get.root.ids.f_brain.ids.brain_37.background_normal = ''
            get.root.ids.f_brain.ids.brain_37.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_37.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_38.state == "down":
            get.root.ids.f_brain.ids.brain_38.background_normal = ''
            get.root.ids.f_brain.ids.brain_38.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_38.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_39.state == "down":
            get.root.ids.f_brain.ids.brain_39.background_normal = ''
            get.root.ids.f_brain.ids.brain_39.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_39.background_color = (0, 1, 0, 1)

        if get.root.ids.f_brain.ids.brain_40.state == "down":
            get.root.ids.f_brain.ids.brain_40.background_normal = ''
            get.root.ids.f_brain.ids.brain_40.background_color = (247/255, 7/255, 223/255, 1)
        else:
            get.root.ids.f_brain.ids.brain_40.background_color = (0, 1, 0, 1)


class DuckField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos10_x and y == p1_pos10_y:
                Clock.schedule_once(self.player_1_duck, 0.5)
            if x == p1_pos29_x and y == p1_pos29_y:
                Clock.schedule_once(self.player_1_duck, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos9_x and y == p1_pos9_y:
                Clock.schedule_once(self.player_1_duck, 0.7)
            if x == p1_pos28_x and y == p1_pos28_y:
                Clock.schedule_once(self.player_1_duck, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos8_x and y == p1_pos8_y:
                Clock.schedule_once(self.player_1_duck, 0.9)
            if x == p1_pos27_x and y == p1_pos27_y:
                Clock.schedule_once(self.player_1_duck, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos7_x and y == p1_pos7_y:
                Clock.schedule_once(self.player_1_duck, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos6_x and y == p1_pos6_y:
                Clock.schedule_once(self.player_1_duck, 1.3)
            if x == p1_pos25_x and y == p1_pos25_y:
                Clock.schedule_once(self.player_1_duck, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos5_x and y == p1_pos5_y:
                Clock.schedule_once(self.player_1_duck, 1.5)
            if x == p1_pos24_x and y == p1_pos24_y:
                Clock.schedule_once(self.player_1_duck, 1.5)

    @staticmethod
    def player_1_duck(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        def not_owned(*args):
            get.root.ids.p1.ids.player_1_yes.disabled = False
            get.root.ids.p1.ids.yes_button_image.opacity = 1
            get.root.ids.p1.ids.player_1_no.disabled = False
            get.root.ids.p1.ids.no_button_image.opacity = 1
            get.root.ids.board.ids.big.text = duck_fields
            get.root.ids.board.ids.big.font_size = 30

        def owned_player_1(*args):
            get.root.ids.board.ids.big.text = "You own this property."
            get.root.ids.board.ids.big.valign = "middle"
            unblock_roll()

        def owned_player_2(*args):
            get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Player 2{'[/color]'} owns this property."
            get.root.ids.board.ids.big.valign = "middle"
            unblock_roll()

        def trigger():
            if get.root.ids.board.ids.field_11.text == "":
                not_owned()
            if get.root.ids.board.ids.field_11.text == "purple":
                owned_player_1()
            if get.root.ids.board.ids.field_11.text == "green":
                owned_player_2()

        def trigger_2():
            if get.root.ids.board.ids.field_30.text == "":
                not_owned()
            if get.root.ids.board.ids.field_30.text == "purple":
                owned_player_1()
            if get.root.ids.board.ids.field_30.text == "green":
                owned_player_2()

        if x == p1_pos11_x and y == p1_pos11_y:
            trigger()
        if x == p1_pos30_x and y == p1_pos30_y:
            trigger_2()

    @staticmethod
    def player_1_duck_on_turn(*args):
        get = App.get_running_app()

        def end_anim(*args):
            hide_points_count()
            if get.root.ids.board.ids.field_11.text == "purple" or get.root.ids.board.ids.field_30.text == "purple":
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 15}"
            elif get.root.ids.board.ids.field_11.text == "purple" and get.root.ids.board.ids.field_30.text == "purple":
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 30}"
            money_update()

        if get.root.ids.board.ids.field_11.text == "purple" or get.root.ids.board.ids.field_30.text == "purple":
            get.root.ids.board.ids.points_count.text = "+15 pts."
            player_1_points_count()
            Clock.schedule_once(end_anim, 2.2)
        if get.root.ids.board.ids.field_11.text == "purple" and get.root.ids.board.ids.field_30.text == "purple":
            get.root.ids.board.ids.points_count.text = "+30 pts."
            player_1_points_count()
            Clock.schedule_once(end_anim, 2.2)

    @staticmethod
    def player_1_buy(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        def schedule_animation(*args):
            get.root.ids.board.ids.big.text = "Good, now you will start grinding points every turn!"
            Clock.schedule_once(schedule_money, 0.5)

        def schedule_money(*args):
            get.root.ids.board.ids.cash_count.text = "-150 $"
            player_1_cash_count_r()
            Clock.schedule_once(hide_cash_count, 3)
            Clock.schedule_once(end_anim, 3)

        def end_anim(*args):
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"
            if x == p1_pos11_x and y == p1_pos11_y:
                get.root.ids.board.ids.field_11.background_color = player_1_color
                get.root.ids.board.ids.field_11.text = "purple"
            if x == p1_pos30_x and y == p1_pos30_y:
                get.root.ids.board.ids.field_30.background_color = player_1_color
                get.root.ids.board.ids.field_30.text = "purple"

            money_update()
            unblock_roll()

        schedule_animation()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos10_x and y == p2_pos10_y:
                Clock.schedule_once(self.player_2_duck, 0.5)
            if x == p2_pos29_x and y == p2_pos29_y:
                Clock.schedule_once(self.player_2_duck, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos9_x and y == p2_pos9_y:
                Clock.schedule_once(self.player_2_duck, 0.7)
            if x == p2_pos28_x and y == p2_pos28_y:
                Clock.schedule_once(self.player_2_duck, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos8_x and y == p2_pos8_y:
                Clock.schedule_once(self.player_2_duck, 0.9)
            if x == p2_pos27_x and y == p2_pos27_y:
                Clock.schedule_once(self.player_2_duck, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos7_x and y == p2_pos7_y:
                Clock.schedule_once(self.player_2_duck, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos6_x and y == p2_pos6_y:
                Clock.schedule_once(self.player_2_duck, 1.3)
            if x == p2_pos25_x and y == p2_pos25_y:
                Clock.schedule_once(self.player_2_duck, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos5_x and y == p2_pos5_y:
                Clock.schedule_once(self.player_2_duck, 1.5)
            if x == p2_pos24_x and y == p2_pos24_y:
                Clock.schedule_once(self.player_2_duck, 1.5)

    @staticmethod
    def player_2_duck(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        def not_owned(*args):
            get.root.ids.p2.ids.player_2_yes.disabled = False
            get.root.ids.p2.ids.yes_button_image.opacity = 1
            get.root.ids.p2.ids.player_2_no.disabled = False
            get.root.ids.p2.ids.no_button_image.opacity = 1
            get.root.ids.board.ids.big.text = duck_fields
            get.root.ids.board.ids.big.font_size = 30

        def owned_player_1(*args):
            get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Player 1{'[/color]'} owns this property."
            get.root.ids.board.ids.big.valign = "middle"
            unblock_roll()

        def owned_player_2(*args):
            get.root.ids.board.ids.big.text = "You own this property."
            get.root.ids.board.ids.big.valign = "middle"
            unblock_roll()

        def trigger():
            if get.root.ids.board.ids.field_11.text == "":
                not_owned()
            if get.root.ids.board.ids.field_11.text == "purple":
                owned_player_1()
            if get.root.ids.board.ids.field_11.text == "green":
                owned_player_2()

        def trigger_2():
            if get.root.ids.board.ids.field_30.text == "":
                not_owned()
            if get.root.ids.board.ids.field_30.text == "purple":
                owned_player_1()
            if get.root.ids.board.ids.field_30.text == "green":
                owned_player_2()

        if x == p2_pos11_x and y == p2_pos11_y:
            trigger()
        if x == p2_pos30_x and y == p2_pos30_y:
            trigger_2()

    @staticmethod
    def player_2_duck_on_turn(*args):
        get = App.get_running_app()

        def end_anim(*args):
            hide_points_count()
            if get.root.ids.board.ids.field_11.text == "green" or get.root.ids.board.ids.field_30.text == "green":
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 15}"
            elif get.root.ids.board.ids.field_11.text == "green" and get.root.ids.board.ids.field_30.text == "green":
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 30}"
            money_update()

        if get.root.ids.board.ids.field_11.text == "green" or get.root.ids.board.ids.field_30.text == "green":
            get.root.ids.board.ids.points_count.text = "+15 pts."
            player_2_points_count()
            Clock.schedule_once(end_anim, 2.2)
        if get.root.ids.board.ids.field_11.text == "green" and get.root.ids.board.ids.field_30.text == "green":
            get.root.ids.board.ids.points_count.text = "+30 pts."
            player_2_points_count()
            Clock.schedule_once(end_anim, 2.2)

    @staticmethod
    def player_2_buy(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        def schedule_animation(*args):
            get.root.ids.board.ids.big.text = "Good, now you will start grinding points every turn!"
            Clock.schedule_once(schedule_money, 0.5)

        def schedule_money(*args):
            get.root.ids.board.ids.cash_count.text = "-150 $"
            player_2_cash_count_r()
            Clock.schedule_once(hide_cash_count, 3)
            Clock.schedule_once(end_anim, 3)

        def end_anim(*args):
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"
            if x == p2_pos11_x and y == p2_pos11_y:
                get.root.ids.board.ids.field_11.background_color = player_2_color
                get.root.ids.board.ids.field_11.text = "green"
            if x == p2_pos30_x and y == p2_pos30_y:
                get.root.ids.board.ids.field_30.background_color = player_2_color
                get.root.ids.board.ids.field_30.text = "green"
            money_update()
            unblock_roll()

        schedule_animation()


class HospitalField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos11_x and y == p1_pos11_y:
                Clock.schedule_once(self.hospital_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos10_x and y == p1_pos10_y:
                Clock.schedule_once(self.hospital_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos9_x and y == p1_pos9_y:
                Clock.schedule_once(self.hospital_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos8_x and y == p1_pos8_y:
                Clock.schedule_once(self.hospital_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos7_x and y == p1_pos7_y:
                Clock.schedule_once(self.hospital_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos6_x and y == p1_pos6_y:
                Clock.schedule_once(self.hospital_main, 1.5)

    def player_1_butt_1(self):
        get = App.get_running_app()

        def animate(*args):
            player_1_cash_count_r()
            Clock.schedule_once(take_money, 1.7)

        def take_money(*args):
            hide_cash_count()

            if hospital_luck == 1:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 25}"
            if hospital_luck == 2:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 50}"
            if hospital_luck == 3:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 75}"
            if hospital_luck == 4:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 100}"

            money_update()
            Clock.schedule_once(self.reset_board, 1)
            Clock.schedule_once(reset, 1.1)

        def reset(*args):
            get.root.ids.board.ids.big.text = f"You paid {'[color=ff0000]'}{afterwards} ${'[/color]'} " \
                                              f"to have your treatment."
            get.root.ids.board.ids.big.font_size = 35

        hospital_luck = randint(1, 4)

        if hospital_luck == 1:
            get.root.ids.board.ids.cash_count.text = "-25 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.text = "-25 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.font_size = 75
            afterwards = 25
            animate()
        if hospital_luck == 2:
            get.root.ids.board.ids.cash_count.text = "-50 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.text = "-50 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.font_size = 75
            afterwards = 50
            animate()
        if hospital_luck == 3:
            get.root.ids.board.ids.cash_count.text = "-75 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.text = "-75 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.font_size = 75
            afterwards = 75
            animate()
        if hospital_luck == 4:
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.text = "-100 $"
            get.root.ids.f_hospital.ids.hospital_butt_1.font_size = 75
            afterwards = 100
            animate()

    def player_1_butt_2(self):
        get = App.get_running_app()

        def animate(*args):
            player_1_points_count()
            Clock.schedule_once(take_points, 1.7)

        def take_points(*args):
            hide_points_count()

            Clock.schedule_once(self.reset_board, 1)
            Clock.schedule_once(reset, 1.1)

            if hospital_points == 1:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 6}"
            if hospital_points == 2:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 12}"
            if hospital_points == 3:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 18}"
            if hospital_points == 4:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 24}"

            money_update()

        def reset(*args):
            get.root.ids.board.ids.big.text = f"You paid {'[color=ff0000]'}{afterwards} pts.{'[/color]'} " \
                                              f"to have your treatment."
            get.root.ids.board.ids.big.font_size = 35

        hospital_points = randint(1, 4)

        if hospital_points == 1:
            get.root.ids.board.ids.points_count.text = "-6 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.text = "-6 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.font_size = 50
            afterwards = 6
            animate()
        if hospital_points == 2:
            get.root.ids.board.ids.points_count.text = "-12 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.text = "-12 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.font_size = 50
            afterwards = 12
            animate()
        if hospital_points == 3:
            get.root.ids.board.ids.points_count.text = "-18 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.text = "-18 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.font_size = 50
            afterwards = 18
            animate()
        if hospital_points == 4:
            get.root.ids.board.ids.points_count.text = "-24 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.text = "-24 pts."
            get.root.ids.f_hospital.ids.hospital_butt_2.font_size = 50
            afterwards = 24
            animate()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos11_x and y == p2_pos11_y:
                Clock.schedule_once(self.hospital_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos10_x and y == p2_pos10_y:
                Clock.schedule_once(self.hospital_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos9_x and y == p2_pos9_y:
                Clock.schedule_once(self.hospital_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos8_x and y == p2_pos8_y:
                Clock.schedule_once(self.hospital_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos7_x and y == p2_pos7_y:
                Clock.schedule_once(self.hospital_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos6_x and y == p2_pos6_y:
                Clock.schedule_once(self.hospital_main, 1.5)

    def player_2_butt_1(self):
        get = App.get_running_app()

        def animate(*args):
            player_2_cash_count_r()
            Clock.schedule_once(take_money, 1.7)

        def take_money(*args):
            hide_cash_count()

            if hospital_luck == 1:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 25}"
            if hospital_luck == 2:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 50}"
            if hospital_luck == 3:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 75}"
            if hospital_luck == 4:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 100}"

            money_update()
            Clock.schedule_once(self.reset_board, 1)
            Clock.schedule_once(reset, 1.1)

        def reset(*args):
            get.root.ids.board.ids.big.text = f"You paid {'[color=ff0000]'}{afterwards} ${'[/color]'} " \
                                              f"to have your treatment."
            get.root.ids.board.ids.big.font_size = 35

        hospital_luck = randint(1, 4)

        if hospital_luck == 1:
            get.root.ids.board.ids.cash_count.text = "-25 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.text = "-25 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.font_size = 75
            afterwards = 25
            animate()
        if hospital_luck == 2:
            get.root.ids.board.ids.cash_count.text = "-50 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.text = "-50 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.font_size = 75
            afterwards = 50
            animate()
        if hospital_luck == 3:
            get.root.ids.board.ids.cash_count.text = "-75 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.text = "-75 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.font_size = 75
            afterwards = 75
            animate()
        if hospital_luck == 4:
            get.root.ids.board.ids.cash_count.text = "-100 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.text = "-100 $"
            get.root.ids.f_hospital.ids.hospital_butt_3.font_size = 75
            afterwards = 100
            animate()

    def player_2_butt_2(self):
        get = App.get_running_app()

        def animate(*args):
            player_2_points_count()
            Clock.schedule_once(take_points, 1.7)

        def take_points(*args):
            hide_points_count()

            Clock.schedule_once(self.reset_board, 1)
            Clock.schedule_once(reset, 1.1)

            if hospital_points == 1:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 6}"
            if hospital_points == 2:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 12}"
            if hospital_points == 3:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 18}"
            if hospital_points == 4:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 24}"

            money_update()

        def reset(*args):
            get.root.ids.board.ids.big.text = f"You paid {'[color=ff0000]'}{afterwards} pts.{'[/color]'} " \
                                              f"to have your treatment."
            get.root.ids.board.ids.big.font_size = 35

        hospital_points = randint(1, 4)

        if hospital_points == 1:
            get.root.ids.board.ids.points_count.text = "-6 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.text = "-6 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.font_size = 50
            afterwards = 6
            animate()
        if hospital_points == 2:
            get.root.ids.board.ids.points_count.text = "-12 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.text = "-12 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.font_size = 50
            afterwards = 12
            animate()
        if hospital_points == 3:
            get.root.ids.board.ids.points_count.text = "-18 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.text = "-18 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.font_size = 50
            afterwards = 18
            animate()
        if hospital_points == 4:
            get.root.ids.board.ids.points_count.text = "-24 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.text = "-24 pts."
            get.root.ids.f_hospital.ids.hospital_butt_4.font_size = 50
            afterwards = 24
            animate()

    # Both Players - General Functions

    @staticmethod
    def reset_board(*args):
        get = App.get_running_app()

        label_anim = Animation(opacity=1)
        butt_1_anim = Animation(opacity=0)
        butt_1_anim += Animation(pos=(dp(0), dp(0)), size=(dp(0), dp(0)), duration=0.05)
        butt_2_anim = Animation(opacity=0)
        butt_2_anim += Animation(pos=(dp(0), dp(0)), size=(dp(0), dp(0)), duration=0.05)
        butt_3_anim = Animation(opacity=0)
        butt_3_anim += Animation(pos=(dp(0), dp(0)), size=(dp(0), dp(0)), duration=0.05)
        butt_4_anim = Animation(opacity=0)
        butt_4_anim += Animation(pos=(dp(0), dp(0)), size=(dp(0), dp(0)), duration=0.05)

        label_anim.start(get.root.ids.board.ids.big)
        butt_1_anim.start(get.root.ids.f_hospital.ids.hospital_butt_1)
        butt_2_anim.start(get.root.ids.f_hospital.ids.hospital_butt_2)
        butt_3_anim.start(get.root.ids.f_hospital.ids.hospital_butt_3)
        butt_4_anim.start(get.root.ids.f_hospital.ids.hospital_butt_4)
        unblock_roll()

    @staticmethod
    def hospital_main(*args):
        get = App.get_running_app()
        butt_1 = get.root.ids.f_hospital.ids.hospital_butt_1
        butt_2 = get.root.ids.f_hospital.ids.hospital_butt_2
        butt_3 = get.root.ids.f_hospital.ids.hospital_butt_3
        butt_4 = get.root.ids.f_hospital.ids.hospital_butt_4

        def show_options(*args):
            get.root.ids.board.ids.big.opacity = 0
            if get.root.ids.p1.ids.turn_1.active:
                butt_1.disabled = False
                butt_2.disabled = False
                butt_1.text = hospital_1_text
                butt_2.text = hospital_2_text
            if get.root.ids.p2.ids.turn_2.active:
                butt_3.disabled = False
                butt_4.disabled = False
                butt_3.text = hospital_1_text
                butt_4.text = hospital_2_text

            if get.root.ids.p1.ids.turn_1.active:
                if int(get.root.ids.p1.ids.p1_points_stash.text) < 24:
                    butt_2.disabled = True
                    butt_2.text = f"Not enough\npoints to\nchoose\nthis option."

                butt_1_anim = Animation(pos=(dp(405), dp(240)), size=(dp(250), dp(150)), duration=0.05)
                butt_1_anim += Animation(opacity=1, background_color=(137 / 255, 146 / 255, 150 / 255, 1),
                                         color=(1, 0, 0, 1), bold=True, font_size=25, duration=0.7)

                butt_2_anim = Animation(pos=(dp(660), dp(240)), size=(dp(250), dp(150)), duration=0.05)
                butt_2_anim += Animation(opacity=1, background_color=(111 / 255, 3 / 255, 252 / 255, 1),
                                         color=(233 / 255, 245 / 255, 5 / 255, 1), bold=True, font_size=25,
                                         duration=0.7)

                butt_1_anim.start(butt_1)
                butt_2_anim.start(butt_2)

            if get.root.ids.p2.ids.turn_2.active:
                if int(get.root.ids.p2.ids.p2_points_stash.text) < 24:
                    butt_4.disabled = True
                    butt_4.text = f"Not enough\npoints to\nchoose\nthis option."

                butt_3_anim = Animation(pos=(dp(405), dp(240)), size=(dp(250), dp(150)), duration=0.05)
                butt_3_anim += Animation(opacity=1, background_color=(137 / 255, 146 / 255, 150 / 255, 1),
                                         color=(1, 0, 0, 1), bold=True, font_size=25, duration=0.7)

                butt_4_anim = Animation(pos=(dp(660), dp(240)), size=(dp(250), dp(150)), duration=0.05)
                butt_4_anim += Animation(opacity=1, background_color=(111 / 255, 3 / 255, 252 / 255, 1),
                                         color=(233 / 255, 245 / 255, 5 / 255, 1), bold=True, font_size=25,
                                         duration=0.7)

                butt_3_anim.start(butt_3)
                butt_4_anim.start(butt_4)

        get.root.ids.board.ids.big.text = hospital_fields
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(show_options, 5)


class ColiseumField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos12_x and y == p1_pos12_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos11_x and y == p1_pos11_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos10_x and y == p1_pos10_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos9_x and y == p1_pos9_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos8_x and y == p1_pos8_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos7_x and y == p1_pos7_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.5)

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_13.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_13.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_13.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = coliseum_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Coliseum is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-280 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 280}"
        get.root.ids.board.ids.field_13.background_color = player_1_color
        get.root.ids.board.ids.field_13.text = "purple"

        money_update()
        unblock_roll()

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 0:
            fee = 70
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 1:
            fee = 110
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 2:
            fee = 150
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 3:
            fee = 190
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money, 1.5)

    def player_1_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 0:
            fee = 70
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 1:
            fee = 110
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 2:
            fee = 150
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 3:
            fee = 190
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) - fee)}"
        player_1_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_1_move_label, 1.5)

    def player_1_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money, 1)

    def player_2_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 0:
            fee = 70
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 1:
            fee = 110
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 2:
            fee = 150
        if int(get.root.ids.f_shop.ids.coliseum_count_2_2.text) == 3:
            fee = 190
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos12_x and y == p2_pos12_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos11_x and y == p2_pos11_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos10_x and y == p2_pos10_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos9_x and y == p2_pos9_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos8_x and y == p2_pos8_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos7_x and y == p2_pos7_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.5)

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_13.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_13.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_13.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = coliseum_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Coliseum is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-280 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 280}"
        get.root.ids.board.ids.field_13.background_color = player_2_color
        get.root.ids.board.ids.field_13.text = "green"

        money_update()
        unblock_roll()

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 0:
            fee = 70
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 1:
            fee = 110
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 2:
            fee = 150
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 3:
            fee = 190
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money, 1.5)

    def player_2_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 0:
            fee = 70
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 1:
            fee = 110
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 2:
            fee = 150
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 3:
            fee = 190
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) - fee)}"
        player_2_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_2_move_label, 1.5)

    def player_2_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money, 1)

    def player_1_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 0:
            fee = 70
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 1:
            fee = 110
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 2:
            fee = 150
        if int(get.root.ids.f_shop.ids.coliseum_count_2.text) == 3:
            fee = 190
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class StickyField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos13_x and y == p1_pos13_y:
                Clock.schedule_once(self.player_1_sticky, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos12_x and y == p1_pos12_y:
                Clock.schedule_once(self.player_1_sticky, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos11_x and y == p1_pos11_y:
                Clock.schedule_once(self.player_1_sticky, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos10_x and y == p1_pos10_y:
                Clock.schedule_once(self.player_1_sticky, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos9_x and y == p1_pos9_y:
                Clock.schedule_once(self.player_1_sticky, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos8_x and y == p1_pos8_y:
                Clock.schedule_once(self.player_1_sticky, 1.5)

        if x == p1_pos14_x and y == 120:
            player_1_animate = Animation(pos=(dp(p1_pos14_x), dp(124)), duration=0.5)
            player_1_animate.start(get.root.ids.p1.ids.player_1)
            player_1_animate.bind(on_complete=unblock_roll)
        if x == p1_pos14_x and y == 124:
            player_1_animate = Animation(pos=(dp(p1_pos14_x), dp(128)), duration=0.5)
            player_1_animate.start(get.root.ids.p1.ids.player_1)
            player_1_animate.bind(on_complete=unblock_roll)

    @staticmethod
    def player_1_sticky(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = sticky_fields
        get.root.ids.board.ids.big.valign = "middle"

        player_1_anim = Animation(pos=(dp(p1_pos14_x), dp(120)), duration=0.5)
        player_1_anim.start(get.root.ids.p1.ids.player_1)
        unblock_roll()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos13_x and y == p2_pos13_y:
                Clock.schedule_once(self.player_2_sticky, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos12_x and y == p2_pos12_y:
                Clock.schedule_once(self.player_2_sticky, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos11_x and y == p2_pos11_y:
                Clock.schedule_once(self.player_2_sticky, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos10_x and y == p2_pos10_y:
                Clock.schedule_once(self.player_2_sticky, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos9_x and y == p2_pos9_y:
                Clock.schedule_once(self.player_2_sticky, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos8_x and y == p2_pos8_y:
                Clock.schedule_once(self.player_2_sticky, 1.5)

        if x == p2_pos14_x and y == 120:
            player_2_animate = Animation(pos=(dp(p2_pos14_x), dp(124)), duration=0.5)
            player_2_animate.start(get.root.ids.p2.ids.player_2)
            player_2_animate.bind(on_complete=unblock_roll)
        if x == p2_pos14_x and y == 124:
            player_2_animate = Animation(pos=(dp(p2_pos14_x), dp(128)), duration=0.5)
            player_2_animate.start(get.root.ids.p2.ids.player_2)
            player_2_animate.bind(on_complete=unblock_roll)

    @staticmethod
    def player_2_sticky(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = sticky_fields
        get.root.ids.board.ids.big.valign = "middle"

        player_2_anim = Animation(pos=(dp(p2_pos14_x), dp(120)), duration=0.5)
        player_2_anim.start(get.root.ids.p2.ids.player_2)
        unblock_roll()


class MathsField(Widget):
    math_countdown = NumericProperty(20)

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos14_x and y == p1_pos14_y:
                Clock.schedule_once(self.maths_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos13_x and y == p1_pos13_y:
                Clock.schedule_once(self.maths_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos12_x and y == p1_pos12_y:
                Clock.schedule_once(self.maths_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos11_x and y == p1_pos11_y:
                Clock.schedule_once(self.maths_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos10_x and y == p1_pos10_y:
                Clock.schedule_once(self.maths_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos9_x and y == p1_pos9_y:
                Clock.schedule_once(self.maths_main, 1.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos14_x and y == p2_pos14_y:
                Clock.schedule_once(self.maths_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos13_x and y == p2_pos13_y:
                Clock.schedule_once(self.maths_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos12_x and y == p2_pos12_y:
                Clock.schedule_once(self.maths_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos11_x and y == p2_pos11_y:
                Clock.schedule_once(self.maths_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos10_x and y == p2_pos10_y:
                Clock.schedule_once(self.maths_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos9_x and y == p2_pos9_y:
                Clock.schedule_once(self.maths_main, 1.5)

    # Both Players - General Functions

    def maths_main(self, *args):
        global math_reset

        get = App.get_running_app()
        self.math_countdown = 20
        math_reset = 0

        def start(*args):
            get.root.ids.board.ids.big.text = math_fields
            Clock.schedule_once(self.maths, 5)
            Clock.schedule_once(schedule_timer, 5)

        def schedule_timer(*args):
            Clock.schedule_interval(decrement_time, .1)

        def decrement_time(*args):
            get.root.ids.board.ids.maths_count_down.opacity = 1
            get.root.ids.board.ids.maths_count_down.pos = dp(580), dp(520)
            get.root.ids.board.ids.maths_count_down.size = dp(150), dp(100)
            get.root.ids.board.ids.maths_count_down.font_size = 50
            get.root.ids.board.ids.maths_count_down.text = f"{self.math_countdown}"
            self.math_countdown -= .1
            self.math_countdown = round(self.math_countdown, 2)

            if self.math_countdown < 10:
                get.root.ids.board.ids.maths_count_down.color = (1, 0, 0, 1)
            elif self.math_countdown >= 10:
                get.root.ids.board.ids.maths_count_down.color = (0, 1, 0, 1)

            if self.math_countdown == 0:
                Clock.unschedule(decrement_time)
                Clock.schedule_once(show_result, 0)

        def show_result(*args):
            global math_reset

            get.root.ids.board.ids.big.size = dp(545), dp(270)
            get.root.ids.board.ids.big.pos = dp(385), dp(203)
            get.root.ids.board.ids.big.font_size = 35
            get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Time is out!{'[/color]'}\n\nYou had " \
                                              f"{'[color=09ff00]'}" \
                                              f"{round(math_reset / 10)} correct{'[/color]'} answers and you won " \
                                              f"{'[color=09ff00]'}{math_reset} $."

            get.root.ids.f_maths.ids.math_butt_1.size = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_1.pos = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_1.opacity = 0
            get.root.ids.f_maths.ids.math_butt_1.disabled = True

            get.root.ids.f_maths.ids.math_butt_2.size = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_2.pos = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_2.opacity = 0
            get.root.ids.f_maths.ids.math_butt_2.disabled = True

            get.root.ids.f_maths.ids.math_butt_3.size = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_3.pos = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_3.opacity = 0
            get.root.ids.f_maths.ids.math_butt_3.disabled = True

            get.root.ids.f_maths.ids.math_butt_4.size = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_4.pos = dp(0), dp(0)
            get.root.ids.f_maths.ids.math_butt_4.opacity = 0
            get.root.ids.f_maths.ids.math_butt_4.disabled = True

            get.root.ids.board.ids.maths_count_down.opacity = 0
            get.root.ids.board.ids.maths_count_down.pos = dp(0), dp(0)
            get.root.ids.board.ids.maths_count_down.size = dp(0), dp(0)
            get.root.ids.board.ids.maths_count_down.font_size = 0

            if get.root.ids.p1.ids.turn_1.active:
                get.root.ids.p1.ids.p1_money_stash.text = \
                    f"{int(get.root.ids.p1.ids.p1_money_stash.text) + math_reset}"
            if get.root.ids.p2.ids.turn_2.active:
                get.root.ids.p2.ids.p2_money_stash.text = \
                    f"{int(get.root.ids.p2.ids.p2_money_stash.text) + math_reset}"

            Clock.schedule_once(money_update, 3)
            Clock.schedule_once(end_anim, 3)

        def end_anim(*args):
            global math_reset

            hide_cash_count()
            unblock_roll()
            math_reset = 0

        start()

    @staticmethod
    def maths(*args):
        global math_answer, add_result

        get = App.get_running_app()

        math_add_tuple = (randint(0, 50), randint(0, 50))

        get.root.ids.board.ids.big.font_size = 50
        get.root.ids.board.ids.big.size = dp(545), dp(173)
        get.root.ids.board.ids.big.pos = dp(385), dp(300)
        get.root.ids.board.ids.big.valign = "middle"
        get.root.ids.board.ids.big.text = f"{math_add_tuple[0]} + {math_add_tuple[1]} = ?"

        get.root.ids.f_maths.ids.math_butt_1.size = dp(120), dp(70)
        get.root.ids.f_maths.ids.math_butt_1.pos = dp(400), dp(220)
        get.root.ids.f_maths.ids.math_butt_1.opacity = 1
        get.root.ids.f_maths.ids.math_butt_1.disabled = False

        get.root.ids.f_maths.ids.math_butt_2.size = dp(120), dp(70)
        get.root.ids.f_maths.ids.math_butt_2.pos = dp(532), dp(220)
        get.root.ids.f_maths.ids.math_butt_2.opacity = 1
        get.root.ids.f_maths.ids.math_butt_2.disabled = False

        get.root.ids.f_maths.ids.math_butt_3.size = dp(120), dp(70)
        get.root.ids.f_maths.ids.math_butt_3.pos = dp(663), dp(220)
        get.root.ids.f_maths.ids.math_butt_3.opacity = 1
        get.root.ids.f_maths.ids.math_butt_3.disabled = False

        get.root.ids.f_maths.ids.math_butt_4.size = dp(120), dp(70)
        get.root.ids.f_maths.ids.math_butt_4.pos = dp(795), dp(220)
        get.root.ids.f_maths.ids.math_butt_4.opacity = 1
        get.root.ids.f_maths.ids.math_butt_4.disabled = False

        add_result = math_add_tuple[0] + math_add_tuple[1]
        math_answer = randint(1, 4)
        b = randint(1, 5)

        if math_answer == 1:
            if not b > add_result:
                get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result - b}"
            else:
                get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result + b}"

            get.root.ids.f_maths.ids.math_butt_1.text = f"{add_result}"
            get.root.ids.f_maths.ids.math_butt_2.text = f"{add_result + b}"
            get.root.ids.f_maths.ids.math_butt_4.text = f"{add_result + b * 2}"

        if math_answer == 2:
            if not b > add_result:
                get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result - b}"
            else:
                get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result + b}"

            get.root.ids.f_maths.ids.math_butt_1.text = f"{add_result + b}"
            get.root.ids.f_maths.ids.math_butt_2.text = f"{add_result}"
            get.root.ids.f_maths.ids.math_butt_4.text = f"{add_result + b * 2}"

        if math_answer == 3:
            if not b > add_result:
                get.root.ids.f_maths.ids.math_butt_1.text = f"{add_result - b}"
            else:
                get.root.ids.f_maths.ids.math_butt_1.text = f"{add_result + b}"

            get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result}"
            get.root.ids.f_maths.ids.math_butt_2.text = f"{add_result + b}"
            get.root.ids.f_maths.ids.math_butt_4.text = f"{add_result + b * 2}"

        if math_answer == 4:
            if not b > add_result:
                get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result - b}"
            else:
                get.root.ids.f_maths.ids.math_butt_3.text = f"{add_result + b}"

            get.root.ids.f_maths.ids.math_butt_1.text = f"{add_result + b}"
            get.root.ids.f_maths.ids.math_butt_2.text = f"{add_result + b * 2}"
            get.root.ids.f_maths.ids.math_butt_4.text = f"{add_result}"

    def math_butt_1(self):
        global math_reset

        get = App.get_running_app()
        if math_answer == 1:
            math_reset += 10
            get.root.ids.board.ids.cash_count.text = f"+{math_reset} $"
        self.maths()
        if get.root.ids.p1.ids.turn_1.active:
            player_1_cash_count_g()
        if get.root.ids.p2.ids.turn_2.active:
            player_2_cash_count_g()

    def math_butt_2(self):
        global math_reset

        get = App.get_running_app()
        if math_answer == 2:
            math_reset += 10
            get.root.ids.board.ids.cash_count.text = f"+{math_reset} $"

        self.maths()
        if get.root.ids.p1.ids.turn_1.active:
            player_1_cash_count_g()
        if get.root.ids.p2.ids.turn_2.active:
            player_2_cash_count_g()

    def math_butt_3(self):
        global math_reset

        get = App.get_running_app()
        if math_answer == 3:
            math_reset += 10
            get.root.ids.board.ids.cash_count.text = f"+{math_reset} $"

        self.maths()
        if get.root.ids.p1.ids.turn_1.active:
            player_1_cash_count_g()
        if get.root.ids.p2.ids.turn_2.active:
            player_2_cash_count_g()

    def math_butt_4(self):
        global math_reset

        get = App.get_running_app()
        if math_answer == 4:
            math_reset += 10
            get.root.ids.board.ids.cash_count.text = f"+{math_reset} $"

        self.maths()
        if get.root.ids.p1.ids.turn_1.active:
            player_1_cash_count_g()
        if get.root.ids.p2.ids.turn_2.active:
            player_2_cash_count_g()


class CounterfeitCashField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos15_x and y == p1_pos15_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos14_x and y == p1_pos14_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos13_x and y == p1_pos13_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos12_x and y == p1_pos12_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos11_x and y == p1_pos11_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos10_x and y == p1_pos10_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.5)

        if get.root.ids.board.ids.field_16.text == "purple":
            self.progress_bar()

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_16.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_16.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_16.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = counterfeit_cash_fields
        get.root.ids.board.ids.big.font_size = 25
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    @staticmethod
    def player_1_opponent_owned(*args):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Player 2{'[/color]'} owns this property!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Counterfeit Cash Factory is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-350 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 350}"
        get.root.ids.board.ids.field_16.background_color = player_1_color
        get.root.ids.board.ids.field_16.text = "purple"
        get.root.ids.f_counterfeit.ids.ccf_progress.opacity = 1
        get.root.ids.f_counterfeit.ids.ccf_progress.size = dp(100), dp(23)
        get.root.ids.f_counterfeit.ids.ccf_progress.pos = dp(212), dp(637)
        get.root.ids.f_counterfeit.ids.ccf_progress_label.opacity = 1
        get.root.ids.f_counterfeit.ids.ccf_progress_label.size = dp(50), dp(20)
        get.root.ids.f_counterfeit.ids.ccf_progress_label.pos = dp(318), dp(637)
        get.root.ids.f_counterfeit.ids.ccf_progress_label.text = "0 %"
        get.root.ids.f_counterfeit.ids.ccf_progress_label.halign = "left"
        get.root.ids.f_counterfeit.ids.ccf_image.opacity = 1
        get.root.ids.f_counterfeit.ids.ccf_image.size = dp(23), dp(23)
        get.root.ids.f_counterfeit.ids.ccf_image.pos = dp(180), dp(637)

        money_update()
        unblock_roll()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos15_x and y == p2_pos15_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos14_x and y == p2_pos14_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos13_x and y == p2_pos13_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos12_x and y == p2_pos12_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos11_x and y == p2_pos11_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos10_x and y == p2_pos10_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.5)

        if get.root.ids.board.ids.field_16.text == "green":
            self.progress_bar()

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_16.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_16.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_16.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = counterfeit_cash_fields
        get.root.ids.board.ids.big.font_size = 25
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    @staticmethod
    def player_2_opponent_owned(*args):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Player 1{'[/color]'} owns this property!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Counterfeit Cash Factory is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-350 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 350}"
        get.root.ids.board.ids.field_16.background_color = player_2_color
        get.root.ids.board.ids.field_16.text = "green"
        get.root.ids.f_counterfeit.ids.ccf_progress.opacity = 1
        get.root.ids.f_counterfeit.ids.ccf_progress.size = dp(100), dp(23)
        get.root.ids.f_counterfeit.ids.ccf_progress.pos = dp(1018), dp(637)
        get.root.ids.f_counterfeit.ids.ccf_progress_label.opacity = 1
        get.root.ids.f_counterfeit.ids.ccf_progress_label.size = dp(50), dp(20)
        get.root.ids.f_counterfeit.ids.ccf_progress_label.pos = dp(962), dp(637)
        get.root.ids.f_counterfeit.ids.ccf_progress_label.text = "0 %"
        get.root.ids.f_counterfeit.ids.ccf_progress_label.halign = "right"
        get.root.ids.f_counterfeit.ids.ccf_image.opacity = 1
        get.root.ids.f_counterfeit.ids.ccf_image.size = dp(23), dp(23)
        get.root.ids.f_counterfeit.ids.ccf_image.pos = dp(1127), dp(637)

        money_update()
        unblock_roll()

    # Both Players - General Functions

    @staticmethod
    def progress_bar(*args):
        get = App.get_running_app()
        progress_1 = get.root.ids.f_counterfeit.ids.ccf_progress.value

        if get.root.ids.board.ids.dice.text == "1":
            progress_1 += 2
            get.root.ids.f_counterfeit.ids.ccf_progress.value = progress_1
            get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "2":
            progress_1 += 4
            get.root.ids.f_counterfeit.ids.ccf_progress.value = progress_1
            get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "3":
            progress_1 += 6
            get.root.ids.f_counterfeit.ids.ccf_progress.value = progress_1
            get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "4":
            progress_1 += 8
            get.root.ids.f_counterfeit.ids.ccf_progress.value = progress_1
            get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "5":
            progress_1 += 10
            get.root.ids.f_counterfeit.ids.ccf_progress.value = progress_1
            get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "6":
            progress_1 += 20
            get.root.ids.f_counterfeit.ids.ccf_progress.value = progress_1
            get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"

        if progress_1 >= 100:
            if get.root.ids.board.ids.field_16.text == "purple":
                get.root.ids.f_counterfeit.ids.ccf_progress.value = 100
                get.root.ids.f_counterfeit.ids.ccf_progress_label.text = ""
                get.root.ids.f_counterfeit.ids.ccf_claim.opacity = 1
                get.root.ids.f_counterfeit.ids.ccf_point.opacity = 1
                get.root.ids.f_counterfeit.ids.ccf_point.source = 'images/claim_point.png'
                get.root.ids.f_counterfeit.ids.ccf_point.size = dp(30), dp(20)
                get.root.ids.f_counterfeit.ids.ccf_point.pos = dp(380), dp(640)
                get.root.ids.f_counterfeit.ids.ccf_claim.disabled = False
                get.root.ids.f_counterfeit.ids.ccf_claim.size = dp(50), dp(20)
                get.root.ids.f_counterfeit.ids.ccf_claim.pos = dp(320), dp(640)

                Animation.cancel_all(get.root.ids.f_star_points.ids.fs_point)

                anim = Animation(pos=(dp(380), dp(613)), duration=0.7)
                anim += Animation(pos=(dp(395), dp(613)), duration=0.7)
                anim.repeat = True

                anim2 = Animation(pos=(dp(380), dp(640)), duration=0.7)
                anim2 += Animation(pos=(dp(395), dp(640)), duration=0.7)
                anim2.repeat = True

                anim.start(get.root.ids.f_star_points.ids.fs_point)
                anim2.start(get.root.ids.f_counterfeit.ids.ccf_point)

            if get.root.ids.board.ids.field_16.text == "green":
                get.root.ids.f_counterfeit.ids.ccf_progress.value = 100
                get.root.ids.f_counterfeit.ids.ccf_progress_label.text = ""
                get.root.ids.f_counterfeit.ids.ccf_claim.opacity = 1
                get.root.ids.f_counterfeit.ids.ccf_point.opacity = 1
                get.root.ids.f_counterfeit.ids.ccf_point.source = 'images/claim_point_2.png'
                get.root.ids.f_counterfeit.ids.ccf_point.size = dp(30), dp(20)
                get.root.ids.f_counterfeit.ids.ccf_point.pos = dp(918), dp(640)
                get.root.ids.f_counterfeit.ids.ccf_claim.disabled = False
                get.root.ids.f_counterfeit.ids.ccf_claim.size = dp(50), dp(20)
                get.root.ids.f_counterfeit.ids.ccf_claim.pos = dp(958), dp(640)

                Animation.cancel_all(get.root.ids.f_star_points.ids.fs_point)

                anim = Animation(pos=(dp(918), dp(613)), duration=0.7)
                anim += Animation(pos=(dp(903), dp(613)), duration=0.7)
                anim.repeat = True

                anim2 = Animation(pos=(dp(918), dp(640)), duration=0.7)
                anim2 += Animation(pos=(dp(903), dp(640)), duration=0.7)
                anim2.repeat = True

                anim.start(get.root.ids.f_star_points.ids.fs_point)
                anim2.start(get.root.ids.f_counterfeit.ids.ccf_point)

    def progress_bar_pop(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "+200 $"
        if get.root.ids.board.ids.field_16.text == "purple":
            player_1_cash_count_g()
        if get.root.ids.board.ids.field_16.text == "green":
            player_2_cash_count_g()
        get.root.ids.f_counterfeit.ids.ccf_claim.disabled = True
        Clock.schedule_once(self.progress_bar_reset, 2)

    @staticmethod
    def progress_bar_reset(*args):
        get = App.get_running_app()
        hide_cash_count()

        if get.root.ids.board.ids.field_16.text == "purple":
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 200}"
        if get.root.ids.board.ids.field_16.text == "green":
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 200}"

        progress_1 = 0
        get.root.ids.f_counterfeit.ids.ccf_progress.value = 0
        get.root.ids.f_counterfeit.ids.ccf_progress_label.text = f"{int(progress_1)}%"
        get.root.ids.f_counterfeit.ids.ccf_claim.opacity = 0
        get.root.ids.f_counterfeit.ids.ccf_claim.size = dp(0), dp(0)
        get.root.ids.f_counterfeit.ids.ccf_claim.pos = dp(0), dp(0)
        get.root.ids.f_counterfeit.ids.ccf_point.opacity = 0
        get.root.ids.f_counterfeit.ids.ccf_point.size = dp(0), dp(0)
        get.root.ids.f_counterfeit.ids.ccf_point.pos = dp(0), dp(0)
        Animation.cancel_all(get.root.ids.f_counterfeit.ids.ccf_point)
        if get.root.ids.f_star_points.ids.fs_claim.opacity == 0:
            Animation.cancel_all(get.root.ids.f_star_points.ids.fs_point)

        money_update()

    def ccf_claim(self):
        self.progress_bar_pop()
        self.ids.ccf_claim.color = (1, 1, 1, 1)
        self.ids.ccf_claim.outline_color = (0, 0, 0, 1)

    def ccf_pressed(self):
        self.ids.ccf_claim.color = (0, 0, 0, 1)
        self.ids.ccf_claim.outline_color = (1, 1, 1, 1)


class PisaField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos16_x and y == p1_pos16_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos15_x and y == p1_pos15_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos14_x and y == p1_pos14_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos13_x and y == p1_pos13_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos12_x and y == p1_pos12_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos11_x and y == p1_pos11_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.5)

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_17.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_17.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_17.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = pisa_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 0:
            fee = 100
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 1:
            fee = 150
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 2:
            fee = 200
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 3:
            fee = 250
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money, 1.5)

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Leaning Pisa Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-400 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 400}"
        get.root.ids.board.ids.field_17.background_color = player_1_color
        get.root.ids.board.ids.field_17.text = "purple"

        money_update()
        unblock_roll()

    def player_1_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 0:
            fee = 100
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 1:
            fee = 150
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 2:
            fee = 200
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 3:
            fee = 250
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) - fee)}"
        player_1_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_1_move_label, 1.5)

    def player_1_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money, 1)

    def player_2_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 0:
            fee = 100
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 1:
            fee = 150
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 2:
            fee = 200
        if int(get.root.ids.f_shop.ids.pisa_count_2_2.text) == 3:
            fee = 250
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos16_x and y == p2_pos16_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos15_x and y == p2_pos15_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos14_x and y == p2_pos14_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos13_x and y == p2_pos13_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos12_x and y == p2_pos12_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos11_x and y == p2_pos11_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.5)

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_17.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_17.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_17.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = pisa_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 0:
            fee = 100
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 1:
            fee = 150
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 2:
            fee = 200
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 3:
            fee = 250
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money, 1.5)

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Leaning Pisa Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-400 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 400}"
        get.root.ids.board.ids.field_17.background_color = player_2_color
        get.root.ids.board.ids.field_17.text = "green"

        money_update()
        unblock_roll()

    def player_2_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 0:
            fee = 100
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 1:
            fee = 150
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 2:
            fee = 200
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 3:
            fee = 250
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) - fee)}"
        player_2_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_2_move_label, 1.5)

    def player_2_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money, 1)

    def player_1_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 0:
            fee = 100
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 1:
            fee = 150
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 2:
            fee = 200
        if int(get.root.ids.f_shop.ids.pisa_count_2.text) == 3:
            fee = 250
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class StarPointsField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos18_x and y == p1_pos18_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos17_x and y == p1_pos17_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos16_x and y == p1_pos16_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos15_x and y == p1_pos15_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos14_x and y == p1_pos14_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos13_x and y == p1_pos13_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.5)

        if get.root.ids.board.ids.field_19.text == "purple":
            self.progress_bar()

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_19.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_19.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_19.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = star_points_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    @staticmethod
    def player_1_opponent_owned(*args):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Player 2{'[/color]'} owns this property !"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Falling Star is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-300 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 300}"
        get.root.ids.board.ids.field_19.background_color = player_1_color
        get.root.ids.board.ids.field_19.text = "purple"
        get.root.ids.f_star_points.ids.fs_progress.opacity = 1
        get.root.ids.f_star_points.ids.fs_progress.size = dp(100), dp(23)
        get.root.ids.f_star_points.ids.fs_progress.pos = dp(212), dp(613)
        get.root.ids.f_star_points.ids.fs_progress_label.opacity = 1
        get.root.ids.f_star_points.ids.fs_progress_label.text = "0 %"
        get.root.ids.f_star_points.ids.fs_progress_label.size = dp(50), dp(20)
        get.root.ids.f_star_points.ids.fs_progress_label.pos = dp(318), dp(613)
        get.root.ids.f_star_points.ids.fs_progress_label.halign = "left"
        get.root.ids.f_star_points.ids.fs_image.opacity = 1
        get.root.ids.f_star_points.ids.fs_image.size = dp(23), dp(23)
        get.root.ids.f_star_points.ids.fs_image.pos = dp(180), dp(613)

        money_update()
        unblock_roll()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos18_x and y == p2_pos18_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos17_x and y == p2_pos17_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos16_x and y == p2_pos16_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos15_x and y == p2_pos15_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos14_x and y == p2_pos14_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos13_x and y == p2_pos13_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.5)

        if get.root.ids.board.ids.field_19.text == "green":
            self.progress_bar()

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_19.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_19.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_19.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = star_points_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    @staticmethod
    def player_2_opponent_owned(*args):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = f"{'[color=ff0000]'}Player 1{'[/color]'} owns this property !"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Falling Star is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-300 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()

        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 300}"
        get.root.ids.board.ids.field_19.background_color = player_2_color
        get.root.ids.board.ids.field_19.text = "green"
        get.root.ids.f_star_points.ids.fs_progress.opacity = 1
        get.root.ids.f_star_points.ids.fs_progress.size = dp(100), dp(23)
        get.root.ids.f_star_points.ids.fs_progress.pos = dp(1018), dp(613)
        get.root.ids.f_star_points.ids.fs_progress_label.opacity = 1
        get.root.ids.f_star_points.ids.fs_progress_label.text = "0 %"
        get.root.ids.f_star_points.ids.fs_progress_label.size = dp(50), dp(20)
        get.root.ids.f_star_points.ids.fs_progress_label.pos = dp(962), dp(613)
        get.root.ids.f_star_points.ids.fs_progress_label.halign = "right"
        get.root.ids.f_star_points.ids.fs_image.opacity = 1
        get.root.ids.f_star_points.ids.fs_image.size = dp(23), dp(23)
        get.root.ids.f_star_points.ids.fs_image.pos = dp(1127), dp(613)

        money_update()
        unblock_roll()

    # Both Players - General Functions

    @staticmethod
    def progress_bar(*args):
        get = App.get_running_app()
        progress_1 = get.root.ids.f_star_points.ids.fs_progress.value

        if get.root.ids.board.ids.dice.text == "1":
            progress_1 += 2
            get.root.ids.f_star_points.ids.fs_progress.value = progress_1
            get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "2":
            progress_1 += 4
            get.root.ids.f_star_points.ids.fs_progress.value = progress_1
            get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "3":
            progress_1 += 6
            get.root.ids.f_star_points.ids.fs_progress.value = progress_1
            get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "4":
            progress_1 += 8
            get.root.ids.f_star_points.ids.fs_progress.value = progress_1
            get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "5":
            progress_1 += 10
            get.root.ids.f_star_points.ids.fs_progress.value = progress_1
            get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"
        if get.root.ids.board.ids.dice.text == "6":
            progress_1 += 20
            get.root.ids.f_star_points.ids.fs_progress.value = progress_1
            get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"

        if progress_1 >= 100:
            if get.root.ids.board.ids.field_19.text == "purple":
                get.root.ids.f_star_points.ids.fs_progress.value = 100
                get.root.ids.f_star_points.ids.fs_progress_label.text = ""
                get.root.ids.f_star_points.ids.fs_claim.opacity = 1
                get.root.ids.f_star_points.ids.fs_point.opacity = 1
                get.root.ids.f_star_points.ids.fs_point.size = dp(30), dp(20)
                get.root.ids.f_star_points.ids.fs_point.pos = dp(380), dp(613)
                get.root.ids.f_star_points.ids.fs_claim.disabled = False
                get.root.ids.f_star_points.ids.fs_claim.size = dp(50), dp(20)
                get.root.ids.f_star_points.ids.fs_claim.pos = dp(320), dp(613)

                Animation.cancel_all(get.root.ids.f_counterfeit.ids.ccf_point)

                anim = Animation(pos=(dp(380), dp(613)), duration=0.7)
                anim += Animation(pos=(dp(395), dp(613)), duration=0.7)
                anim.repeat = True

                anim2 = Animation(pos=(dp(380), dp(640)), duration=0.7)
                anim2 += Animation(pos=(dp(395), dp(640)), duration=0.7)
                anim2.repeat = True

                anim.start(get.root.ids.f_star_points.ids.fs_point)
                anim2.start(get.root.ids.f_counterfeit.ids.ccf_point)

            if get.root.ids.board.ids.field_19.text == "green":
                get.root.ids.f_star_points.ids.fs_progress.value = 100
                get.root.ids.f_star_points.ids.fs_progress_label.text = ""
                get.root.ids.f_star_points.ids.fs_claim.opacity = 1
                get.root.ids.f_star_points.ids.fs_point.opacity = 1
                get.root.ids.f_star_points.ids.fs_point.source = 'images/claim_point_2.png'
                get.root.ids.f_star_points.ids.fs_point.size = dp(30), dp(20)
                get.root.ids.f_star_points.ids.fs_point.pos = dp(918), dp(613)
                get.root.ids.f_star_points.ids.fs_claim.disabled = False
                get.root.ids.f_star_points.ids.fs_claim.size = dp(50), dp(20)
                get.root.ids.f_star_points.ids.fs_claim.pos = dp(958), dp(613)

                Animation.cancel_all(get.root.ids.f_star_points.ids.fs_point)

                anim = Animation(pos=(dp(918), dp(613)), duration=0.7)
                anim += Animation(pos=(dp(903), dp(613)), duration=0.7)
                anim.repeat = True

                anim2 = Animation(pos=(dp(918), dp(640)), duration=0.7)
                anim2 += Animation(pos=(dp(903), dp(640)), duration=0.7)
                anim2.repeat = True

                anim.start(get.root.ids.f_star_points.ids.fs_point)
                anim2.start(get.root.ids.f_counterfeit.ids.ccf_point)

    def progress_bar_pop(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.points_count.text = f"+{30} pts"
        if get.root.ids.board.ids.field_19.text == "purple":
            player_1_points_count()
            get.root.ids.p1.ids.p1_points_stash.text = \
                f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 30}"
        if get.root.ids.board.ids.field_19.text == "green":
            player_2_points_count()
            get.root.ids.p2.ids.p2_points_stash.text = \
                f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 30}"
        get.root.ids.f_star_points.ids.fs_claim.disabled = True
        Clock.schedule_once(self.progress_bar_reset, 2)

    @staticmethod
    def progress_bar_reset(*args):
        get = App.get_running_app()
        hide_points_count()

        progress_1 = 0
        get.root.ids.f_star_points.ids.fs_progress.value = 0
        get.root.ids.f_star_points.ids.fs_progress_label.text = f"{int(progress_1)}%"
        get.root.ids.f_star_points.ids.fs_claim.opacity = 0
        get.root.ids.f_star_points.ids.fs_claim.size = dp(0), dp(0)
        get.root.ids.f_star_points.ids.fs_claim.pos = dp(0), dp(0)
        get.root.ids.f_star_points.ids.fs_point.opacity = 0
        get.root.ids.f_star_points.ids.fs_point.size = dp(0), dp(0)
        get.root.ids.f_star_points.ids.fs_point.pos = dp(0), dp(0)
        Animation.cancel_all(get.root.ids.f_star_points.ids.fs_point)
        if get.root.ids.f_counterfeit.ids.ccf_claim.opacity == 0:
            Animation.cancel_all(get.root.ids.f_counterfeit.ids.ccf_point)

        money_update()

    def fs_claim(self):
        self.progress_bar_pop()
        self.ids.fs_claim.color = (1, 1, 1, 1)
        self.ids.fs_claim.outline_color = (0, 0, 0, 1)

    def fs_pressed(self):
        self.ids.fs_claim.color = (0, 0, 0, 1)
        self.ids.fs_claim.outline_color = (1, 1, 1, 1)


class MoveBackField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos19_x and y == p1_pos19_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.choice, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos18_x and y == p1_pos18_y:
                Clock.schedule_once(self.text, 0.7)
                Clock.schedule_once(self.choice, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos17_x and y == p1_pos17_y:
                Clock.schedule_once(self.text, 0.9)
                Clock.schedule_once(self.choice, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos16_x and y == p1_pos16_y:
                Clock.schedule_once(self.text, 1.1)
                Clock.schedule_once(self.choice, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos15_x and y == p1_pos15_y:
                Clock.schedule_once(self.text, 1.3)
                Clock.schedule_once(self.choice, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos14_x and y == p1_pos14_y:
                Clock.schedule_once(self.text, 1.5)
                Clock.schedule_once(self.choice, 1.5)

    @staticmethod
    def player_1_move_anim(*args):
        get = App.get_running_app()
        pl_1 = get.root.ids.p1.ids.player_1
        pl_1_anim = Animation(pos=(dp(p1_pos20_x), dp(p1_pos17_y)), duration=0.7)
        pl_1_anim += Animation(pos=(dp(p1_pos14_x), dp(p1_pos14_y)), duration=0.8)
        pl_1_anim += Animation(pos=(dp(p1_pos14_x), dp(120)), duration=0.5)
        pl_1_anim.start(pl_1)
        unblock_roll()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos19_x and y == p2_pos19_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.choice, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos18_x and y == p2_pos18_y:
                Clock.schedule_once(self.text, 0.7)
                Clock.schedule_once(self.choice, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos17_x and y == p2_pos17_y:
                Clock.schedule_once(self.text, 0.9)
                Clock.schedule_once(self.choice, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos16_x and y == p2_pos16_y:
                Clock.schedule_once(self.text, 1.1)
                Clock.schedule_once(self.choice, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos15_x and y == p2_pos15_y:
                Clock.schedule_once(self.text, 1.3)
                Clock.schedule_once(self.choice, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos14_x and y == p2_pos14_y:
                Clock.schedule_once(self.text, 1.5)
                Clock.schedule_once(self.choice, 1.5)

    @staticmethod
    def player_2_move_anim(*args):
        get = App.get_running_app()
        pl_2 = get.root.ids.p2.ids.player_2
        pl_2_anim = Animation(pos=(dp(p2_pos20_x), dp(p2_pos17_y)), duration=0.7)
        pl_2_anim += Animation(pos=(dp(p2_pos14_x), dp(p2_pos14_y)), duration=0.8)
        pl_2_anim += Animation(pos=(dp(p2_pos14_x), dp(120)), duration=0.5)
        pl_2_anim.start(pl_2)
        unblock_roll()

    # Both Players - General Functions

    @staticmethod
    def text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = move_back_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def choice(*args):
        get = App.get_running_app()
        if get.root.ids.p1.ids.turn_1.active:
            get.root.ids.p1.ids.player_1_yes.disabled = False
            get.root.ids.p1.ids.yes_button_image.opacity = 1
            get.root.ids.p1.ids.player_1_no.disabled = False
            get.root.ids.p1.ids.no_button_image.opacity = 1
        if get.root.ids.p2.ids.turn_2.active:
            get.root.ids.p2.ids.player_2_yes.disabled = False
            get.root.ids.p2.ids.yes_button_image.opacity = 1
            get.root.ids.p2.ids.player_2_no.disabled = False
            get.root.ids.p2.ids.no_button_image.opacity = 1

    def yes(self):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-100 $"
        if get.root.ids.p1.ids.turn_1.active:
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 100}"
            player_1_cash_count_r()
        if get.root.ids.p2.ids.turn_2.active:
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 100}"
            player_2_cash_count_r()
        Clock.schedule_once(self.end, 3)

    @staticmethod
    def end(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class WinCashField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos20_x and y == p1_pos20_y:
                Clock.schedule_once(self.player_1_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos19_x and y == p1_pos19_y:
                Clock.schedule_once(self.player_1_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos18_x and y == p1_pos18_y:
                Clock.schedule_once(self.player_1_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos17_x and y == p1_pos17_y:
                Clock.schedule_once(self.player_1_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos16_x and y == p1_pos16_y:
                Clock.schedule_once(self.player_1_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos15_x and y == p1_pos15_y:
                Clock.schedule_once(self.player_1_main, 1.5)

    @staticmethod
    def player_1_main(*args):
        get = App.get_running_app()
        random_luck = randint(0, 7)
        get.root.ids.board.ids.big.font_size = 40
        get.root.ids.board.ids.big.valign = "middle"

        def money(*args):
            if random_luck == 0:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 150}"
            if random_luck == 1:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 100}"
            if random_luck == 2:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 50}"
            if random_luck == 3:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 70}"
            if random_luck == 4:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 25}"
            if random_luck == 5:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 30}"
            if random_luck == 6:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 15}"
            if random_luck == 7:
                get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 40}"
            unblock_roll()

        if random_luck == 0:
            get.root.ids.board.ids.big.text = win_cash[0]
            get.root.ids.board.ids.cash_count.text = "+150 $"
            player_1_cash_count_g()

        if random_luck == 1:
            get.root.ids.board.ids.big.text = win_cash[1]
            get.root.ids.board.ids.cash_count.text = "+100 $"
            player_1_cash_count_g()

        if random_luck == 2:
            get.root.ids.board.ids.big.text = win_cash[2]
            get.root.ids.board.ids.cash_count.text = "+50 $"
            player_1_cash_count_g()

        if random_luck == 3:
            get.root.ids.board.ids.big.text = win_cash[3]
            get.root.ids.board.ids.cash_count.text = "+70 $"
            player_1_cash_count_g()

        if random_luck == 4:
            get.root.ids.board.ids.big.text = win_cash[4]
            get.root.ids.board.ids.cash_count.text = "+25 $"
            player_1_cash_count_g()

        if random_luck == 5:
            get.root.ids.board.ids.big.text = win_cash[5]
            get.root.ids.board.ids.cash_count.text = "+30 $"
            player_1_cash_count_g()

        if random_luck == 6:
            get.root.ids.board.ids.big.text = win_cash[6]
            get.root.ids.board.ids.cash_count.text = "+15 $"
            player_1_cash_count_g()

        if random_luck == 7:
            get.root.ids.board.ids.big.text = win_cash[7]
            get.root.ids.board.ids.cash_count.text = "+40 $"
            player_1_cash_count_g()

        Clock.schedule_once(hide_cash_count, 2.5)
        Clock.schedule_once(money, 2.5)
        Clock.schedule_once(money_update, 2.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos20_x and y == p2_pos20_y:
                Clock.schedule_once(self.player_2_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos19_x and y == p2_pos19_y:
                Clock.schedule_once(self.player_2_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos18_x and y == p2_pos18_y:
                Clock.schedule_once(self.player_2_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos17_x and y == p2_pos17_y:
                Clock.schedule_once(self.player_2_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos16_x and y == p2_pos16_y:
                Clock.schedule_once(self.player_2_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos15_x and y == p2_pos15_y:
                Clock.schedule_once(self.player_2_main, 1.5)

    @staticmethod
    def player_2_main(*args):
        get = App.get_running_app()
        random_luck = randint(0, 7)
        get.root.ids.board.ids.big.font_size = 40
        get.root.ids.board.ids.big.valign = "middle"

        def money(*args):
            if random_luck == 0:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 150}"
            if random_luck == 1:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 100}"
            if random_luck == 2:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 50}"
            if random_luck == 3:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 70}"
            if random_luck == 4:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 25}"
            if random_luck == 5:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 30}"
            if random_luck == 6:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 15}"
            if random_luck == 7:
                get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 40}"
            unblock_roll()

        if random_luck == 0:
            get.root.ids.board.ids.big.text = win_cash[0]
            get.root.ids.board.ids.cash_count.text = "+150 $"
            player_2_cash_count_g()

        if random_luck == 1:
            get.root.ids.board.ids.big.text = win_cash[1]
            get.root.ids.board.ids.cash_count.text = "+100 $"
            player_2_cash_count_g()

        if random_luck == 2:
            get.root.ids.board.ids.big.text = win_cash[2]
            get.root.ids.board.ids.cash_count.text = "+50 $"
            player_2_cash_count_g()

        if random_luck == 3:
            get.root.ids.board.ids.big.text = win_cash[3]
            get.root.ids.board.ids.cash_count.text = "+70 $"
            player_2_cash_count_g()

        if random_luck == 4:
            get.root.ids.board.ids.big.text = win_cash[4]
            get.root.ids.board.ids.cash_count.text = "+25 $"
            player_2_cash_count_g()

        if random_luck == 5:
            get.root.ids.board.ids.big.text = win_cash[5]
            get.root.ids.board.ids.cash_count.text = "+30 $"
            player_2_cash_count_g()

        if random_luck == 6:
            get.root.ids.board.ids.big.text = win_cash[6]
            get.root.ids.board.ids.cash_count.text = "+15 $"
            player_2_cash_count_g()

        if random_luck == 7:
            get.root.ids.board.ids.big.text = win_cash[7]
            get.root.ids.board.ids.cash_count.text = "+40 $"
            player_2_cash_count_g()

        Clock.schedule_once(hide_cash_count, 2.5)
        Clock.schedule_once(money, 2.5)
        Clock.schedule_once(money_update, 2.5)


class SydneyField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos21_x and y == p1_pos21_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos20_x and y == p1_pos20_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos19_x and y == p1_pos19_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos18_x and y == p1_pos18_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos17_x and y == p1_pos17_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos16_x and y == p1_pos16_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.5)

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_22.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_22.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_22.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = sydney_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 0:
            fee = 130
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 1:
            fee = 200
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 2:
            fee = 250
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 3:
            fee = 300
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money, 1.5)

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Sydney Opera is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-520 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 520}"
        get.root.ids.board.ids.field_22.background_color = player_1_color
        get.root.ids.board.ids.field_22.text = "purple"

        money_update()
        unblock_roll()

    def player_1_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 0:
            fee = 130
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 1:
            fee = 200
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 2:
            fee = 250
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 3:
            fee = 300
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) - fee)}"
        player_1_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_1_move_label, 1.5)

    def player_1_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money, 1)

    def player_2_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 0:
            fee = 130
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 1:
            fee = 200
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 2:
            fee = 250
        if int(get.root.ids.f_shop.ids.sydney_count_2_2.text) == 3:
            fee = 300
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos21_x and y == p2_pos21_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos20_x and y == p2_pos20_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos19_x and y == p2_pos19_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos18_x and y == p2_pos18_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos17_x and y == p2_pos17_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos16_x and y == p2_pos16_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.5)

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_22.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_22.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_22.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = sydney_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 0:
            fee = 130
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 1:
            fee = 200
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 2:
            fee = 250
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 3:
            fee = 300
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money, 1.5)

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Sydney Opera is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-520 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 520}"
        get.root.ids.board.ids.field_22.background_color = player_2_color
        get.root.ids.board.ids.field_22.text = "green"

        money_update()
        unblock_roll()

    def player_2_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 0:
            fee = 130
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 1:
            fee = 200
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 2:
            fee = 250
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 3:
            fee = 300
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) - fee)}"
        player_2_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_2_move_label, 1.5)

    def player_2_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money, 1)

    def player_1_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 0:
            fee = 130
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 1:
            fee = 200
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 2:
            fee = 250
        if int(get.root.ids.f_shop.ids.sydney_count_2.text) == 3:
            fee = 300
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class BlackFridayField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos22_x and y == p1_pos22_y:
                Clock.schedule_once(self.text, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos21_x and y == p1_pos21_y:
                Clock.schedule_once(self.text, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos20_x and y == p1_pos20_y:
                Clock.schedule_once(self.text, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos19_x and y == p1_pos19_y:
                Clock.schedule_once(self.text, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos18_x and y == p1_pos18_y:
                Clock.schedule_once(self.text, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos17_x and y == p1_pos17_y:
                Clock.schedule_once(self.text, 1.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos22_x and y == p2_pos22_y:
                Clock.schedule_once(self.text, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos21_x and y == p2_pos21_y:
                Clock.schedule_once(self.text, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos20_x and y == p2_pos20_y:
                Clock.schedule_once(self.text, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos19_x and y == p2_pos19_y:
                Clock.schedule_once(self.text, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos18_x and y == p2_pos18_y:
                Clock.schedule_once(self.text, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos17_x and y == p2_pos17_y:
                Clock.schedule_once(self.text, 1.5)

    # Both Players - General Functions

    @staticmethod
    def text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = black_friday
        get.root.ids.board.ids.big.valign = "middle"
        get.root.ids.board.ids.big.font_size = 35
        unblock_roll()


class CardsWarField(Widget):
    tries = NumericProperty(0)
    play_1 = NumericProperty(0)
    play_2 = NumericProperty(0)

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos23_x and y == p1_pos23_y:
                Clock.schedule_once(self.show_text, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos22_x and y == p1_pos22_y:
                Clock.schedule_once(self.show_text, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos21_x and y == p1_pos21_y:
                Clock.schedule_once(self.show_text, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos20_x and y == p1_pos20_y:
                Clock.schedule_once(self.show_text, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos19_x and y == p1_pos19_y:
                Clock.schedule_once(self.show_text, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos18_x and y == p1_pos18_y:
                Clock.schedule_once(self.show_text, 1.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos23_x and y == p2_pos23_y:
                Clock.schedule_once(self.show_text, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos22_x and y == p2_pos22_y:
                Clock.schedule_once(self.show_text, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos21_x and y == p2_pos21_y:
                Clock.schedule_once(self.show_text, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos20_x and y == p2_pos20_y:
                Clock.schedule_once(self.show_text, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos19_x and y == p2_pos19_y:
                Clock.schedule_once(self.show_text, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos18_x and y == p2_pos18_y:
                Clock.schedule_once(self.show_text, 1.5)

    # Both Players - General Functions

    def show_text(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = cards_war
        get.root.ids.board.ids.big.valign = "middle"
        get.root.ids.board.ids.big.font_size = 30

        Clock.schedule_once(self.show_board, 3)

    @staticmethod
    def show_board(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.opacity = 0

        get.root.ids.f_cards_war.ids.player_1_card.opacity = 1
        get.root.ids.f_cards_war.ids.player_1_card.source = "card_deck/card_back.png"
        get.root.ids.f_cards_war.ids.player_1_card.size = dp(120), dp(170)
        get.root.ids.f_cards_war.ids.player_1_card.pos = dp(420), dp(250)

        get.root.ids.f_cards_war.ids.player_2_card.opacity = 1
        get.root.ids.f_cards_war.ids.player_2_card.source = "card_deck/card_back.png"
        get.root.ids.f_cards_war.ids.player_2_card.size = dp(120), dp(170)
        get.root.ids.f_cards_war.ids.player_2_card.pos = dp(775), dp(250)

        get.root.ids.f_cards_war.ids.player_1_draw.opacity = 1
        get.root.ids.f_cards_war.ids.player_1_draw.disabled = False
        get.root.ids.f_cards_war.ids.player_1_draw.size = dp(155), dp(35)
        get.root.ids.f_cards_war.ids.player_1_draw.pos = dp(580), dp(250)

        get.root.ids.f_cards_war.ids.card_label.opacity = 1
        get.root.ids.f_cards_war.ids.card_label.text = "0"
        get.root.ids.f_cards_war.ids.card_label.size = dp(80), dp(45)
        get.root.ids.f_cards_war.ids.card_label.pos = dp(618), dp(420)

        get.root.ids.f_cards_war.ids.player_1_card_score.opacity = 1
        get.root.ids.f_cards_war.ids.player_1_card_score.text = "0"
        get.root.ids.f_cards_war.ids.player_1_card_score.size = dp(60), dp(60)
        get.root.ids.f_cards_war.ids.player_1_card_score.pos = dp(560), dp(330)

        get.root.ids.f_cards_war.ids.player_2_card_score.opacity = 1
        get.root.ids.f_cards_war.ids.player_2_card_score.text = "0"
        get.root.ids.f_cards_war.ids.player_2_card_score.size = dp(60), dp(60)
        get.root.ids.f_cards_war.ids.player_2_card_score.pos = dp(695), dp(330)

    def draw_cards(self):
        get = App.get_running_app()

        p1_cards = randint(0, 53)
        p2_cards = randint(0, 53)
        self.tries += 1

        get.root.ids.f_cards_war.ids.player_1_card.source = card_deck[p1_cards]
        get.root.ids.f_cards_war.ids.player_2_card.source = card_deck[p2_cards]

        card = 0
        card_2 = 0

        if 0 <= p1_cards <= 3:
            card = 2
        if 3 < p1_cards <= 7:
            card = 3
        if 7 < p1_cards <= 11:
            card = 4
        if 11 < p1_cards <= 15:
            card = 5
        if 15 < p1_cards <= 19:
            card = 6
        if 19 < p1_cards <= 23:
            card = 7
        if 23 < p1_cards <= 27:
            card = 8
        if 27 < p1_cards <= 31:
            card = 9
        if 31 < p1_cards <= 35:
            card = 10
        if 35 < p1_cards <= 39:
            card = 11
        if 39 < p1_cards <= 43:
            card = 12
        if 43 < p1_cards <= 47:
            card = 13
        if 47 < p1_cards <= 51:
            card = 14
        if p1_cards == 52 or p1_cards == 53:
            card = 15

        if 0 <= p2_cards <= 3:
            card_2 = 2
        if 3 < p2_cards <= 7:
            card_2 = 3
        if 7 < p2_cards <= 11:
            card_2 = 4
        if 11 < p2_cards <= 15:
            card_2 = 5
        if 15 < p2_cards <= 19:
            card_2 = 6
        if 19 < p2_cards <= 23:
            card_2 = 7
        if 23 < p2_cards <= 27:
            card_2 = 8
        if 27 < p2_cards <= 31:
            card_2 = 9
        if 31 < p2_cards <= 35:
            card_2 = 10
        if 35 < p2_cards <= 39:
            card_2 = 11
        if 39 < p2_cards <= 43:
            card_2 = 12
        if 43 < p2_cards <= 47:
            card_2 = 13
        if 47 < p2_cards <= 51:
            card_2 = 14
        if p2_cards == 52 or p2_cards == 53:
            card_2 = 15

        if card > card_2:
            self.play_1 += 1
            get.root.ids.f_cards_war.ids.player_1_card_score.text = f"{self.play_1}"
        if card_2 > card:
            self.play_2 += 1
            get.root.ids.f_cards_war.ids.player_2_card_score.text = f"{self.play_2}"
        if card == card_2:
            self.tries -= 1

        get.root.ids.f_cards_war.ids.card_label.text = f"{self.tries}"

        if get.root.ids.f_cards_war.ids.card_label.text == "3":
            get.root.ids.f_cards_war.ids.player_1_draw.disabled = True
            Clock.schedule_once(self.reset_all, 1.5)

    def reset_all(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.opacity = 1

        get.root.ids.f_cards_war.ids.player_1_card.opacity = 0
        get.root.ids.f_cards_war.ids.player_1_card.size = dp(0), dp(0)
        get.root.ids.f_cards_war.ids.player_1_card.pos = dp(0), dp(0)

        get.root.ids.f_cards_war.ids.player_2_card.opacity = 0
        get.root.ids.f_cards_war.ids.player_2_card.size = dp(0), dp(0)
        get.root.ids.f_cards_war.ids.player_2_card.pos = dp(0), dp(0)

        get.root.ids.f_cards_war.ids.player_1_draw.opacity = 0
        get.root.ids.f_cards_war.ids.player_1_draw.size = dp(0), dp(0)
        get.root.ids.f_cards_war.ids.player_1_draw.pos = dp(0), dp(0)

        get.root.ids.f_cards_war.ids.card_label.opacity = 0
        get.root.ids.f_cards_war.ids.card_label.size = dp(0), dp(0)
        get.root.ids.f_cards_war.ids.card_label.pos = dp(0), dp(0)

        get.root.ids.f_cards_war.ids.player_1_card_score.opacity = 0
        get.root.ids.f_cards_war.ids.player_1_card_score.size = dp(0), dp(0)
        get.root.ids.f_cards_war.ids.player_1_card_score.pos = dp(0), dp(0)

        get.root.ids.f_cards_war.ids.player_2_card_score.opacity = 0
        get.root.ids.f_cards_war.ids.player_2_card_score.size = dp(0), dp(0)
        get.root.ids.f_cards_war.ids.player_2_card_score.pos = dp(0), dp(0)

        if self.play_1 == 3:
            get.root.ids.board.ids.big.text = f"Player 1 won 3 times so they take 300 $ from Player 2!"
            get.root.ids.board.ids.cash_count.text = "+300 $"
        if self.play_1 == 2:
            get.root.ids.board.ids.big.text = f"Player 1 won 2 times so they take 200 $ from Player 2!"
            get.root.ids.board.ids.cash_count.text = "+200 $"

        if self.play_2 == 3:
            get.root.ids.board.ids.big.text = f"Player 2 won 3 times so they take 300 $ from Player 1!"
            get.root.ids.board.ids.cash_count.text = "+300 $"
        if self.play_2 == 2:
            get.root.ids.board.ids.big.text = f"Player 2 won 2 times so they take 200 $ from Player 1!"
            get.root.ids.board.ids.cash_count.text = "+200 $"

        Clock.schedule_once(self.money_anim, 1)

    def money_anim(self, *args):
        get = App.get_running_app()

        def player_1_300(*args):
            get.root.ids.board.ids.cash_count.text = "+250 $"
            player_1_cash_count_g()
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 250}"
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)
            Clock.schedule_once(unblock_roll, 1.5)

        def player_1_200(*args):
            get.root.ids.board.ids.cash_count.text = "+150 $"
            player_1_cash_count_g()
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) + 150}"
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)
            Clock.schedule_once(unblock_roll, 1.5)

        def player_2_300(*args):
            get.root.ids.board.ids.cash_count.text = "+250 $"
            player_2_cash_count_g()
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 250}"
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)
            Clock.schedule_once(unblock_roll, 1.5)

        def player_2_200(*args):
            get.root.ids.board.ids.cash_count.text = "+150 $"
            player_2_cash_count_g()
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) + 150}"
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)
            Clock.schedule_once(unblock_roll, 1.5)

        if self.play_1 == 3:
            get.root.ids.board.ids.cash_count.text = "-250 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 250}"
            player_2_cash_count_r()
            Clock.schedule_once(player_1_300, 2)
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)

        if self.play_1 == 2:
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 150}"
            player_2_cash_count_r()
            Clock.schedule_once(player_1_200, 2)
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)

        if self.play_2 == 3:
            get.root.ids.board.ids.cash_count.text = "-250 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 250}"
            player_1_cash_count_r()
            Clock.schedule_once(player_2_300, 2)
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)

        if self.play_2 == 2:
            get.root.ids.board.ids.cash_count.text = "-150 $"
            get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 150}"
            player_1_cash_count_r()
            Clock.schedule_once(player_2_200, 2)
            Clock.schedule_once(hide_cash_count, 1.5)
            Clock.schedule_once(money_update, 1.5)

        self.play_1 = 0
        self.play_2 = 0
        self.tries = 0


class ChancePointsField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos24_x and y == p1_pos24_y:
                Clock.schedule_once(self.player_1_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos23_x and y == p1_pos23_y:
                Clock.schedule_once(self.player_1_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos22_x and y == p1_pos22_y:
                Clock.schedule_once(self.player_1_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos21_x and y == p1_pos21_y:
                Clock.schedule_once(self.player_1_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos20_x and y == p1_pos20_y:
                Clock.schedule_once(self.player_1_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos19_x and y == p1_pos19_y:
                Clock.schedule_once(self.player_1_main, 1.5)

    @staticmethod
    def player_1_main(*args):
        get = App.get_running_app()
        random_luck = randint(0, 9)
        get.root.ids.board.ids.big.font_size = 40
        get.root.ids.board.ids.big.valign = "middle"

        def points(*args):
            if random_luck == 0:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 10}"
            if random_luck == 1:
                if int(get.root.ids.p1.ids.p1_points_stash.text) - 10 < 0:
                    get.root.ids.p1.ids.p1_points_stash.text = "0"
                else:
                    get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 10}"
            if random_luck == 2:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 20}"
            if random_luck == 3:
                if int(get.root.ids.p1.ids.p1_points_stash.text) - 20 < 0:
                    get.root.ids.p1.ids.p1_points_stash.text = "0"
                else:
                    get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 20}"
            if random_luck == 4:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 25}"
            if random_luck == 5:
                if int(get.root.ids.p1.ids.p1_points_stash.text) - 25 < 0:
                    get.root.ids.p1.ids.p1_points_stash.text = "0"
                else:
                    get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 25}"
            if random_luck == 6:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 30}"
            if random_luck == 7:
                if int(get.root.ids.p1.ids.p1_points_stash.text) - 30 < 0:
                    get.root.ids.p1.ids.p1_points_stash.text = "0"
                else:
                    get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 30}"
            if random_luck == 8:
                get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) + 40}"
            if random_luck == 9:
                if int(get.root.ids.p1.ids.p1_points_stash.text) - 40 < 0:
                    get.root.ids.p1.ids.p1_points_stash.text = "0"
                else:
                    get.root.ids.p1.ids.p1_points_stash.text = f"{int(get.root.ids.p1.ids.p1_points_stash.text) - 40}"
            unblock_roll()

        if random_luck == 0:
            get.root.ids.board.ids.big.text = points_luck[0]
            get.root.ids.board.ids.points_count.text = "+10 pts"
            player_1_points_count()

        if random_luck == 1:
            get.root.ids.board.ids.big.text = points_luck[1]
            get.root.ids.board.ids.points_count.text = "-10 pts"
            if int(get.root.ids.p1.ids.p1_points_stash.text) - 10 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p1.ids.p1_points_stash.text)} pts"
            player_1_points_count()

        if random_luck == 2:
            get.root.ids.board.ids.big.text = points_luck[2]
            get.root.ids.board.ids.points_count.text = "+20 pts"
            player_1_points_count()

        if random_luck == 3:
            get.root.ids.board.ids.big.text = points_luck[3]
            get.root.ids.board.ids.points_count.text = "-20 pts"
            if int(get.root.ids.p1.ids.p1_points_stash.text) - 20 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p1.ids.p1_points_stash.text)} pts"
            player_1_points_count()

        if random_luck == 4:
            get.root.ids.board.ids.big.text = points_luck[4]
            get.root.ids.board.ids.points_count.text = "+25 pts"
            player_1_points_count()

        if random_luck == 5:
            get.root.ids.board.ids.big.text = points_luck[5]
            get.root.ids.board.ids.points_count.text = "-25 pts"
            if int(get.root.ids.p1.ids.p1_points_stash.text) - 25 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p1.ids.p1_points_stash.text)} pts"
            player_1_points_count()

        if random_luck == 6:
            get.root.ids.board.ids.big.text = points_luck[6]
            get.root.ids.board.ids.points_count.text = "+30 pts"
            player_1_points_count()

        if random_luck == 7:
            get.root.ids.board.ids.big.text = points_luck[7]
            get.root.ids.board.ids.points_count.text = "-30 pts"
            if int(get.root.ids.p1.ids.p1_points_stash.text) - 30 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p1.ids.p1_points_stash.text)} pts"
            player_1_points_count()

        if random_luck == 8:
            get.root.ids.board.ids.big.text = points_luck[8]
            get.root.ids.board.ids.points_count.text = "+40 pts"
            player_1_points_count()

        if random_luck == 9:
            get.root.ids.board.ids.big.text = points_luck[9]
            get.root.ids.board.ids.points_count.text = "-40 pts"
            if int(get.root.ids.p1.ids.p1_points_stash.text) - 40 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p1.ids.p1_points_stash.text)} pts"
            player_1_points_count()

        Clock.schedule_once(hide_points_count, 2.5)
        Clock.schedule_once(points, 2.5)
        Clock.schedule_once(money_update, 2.5)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos24_x and y == p2_pos24_y:
                Clock.schedule_once(self.player_2_main, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos23_x and y == p2_pos23_y:
                Clock.schedule_once(self.player_2_main, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos22_x and y == p2_pos22_y:
                Clock.schedule_once(self.player_2_main, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos21_x and y == p2_pos21_y:
                Clock.schedule_once(self.player_2_main, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos20_x and y == p2_pos20_y:
                Clock.schedule_once(self.player_2_main, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos19_x and y == p2_pos19_y:
                Clock.schedule_once(self.player_2_main, 1.5)

    @staticmethod
    def player_2_main(*args):
        get = App.get_running_app()
        random_luck = randint(0, 9)
        get.root.ids.board.ids.big.font_size = 40
        get.root.ids.board.ids.big.valign = "middle"

        def points(*args):
            if random_luck == 0:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 10}"
            if random_luck == 1:
                if int(get.root.ids.p2.ids.p2_points_stash.text) - 10 < 0:
                    get.root.ids.p2.ids.p2_points_stash.text = "0"
                else:
                    get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 10}"
            if random_luck == 2:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 20}"
            if random_luck == 3:
                if int(get.root.ids.p2.ids.p2_points_stash.text) - 20 < 0:
                    get.root.ids.p2.ids.p2_points_stash.text = "0"
                else:
                    get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 20}"
            if random_luck == 4:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 25}"
            if random_luck == 5:
                if int(get.root.ids.p2.ids.p2_points_stash.text) - 25 < 0:
                    get.root.ids.p2.ids.p2_points_stash.text = "0"
                else:
                    get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 25}"
            if random_luck == 6:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 30}"
            if random_luck == 7:
                if int(get.root.ids.p2.ids.p2_points_stash.text) - 30 < 0:
                    get.root.ids.p2.ids.p2_points_stash.text = "0"
                else:
                    get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 30}"
            if random_luck == 8:
                get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) + 40}"
            if random_luck == 9:
                if int(get.root.ids.p2.ids.p2_points_stash.text) - 40 < 0:
                    get.root.ids.p2.ids.p2_points_stash.text = "0"
                else:
                    get.root.ids.p2.ids.p2_points_stash.text = f"{int(get.root.ids.p2.ids.p2_points_stash.text) - 40}"
            unblock_roll()

        if random_luck == 0:
            get.root.ids.board.ids.big.text = points_luck[0]
            get.root.ids.board.ids.points_count.text = "+10 pts"
            player_2_points_count()

        if random_luck == 1:
            get.root.ids.board.ids.big.text = points_luck[1]
            get.root.ids.board.ids.points_count.text = "-10 pts"
            if int(get.root.ids.p2.ids.p2_points_stash.text) - 10 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p2.ids.p2_points_stash.text)} pts"
            player_2_points_count()

        if random_luck == 2:
            get.root.ids.board.ids.big.text = points_luck[2]
            get.root.ids.board.ids.points_count.text = "+20 pts"
            player_2_points_count()

        if random_luck == 3:
            get.root.ids.board.ids.big.text = points_luck[3]
            get.root.ids.board.ids.points_count.text = "-20 pts"
            if int(get.root.ids.p2.ids.p2_points_stash.text) - 20 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p2.ids.p2_points_stash.text)} pts"
            player_2_points_count()

        if random_luck == 4:
            get.root.ids.board.ids.big.text = points_luck[4]
            get.root.ids.board.ids.points_count.text = "+25 pts"
            player_2_points_count()

        if random_luck == 5:
            get.root.ids.board.ids.big.text = points_luck[5]
            get.root.ids.board.ids.points_count.text = "-25 pts"
            if int(get.root.ids.p2.ids.p2_points_stash.text) - 25 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p2.ids.p2_points_stash.text)} pts"
            player_2_points_count()

        if random_luck == 6:
            get.root.ids.board.ids.big.text = points_luck[6]
            get.root.ids.board.ids.points_count.text = "+30 pts"
            player_2_points_count()

        if random_luck == 7:
            get.root.ids.board.ids.big.text = points_luck[7]
            get.root.ids.board.ids.points_count.text = "-30 pts"
            if int(get.root.ids.p2.ids.p2_points_stash.text) - 30 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p2.ids.p2_points_stash.text)} pts"
            player_2_points_count()

        if random_luck == 8:
            get.root.ids.board.ids.big.text = points_luck[8]
            get.root.ids.board.ids.points_count.text = "+40 pts"
            player_2_points_count()

        if random_luck == 9:
            get.root.ids.board.ids.big.text = points_luck[9]
            get.root.ids.board.ids.points_count.text = "-40 pts"
            if int(get.root.ids.p2.ids.p2_points_stash.text) - 40 < 0:
                get.root.ids.board.ids.points_count.text = f"-{int(get.root.ids.p2.ids.p2_points_stash.text)} pts"
            player_2_points_count()

        Clock.schedule_once(hide_points_count, 2.5)
        Clock.schedule_once(points, 2.5)
        Clock.schedule_once(money_update, 2.5)


class SkipDangerField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos25_x and y == p1_pos25_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.player_1_move_anim, 2.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos24_x and y == p1_pos24_y:
                Clock.schedule_once(self.text, 0.7)
                Clock.schedule_once(self.player_1_move_anim, 2.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos23_x and y == p1_pos23_y:
                Clock.schedule_once(self.text, 0.9)
                Clock.schedule_once(self.player_1_move_anim, 2.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos22_x and y == p1_pos22_y:
                Clock.schedule_once(self.text, 1.1)
                Clock.schedule_once(self.player_1_move_anim, 3.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos21_x and y == p1_pos21_y:
                Clock.schedule_once(self.text, 1.3)
                Clock.schedule_once(self.player_1_move_anim, 3.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos20_x and y == p1_pos20_y:
                Clock.schedule_once(self.text, 1.5)
                Clock.schedule_once(self.player_1_move_anim, 3.5)

    def player_1_move_anim(self, *args):
        get = App.get_running_app()
        pl_1 = get.root.ids.p1.ids.player_1
        pl_1_anim = Animation(pos=(dp(p1_pos34_x + 55), dp(p1_pos34_y)), duration=2.1)
        pl_1_anim += Animation(pos=(dp(p1_pos1_x), dp(p1_pos1_y)), duration=0.3)
        pl_1_anim.start(pl_1)

        Clock.schedule_once(self.player_1_salary, 2.4)

    @staticmethod
    def player_1_salary(*args):
        Salary.player_1_show_salary(f_salary)
        unblock_roll()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos25_x and y == p2_pos25_y:
                Clock.schedule_once(self.text, 0.5)
                Clock.schedule_once(self.player_2_move_anim, 2.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos24_x and y == p2_pos24_y:
                Clock.schedule_once(self.text, 0.7)
                Clock.schedule_once(self.player_2_move_anim, 2.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos23_x and y == p2_pos23_y:
                Clock.schedule_once(self.text, 0.9)
                Clock.schedule_once(self.player_2_move_anim, 2.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos22_x and y == p2_pos22_y:
                Clock.schedule_once(self.text, 1.1)
                Clock.schedule_once(self.player_2_move_anim, 3.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos21_x and y == p2_pos21_y:
                Clock.schedule_once(self.text, 1.3)
                Clock.schedule_once(self.player_2_move_anim, 3.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos20_x and y == p2_pos20_y:
                Clock.schedule_once(self.text, 1.5)
                Clock.schedule_once(self.player_2_move_anim, 3.5)

    def player_2_move_anim(self, *args):
        get = App.get_running_app()
        pl_2 = get.root.ids.p2.ids.player_2
        pl_2_anim = Animation(pos=(dp(p2_pos34_x + 37), dp(p2_pos34_y)), duration=2.1)
        pl_2_anim += Animation(pos=(dp(p2_pos1_x), dp(p2_pos1_y)), duration=0.3)
        pl_2_anim.start(pl_2)

        Clock.schedule_once(self.player_2_salary, 2.4)

    @staticmethod
    def player_2_salary(*args):
        Salary.player_2_show_salary(f_salary)
        unblock_roll()

    # Both Players - General Functions

    @staticmethod
    def text(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = skip_danger
        get.root.ids.board.ids.big.font_size = 35


class OpTowers(Widget):

    # Player 1 - Own Functions

    # Tower 1

    def player_1_tower_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos25_x and y == p1_pos25_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_1, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos24_x and y == p1_pos24_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_1, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos23_x and y == p1_pos23_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_1, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos22_x and y == p1_pos22_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_1, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos21_x and y == p1_pos21_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_1, 1.5)

    def player_1_determine_ownership_tower_1(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_27.text == "":
            self.player_1_not_owned_tower_1()
        if get.root.ids.board.ids.field_27.text == "purple":
            self.player_1_self_owned_tower_1()
        if get.root.ids.board.ids.field_27.text == "green":
            self.player_1_opponent_owned_tower_1()

    @staticmethod
    def player_1_not_owned_tower_1(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = tower_1
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned_tower_1(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned_tower_1(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_27.text == "green":
            perc = 10

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 25

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 30

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45

        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{perc} %{'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money_tower_1, 1.5)

    def player_1_buy_tower_1(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The First Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money_tower_1, 0.3)

    def player_1_schedule_money_tower_1(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-400 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money_tower_1, 3)

    @staticmethod
    def player_1_unschedule_money_tower_1(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 400}"
        get.root.ids.board.ids.field_27.background_color = player_1_color
        get.root.ids.board.ids.field_27.text = "purple"

        money_update()
        unblock_roll()

    def player_1_take_money_tower_1(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_27.text == "green":
            perc = 10/100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 25/100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 30/100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45/100

        get.root.ids.board.ids.cash_count.text = f"-{int(perc * int(get.root.ids.p1.ids.p1_money_stash.text))} $"

        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_move_label_tower_1, 1.5)

    def player_1_move_label_tower_1(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money_tower_1, 1)

    def player_2_give_money_tower_1(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_27.text == "green":
            perc = 10 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 25 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 30 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"+{int(perc * int(get.root.ids.p1.ids.p1_money_stash.text))} $"

        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_end_anim_tower_1, 1.8)

    @staticmethod
    def player_1_end_anim_tower_1(*args):
        get = App.get_running_app()
        hide_cash_count()

        perc = 0

        if get.root.ids.board.ids.field_27.text == "green":
            perc = 10 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 25 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 30 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        p1_res = int(
            int(get.root.ids.p1.ids.p1_money_stash.text) - perc * int(get.root.ids.p1.ids.p1_money_stash.text))
        p2_res = int(
            int(get.root.ids.p2.ids.p2_money_stash.text) + perc * int(get.root.ids.p1.ids.p1_money_stash.text))
        get.root.ids.p1.ids.p1_money_stash.text = f"{p1_res}"
        get.root.ids.p2.ids.p2_money_stash.text = f"{p2_res}"
        money_update()
        unblock_roll()

    # Tower 2

    def player_1_tower_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos28_x and y == p1_pos28_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_2, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos27_x and y == p1_pos27_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_2, 0.7)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos25_x and y == p1_pos25_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_2, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos24_x and y == p1_pos24_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_2, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos23_x and y == p1_pos23_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_2, 1.5)

    def player_1_determine_ownership_tower_2(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_29.text == "":
            self.player_1_not_owned_tower_2()
        if get.root.ids.board.ids.field_29.text == "purple":
            self.player_1_self_owned_tower_2()
        if get.root.ids.board.ids.field_29.text == "green":
            self.player_1_opponent_owned_tower_2()

    @staticmethod
    def player_1_not_owned_tower_2(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = tower_2
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned_tower_2(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned_tower_2(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_29.text == "green":
            perc = 15

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 25

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 35

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45

        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{perc} %{'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money_tower_2, 1.5)

    def player_1_buy_tower_2(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Second Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money_tower_2, 0.3)

    def player_1_schedule_money_tower_2(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-600 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money_tower_2, 3)

    @staticmethod
    def player_1_unschedule_money_tower_2(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 600}"
        get.root.ids.board.ids.field_29.background_color = player_1_color
        get.root.ids.board.ids.field_29.text = "purple"

        money_update()
        unblock_roll()

    def player_1_take_money_tower_2(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_29.text == "green":
            perc = 15 / 100

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 25 / 100

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"-{int(perc * int(get.root.ids.p1.ids.p1_money_stash.text))} $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_move_label_tower_2, 1.5)

    def player_1_move_label_tower_2(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money_tower_2, 1)

    def player_2_give_money_tower_2(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_29.text == "green":
            perc = 15 / 100

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 25 / 100

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"+{int(perc * int(get.root.ids.p1.ids.p1_money_stash.text))} $"

        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_end_anim_tower_2, 1.8)

    @staticmethod
    def player_1_end_anim_tower_2(*args):
        get = App.get_running_app()
        hide_cash_count()
        perc = 0

        if get.root.ids.board.ids.field_29.text == "green":
            perc = 15 / 100

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 25 / 100

        if get.root.ids.board.ids.field_29.text == "green" and get.root.ids.board.ids.field_31.text == "green":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        p1_res = int(
            int(get.root.ids.p1.ids.p1_money_stash.text) - perc * int(get.root.ids.p1.ids.p1_money_stash.text))
        p2_res = int(
            int(get.root.ids.p2.ids.p2_money_stash.text) + perc * int(get.root.ids.p1.ids.p1_money_stash.text))
        get.root.ids.p1.ids.p1_money_stash.text = f"{p1_res}"
        get.root.ids.p2.ids.p2_money_stash.text = f"{p2_res}"
        money_update()
        unblock_roll()

    # Tower 3

    def player_1_tower_3_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos30_x and y == p1_pos30_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_3, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos29_x and y == p1_pos29_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_3, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos28_x and y == p1_pos28_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_3, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos27_x and y == p1_pos27_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_3, 1.1)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos25_x and y == p1_pos25_y:
                Clock.schedule_once(self.player_1_determine_ownership_tower_3, 1.5)

    def player_1_determine_ownership_tower_3(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_31.text == "":
            self.player_1_not_owned_tower_3()
        if get.root.ids.board.ids.field_31.text == "purple":
            self.player_1_self_owned_tower_3()
        if get.root.ids.board.ids.field_31.text == "green":
            self.player_1_opponent_owned_tower_3()

    @staticmethod
    def player_1_not_owned_tower_3(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = tower_3
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned_tower_3(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned_tower_3(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_31.text == "green":
            perc = 20

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 30

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 35

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45

        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{perc} %{'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money_tower_3, 1.5)

    def player_1_buy_tower_3(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Third Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money_tower_3, 0.3)

    def player_1_schedule_money_tower_3(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-800 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money_tower_3, 3)

    @staticmethod
    def player_1_unschedule_money_tower_3(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 800}"
        get.root.ids.board.ids.field_31.background_color = player_1_color
        get.root.ids.board.ids.field_31.text = "purple"

        money_update()
        unblock_roll()

    def player_1_take_money_tower_3(self, *args):
        get = App.get_running_app()
        perc = 0
        if get.root.ids.board.ids.field_31.text == "green":
            perc = 20 / 100

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 30 / 100

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"-{int(perc * int(get.root.ids.p1.ids.p1_money_stash.text))} $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_move_label_tower_3, 1.5)

    def player_1_move_label_tower_3(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money_tower_3, 1)

    def player_2_give_money_tower_3(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_31.text == "green":
            perc = 20 / 100

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 30 / 100

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"+{int(perc * int(get.root.ids.p1.ids.p1_money_stash.text))} $"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_end_anim_tower_3, 1.8)

    @staticmethod
    def player_1_end_anim_tower_3(*args):
        get = App.get_running_app()
        hide_cash_count()
        perc = 0

        if get.root.ids.board.ids.field_31.text == "green":
            perc = 20 / 100

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_27.text == "green":
            perc = 30 / 100

        if get.root.ids.board.ids.field_31.text == "green" and get.root.ids.board.ids.field_29.text == "green":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "green" and get.root.ids.board.ids.field_29.text == "green" \
                and get.root.ids.board.ids.field_31.text == "green":
            perc = 45 / 100

        p1_res = int(
            int(get.root.ids.p1.ids.p1_money_stash.text) - perc * int(get.root.ids.p1.ids.p1_money_stash.text))
        p2_res = int(
            int(get.root.ids.p2.ids.p2_money_stash.text) + perc * int(get.root.ids.p1.ids.p1_money_stash.text))
        get.root.ids.p1.ids.p1_money_stash.text = f"{p1_res}"
        get.root.ids.p2.ids.p2_money_stash.text = f"{p2_res}"
        money_update()
        unblock_roll()

    # Player 2 - Own Functions

    # Tower 1

    def player_2_tower_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos25_x and y == p2_pos25_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_1, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos24_x and y == p2_pos24_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_1, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos23_x and y == p2_pos23_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_1, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos22_x and y == p2_pos22_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_1, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos21_x and y == p2_pos21_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_1, 1.5)

    def player_2_determine_ownership_tower_1(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_27.text == "":
            self.player_2_not_owned_tower_1()
        if get.root.ids.board.ids.field_27.text == "green":
            self.player_2_self_owned_tower_1()
        if get.root.ids.board.ids.field_27.text == "purple":
            self.player_2_opponent_owned_tower_1()

    @staticmethod
    def player_2_not_owned_tower_1(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = tower_1
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned_tower_1(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned_tower_1(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_27.text == "purple":
            perc = 10

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 25

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 30

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45

        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{perc} %{'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money_tower_1, 1.5)

    def player_2_buy_tower_1(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The First Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money_tower_1, 0.3)

    def player_2_schedule_money_tower_1(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-400 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money_tower_1, 3)

    @staticmethod
    def player_2_unschedule_money_tower_1(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 400}"
        get.root.ids.board.ids.field_27.background_color = player_2_color
        get.root.ids.board.ids.field_27.text = "green"

        money_update()
        unblock_roll()

    def player_2_take_money_tower_1(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_27.text == "purple":
            perc = 10 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 25 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 30 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"-{int(perc * int(get.root.ids.p2.ids.p2_money_stash.text))} $"

        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_move_label_tower_1, 1.5)

    def player_2_move_label_tower_1(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money_tower_1, 1)

    def player_1_give_money_tower_1(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_27.text == "purple":
            perc = 10 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 25 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 30 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"+{int(perc * int(get.root.ids.p2.ids.p2_money_stash.text))} $"

        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_end_anim_tower_1, 1.8)

    @staticmethod
    def player_2_end_anim_tower_1(*args):
        get = App.get_running_app()
        hide_cash_count()

        perc = 0

        if get.root.ids.board.ids.field_27.text == "purple":
            perc = 10 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 25 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 30 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        p2_res = int(
            int(get.root.ids.p2.ids.p2_money_stash.text) - perc * int(get.root.ids.p2.ids.p2_money_stash.text))
        p1_res = int(
            int(get.root.ids.p1.ids.p1_money_stash.text) + perc * int(get.root.ids.p2.ids.p2_money_stash.text))
        get.root.ids.p1.ids.p1_money_stash.text = f"{p1_res}"
        get.root.ids.p2.ids.p2_money_stash.text = f"{p2_res}"
        money_update()
        unblock_roll()

    # Tower 2

    def player_2_tower_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos28_x and y == p2_pos28_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_2, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos27_x and y == p2_pos27_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_2, 0.7)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos25_x and y == p2_pos25_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_2, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos24_x and y == p2_pos24_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_2, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos23_x and y == p2_pos23_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_2, 1.5)

    def player_2_determine_ownership_tower_2(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_29.text == "":
            self.player_2_not_owned_tower_2()
        if get.root.ids.board.ids.field_29.text == "green":
            self.player_2_self_owned_tower_2()
        if get.root.ids.board.ids.field_29.text == "purple":
            self.player_2_opponent_owned_tower_2()

    @staticmethod
    def player_2_not_owned_tower_2(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = tower_2
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned_tower_2(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned_tower_2(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_29.text == "purple":
            perc = 15

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 25

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 35

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45

        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{perc} %{'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money_tower_2, 1.5)

    def player_2_buy_tower_2(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Second Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money_tower_2, 0.3)

    def player_2_schedule_money_tower_2(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-600 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money_tower_2, 3)

    @staticmethod
    def player_2_unschedule_money_tower_2(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 600}"
        get.root.ids.board.ids.field_29.background_color = player_2_color
        get.root.ids.board.ids.field_29.text = "green"

        money_update()
        unblock_roll()

    def player_2_take_money_tower_2(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_29.text == "purple":
            perc = 15 / 100

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 25 / 100

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"-{int(perc * int(get.root.ids.p2.ids.p2_money_stash.text))} $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_move_label_tower_2, 1.5)

    def player_2_move_label_tower_2(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money_tower_2, 1)

    def player_1_give_money_tower_2(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_29.text == "purple":
            perc = 15 / 100

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 25 / 100

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"+{int(perc * int(get.root.ids.p2.ids.p2_money_stash.text))} $"

        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_end_anim_tower_2, 1.8)

    @staticmethod
    def player_2_end_anim_tower_2(*args):
        get = App.get_running_app()
        hide_cash_count()
        perc = 0

        if get.root.ids.board.ids.field_29.text == "purple":
            perc = 15 / 100

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 25 / 100

        if get.root.ids.board.ids.field_29.text == "purple" and get.root.ids.board.ids.field_31.text == "purple":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        p2_res = int(
            int(get.root.ids.p2.ids.p2_money_stash.text) - perc * int(get.root.ids.p2.ids.p2_money_stash.text))
        p1_res = int(
            int(get.root.ids.p1.ids.p1_money_stash.text) + perc * int(get.root.ids.p2.ids.p2_money_stash.text))
        get.root.ids.p1.ids.p1_money_stash.text = f"{p1_res}"
        get.root.ids.p2.ids.p2_money_stash.text = f"{p2_res}"
        money_update()
        unblock_roll()

    # Tower 3

    def player_2_tower_3_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos30_x and y == p2_pos30_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_3, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos29_x and y == p2_pos29_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_3, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos28_x and y == p2_pos28_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_3, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos27_x and y == p2_pos27_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_3, 1.1)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos25_x and y == p2_pos25_y:
                Clock.schedule_once(self.player_2_determine_ownership_tower_3, 1.5)

    def player_2_determine_ownership_tower_3(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_31.text == "":
            self.player_2_not_owned_tower_3()
        if get.root.ids.board.ids.field_31.text == "green":
            self.player_2_self_owned_tower_3()
        if get.root.ids.board.ids.field_31.text == "purple":
            self.player_2_opponent_owned_tower_3()

    @staticmethod
    def player_2_not_owned_tower_3(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = tower_3
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned_tower_3(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned_tower_3(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_31.text == "purple":
            perc = 20

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 30

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 35

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45

        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{perc} %{'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money_tower_3, 1.5)

    def player_2_buy_tower_3(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. The Third Tower is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money_tower_3, 0.3)

    def player_2_schedule_money_tower_3(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-800 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money_tower_3, 3)

    @staticmethod
    def player_2_unschedule_money_tower_3(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 800}"
        get.root.ids.board.ids.field_31.background_color = player_2_color
        get.root.ids.board.ids.field_31.text = "green"

        money_update()
        unblock_roll()

    def player_2_take_money_tower_3(self, *args):
        get = App.get_running_app()
        perc = 0
        if get.root.ids.board.ids.field_31.text == "purple":
            perc = 20 / 100

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 30 / 100

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"-{int(perc * int(get.root.ids.p2.ids.p2_money_stash.text))} $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_move_label_tower_3, 1.5)

    def player_2_move_label_tower_3(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money_tower_3, 1)

    def player_1_give_money_tower_3(self, *args):
        get = App.get_running_app()

        perc = 0
        if get.root.ids.board.ids.field_31.text == "purple":
            perc = 20 / 100

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 30 / 100

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        get.root.ids.board.ids.cash_count.text = f"+{int(perc * int(get.root.ids.p2.ids.p2_money_stash.text))} $"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_end_anim_tower_3, 1.8)

    @staticmethod
    def player_2_end_anim_tower_3(*args):
        get = App.get_running_app()
        hide_cash_count()
        perc = 0

        if get.root.ids.board.ids.field_31.text == "purple":
            perc = 20 / 100

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_27.text == "purple":
            perc = 30 / 100

        if get.root.ids.board.ids.field_31.text == "purple" and get.root.ids.board.ids.field_29.text == "purple":
            perc = 35 / 100

        if get.root.ids.board.ids.field_27.text == "purple" and get.root.ids.board.ids.field_29.text == "purple" \
                and get.root.ids.board.ids.field_31.text == "purple":
            perc = 45 / 100

        p2_res = int(
            int(get.root.ids.p2.ids.p2_money_stash.text) - perc * int(get.root.ids.p2.ids.p2_money_stash.text))
        p1_res = int(
            int(get.root.ids.p1.ids.p1_money_stash.text) + perc * int(get.root.ids.p2.ids.p2_money_stash.text))
        get.root.ids.p1.ids.p1_money_stash.text = f"{p1_res}"
        get.root.ids.p2.ids.p2_money_stash.text = f"{p2_res}"
        money_update()
        unblock_roll()


class SalaryBuilding(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos31_x and y == p1_pos31_y:
                Clock.schedule_once(self.player_1_determine_ownership_1, 0.5)
            if x == p1_pos33_x and y == p1_pos33_y:
                Clock.schedule_once(self.player_1_determine_ownership_2, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos30_x and y == p1_pos30_y:
                Clock.schedule_once(self.player_1_determine_ownership_1, 0.7)
            if x == p1_pos32_x and y == p1_pos32_y:
                Clock.schedule_once(self.player_1_determine_ownership_2, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos29_x and y == p1_pos29_y:
                Clock.schedule_once(self.player_1_determine_ownership_1, 0.9)
            if x == p1_pos31_x and y == p1_pos31_y:
                Clock.schedule_once(self.player_1_determine_ownership_2, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos28_x and y == p1_pos28_y:
                Clock.schedule_once(self.player_1_determine_ownership_1, 1.1)
            if x == p1_pos30_x and y == p1_pos30_y:
                Clock.schedule_once(self.player_1_determine_ownership_2, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos27_x and y == p1_pos27_y:
                Clock.schedule_once(self.player_1_determine_ownership_1, 1.3)
            if x == p1_pos29_x and y == p1_pos29_y:
                Clock.schedule_once(self.player_1_determine_ownership_2, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos28_x and y == p1_pos28_y:
                Clock.schedule_once(self.player_1_determine_ownership_2, 1.5)

    def player_1_determine_ownership_1(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_32.text == "":
            if not get.root.ids.board.ids.field_34.text == "purple":
                self.player_1_not_owned()
            else:
                get.root.ids.board.ids.big.text = "You cannot have your salary increased twice!"
                get.root.ids.board.ids.big.valign = "middle"
                unblock_roll()
        if get.root.ids.board.ids.field_32.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_32.text == "green":
            self.player_1_opponent_owned()

    def player_1_determine_ownership_2(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_34.text == "":
            if not get.root.ids.board.ids.field_32.text == "purple":
                self.player_1_not_owned()
            else:
                get.root.ids.board.ids.big.text = "You cannot have your salary increased twice!"
                get.root.ids.board.ids.big.valign = "middle"
                unblock_roll()
        if get.root.ids.board.ids.field_34.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_34.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = salary_building_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    @staticmethod
    def player_1_opponent_owned(*args):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = f"Player 2 owns this property!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. Your salary is now increased!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-500 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 500}"

        if x == p1_pos32_x and y == p1_pos32_y:
            get.root.ids.board.ids.field_32.background_color = player_1_color
            get.root.ids.board.ids.field_32.text = "purple"
        if x == p1_pos34_x and y == p1_pos34_y:
            get.root.ids.board.ids.field_34.background_color = player_1_color
            get.root.ids.board.ids.field_34.text = "purple"

        money_update()
        unblock_roll()

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos31_x and y == p2_pos31_y:
                Clock.schedule_once(self.player_2_determine_ownership_1, 0.5)
            if x == p2_pos33_x and y == p2_pos33_y:
                Clock.schedule_once(self.player_2_determine_ownership_2, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos30_x and y == p2_pos30_y:
                Clock.schedule_once(self.player_2_determine_ownership_1, 0.7)
            if x == p2_pos32_x and y == p2_pos32_y:
                Clock.schedule_once(self.player_2_determine_ownership_2, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos29_x and y == p2_pos29_y:
                Clock.schedule_once(self.player_2_determine_ownership_1, 0.9)
            if x == p2_pos31_x and y == p2_pos31_y:
                Clock.schedule_once(self.player_2_determine_ownership_2, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos28_x and y == p2_pos28_y:
                Clock.schedule_once(self.player_2_determine_ownership_1, 1.1)
            if x == p2_pos30_x and y == p2_pos30_y:
                Clock.schedule_once(self.player_2_determine_ownership_2, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos27_x and y == p2_pos27_y:
                Clock.schedule_once(self.player_2_determine_ownership_1, 1.3)
            if x == p2_pos29_x and y == p2_pos29_y:
                Clock.schedule_once(self.player_2_determine_ownership_2, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos28_x and y == p2_pos28_y:
                Clock.schedule_once(self.player_2_determine_ownership_2, 1.5)

    def player_2_determine_ownership_1(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_32.text == "":
            if not get.root.ids.board.ids.field_34.text == "green":
                self.player_2_not_owned()
            else:
                get.root.ids.board.ids.big.text = "You cannot have your salary increased twice!"
                get.root.ids.board.ids.big.valign = "middle"
                unblock_roll()
        if get.root.ids.board.ids.field_32.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_32.text == "purple":
            self.player_2_opponent_owned()

    def player_2_determine_ownership_2(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_34.text == "":
            if not get.root.ids.board.ids.field_32.text == "green":
                self.player_2_not_owned()
            else:
                get.root.ids.board.ids.big.text = "You cannot have your salary increased twice!"
                get.root.ids.board.ids.big.valign = "middle"
                unblock_roll()
        if get.root.ids.board.ids.field_34.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_34.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = salary_building_fields
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    @staticmethod
    def player_2_opponent_owned(*args):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = f"Player 1 owns this property!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. Your salary is now increased!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-500 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 500}"

        if x == p2_pos32_x and y == p2_pos32_y:
            get.root.ids.board.ids.field_32.background_color = player_2_color
            get.root.ids.board.ids.field_32.text = "green"
        if x == p2_pos34_x and y == p2_pos34_y:
            get.root.ids.board.ids.field_34.background_color = player_2_color
            get.root.ids.board.ids.field_34.text = "green"

        money_update()
        unblock_roll()


class LouvreField(Widget):

    # Player 1 - Own Functions

    def player_1_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p1.ids.player_1.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p1_pos32_x and y == p1_pos32_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p1_pos31_x and y == p1_pos31_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p1_pos30_x and y == p1_pos30_y:
                Clock.schedule_once(self.player_1_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p1_pos29_x and y == p1_pos29_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p1_pos28_x and y == p1_pos28_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p1_pos27_x and y == p1_pos27_y:
                Clock.schedule_once(self.player_1_determine_ownership, 1.5)

    def player_1_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_33.text == "":
            self.player_1_not_owned()
        if get.root.ids.board.ids.field_33.text == "purple":
            self.player_1_self_owned()
        if get.root.ids.board.ids.field_33.text == "green":
            self.player_1_opponent_owned()

    @staticmethod
    def player_1_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p1.ids.player_1_yes.disabled = False
        get.root.ids.p1.ids.yes_button_image.opacity = 1
        get.root.ids.p1.ids.player_1_no.disabled = False
        get.root.ids.p1.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = louvre
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_1_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_1_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 0:
            fee = 150
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 1:
            fee = 230
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 2:
            fee = 300
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 3:
            fee = 350
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 2 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_1_take_money, 1.5)

    def player_1_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. Le Louvre is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_1_schedule_money, 0.3)

    def player_1_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-600 $"
        player_1_cash_count_r()
        Clock.schedule_once(self.player_1_unschedule_money, 3)

    @staticmethod
    def player_1_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p1.ids.p1_money_stash.text = f"{int(get.root.ids.p1.ids.p1_money_stash.text) - 600}"
        get.root.ids.board.ids.field_33.background_color = player_1_color
        get.root.ids.board.ids.field_33.text = "purple"

        money_update()
        unblock_roll()

    def player_1_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 0:
            fee = 150
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 1:
            fee = 230
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 2:
            fee = 300
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 3:
            fee = 350
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) - fee)}"
        player_1_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_1_move_label, 1.5)

    def player_1_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(1055), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_2_give_money, 1)

    def player_2_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 0:
            fee = 150
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 1:
            fee = 230
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 2:
            fee = 300
        if int(get.root.ids.f_shop.ids.louvre_count_2_2.text) == 3:
            fee = 350
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Player 2 - Own Functions

    def player_2_trigger(self):
        get = App.get_running_app()
        x, y = get.root.ids.p2.ids.player_2.pos

        if get.root.ids.board.ids.dice.text == "1":
            if x == p2_pos32_x and y == p2_pos32_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.5)

        if get.root.ids.board.ids.dice.text == "2":
            if x == p2_pos31_x and y == p2_pos31_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.7)

        if get.root.ids.board.ids.dice.text == "3":
            if x == p2_pos30_x and y == p2_pos30_y:
                Clock.schedule_once(self.player_2_determine_ownership, 0.9)

        if get.root.ids.board.ids.dice.text == "4":
            if x == p2_pos29_x and y == p2_pos29_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.1)

        if get.root.ids.board.ids.dice.text == "5":
            if x == p2_pos28_x and y == p2_pos28_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.3)

        if get.root.ids.board.ids.dice.text == "6":
            if x == p2_pos27_x and y == p2_pos27_y:
                Clock.schedule_once(self.player_2_determine_ownership, 1.5)

    def player_2_determine_ownership(self, *args):
        get = App.get_running_app()

        if get.root.ids.board.ids.field_33.text == "":
            self.player_2_not_owned()
        if get.root.ids.board.ids.field_33.text == "green":
            self.player_2_self_owned()
        if get.root.ids.board.ids.field_33.text == "purple":
            self.player_2_opponent_owned()

    @staticmethod
    def player_2_not_owned(*args):
        get = App.get_running_app()

        get.root.ids.p2.ids.player_2_yes.disabled = False
        get.root.ids.p2.ids.yes_button_image.opacity = 1
        get.root.ids.p2.ids.player_2_no.disabled = False
        get.root.ids.p2.ids.no_button_image.opacity = 1
        get.root.ids.board.ids.big.text = louvre
        get.root.ids.board.ids.big.font_size = 30
        get.root.ids.board.ids.big.valign = "top"

    @staticmethod
    def player_2_self_owned(*args):
        get = App.get_running_app()
        get.root.ids.board.ids.big.text = "You are at home!"
        get.root.ids.board.ids.big.valign = "middle"
        unblock_roll()

    def player_2_opponent_owned(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 0:
            fee = 150
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 1:
            fee = 230
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 2:
            fee = 300
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 3:
            fee = 350
        get.root.ids.board.ids.big.text = \
            f"Oops, you have to pay {'[color=ff0000]'}{fee} ${'[/color]'} fee to Player 1 !"
        get.root.ids.board.ids.big.valign = "middle"
        Clock.schedule_once(self.player_2_take_money, 1.5)

    def player_2_buy(self):
        get = App.get_running_app()

        get.root.ids.board.ids.big.text = "Good Choice. Le Louvre is now yours!"
        get.root.ids.board.ids.big.valign = "middle"

        Clock.schedule_once(self.player_2_schedule_money, 0.3)

    def player_2_schedule_money(self, *args):
        get = App.get_running_app()
        get.root.ids.board.ids.cash_count.text = "-600 $"
        player_2_cash_count_r()
        Clock.schedule_once(self.player_2_unschedule_money, 3)

    @staticmethod
    def player_2_unschedule_money(*args):
        get = App.get_running_app()
        hide_cash_count()
        get.root.ids.p2.ids.p2_money_stash.text = f"{int(get.root.ids.p2.ids.p2_money_stash.text) - 600}"
        get.root.ids.board.ids.field_33.background_color = player_2_color
        get.root.ids.board.ids.field_33.text = "green"

        money_update()
        unblock_roll()

    def player_2_take_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 0:
            fee = 150
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 1:
            fee = 230
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 2:
            fee = 300
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 3:
            fee = 350
        get.root.ids.board.ids.cash_count.text = f"-{fee} $"
        get.root.ids.p2.ids.p2_money_stash.text = f"{(int(get.root.ids.p2.ids.p2_money_stash.text) - fee)}"
        player_2_cash_count_r()
        Clock.schedule_once(money_update, 1.5)
        Clock.schedule_once(self.player_2_move_label, 1.5)

    def player_2_move_label(self, *args):
        get = App.get_running_app()

        get.root.ids.board.ids.cash_count.text = ""
        cash_anim = Animation(opacity=0, duration=0.05)
        cash_anim += Animation(size=(dp(100), dp(50)), pos=(dp(175), dp(559)), color=(0, 1, 0, 1), duration=0.05)
        cash_anim.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.player_1_give_money, 1)

    def player_1_give_money(self, *args):
        get = App.get_running_app()
        fee = 0
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 0:
            fee = 150
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 1:
            fee = 230
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 2:
            fee = 300
        if int(get.root.ids.f_shop.ids.louvre_count_2.text) == 3:
            fee = 350
        get.root.ids.board.ids.cash_count.text = f"+{fee} $"
        get.root.ids.p1.ids.p1_money_stash.text = f"{(int(get.root.ids.p1.ids.p1_money_stash.text) + fee)}"
        cash_anim_move = Animation(opacity=1)
        cash_anim_move.start(get.root.ids.board.ids.cash_count)

        Clock.schedule_once(self.end_anim, 1.8)

    # Both Players - General Functions

    @staticmethod
    def end_anim(*args):
        hide_cash_count()
        money_update()
        unblock_roll()


class PlayerOne(Widget):
    @staticmethod
    def roll():
        money_update()
        MovePlayers.player_1(f_move)
        Salary.player_1_trigger(f_salary)
        TaxField.player_1_trigger(f_tax)
        MoveField.player_1_trigger(f_move_field)
        PointsField.player_1_trigger(f_points)
        BigBenField.player_1_trigger(f_big_ben)
        CryptoField.player_1_trigger(f_crypto)
        CryptoField.player_1_crypto_update(f_crypto)
        ThiefField.player_1_trigger(f_thief)
        ChanceField.player_1_trigger(f_chance)
        EiffelTowerField.player_1_trigger(f_eiffel)
        BrainMemoryField.player_1_trigger(f_brain)
        DuckField.player_1_trigger(f_duck)
        HospitalField.player_1_trigger(f_hospital)
        ColiseumField.player_1_trigger(f_coliseum)
        StickyField.player_1_trigger(f_sticky)
        MathsField.player_1_trigger(f_maths)
        CounterfeitCashField.player_1_trigger(f_counterfeit)
        PisaField.player_1_trigger(f_pisa)
        StarPointsField.player_1_trigger(f_star_points)
        MoveBackField.player_1_trigger(f_move_back)
        WinCashField.player_1_trigger(f_win_cash)
        SydneyField.player_1_trigger(f_sydney)
        BlackFridayField.player_1_trigger(f_black_friday)
        CardsWarField.player_1_trigger(f_cards_war)
        ChancePointsField.player_1_trigger(f_chance_points)
        SkipDangerField.player_1_trigger(f_skip_danger)
        OpTowers.player_1_tower_1_trigger(f_towers)
        OpTowers.player_1_tower_2_trigger(f_towers)
        OpTowers.player_1_tower_3_trigger(f_towers)
        SalaryBuilding.player_1_trigger(f_salary_building)
        LouvreField.player_1_trigger(f_louvre)

    @staticmethod
    def block_roll():
        get = App.get_running_app()
        get.root.ids.p1.ids.player_1_roll.disabled = True

    def cancel(self):
        if self.ids.p1_input.focus:
            self.ids.p1_input.text = ''

    def yes_button(self):
        x, y = self.ids.player_1.pos

        def block_buttons():
            self.ids.player_1_yes.disabled = True
            self.ids.yes_button_image.opacity = 0
            self.ids.player_1_no.disabled = True
            self.ids.no_button_image.opacity = 0

        if x == p1_pos5_x and y == p1_pos5_y:
            BigBenField.player_1_buy(f_big_ben)
        if x == p1_pos6_x and y == p1_pos6_y:
            CryptoField.player_1_buy(f_crypto)
        if x == p1_pos9_x and y == p1_pos9_y:
            EiffelTowerField.player_1_buy(f_eiffel)
        if x == p1_pos11_x and y == p1_pos11_y or x == p1_pos30_x and y == p1_pos30_y:
            DuckField.player_1_buy(f_duck)
        if x == p1_pos13_x and y == p1_pos13_y:
            ColiseumField.player_1_buy(f_coliseum)
        if x == p1_pos16_x and y == p1_pos16_y:
            CounterfeitCashField.player_1_buy(f_counterfeit)
        if x == p1_pos17_x and y == p1_pos17_y:
            PisaField.player_1_buy(f_pisa)
        if x == p1_pos19_x and y == p1_pos19_y:
            StarPointsField.player_1_buy(f_star_points)
        if x == p1_pos20_x and y == p1_pos20_y:
            MoveBackField.yes(f_move_back)
        if x == p1_pos22_x and y == p1_pos22_y:
            SydneyField.player_1_buy(f_sydney)
        if x == p1_pos27_x and y == p1_pos27_y:
            OpTowers.player_1_buy_tower_1(f_towers)
        if x == p1_pos29_x and y == p1_pos29_y:
            OpTowers.player_1_buy_tower_2(f_towers)
        if x == p1_pos31_x and y == p1_pos31_y:
            OpTowers.player_1_buy_tower_3(f_towers)
        if x == p1_pos32_x and y == p1_pos32_y:
            SalaryBuilding.player_1_buy(f_salary_building)
        if x == p1_pos34_x and y == p1_pos34_y:
            SalaryBuilding.player_1_buy(f_salary_building)
        if x == p1_pos33_x and y == p1_pos33_y:
            LouvreField.player_1_buy(f_louvre)

        block_buttons()

    def yes_button_image_on(self):
        self.ids.yes_button_image.source = "images/yes_button_pressed.png"

    def yes_button_image_off(self):
        self.ids.yes_button_image.source = "images/yes_button.png"

    def no_button(self):
        x, y = self.ids.player_1.pos

        def block_buttons():
            self.ids.player_1_yes.disabled = True
            self.ids.player_1_no.disabled = True
            self.ids.yes_button_image.opacity = 0
            self.ids.no_button_image.opacity = 0

        if x == p1_pos20_x and y == p1_pos20_y:
            MoveBackField.player_1_move_anim(f_move_back)

        block_buttons()
        unblock_roll()

    def no_button_image_on(self):
        self.ids.no_button_image.source = "images/no_button_pressed.png"

    def no_button_image_off(self):
        self.ids.no_button_image.source = "images/no_button.png"

    @staticmethod
    def sell_crypto():
        CryptoField.player_1_sell(f_crypto)

    def crypto_button_image_on(self):
        self.ids.crypto_button_image.source = "images/btc_pressed.png"

    def crypto_button_image_off(self):
        self.ids.crypto_button_image.source = "images/btc.png"


class PlayerTwo(Widget):
    @staticmethod
    def roll():
        money_update()
        MovePlayers.player_2(f_move)
        Salary.player_2_trigger(f_salary)
        TaxField.player_2_trigger(f_tax)
        MoveField.player_2_trigger(f_move_field)
        PointsField.player_2_trigger(f_points)
        BigBenField.player_2_trigger(f_big_ben)
        CryptoField.player_2_trigger(f_crypto)
        CryptoField.player_2_crypto_update(f_crypto)
        ThiefField.player_2_trigger(f_thief)
        ChanceField.player_2_trigger(f_chance)
        EiffelTowerField.player_2_trigger(f_eiffel)
        BrainMemoryField.player_2_trigger(f_brain)
        DuckField.player_2_trigger(f_duck)
        HospitalField.player_2_trigger(f_hospital)
        ColiseumField.player_2_trigger(f_coliseum)
        StickyField.player_2_trigger(f_sticky)
        MathsField.player_2_trigger(f_maths)
        CounterfeitCashField.player_2_trigger(f_counterfeit)
        PisaField.player_2_trigger(f_pisa)
        StarPointsField.player_2_trigger(f_star_points)
        MoveBackField.player_2_trigger(f_move_back)
        WinCashField.player_2_trigger(f_win_cash)
        SydneyField.player_2_trigger(f_sydney)
        BlackFridayField.player_2_trigger(f_black_friday)
        CardsWarField.player_2_trigger(f_cards_war)
        ChancePointsField.player_2_trigger(f_chance_points)
        SkipDangerField.player_2_trigger(f_skip_danger)
        OpTowers.player_2_tower_1_trigger(f_towers)
        OpTowers.player_2_tower_2_trigger(f_towers)
        OpTowers.player_2_tower_3_trigger(f_towers)
        SalaryBuilding.player_2_trigger(f_salary_building)
        LouvreField.player_2_trigger(f_louvre)

    @staticmethod
    def block_roll():
        get = App.get_running_app()
        get.root.ids.p2.ids.player_2_roll.disabled = True

    def cancel(self):
        if self.ids.p2_input.focus:
            self.ids.p2_input.text = ''

    def yes_button(self):
        x, y = self.ids.player_2.pos

        def block_buttons():
            self.ids.player_2_yes.disabled = True
            self.ids.yes_button_image.opacity = 0
            self.ids.player_2_no.disabled = True
            self.ids.no_button_image.opacity = 0

        if x == p2_pos5_x and y == p2_pos5_y:
            BigBenField.player_2_buy(f_big_ben)
        if x == p2_pos6_x and y == p2_pos6_y:
            CryptoField.player_2_buy(f_crypto)
        if x == p2_pos9_x and y == p2_pos9_y:
            EiffelTowerField.player_2_buy(f_eiffel)
        if x == p2_pos11_x and y == p2_pos11_y or x == p2_pos30_x and y == p2_pos30_y:
            DuckField.player_2_buy(f_duck)
        if x == p2_pos13_x and y == p2_pos13_y:
            ColiseumField.player_2_buy(f_coliseum)
        if x == p2_pos16_x and y == p2_pos16_y:
            CounterfeitCashField.player_2_buy(f_counterfeit)
        if x == p2_pos17_x and y == p2_pos17_y:
            PisaField.player_2_buy(f_pisa)
        if x == p2_pos19_x and y == p2_pos19_y:
            StarPointsField.player_2_buy(f_star_points)
        if x == p2_pos20_x and y == p2_pos20_y:
            MoveBackField.yes(f_move_back)
        if x == p2_pos22_x and y == p2_pos22_y:
            SydneyField.player_2_buy(f_sydney)
        if x == p2_pos27_x and y == p2_pos27_y:
            OpTowers.player_2_buy_tower_1(f_towers)
        if x == p2_pos29_x and y == p2_pos29_y:
            OpTowers.player_2_buy_tower_2(f_towers)
        if x == p2_pos31_x and y == p2_pos31_y:
            OpTowers.player_2_buy_tower_3(f_towers)
        if x == p2_pos32_x and y == p2_pos32_y or x == p2_pos34_x and y == p2_pos34_y:
            SalaryBuilding.player_2_buy(f_salary_building)
        if x == p2_pos33_x and y == p2_pos33_y:
            LouvreField.player_2_buy(f_louvre)

        block_buttons()

    def yes_button_image_on(self):
        self.ids.yes_button_image.source = "images/yes_button_pressed.png"

    def yes_button_image_off(self):
        self.ids.yes_button_image.source = "images/yes_button.png"

    def no_button(self):
        x, y = self.ids.player_2.pos

        def block_buttons():
            self.ids.player_2_yes.disabled = True
            self.ids.player_2_no.disabled = True
            self.ids.yes_button_image.opacity = 0
            self.ids.no_button_image.opacity = 0

        if x == p2_pos20_x and y == p2_pos20_y:
            MoveBackField.player_2_move_anim(f_move_back)

        block_buttons()
        unblock_roll()

    def no_button_image_on(self):
        self.ids.no_button_image.source = "images/no_button_pressed.png"

    def no_button_image_off(self):
        self.ids.no_button_image.source = "images/no_button.png"

    @staticmethod
    def sell_crypto():
        CryptoField.player_2_sell(f_crypto)

    def crypto_button_image_on(self):
        self.ids.crypto_button_image.source = "images/btc_pressed.png"

    def crypto_button_image_off(self):
        self.ids.crypto_button_image.source = "images/btc.png"


class Board(Widget):
    # Start the Game
    def load_game(self):
        get = App.get_running_app()

        p1 = randint(1, 6)
        p2 = randint(1, 6)

        get.root.ids.p1.ids.p1_money_stash.text = "2000"
        get.root.ids.p2.ids.p2_money_stash.text = "2000"

        get.root.ids.p1.ids.p1_points_stash.text = "0"
        get.root.ids.p2.ids.p2_points_stash.text = "0"

        get.root.ids.p1.ids.p1_crypto_stash.text = "0"
        get.root.ids.p2.ids.p2_crypto_stash.text = "0"

        get.root.ids.p1.ids.player_1_money.text = f"{2000:,} $"
        get.root.ids.p2.ids.player_2_money.text = f"{2000:,} $"

        get.root.ids.p1.ids.player_1_points.text = f"{0:,} pts."
        get.root.ids.p2.ids.player_2_points.text = f"{0:,} pts."

        get.root.ids.p1.ids.p1_crypto.text = f"{0.0:,}"
        get.root.ids.p2.ids.p2_crypto.text = f"{0.0:,}"

        if p1 > p2:
            self.ids.big.text = "Player 1 is first"
            get.root.ids.p1.ids.player_1_roll.disabled = False
            self.ids.start.disabled = True
            self.ids.start.text = "Start Game"
        if p1 == p2:
            self.ids.big.text = "Equal roll, try again!!"
            self.ids.start.text = "Roll Again"
        if p1 < p2:
            self.ids.big.text = "Player 2 is first"
            get.root.ids.p2.ids.player_2_roll.disabled = False
            self.ids.start.disabled = True
            self.ids.start.text = "Start Game"

    def restart_game(self):
        get = App.get_running_app()
        self.load_game()
        get.root.ids.p1.ids.player_1.pos = (p1_pos1_x, p1_pos1_y)
        get.root.ids.p2.ids.player_2.pos = (p2_pos1_x, p2_pos1_y)


class GameWindow(Widget):
    pass


kv = Builder.load_file("game_build.kv")

game = GameWindow()
player_1 = PlayerOne()
player_2 = PlayerTwo()
board = Board()

f_shop = Shop()
f_move = MovePlayers()
f_salary = Salary()
f_tax = TaxField()
f_move_field = MoveField()
f_points = PointsField()
f_big_ben = BigBenField()
f_crypto = CryptoField()
f_thief = ThiefField()
f_chance = ChanceField()
f_eiffel = EiffelTowerField()
f_brain = BrainMemoryField()
f_duck = DuckField()
f_hospital = HospitalField()
f_coliseum = ColiseumField()
f_sticky = StickyField()
f_maths = MathsField()
f_counterfeit = CounterfeitCashField()
f_pisa = PisaField()
f_star_points = StarPointsField()
f_move_back = MoveBackField()
f_win_cash = WinCashField()
f_sydney = SydneyField()
f_black_friday = BlackFridayField()
f_cards_war = CardsWarField()
f_chance_points = ChancePointsField()
f_skip_danger = SkipDangerField()
f_towers = OpTowers()
f_salary_building = SalaryBuilding()
f_louvre = LouvreField()


class GameApp(App):

    def build(self):
        Config.set('graphics', 'resizable', True)
        Config.set('graphics', 'fullscreen', False)
        Config.write()
        Window.resize = True
        Window.size = (1330, 675)
        Window.top = 40
        Window.left = 20
        self.icon = 'images/icon.png'
        return game

    def restart(self):
        self.root.clear_widgets()
        self.stop()
        return GameApp().run()


if __name__ == '__main__':
    GameApp().run()
