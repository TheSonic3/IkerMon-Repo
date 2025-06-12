import random
from time import sleep
from enum import Enum, auto
import copy


class Move:
    def __init__(self, name, attackDamage, attackStatus, attackStatusChance, attackType):

        self.name = name
        self.attackDamage = attackDamage
        self.attackStatus = attackStatus
        self.attackStatusChance = attackStatusChance
        self.attackType = attackType

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Monster:
    def __init__(self, name, exhausted, level, totalHp, hp, armour, typ, attackRatio, speed, status, statusMoveCounter, moves,):

        self.name = name
        self.exhausted = exhausted
        self.level = level
        self.typ = typ
        self.totalHp = totalHp
        self.hp = hp
        self.armour = armour
        self.attackRatio = attackRatio
        self.speed = speed
        self.status = status
        self.statusMoveCounter = statusMoveCounter
        self.moves: list[str] = moves

        self.all_moves = [
            Move("Euler's Number", 25, 1, 70, "normal"),
            Move("BARIUM!!!", 25, 1, 70, "normal"),
            Move("Lacerate", 50, 0, 0, "fighting"),
            Move("GPE", 50, 0, 0, "fighting"),
            Move("Fire Gun", 40, 2, 40, "fire"),
            Move("Steve Lava", 30, 2, 55, "fire"),
            Move("Water Blade", 55, 0, 0, "water"),
            Move("Water Noose", 70, 0, 0, "water"),
            Move("Grass Syringe", 45, 3, 45, "grass"),
            Move("Foilage Whip", 60, 0, 0, "grass"),
            Move("Browsing History", 50, 1, 20, "paralysis"),
        ]

    def copy(self) -> "Monster":
        return Monster(
            self.name,
            self.exhausted,
            self.level,
            self.totalHp,
            self.hp,
            self.armour,
            self.typ,
            self.attackRatio,
            self.speed,
            self.status,
            self.statusMoveCounter,
            self.moves.copy(),
        )

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def getMove(self, name):
        assert name is not self.moves
        for move in self.all_moves:
            if move.name == name:
                return move
        print("couldn't find a valid move")
        exit(-1)


monsters = [
    Monster(
        "Bat",
        False,
        1,
        75,
        75,
        4,
        "flying",
        0.4,
        4,
        "none",
        "0",
        ["Lacerate", "Fire Gun"],
    ),
    Monster(
        "Jorell",
        False,
        1,
        85,
        85,
        6,
        "normal",
        0.5,
        6,
        "none",
        "0",
        ["Euler's Number", "Fire Gun"],
    ),
    Monster(
        "Sigma Man",
        False,
        1,
        95,
        95,
        6,
        "fighting",
        0.4,
        3,
        "none",
        "0",
        ["Lacerate", "Fire Gun"],
    ),
    Monster(
        "Spalacinae",
        False,
        1,
        105,
        105,
        10,
        "ghost",
        0.3,
        1,
        "none",
        "0",
        ["Lacerate", "Fire Gun"],
    ),
    Monster(
        "Matty",
        False,
        1,
        55,
        55,
        4,
        "grass",
        0.6,
        1,
        "none",
        "0",
        ["Grass Syringe", "BARIUM!!!"],
    ),
    Monster(
        "Anthony",
        False,
        1,
        70,
        70,
        4,
        "ghost",
        0.4,
        0.5,
        "none",
        "0",
        ["Euler's Number", "GPE"],
    ),
    Monster(
        "Google_Chrome",
        False,
        1,
        80,
        80,
        2,
        "ghost",
        0.6,
        1,
        "none",
        "0",
        ["Euler's Number", "Browsing History"],
    ),
    Monster(
        "Atoll Duck",
        False,
        1,
        70,
        70,
        7,
        "ghost",
        0.3,
        1,
        "none",
        "0",
        ["Euler's Number", "Browsing History"],
    ),
    Monster(
        "Arthur Korrea",
        False,
        1,
        70,
        70,
        4,
        "ghost",
        0.4,
        1,
        "none",
        "0",
        ["Euler's Number", "Browsing History"],
    ),
]


def getMonster(name):
    for monster in monsters:
        if monster.name == name:
            return monster
    assert False


