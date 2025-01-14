import time

from rpg.locations import Location


class CastleInside(Location):
    CHOICES = ["shout", "go_north", "go_south", "go_east"]

    def welcome_message(self):
        return (
            "You step inside the castle. "
            "You see long corridor at each directions in front of you."
        )

    def go_south(self):
        from rpg.locations.castle.castle_entrance import (
            CastleDoorReturned,
        )

        print("You choose to go back. Coward...")
        return CastleDoorReturned

    def go_east(self):
        from rpg.locations.castle.castle_maze import CastleMaze

        print("You choose to go east. Is that a minotaur?")
        return CastleMaze

    def go_north(self):
        print(
            "You decide to go north. You follow the direction for two good minutes. "
            "There are a lot of paintings and torches on the wall."
        )
        return CastleBossDoor

    def shout(self):
        print(
            "You feel less scared, but you haven't made any progress in getting the scroll."
        )
        return CastleInside


class StillCastleInside(CastleInside):
    def welcome_message(self):
        return "You still are at the entrance of the castle."


class BackAtCastleInsideFromMaze(CastleInside):
    def welcome_message(self):
        return "You recognize the entrance of the castle! That is a good news. Ok, back to square one."


class BackAtCastleInside(CastleInside):
    def welcome_message(self):
        return "You are back at the entrance of the castle."


class CastleBossDoor(Location):
    def welcome_message(self):
        return "After few minutes of walking, you see a huge door."

    def go_west(self):
        print(
            "You can see a pile of bones. You are starting to panicking, it means some people has died here."
        )

    def go_east(self):
        pass

    def go_north(self):
        from rpg.objects.key import Keys

        print("You try to push the large door.")
        time.sleep(3)
        print("...")
        time.sleep(3)

        if Keys.CASTLE_BOSS in self.game.bag.keys:
            if not Keys.CASTLE_BOSS.value.door_opened:
                print(
                    "You look at the rusty lock. "
                    "It looks a lot like the key you got in the maze."
                )
                return StillCastleBossDoor
            else:
                print("The door is opened and you can step inside.")
                return CastleBoss
        else:
            print(
                "Unfortunately, no matter how hard you push, she doesn't move an inch. "
                "You observe the door for a minute and notice a rusty lock."
            )
            return StillCastleBossDoor

    def go_south(self):
        return BackAtCastleInside


class StillCastleBossDoor(CastleBossDoor):
    def welcome_message(self):
        return "You still are in front of the huge door."


class CastleBoss(Location):
    def unfold_scenario(self):
        print(
            "You can see in the distance an armour. The scroll! It's in the hand of the armour"
        )
        print(
            "Before you notice, it starts moving. The armour draws its sword of frost that seems very powerful."
        )
        print("You prepare for the fight.")
        from rpg.fight import Fight, Character

        fight = Fight(
            game=self.game,
            foe=Character(
                name="Lich King",
                life_points=40,
                level=5,
                strength=20,
            ),
            player_started_the_fight=False,
        )

        success = fight.fight()
        if success:
            print(
                "After few minutes of intense fighting, you gather your last forces and give the last stroke "
                "into the armour. It suddenly falls into pieces."
            )
            time.sleep(3)
            print(
                "You get your breath back and cheers of this epic victory. You get the scroll and leave the room."
            )
            time.sleep(3)
            print(
                "You find your way back into the forest and to the nearby village to return the scroll to the maid."
            )
            time.sleep(3)
            print(
                "You cannot help looking at the scroll once mounted on your horse. You recognize the writing, "
                "it's common tongue. It says:"
            )
            time.sleep(3)
            print(
                """
                Dear Vacations,
                
                I would like to take this period off : 18/10/21 - 22/10/21.
                Thanks a lot in advance.
                Kind regards.
                """
            )
            time.sleep(3)
            print(
                "You feel like you're been mocked. What the hell is this joke? All of this adventure for that? "
                "That's not an epic victory at all. No glorious treasure. Just useless piece of paper..."
            )
            time.sleep(3)
            self.game.win()