moves = [
    Move("Euler's Number", 25, 1, 70, "normal"),
    Move("BARIUM!!!", 25, 1, 70, "normal"),
    Move("Lacerate", 50, 0, 0, "fighting"),
    Move("GPE", 50, 0, 0, "fighting"),
    Move("Fire Gun", 40, 2, 40, "fire"),
    Move("Steve Lava", 30, 2, 55, "fire"),
    Move("Water Blade", 55, 0, 0, "water"),
    Move("Water Noose", 70, 0, 0, "water"),
    Move("Grass Syringe", 45, 3, 45, "grass"),
    Move("Foilage Whip", 60, 0, 0, "grass"),
    Move("Browsing History", 50, 1, 20, "paralysis"),
]

typeDynamics = {
    "flyingWeakness": "fighting",
    "flyingStrength": "normal",
    "normalWeakness": "flying",
    "normalStrength": "ghost",
    "fightingWeakness": "ghost",
    "fightingStrength": "flying",
    "ghostWeakness": "normal",
    "ghostStrength": "flying",
    "waterWeakness": "grass",
    "waterStrength": "fire",
    "fireWeakness": "water",
    "fireStrength": "grass",
    "grassWeakness": "fire",
    "grassStrength": "water",
}

itemValue = {
    "Syringe": 20,
    "Burn Ointment": "none",
}


class ItemType(Enum):
    SYRINGE = auto()
    BIG_SYRINGE = auto()
    STRENGHTER = auto()
    BURNCURER = auto()
    POISONCURER = auto()
    SLEEPCURER = auto()
    PARALYSISCURER = auto()

    def val(self):
        if self == ItemType.SYRINGE:
            return 30
        elif self == ItemType.BIG_SYRINGE:
            return 60
        elif self == ItemType.STRENGHTER:
            return 0.1
        elif self in (
                ItemType.BURNCURER,
                ItemType.POISONCURER,
                ItemType.SLEEPCURER,
                ItemType.PARALYSISCURER,
        ):
            return "none"
        else:
            return 0

    def is_healing(self):
        return self == ItemType.BIG_SYRINGE or self == ItemType.SYRINGE

    def is_strength(self):
        return self == ItemType.STRENGHTER

    def is_status_change(self):
        return self in {
            ItemType.BURNCURER,
            ItemType.SLEEPCURER,
            ItemType.POISONCURER,
            ItemType.PARALYSISCURER,
        }


class Item:
    def __init__(self, type: ItemType, quantity):
        self.type = type
        self.quantity = quantity
        self.value = type.val()


userItems = [
    Item(ItemType.SYRINGE, 2),
    Item(ItemType.BIG_SYRINGE, 1),
    Item(ItemType.BURNCURER, 1),
]


def itemHandler(monster: Monster, itemsAvailable):
    userItemsLen = len(itemsAvailable)
    for item in itemsAvailable:
        print(f"You have {item.quantity} {item.type.name}s \n")
    userInput = (
                    int(input(f"Which item would you like to use, choose from 1 to {userItemsLen} \n"))) - 1
    item = itemsAvailable[userInput]
    item.quantity -= 1
    if item.quantity <= 0:
        del itemsAvailable[userInput]

    # print(item.type)
    # print(f"index is: {userInput}")
    if item.type.is_healing():
        # print("found a healing type")
        totalHpHeal = monster.hp + item.value
        if totalHpHeal > (monster.totalHp):
            totalHpHeal = monster.totalHp
        # print(f"HP after healing is {totalHpHeal}")
        monster.hp = totalHpHeal
    elif item.type.is_strength():
        monster.attackRatio = int(monster.attackRatio) + item.value
    elif item.type.is_status_change():
        initialStatus = monster.status
        if item.type == ItemType.BURNCURER:
            if initialStatus == "burn":
                monster.status = item.value
        elif item.type == ItemType.PARALYSISCURER:
            if initialStatus == "paralysis":
                monster.status = item.value
        elif item.type == ItemType.SLEEPCURER:
            if initialStatus == "sleep":
                monster.status = item.value
        elif item.type == ItemType.POISONCURER:
            if initialStatus == "poison":
                monster.status = item.value
    for item in itemsAvailable:
        print(f"You have {item.quantity} {item.type.name}s \n")


def attackRatioCalc(attacker: Monster, move):
    moveDamage = move.attackDamage
    attackRatio = float(attacker.attackRatio)
    return attackRatio * moveDamage


def armourDamageCalc(attackRatioDamage, receiver: Monster):
    # Calculates the damage after armour stat is calculated, could be revamped.
    # print(f"armour: {receiver.armour}")
    moveArmorDamage = attackRatioDamage * (6 / receiver.armour)
    # print("moveDamage: ", moveArmorDamage)
    return moveArmorDamage


def checkStatus(move, receiver: Monster):
    if receiver.status != "none":
        return
    chance = move.attackStatusChance
    if random.randint(1, 100) <= chance:
        statusDict = {0: "none", 1: "paralysis", 2: "burn", 3: "poison", 4: "sleep"}
        newStatus = statusDict.get(move.attackStatus, "none")
        # Checks if the move's status is none or something, if it's none, skips the applying
        if newStatus != "none":
            receiver.status = newStatus
            receiver.statusMoveCounter = "0"
            # print (f"{receiver.name} is now affected by {newStatus}")


def currentStatusUpdating(receiver: Monster):
    status = receiver.status
    counter = int(receiver.statusMoveCounter)
    if status == "none":
        return

    statusRemovalChance = counter * 20
    if random.randint(1, 100) <= statusRemovalChance:
        # print (f"{receiver.name}'s status has been removed")
        receiver.status = "none"
        receiver.statusMoveCounter = "0"
    else:
        receiver.statusMoveCounter = str(counter + 1)


def effectivenessCalc(receiver: Monster, move, typeDynamics, armourRatioDamage):
    attackType = move.attackType
    attackStrength = typeDynamics.get(f"{attackType}Strength")
    attackWeakness = typeDynamics.get(f"{attackType}Weakness")
    receiverType = receiver.typ

    if receiverType == attackStrength:
        damage = armourRatioDamage * 2
        # print(f"2X of {damage/2}")
    elif receiverType == attackWeakness:
        damage = armourRatioDamage * 0.5
    else:
        damage = armourRatioDamage
    return damage


def finalDamageCalculator(netDamageReceiver, netDamageAttacker, receiver: Monster, attacker: Monster):
    print("netDamageReceiever:", netDamageReceiver)
    print("netDamageAttacker:", netDamageAttacker)

    # attacker = getMonster(attacker.name)
    if receiver.status not in ["burn", "poison"]:
        netDamageReceiver = round(netDamageReceiver)


    elif receiver.status == "burn":
        burnDamageReceiver = 0.1 * int(receiver.totalHp)
        # print("Receiver Burn:", burnDamageReceiver)
        netDamageReceiver = round(netDamageReceiver + (burnDamageReceiver))


    elif receiver.status == "poison":
        poisonDamageReceiver = 0.1 * int(receiver.totalHp)
        # print("Receiver poison:", poisonDamageReceiver)
        netDamageReceiver = round(netDamageReceiver + (poisonDamageReceiver))

    if attacker.status not in ["burn", "poison"]:
        netDamageAttacker = 0


    elif attacker.status == "burn":
        burnDamageAttacker = 0.1 * int(receiver.totalHp)
        # print("Attacker Burn:", burnDamageAttacker)
        netDamageAttacker = round(burnDamageAttacker)


    elif attacker.status == "poison":
        poisonDamageAttacker = 0.1 * int(receiver.totalHp)
        # print("Attacker Poison:", poisonDamageAttacker)
        netDamageAttacker = round(poisonDamageAttacker)
    return netDamageReceiver, netDamageAttacker


def damageApplier(netDamageReceiver, netDamageAttacker, receiver: Monster, attacker: Monster):
    # print(f"Defender: {receiver.name} has {receiver.hp} hp")
    # print(f"Attacker: {attacker.name} has {attacker.hp} hp")
    if receiver.hp - netDamageReceiver < 0:
        receiver.hp = 0
        # print(f"{receiver.name}, has no hp left")
    else:
        receiver.hp = receiver.hp - netDamageReceiver
        print(f"Receiver {receiver.name} net damage is:", netDamageReceiver)
    if attacker.hp - netDamageAttacker < 0:
        attacker.hp = 0
        # print(f"{attacker.name}, has no hp left")
    else:
        attacker.hp = attacker.hp - netDamageAttacker
        # print(f"Attacker {attacker.name} net damage is:", netDamageAttacker)
    # print(f"Defender: {receiver.name} has {receiver.hp} hp left")
    # print(f"Attacker: {attacker.name} has {attacker.hp} hp left")


def monsterSwapper(monster, team1: list[Monster], forcedSwap=False):
    team1[:] = [e for e in team1 if e.hp > 0]
    team1MonsterExhausted = monster.exhausted

    if len(team1) == 1:
        print("Only 1 monster is left")
        team1Monster = team1[0]
    elif monster.hp != 0 and len(team1) > 1:
        swap = input("do you want to swap monsters? (yes or no)") == "yes"
        if swap:
            for i, m in enumerate(team1):
                print(f"{i + 1}: {m.name} (HP: {m.hp}/{m.totalHp})")
            playerChoice = (int(input(f"Which monster would you like to use (1-{len(team1)})")) - 1)
            team1Monster = team1[playerChoice]
            team1Monster.exhausted = True
        else:
            team1Monster = monster
    elif len(team1) == 0:
        print("All your monsters have been knocked out!")
        exit()
    else:  # forced swap case
        for i, m in enumerate(team1):
            print(f"{i + 1}: {m.name} (HP: {m.hp}/{m.totalHp})")
        playerChoice = (int(input(f"Which monster would you like to use (1-{len(team1)})")) - 1)
        team1Monster = team1[playerChoice]
        team1Monster.exhausted = False

    print("exhaust?:", team1Monster.exhausted)
    return team1Monster


def enemyMonsterSwapper(team2):
    team2[:] = [e for e in team2 if e.hp > 0]
    if len(team2) == 0:
        print("All of your opponent's monsters have been knocked out! You win!")
        exit()
    team2Monster = random.choice(team2)
    team2Monster.exhausted = False
    return team2Monster


def monsterSpeedCheck(monster1: Monster, monster2: Monster) -> tuple[Monster, Monster]:
    # Reset exhaustion at start of each round
    monster1.exhausted = False
    monster2.exhausted = False

    monster1Speed = monster1.speed
    monster2Speed = monster2.speed

    # Determine who would attack based on speed
    if monster1Speed > monster2Speed:
        attacker = monster1
        defender = monster2
    elif monster2Speed > monster1Speed:
        attacker = monster2
        defender = monster1
    else:  # If speeds are equal
        attacker = random.choice([monster1, monster2])
        defender = monster2 if attacker is monster1 else monster1

    # Exhaust the attacker for next turn
    attacker.exhausted = True
    return attacker, defender


def attackCalculator(team1, team2, team1Monster: Monster, team2Monster: Monster):
    # print ("Enemy", team2Monster.exhausted)
    trueDamageReceiver = 0
    trueDamageAttacker = 0
    moveSelection = team2Monster.moves.copy()
    lenMoveSelection = len(moveSelection)
    moveSelected = random.randint(1, lenMoveSelection)
    move = team2Monster.getMove(team2Monster.moves[moveSelected - 1])
    print(move.name)
    currentStatusUpdating(team2Monster)
    if team2Monster.status not in ["paralysis", "sleep"]:
        checkStatus(move, team1Monster)
        currentStatusUpdating(team1Monster)
        attackRatioDamage = attackRatioCalc(team2Monster, move)
        armourRatioDamage = armourDamageCalc(attackRatioDamage, team1Monster)
        # effectivenessDamage is the net damage before considering status effects, no damage has been passed through yet though.
        effectivenessRatioDamage = effectivenessCalc(team1Monster, move, typeDynamics, armourRatioDamage)
        # add missing input variables
        trueDamageReceiver, trueDamageAttacker = finalDamageCalculator(effectivenessRatioDamage, 0, team1Monster,
                                                                       team2Monster)
        # print("trueDamageAttacker:", trueDamageAttacker)
        damageApplier(trueDamageReceiver, trueDamageAttacker, team1Monster, team2Monster)
    else:
        print(f"Enemy {team2Monster.name} is unable to move because of {team2Monster.status}")
    if team1Monster.hp == 0:
        team1Monster = monsterSwapper(team1Monster, team1, forcedSwap=True)
        print(f"{team1Monster.name}, has been knocked out")
        # print ("EA")
    elif team2Monster.hp == 0:
        print(f"Enemy {team2Monster.name}, has been knocked out")
        # print ("OE")
        team2Monster = enemyMonsterSwapper(team2)
    return team1Monster, team2Monster, trueDamageReceiver, trueDamageAttacker


def turnHandler(team1, team2, team1Monster: Monster, team2Monster: Monster):
    # Team1 is mentioned since only the player, who is always team1 can control these options
    # print ("Ally", team1Monster.exhausted)
    trueDamageReceiver = 0
    trueDamageAttacker = 0
    turnChoice = (int(input("What would you like to do? \n Attack = 1, Items = 2, Swap Monster = 3, Run = 4. \n")) - 1)
    turnOptions = {
        0: "attack",
        1: "items",
        2: "swap",
        3: "run",
    }
    turnOptionChosen = turnOptions.get(turnChoice)
    if turnOptionChosen == "attack":
        moveSelection = team1Monster.moves.copy()
        moveSelected = int(input(f"Choose an attack from these using numbers, (1 or 2): {", ".join(moveSelection)}\n"))
        move = team1Monster.getMove(team1Monster.moves[moveSelected - 1])
        currentStatusUpdating(team1Monster)
        if team1Monster.status not in ["paralysis", "sleep"]:
            checkStatus(move, team2Monster)
            currentStatusUpdating(team2Monster)
            attackRatioDamage = attackRatioCalc(team1Monster, move)
            armourRatioDamage = armourDamageCalc(attackRatioDamage, team2Monster)
            # effectivenessDamage is the net damage before considering status effects, no damage has been passed through yet though.
            effectivenessRatioDamage = effectivenessCalc(team2Monster, move, typeDynamics, armourRatioDamage)
            trueDamageReceiver, trueDamageAttacker = finalDamageCalculator(effectivenessRatioDamage, 0, team2Monster,
                                                                           team1Monster)
            print(f"r: {trueDamageReceiver}, a: {trueDamageAttacker}")
            damageApplier(trueDamageReceiver, trueDamageAttacker, team2Monster, team1Monster)
            if team2Monster.hp == 0:
                print(f"{team2Monster.name}, has been knocked out")
                print("AE")
                team2Monster = enemyMonsterSwapper(team2)
        else:
            print(f"Ally {team1Monster.name} is unable to move because of {team1Monster.status}")
    elif turnOptionChosen == "items":
        itemHandler(team1Monster, userItems)
    elif turnOptionChosen == "swap":
        team1Monster = monsterSwapper(team1Monster, team1, forcedSwap=False)
        return team1Monster, team2Monster, trueDamageAttacker, trueDamageReceiver
    elif turnOptionChosen == "run":
        # Currently the run function is static, perhaps it can vary depending on speed or level difference, by changing the 60?
        runChance = random.randint(0, 99)
        if runChance <= 60:
            print("Successfully got away!")
            exit()
    return team1Monster, team2Monster, trueDamageAttacker, trueDamageReceiver


def mainBattle():
    team1 = [copy.deepcopy(getMonster("Anthony")), copy.deepcopy(getMonster("Jorell"))]
    team2 = [copy.deepcopy(getMonster("Anthony")), copy.deepcopy(getMonster("Google_Chrome"))]

    team1Monster = team1[
        int(input(f"team1) which monster would you like to use ({team1[0].name} or {team1[1].name}) \n")) - 1]
    team2Monster = team2[
        int(input(f"team2) which monster would you like to use ({team2[0].name} or {team2[1].name}) \n")) - 1]

    # Initialize turn tracker
    lastAttacker = None

    while True:
        attacker, defender = monsterSpeedCheck(team1Monster, team2Monster)

        # If same monster attacked last time, force the other to attack
        if lastAttacker is not None and attacker is lastAttacker:
            attacker, defender = defender, attacker

        print(f"the attacker is {attacker.name}, and the defender is {defender.name}")

        if attacker in team1:  # Player's turn
            team1Monster, team2Monster, trueDamageAlly, trueDamageEnemy = turnHandler(team1, team2, attacker, defender)
        else:  # AI's turn
            team1Monster, team2Monster, trueDamageAlly, trueDamageEnemy = attackCalculator(team1, team2, defender,
                                                                                           attacker)

        print(f"TDA: {trueDamageAlly}, TDE: {trueDamageEnemy}")

        # Update last attacker
        lastAttacker = attacker

        # Check if battle should end
        if team1Monster.hp <= 0:
            team1Monster = monsterSwapper(team1Monster, team1)
            if not team1Monster:  # All monsters fainted
                print("You lost the battle!")
                break
        if team2Monster.hp <= 0:
            team2Monster = enemyMonsterSwapper(team2)
            if not team2Monster:  # All enemy monsters fainted
                print("You won the battle!")
                break
    return trueDamageAlly, trueDamageEnemy


mainBattle()


