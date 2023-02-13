# ========= MY IMPORTS =========
from Enums import Enums


# ========= OLD IMPORTS =========
# from System import *
# from System.Collections.Generic import *
# from System.Text import *
# from System.Text.RegularExpressions import *
# from UnityEngine import *


# ========= THE CLASS =========

# class CardData(ScriptableObject):
class CardData():
    def __init__(self):
        self.cardName = None
        self.id = None
        self.internalId = None
        self.visible = None
        self.upgradesTo1 = ""
        self.upgradesTo2 = ""
        self.cardUpgraded = None
        self.upgradedFrom = ""
        self.baseCard = ""
        self.cardNumber = None
        self.upgradesToRare = None
        self.description = ""
        self.fluff = ""
        self.fluffPercent = None
        self.descriptionNormalized = ""
        self.relatedCard = None
        self.keyNotes = None
        self.sprite = None
        self.flipSprite = None
        self.showInTome = True
        self.descriptionId = ""
        self.petModel = None
        self.petFront = True
        self.petInvert = True
        self.petOffset = Vector2(0, 0)
        self.petSize = Vector2(1, 1)
        self.isPetAttack = None
        self.isPetCast = None
        self.killPet = None
        self.maxInDeck = None
        self.cardRarity = None
        self.cardType = None
        self.cardTypeAux = None
        self.cardTypeList = None
        self.cardClass = None
        self.item = None
        self.itemEnchantment = None
        self.energyCost = None
        self.exhaustCounter = None
        self.energyReductionPermanent = None
        self.energyReductionTemporal = None
        self.energyReductionToZeroPermanent = None
        self.energyReductionToZeroTemporal = None
        self.energyCostOriginal = None
        self.energyCostForShow = None
        self.playable = True
        self.autoplayDraw = None
        self.autoplayEndTurn = None
        self.effectRequired = ""
        self.vanish = None
        self.innate = None
        self.lazy = None
        self.endTurn = None
        self.moveToCenter = None
        self.corrupted = None
        self.starter = None
        self.onlyInWeekly = None
        self.modifiedByTrait = None
        self.targetType = None
        self.targetSide = None
        self.targetPosition = None
        self.specialValueGlobal = None
        self.specialAuraCurseNameGlobal = None
        self.specialValueModifierGlobal = None
        self.specialValue1 = None
        self.specialAuraCurseName1 = None
        self.specialValueModifier1 = None
        self.specialValue2 = None
        self.specialAuraCurseName2 = None
        self.specialValueModifier2 = None
        self.effectRepeat = 1
        self.effectRepeatDelay = None
        self.effectRepeatEnergyBonus = None
        self.effectRepeatMaxBonus = None
        self.effectRepeatTarget = None
        self.effectRepeatModificator = None
        self.damageType = None
        self.damageTypeOriginal = None
        self.damage = None
        self.damagePreCalculated = None
        self.damageSides = None
        self.damageSidesPreCalculated = None
        self.damageSelf = None
        self.damageSpecialValueGlobal = None
        self.damageSpecialValue1 = None
        self.damageSpecialValue2 = None
        self.damageSelfPreCalculated = None
        self.damageSelfPreCalculated2 = None
        self.ignoreBlock = None
        self.damageType2 = None
        self.damageType2Original = None
        self.damage2 = None
        self.damagePreCalculated2 = None
        self.damageSides2 = None
        self.damageSidesPreCalculated2 = None
        self.damageSelf2 = None
        self.damage2SpecialValueGlobal = None
        self.damage2SpecialValue1 = None
        self.damage2SpecialValue2 = None
        self.ignoreBlock2 = None
        self.selfHealthLoss = None
        self.selfHealthLossSpecialGlobal = None
        self.selfHealthLossSpecialValue1 = None
        self.selfHealthLossSpecialValue2 = None
        self.damageEnergyBonus = None
        self.acEnergyBonus = None
        self.acEnergyBonusQuantity = None
        self.acEnergyBonus2 = None
        self.acEnergyBonus2Quantity = None
        self.heal = None
        self.healPreCalculated = None
        self.healSides = None
        self.healSelf = None
        self.healSelfPreCalculated = None
        self.healEnergyBonus = None
        self.healSelfPerDamageDonePercent = None
        self.healSpecialValueGlobal = None
        self.healSpecialValue1 = None
        self.healSpecialValue2 = None
        self.healSelfSpecialValueGlobal = None
        self.healSelfSpecialValue1 = None
        self.healSelfSpecialValue2 = None
        self.healCurses = None
        self.dispelAuras = None
        self.transferCurses = None
        self.stealAuras = None
        self.reduceCurses = None
        self.reduceAuras = None
        self.increaseCurses = None
        self.increaseAuras = None
        self.healAuraCurseSelf = None
        self.healAuraCurseName = None
        self.healAuraCurseName2 = None
        self.healAuraCurseName3 = None
        self.healAuraCurseName4 = None
        self.energyRecharge = None
        self.aura = None
        self.auraSelf = None
        self.auraCharges = None
        self.auraChargesSpecialValueGlobal = None
        self.auraChargesSpecialValue1 = None
        self.auraChargesSpecialValue2 = None
        self.aura2 = None
        self.auraSelf2 = None
        self.auraCharges2 = None
        self.auraCharges2SpecialValueGlobal = None
        self.auraCharges2SpecialValue1 = None
        self.auraCharges2SpecialValue2 = None
        self.aura3 = None
        self.auraSelf3 = None
        self.auraCharges3 = None
        self.auraCharges3SpecialValueGlobal = None
        self.auraCharges3SpecialValue1 = None
        self.auraCharges3SpecialValue2 = None
        self.curse = None
        self.curseSelf = None
        self.curseCharges = None
        self.curseChargesSpecialValueGlobal = None
        self.curseChargesSpecialValue1 = None
        self.curseChargesSpecialValue2 = None
        self.curse2 = None
        self.curseSelf2 = None
        self.curseCharges2 = None
        self.curseCharges2SpecialValueGlobal = None
        self.curseCharges2SpecialValue1 = None
        self.curseCharges2SpecialValue2 = None
        self.curse3 = None
        self.curseSelf3 = None
        self.curseCharges3 = None
        self.curseCharges3SpecialValueGlobal = None
        self.curseCharges3SpecialValue1 = None
        self.curseCharges3SpecialValue2 = None
        self.pushTarget = None
        self.pullTarget = None
        self.drawCard = None
        self.discardCard = None
        self.discardCardType = None
        self.discardCardTypeAux = None
        self.discardCardAutomatic = None
        self.discardCardPlace = None
        self.addCard = None
        self.addCardId = ""
        self.addCardType = None
        self.addCardTypeAux = None
        self.addCardList = None
        self.addCardChoose = None
        self.addCardFrom = None
        self.addCardPlace = None
        self.addCardReducedCost = None
        self.addCardCostTurn = None
        self.addCardVanish = None
        self.lookCards = None
        self.lookCardsDiscardUpTo = None
        self.lookCardsVanishUpTo = None
        self.summonUnit = None
        self.summonUnitNum = None
        self.summonAura = None
        self.summonAuraCharges = None
        self.summonAura2 = None
        self.summonAuraCharges2 = None
        self.summonAura3 = None
        self.summonAuraCharges3 = None
        self.sound = None
        self.soundPreAction = None
        self.soundPreActionFemale = None
        self.effectPreAction = ""
        self.effectCaster = ""
        self.effectCasterRepeat = None
        self.effectPostCastDelay = None
        self.effectCastCenter = None
        self.effectTrail = ""
        self.effectTrailRepeat = None
        self.effectTrailSpeed = 1
        self.effectTrailAngle = None
        self.effectTarget = ""
        self.effectPostTargetDelay = None
        self.target = ""
        self.enchantDamagePreCalculated = None
        self.colorUpgradePlain = "5E3016"
        self.colorUpgradeGold = "875700"
        self.colorUpgradeBlue = "215382"
        self.colorUpgradeRare = "7F15A6"
        super(CardData, self).__init__()
    @property
    def CardName(self):
        return cardName
    @CardName.setter
    def CardName(self, value):
        cardName = value
    @property
    def Id(self):
        return id
    @Id.setter
    def Id(self, value):
        id = value
    @property
    def InternalId(self):
        return internalId
    @InternalId.setter
    def InternalId(self, value):
        internalId = value
    @property
    def Visible(self):
        return visible
    @Visible.setter
    def Visible(self, value):
        visible = value
    @property
    def UpgradesTo1(self):
        return upgradesTo1
    @UpgradesTo1.setter
    def UpgradesTo1(self, value):
        upgradesTo1 = value
    @property
    def UpgradesTo2(self):
        return upgradesTo2
    @UpgradesTo2.setter
    def UpgradesTo2(self, value):
        upgradesTo2 = value
    @property
    def CardUpgraded(self):
        return cardUpgraded
    @CardUpgraded.setter
    def CardUpgraded(self, value):
        cardUpgraded = value
    @property
    def UpgradedFrom(self):
        return upgradedFrom
    @UpgradedFrom.setter
    def UpgradedFrom(self, value):
        upgradedFrom = value
    @property
    def BaseCard(self):
        return baseCard
    @BaseCard.setter
    def BaseCard(self, value):
        baseCard = value
    @property
    def CardNumber(self):
        return cardNumber
    @CardNumber.setter
    def CardNumber(self, value):
        cardNumber = value
    @property
    def Description(self):
        return description
    @Description.setter
    def Description(self, value):
        description = value
    @property
    def Fluff(self):
        return fluff
    @Fluff.setter
    def Fluff(self, value):
        fluff = value
    @property
    def DescriptionNormalized(self):
        return descriptionNormalized
    @DescriptionNormalized.setter
    def DescriptionNormalized(self, value):
        descriptionNormalized = value
    @property
    def KeyNotes(self):
        return keyNotes
    @KeyNotes.setter
    def KeyNotes(self, value):
        keyNotes = value
    @property
    def Sprite(self):
        return sprite
    @Sprite.setter
    def Sprite(self, value):
        sprite = value
    @property
    def Sound(self):
        return sound
    @Sound.setter
    def Sound(self, value):
        sound = value
    @property
    def SoundPreAction(self):
        return soundPreAction
    @SoundPreAction.setter
    def SoundPreAction(self, value):
        soundPreAction = value
    @property
    def EffectPreAction(self):
        return effectPreAction
    @EffectPreAction.setter
    def EffectPreAction(self, value):
        effectPreAction = value
    @property
    def EffectCaster(self):
        return effectCaster
    @EffectCaster.setter
    def EffectCaster(self, value):
        effectCaster = value
    @property
    def EffectPostCastDelay(self):
        return effectPostCastDelay
    @EffectPostCastDelay.setter
    def EffectPostCastDelay(self, value):
        effectPostCastDelay = value
    @property
    def EffectCasterRepeat(self):
        return effectCasterRepeat
    @EffectCasterRepeat.setter
    def EffectCasterRepeat(self, value):
        effectCasterRepeat = value
    @property
    def EffectCastCenter(self):
        return effectCastCenter
    @EffectCastCenter.setter
    def EffectCastCenter(self, value):
        effectCastCenter = value
    @property
    def EffectTrail(self):
        return effectTrail
    @EffectTrail.setter
    def EffectTrail(self, value):
        effectTrail = value
    @property
    def EffectTrailRepeat(self):
        return effectTrailRepeat
    @EffectTrailRepeat.setter
    def EffectTrailRepeat(self, value):
        effectTrailRepeat = value
    @property
    def EffectTrailSpeed(self):
        return effectTrailSpeed
    @EffectTrailSpeed.setter
    def EffectTrailSpeed(self, value):
        effectTrailSpeed = value
    @property
    def EffectTrailAngle(self):
        return effectTrailAngle
    @EffectTrailAngle.setter
    def EffectTrailAngle(self, value):
        effectTrailAngle = value
    @property
    def EffectTarget(self):
        return effectTarget
    @EffectTarget.setter
    def EffectTarget(self, value):
        effectTarget = value
    @property
    def MaxInDeck(self):
        return maxInDeck
    @MaxInDeck.setter
    def MaxInDeck(self, value):
        maxInDeck = value
    @property
    def CardRarity(self):
        return cardRarity
    @CardRarity.setter
    def CardRarity(self, value):
        cardRarity = value
    @property
    def CardType(self):
        return cardType
    @CardType.setter
    def CardType(self, value):
        cardType = value
    @property
    def CardTypeAux(self):
        return cardTypeAux
    @CardTypeAux.setter
    def CardTypeAux(self, value):
        cardTypeAux = value
    @property
    def CardClass(self):
        return cardClass
    @CardClass.setter
    def CardClass(self, value):
        cardClass = value
    @property
    def EnergyCost(self):
        return energyCost
    @EnergyCost.setter
    def EnergyCost(self, value):
        energyCost = value
    @property
    def EnergyCostOriginal(self):
        return energyCostOriginal
    @EnergyCostOriginal.setter
    def EnergyCostOriginal(self, value):
        energyCostOriginal = value
    @property
    def EnergyCostForShow(self):
        return energyCostForShow
    @EnergyCostForShow.setter
    def EnergyCostForShow(self, value):
        energyCostForShow = value
    @property
    def Playable(self):
        return playable
    @Playable.setter
    def Playable(self, value):
        playable = value
    @property
    def AutoplayDraw(self):
        return autoplayDraw
    @AutoplayDraw.setter
    def AutoplayDraw(self, value):
        autoplayDraw = value
    @property
    def AutoplayEndTurn(self):
        return autoplayEndTurn
    @AutoplayEndTurn.setter
    def AutoplayEndTurn(self, value):
        autoplayEndTurn = value
    @property
    def TargetType(self):
        return targetType
    @TargetType.setter
    def TargetType(self, value):
        targetType = value
    @property
    def TargetSide(self):
        return targetSide
    @TargetSide.setter
    def TargetSide(self, value):
        targetSide = value
    @property
    def TargetPosition(self):
        return targetPosition
    @TargetPosition.setter
    def TargetPosition(self, value):
        targetPosition = value
    @property
    def EffectRequired(self):
        return effectRequired
    @EffectRequired.setter
    def EffectRequired(self, value):
        effectRequired = value
    @property
    def EffectRepeat(self):
        return effectRepeat
    @EffectRepeat.setter
    def EffectRepeat(self, value):
        effectRepeat = value
    @property
    def EffectRepeatDelay(self):
        return effectRepeatDelay
    @EffectRepeatDelay.setter
    def EffectRepeatDelay(self, value):
        effectRepeatDelay = value
    @property
    def EffectRepeatEnergyBonus(self):
        return effectRepeatEnergyBonus
    @EffectRepeatEnergyBonus.setter
    def EffectRepeatEnergyBonus(self, value):
        effectRepeatEnergyBonus = value
    @property
    def EffectRepeatMaxBonus(self):
        return effectRepeatMaxBonus
    @EffectRepeatMaxBonus.setter
    def EffectRepeatMaxBonus(self, value):
        effectRepeatMaxBonus = value
    @property
    def EffectRepeatTarget(self):
        return effectRepeatTarget
    @EffectRepeatTarget.setter
    def EffectRepeatTarget(self, value):
        effectRepeatTarget = value
    @property
    def EffectRepeatModificator(self):
        return effectRepeatModificator
    @EffectRepeatModificator.setter
    def EffectRepeatModificator(self, value):
        effectRepeatModificator = value
    @property
    def DamageType(self):
        return damageType
    @DamageType.setter
    def DamageType(self, value):
        damageType = value
    @property
    def Damage(self):
        return damage
    @Damage.setter
    def Damage(self, value):
        damage = value
    @property
    def DamagePreCalculated(self):
        return damagePreCalculated
    @DamagePreCalculated.setter
    def DamagePreCalculated(self, value):
        damagePreCalculated = value
    @property
    def DamageSides(self):
        return damageSides
    @DamageSides.setter
    def DamageSides(self, value):
        damageSides = value
    @property
    def DamageSidesPreCalculated(self):
        return damageSidesPreCalculated
    @DamageSidesPreCalculated.setter
    def DamageSidesPreCalculated(self, value):
        damageSidesPreCalculated = value
    @property
    def DamageSelf(self):
        return damageSelf
    @DamageSelf.setter
    def DamageSelf(self, value):
        damageSelf = value
    @property
    def DamageSelfPreCalculated(self):
        return damageSelfPreCalculated
    @DamageSelfPreCalculated.setter
    def DamageSelfPreCalculated(self, value):
        damageSelfPreCalculated = value
    @property
    def DamageSelfPreCalculated2(self):
        return damageSelfPreCalculated2
    @DamageSelfPreCalculated2.setter
    def DamageSelfPreCalculated2(self, value):
        damageSelfPreCalculated2 = value
    @property
    def IgnoreBlock(self):
        return ignoreBlock
    @IgnoreBlock.setter
    def IgnoreBlock(self, value):
        ignoreBlock = value
    @property
    def DamageType2(self):
        return damageType2
    @DamageType2.setter
    def DamageType2(self, value):
        damageType2 = value
    @property
    def Damage2(self):
        return damage2
    @Damage2.setter
    def Damage2(self, value):
        damage2 = value
    @property
    def DamagePreCalculated2(self):
        return damagePreCalculated2
    @DamagePreCalculated2.setter
    def DamagePreCalculated2(self, value):
        damagePreCalculated2 = value
    @property
    def DamageSides2(self):
        return damageSides2
    @DamageSides2.setter
    def DamageSides2(self, value):
        damageSides2 = value
    @property
    def DamageSidesPreCalculated2(self):
        return damageSidesPreCalculated2
    @DamageSidesPreCalculated2.setter
    def DamageSidesPreCalculated2(self, value):
        damageSidesPreCalculated2 = value
    @property
    def DamageSelf2(self):
        return damageSelf2
    @DamageSelf2.setter
    def DamageSelf2(self, value):
        damageSelf2 = value
    @property
    def IgnoreBlock2(self):
        return ignoreBlock2
    @IgnoreBlock2.setter
    def IgnoreBlock2(self, value):
        ignoreBlock2 = value
    @property
    def SelfHealthLoss(self):
        return selfHealthLoss
    @SelfHealthLoss.setter
    def SelfHealthLoss(self, value):
        selfHealthLoss = value
    @property
    def DamageEnergyBonus(self):
        return damageEnergyBonus
    @DamageEnergyBonus.setter
    def DamageEnergyBonus(self, value):
        damageEnergyBonus = value
    @property
    def Heal(self):
        return heal
    @Heal.setter
    def Heal(self, value):
        heal = value
    @property
    def HealSides(self):
        return healSides
    @HealSides.setter
    def HealSides(self, value):
        healSides = value
    @property
    def HealSelf(self):
        return healSelf
    @HealSelf.setter
    def HealSelf(self, value):
        healSelf = value
    @property
    def HealEnergyBonus(self):
        return healEnergyBonus
    @HealEnergyBonus.setter
    def HealEnergyBonus(self, value):
        healEnergyBonus = value
    @property
    def HealSelfPerDamageDonePercent(self):
        return healSelfPerDamageDonePercent
    @HealSelfPerDamageDonePercent.setter
    def HealSelfPerDamageDonePercent(self, value):
        healSelfPerDamageDonePercent = value
    @property
    def HealCurses(self):
        return healCurses
    @HealCurses.setter
    def HealCurses(self, value):
        healCurses = value
    @property
    def HealAuraCurseSelf(self):
        return healAuraCurseSelf
    @HealAuraCurseSelf.setter
    def HealAuraCurseSelf(self, value):
        healAuraCurseSelf = value
    @property
    def HealAuraCurseName(self):
        return healAuraCurseName
    @HealAuraCurseName.setter
    def HealAuraCurseName(self, value):
        healAuraCurseName = value
    @property
    def HealAuraCurseName2(self):
        return healAuraCurseName2
    @HealAuraCurseName2.setter
    def HealAuraCurseName2(self, value):
        healAuraCurseName2 = value
    @property
    def HealAuraCurseName3(self):
        return healAuraCurseName3
    @HealAuraCurseName3.setter
    def HealAuraCurseName3(self, value):
        healAuraCurseName3 = value
    @property
    def HealAuraCurseName4(self):
        return healAuraCurseName4
    @HealAuraCurseName4.setter
    def HealAuraCurseName4(self, value):
        healAuraCurseName4 = value
    @property
    def DispelAuras(self):
        return dispelAuras
    @DispelAuras.setter
    def DispelAuras(self, value):
        dispelAuras = value
    @property
    def EnergyRecharge(self):
        return energyRecharge
    @EnergyRecharge.setter
    def EnergyRecharge(self, value):
        energyRecharge = value
    @property
    def Aura(self):
        return aura
    @Aura.setter
    def Aura(self, value):
        aura = value
    @property
    def AuraSelf(self):
        return auraSelf
    @AuraSelf.setter
    def AuraSelf(self, value):
        auraSelf = value
    @property
    def AuraCharges(self):
        return auraCharges
    @AuraCharges.setter
    def AuraCharges(self, value):
        auraCharges = value
    @property
    def Aura2(self):
        return aura2
    @Aura2.setter
    def Aura2(self, value):
        aura2 = value
    @property
    def AuraSelf2(self):
        return auraSelf2
    @AuraSelf2.setter
    def AuraSelf2(self, value):
        auraSelf2 = value
    @property
    def AuraCharges2(self):
        return auraCharges2
    @AuraCharges2.setter
    def AuraCharges2(self, value):
        auraCharges2 = value
    @property
    def Aura3(self):
        return aura3
    @Aura3.setter
    def Aura3(self, value):
        aura3 = value
    @property
    def AuraSelf3(self):
        return auraSelf3
    @AuraSelf3.setter
    def AuraSelf3(self, value):
        auraSelf3 = value
    @property
    def AuraCharges3(self):
        return auraCharges3
    @AuraCharges3.setter
    def AuraCharges3(self, value):
        auraCharges3 = value
    @property
    def Curse(self):
        return curse
    @Curse.setter
    def Curse(self, value):
        curse = value
    @property
    def CurseSelf(self):
        return curseSelf
    @CurseSelf.setter
    def CurseSelf(self, value):
        curseSelf = value
    @property
    def CurseCharges(self):
        return curseCharges
    @CurseCharges.setter
    def CurseCharges(self, value):
        curseCharges = value
    @property
    def Curse2(self):
        return curse2
    @Curse2.setter
    def Curse2(self, value):
        curse2 = value
    @property
    def CurseSelf2(self):
        return curseSelf2
    @CurseSelf2.setter
    def CurseSelf2(self, value):
        curseSelf2 = value
    @property
    def CurseCharges2(self):
        return curseCharges2
    @CurseCharges2.setter
    def CurseCharges2(self, value):
        curseCharges2 = value
    @property
    def Curse3(self):
        return curse3
    @Curse3.setter
    def Curse3(self, value):
        curse3 = value
    @property
    def CurseSelf3(self):
        return curseSelf3
    @CurseSelf3.setter
    def CurseSelf3(self, value):
        curseSelf3 = value
    @property
    def CurseCharges3(self):
        return curseCharges3
    @CurseCharges3.setter
    def CurseCharges3(self, value):
        curseCharges3 = value
    @property
    def PushTarget(self):
        return pushTarget
    @PushTarget.setter
    def PushTarget(self, value):
        pushTarget = value
    @property
    def PullTarget(self):
        return pullTarget
    @PullTarget.setter
    def PullTarget(self, value):
        pullTarget = value
    @property
    def DrawCard(self):
        return drawCard
    @DrawCard.setter
    def DrawCard(self, value):
        drawCard = value
    @property
    def DiscardCard(self):
        return discardCard
    @DiscardCard.setter
    def DiscardCard(self, value):
        discardCard = value
    @property
    def DiscardCardType(self):
        return discardCardType
    @DiscardCardType.setter
    def DiscardCardType(self, value):
        discardCardType = value
    @property
    def DiscardCardTypeAux(self):
        return discardCardTypeAux
    @DiscardCardTypeAux.setter
    def DiscardCardTypeAux(self, value):
        discardCardTypeAux = value
    @property
    def DiscardCardAutomatic(self):
        return discardCardAutomatic
    @DiscardCardAutomatic.setter
    def DiscardCardAutomatic(self, value):
        discardCardAutomatic = value
    @property
    def DiscardCardPlace(self):
        return discardCardPlace
    @DiscardCardPlace.setter
    def DiscardCardPlace(self, value):
        discardCardPlace = value
    @property
    def AddCard(self):
        return addCard
    @AddCard.setter
    def AddCard(self, value):
        addCard = value
    @property
    def AddCardId(self):
        return addCardId
    @AddCardId.setter
    def AddCardId(self, value):
        addCardId = value
    @property
    def AddCardType(self):
        return addCardType
    @AddCardType.setter
    def AddCardType(self, value):
        addCardType = value
    @property
    def AddCardTypeAux(self):
        return addCardTypeAux
    @AddCardTypeAux.setter
    def AddCardTypeAux(self, value):
        addCardTypeAux = value
    @property
    def AddCardChoose(self):
        return addCardChoose
    @AddCardChoose.setter
    def AddCardChoose(self, value):
        addCardChoose = value
    @property
    def AddCardFrom(self):
        return addCardFrom
    @AddCardFrom.setter
    def AddCardFrom(self, value):
        addCardFrom = value
    @property
    def AddCardPlace(self):
        return addCardPlace
    @AddCardPlace.setter
    def AddCardPlace(self, value):
        addCardPlace = value
    @property
    def AddCardReducedCost(self):
        return addCardReducedCost
    @AddCardReducedCost.setter
    def AddCardReducedCost(self, value):
        addCardReducedCost = value
    @property
    def AddCardCostTurn(self):
        return addCardCostTurn
    @AddCardCostTurn.setter
    def AddCardCostTurn(self, value):
        addCardCostTurn = value
    @property
    def AddCardVanish(self):
        return addCardVanish
    @AddCardVanish.setter
    def AddCardVanish(self, value):
        addCardVanish = value
    @property
    def LookCards(self):
        return lookCards
    @LookCards.setter
    def LookCards(self, value):
        lookCards = value
    @property
    def LookCardsDiscardUpTo(self):
        return lookCardsDiscardUpTo
    @LookCardsDiscardUpTo.setter
    def LookCardsDiscardUpTo(self, value):
        lookCardsDiscardUpTo = value
    @property
    def SummonUnit(self):
        return summonUnit
    @SummonUnit.setter
    def SummonUnit(self, value):
        summonUnit = value
    @property
    def SummonUnitNum(self):
        return summonUnitNum
    @SummonUnitNum.setter
    def SummonUnitNum(self, value):
        summonUnitNum = value
    @property
    def Vanish(self):
        return vanish
    @Vanish.setter
    def Vanish(self, value):
        vanish = value
    @property
    def Lazy(self):
        return lazy
    @Lazy.setter
    def Lazy(self, value):
        lazy = value
    @property
    def Innate(self):
        return innate
    @Innate.setter
    def Innate(self, value):
        innate = value
    @property
    def Corrupted(self):
        return corrupted
    @Corrupted.setter
    def Corrupted(self, value):
        corrupted = value
    @property
    def EndTurn(self):
        return endTurn
    @EndTurn.setter
    def EndTurn(self, value):
        endTurn = value
    @property
    def MoveToCenter(self):
        return moveToCenter
    @MoveToCenter.setter
    def MoveToCenter(self, value):
        moveToCenter = value
    @property
    def ModifiedByTrait(self):
        return modifiedByTrait
    @ModifiedByTrait.setter
    def ModifiedByTrait(self, value):
        modifiedByTrait = value
    @property
    def EffectPostTargetDelay(self):
        return effectPostTargetDelay
    @EffectPostTargetDelay.setter
    def EffectPostTargetDelay(self, value):
        effectPostTargetDelay = value
    @property
    def SpecialValueGlobal(self):
        return specialValueGlobal
    @SpecialValueGlobal.setter
    def SpecialValueGlobal(self, value):
        specialValueGlobal = value
    @property
    def SpecialValueModifierGlobal(self):
        return specialValueModifierGlobal
    @SpecialValueModifierGlobal.setter
    def SpecialValueModifierGlobal(self, value):
        specialValueModifierGlobal = value
    @property
    def SpecialValue1(self):
        return specialValue1
    @SpecialValue1.setter
    def SpecialValue1(self, value):
        specialValue1 = value
    @property
    def SpecialValueModifier1(self):
        return specialValueModifier1
    @SpecialValueModifier1.setter
    def SpecialValueModifier1(self, value):
        specialValueModifier1 = value
    @property
    def SpecialValue2(self):
        return specialValue2
    @SpecialValue2.setter
    def SpecialValue2(self, value):
        specialValue2 = value
    @property
    def SpecialValueModifier2(self):
        return specialValueModifier2
    @SpecialValueModifier2.setter
    def SpecialValueModifier2(self, value):
        specialValueModifier2 = value
    @property
    def DamageSpecialValueGlobal(self):
        return damageSpecialValueGlobal
    @DamageSpecialValueGlobal.setter
    def DamageSpecialValueGlobal(self, value):
        damageSpecialValueGlobal = value
    @property
    def DamageSpecialValue1(self):
        return damageSpecialValue1
    @DamageSpecialValue1.setter
    def DamageSpecialValue1(self, value):
        damageSpecialValue1 = value
    @property
    def DamageSpecialValue2(self):
        return damageSpecialValue2
    @DamageSpecialValue2.setter
    def DamageSpecialValue2(self, value):
        damageSpecialValue2 = value
    @property
    def Damage2SpecialValueGlobal(self):
        return damage2SpecialValueGlobal
    @Damage2SpecialValueGlobal.setter
    def Damage2SpecialValueGlobal(self, value):
        damage2SpecialValueGlobal = value
    @property
    def Damage2SpecialValue1(self):
        return damage2SpecialValue1
    @Damage2SpecialValue1.setter
    def Damage2SpecialValue1(self, value):
        damage2SpecialValue1 = value
    @property
    def Damage2SpecialValue2(self):
        return damage2SpecialValue2
    @Damage2SpecialValue2.setter
    def Damage2SpecialValue2(self, value):
        damage2SpecialValue2 = value
    @property
    def SpecialAuraCurseNameGlobal(self):
        return specialAuraCurseNameGlobal
    @SpecialAuraCurseNameGlobal.setter
    def SpecialAuraCurseNameGlobal(self, value):
        specialAuraCurseNameGlobal = value
    @property
    def SpecialAuraCurseName1(self):
        return specialAuraCurseName1
    @SpecialAuraCurseName1.setter
    def SpecialAuraCurseName1(self, value):
        specialAuraCurseName1 = value
    @property
    def SpecialAuraCurseName2(self):
        return specialAuraCurseName2
    @SpecialAuraCurseName2.setter
    def SpecialAuraCurseName2(self, value):
        specialAuraCurseName2 = value
    @property
    def AuraChargesSpecialValue1(self):
        return auraChargesSpecialValue1
    @AuraChargesSpecialValue1.setter
    def AuraChargesSpecialValue1(self, value):
        auraChargesSpecialValue1 = value
    @property
    def AuraChargesSpecialValue2(self):
        return auraChargesSpecialValue2
    @AuraChargesSpecialValue2.setter
    def AuraChargesSpecialValue2(self, value):
        auraChargesSpecialValue2 = value
    @property
    def AuraChargesSpecialValueGlobal(self):
        return auraChargesSpecialValueGlobal
    @AuraChargesSpecialValueGlobal.setter
    def AuraChargesSpecialValueGlobal(self, value):
        auraChargesSpecialValueGlobal = value
    @property
    def AuraCharges2SpecialValue1(self):
        return auraCharges2SpecialValue1
    @AuraCharges2SpecialValue1.setter
    def AuraCharges2SpecialValue1(self, value):
        auraCharges2SpecialValue1 = value
    @property
    def AuraCharges2SpecialValue2(self):
        return auraCharges2SpecialValue2
    @AuraCharges2SpecialValue2.setter
    def AuraCharges2SpecialValue2(self, value):
        auraCharges2SpecialValue2 = value
    @property
    def AuraCharges2SpecialValueGlobal(self):
        return auraCharges2SpecialValueGlobal
    @AuraCharges2SpecialValueGlobal.setter
    def AuraCharges2SpecialValueGlobal(self, value):
        auraCharges2SpecialValueGlobal = value
    @property
    def AuraCharges3SpecialValue1(self):
        return auraCharges3SpecialValue1
    @AuraCharges3SpecialValue1.setter
    def AuraCharges3SpecialValue1(self, value):
        auraCharges3SpecialValue1 = value
    @property
    def AuraCharges3SpecialValue2(self):
        return auraCharges3SpecialValue2
    @AuraCharges3SpecialValue2.setter
    def AuraCharges3SpecialValue2(self, value):
        auraCharges3SpecialValue2 = value
    @property
    def AuraCharges3SpecialValueGlobal(self):
        return auraCharges3SpecialValueGlobal
    @AuraCharges3SpecialValueGlobal.setter
    def AuraCharges3SpecialValueGlobal(self, value):
        auraCharges3SpecialValueGlobal = value
    @property
    def CurseChargesSpecialValue1(self):
        return curseChargesSpecialValue1
    @CurseChargesSpecialValue1.setter
    def CurseChargesSpecialValue1(self, value):
        curseChargesSpecialValue1 = value
    @property
    def CurseChargesSpecialValue2(self):
        return curseChargesSpecialValue2
    @CurseChargesSpecialValue2.setter
    def CurseChargesSpecialValue2(self, value):
        curseChargesSpecialValue2 = value
    @property
    def CurseChargesSpecialValueGlobal(self):
        return curseChargesSpecialValueGlobal
    @CurseChargesSpecialValueGlobal.setter
    def CurseChargesSpecialValueGlobal(self, value):
        curseChargesSpecialValueGlobal = value
    @property
    def CurseCharges2SpecialValue1(self):
        return curseCharges2SpecialValue1
    @CurseCharges2SpecialValue1.setter
    def CurseCharges2SpecialValue1(self, value):
        curseCharges2SpecialValue1 = value
    @property
    def CurseCharges2SpecialValue2(self):
        return curseCharges2SpecialValue2
    @CurseCharges2SpecialValue2.setter
    def CurseCharges2SpecialValue2(self, value):
        curseCharges2SpecialValue2 = value
    @property
    def CurseCharges2SpecialValueGlobal(self):
        return curseCharges2SpecialValueGlobal
    @CurseCharges2SpecialValueGlobal.setter
    def CurseCharges2SpecialValueGlobal(self, value):
        curseCharges2SpecialValueGlobal = value
    @property
    def CurseCharges3SpecialValue1(self):
        return curseCharges3SpecialValue1
    @CurseCharges3SpecialValue1.setter
    def CurseCharges3SpecialValue1(self, value):
        curseCharges3SpecialValue1 = value
    @property
    def CurseCharges3SpecialValue2(self):
        return curseCharges3SpecialValue2
    @CurseCharges3SpecialValue2.setter
    def CurseCharges3SpecialValue2(self, value):
        curseCharges3SpecialValue2 = value
    @property
    def CurseCharges3SpecialValueGlobal(self):
        return curseCharges3SpecialValueGlobal
    @CurseCharges3SpecialValueGlobal.setter
    def CurseCharges3SpecialValueGlobal(self, value):
        curseCharges3SpecialValueGlobal = value
    @property
    def HealSpecialValueGlobal(self):
        return healSpecialValueGlobal
    @HealSpecialValueGlobal.setter
    def HealSpecialValueGlobal(self, value):
        healSpecialValueGlobal = value
    @property
    def HealSpecialValue1(self):
        return healSpecialValue1
    @HealSpecialValue1.setter
    def HealSpecialValue1(self, value):
        healSpecialValue1 = value
    @property
    def HealSpecialValue2(self):
        return healSpecialValue2
    @HealSpecialValue2.setter
    def HealSpecialValue2(self, value):
        healSpecialValue2 = value
    @property
    def SelfHealthLossSpecialGlobal(self):
        return selfHealthLossSpecialGlobal
    @SelfHealthLossSpecialGlobal.setter
    def SelfHealthLossSpecialGlobal(self, value):
        selfHealthLossSpecialGlobal = value
    @property
    def SelfHealthLossSpecialValue1(self):
        return selfHealthLossSpecialValue1
    @SelfHealthLossSpecialValue1.setter
    def SelfHealthLossSpecialValue1(self, value):
        selfHealthLossSpecialValue1 = value
    @property
    def SelfHealthLossSpecialValue2(self):
        return selfHealthLossSpecialValue2
    @SelfHealthLossSpecialValue2.setter
    def SelfHealthLossSpecialValue2(self, value):
        selfHealthLossSpecialValue2 = value
    @property
    def FluffPercent(self):
        return fluffPercent
    @FluffPercent.setter
    def FluffPercent(self, value):
        fluffPercent = value
    @property
    def Item(self):
        return item
    @Item.setter
    def Item(self, value):
        item = value
    @property
    def SummonAura(self):
        return summonAura
    @SummonAura.setter
    def SummonAura(self, value):
        summonAura = value
    @property
    def SummonAuraCharges(self):
        return summonAuraCharges
    @SummonAuraCharges.setter
    def SummonAuraCharges(self, value):
        summonAuraCharges = value
    @property
    def SummonAura2(self):
        return summonAura2
    @SummonAura2.setter
    def SummonAura2(self, value):
        summonAura2 = value
    @property
    def SummonAuraCharges2(self):
        return summonAuraCharges2
    @SummonAuraCharges2.setter
    def SummonAuraCharges2(self, value):
        summonAuraCharges2 = value
    @property
    def SummonAura3(self):
        return summonAura3
    @SummonAura3.setter
    def SummonAura3(self, value):
        summonAura3 = value
    @property
    def SummonAuraCharges3(self):
        return summonAuraCharges3
    @SummonAuraCharges3.setter
    def SummonAuraCharges3(self, value):
        summonAuraCharges3 = value
    @property
    def HealSelfSpecialValueGlobal(self):
        return healSelfSpecialValueGlobal
    @HealSelfSpecialValueGlobal.setter
    def HealSelfSpecialValueGlobal(self, value):
        healSelfSpecialValueGlobal = value
    @property
    def HealSelfSpecialValue1(self):
        return healSelfSpecialValue1
    @HealSelfSpecialValue1.setter
    def HealSelfSpecialValue1(self, value):
        healSelfSpecialValue1 = value
    @property
    def HealSelfSpecialValue2(self):
        return healSelfSpecialValue2
    @HealSelfSpecialValue2.setter
    def HealSelfSpecialValue2(self, value):
        healSelfSpecialValue2 = value
    @property
    def RelatedCard(self):
        return relatedCard
    @RelatedCard.setter
    def RelatedCard(self, value):
        relatedCard = value
    @property
    def PetModel(self):
        return petModel
    @PetModel.setter
    def PetModel(self, value):
        petModel = value
    @property
    def PetFront(self):
        return petFront
    @PetFront.setter
    def PetFront(self, value):
        petFront = value
    @property
    def PetOffset(self):
        return petOffset
    @PetOffset.setter
    def PetOffset(self, value):
        petOffset = value
    @property
    def PetSize(self):
        return petSize
    @PetSize.setter
    def PetSize(self, value):
        petSize = value
    @property
    def PetInvert(self):
        return petInvert
    @PetInvert.setter
    def PetInvert(self, value):
        petInvert = value
    @property
    def IsPetAttack(self):
        return isPetAttack
    @IsPetAttack.setter
    def IsPetAttack(self, value):
        isPetAttack = value
    @property
    def IsPetCast(self):
        return isPetCast
    @IsPetCast.setter
    def IsPetCast(self, value):
        isPetCast = value
    @property
    def UpgradesToRare(self):
        return upgradesToRare
    @UpgradesToRare.setter
    def UpgradesToRare(self, value):
        upgradesToRare = value
    @property
    def ExhaustCounter(self):
        return exhaustCounter
    @ExhaustCounter.setter
    def ExhaustCounter(self, value):
        exhaustCounter = value
    @property
    def Starter(self):
        return starter
    @Starter.setter
    def Starter(self, value):
        starter = value
    @property
    def Target(self):
        return target
    @Target.setter
    def Target(self, value):
        target = value
    @property
    def ItemEnchantment(self):
        return itemEnchantment
    @ItemEnchantment.setter
    def ItemEnchantment(self, value):
        itemEnchantment = value
    @property
    def AddCardList(self):
        return addCardList
    @AddCardList.setter
    def AddCardList(self, value):
        addCardList = value
    @property
    def ShowInTome(self):
        return showInTome
    @ShowInTome.setter
    def ShowInTome(self, value):
        showInTome = value
    @property
    def LookCardsVanishUpTo(self):
        return lookCardsVanishUpTo
    @LookCardsVanishUpTo.setter
    def LookCardsVanishUpTo(self, value):
        lookCardsVanishUpTo = value
    @property
    def TransferCurses(self):
        return transferCurses
    @TransferCurses.setter
    def TransferCurses(self, value):
        transferCurses = value
    @property
    def KillPet(self):
        return killPet
    @KillPet.setter
    def KillPet(self, value):
        killPet = value
    @property
    def ReduceCurses(self):
        return reduceCurses
    @ReduceCurses.setter
    def ReduceCurses(self, value):
        reduceCurses = value
    @property
    def AcEnergyBonus(self):
        return acEnergyBonus
    @AcEnergyBonus.setter
    def AcEnergyBonus(self, value):
        acEnergyBonus = value
    @property
    def AcEnergyBonusQuantity(self):
        return acEnergyBonusQuantity
    @AcEnergyBonusQuantity.setter
    def AcEnergyBonusQuantity(self, value):
        acEnergyBonusQuantity = value
    @property
    def EnergyReductionPermanent(self):
        return energyReductionPermanent
    @EnergyReductionPermanent.setter
    def EnergyReductionPermanent(self, value):
        energyReductionPermanent = value
    @property
    def EnergyReductionTemporal(self):
        return energyReductionTemporal
    @EnergyReductionTemporal.setter
    def EnergyReductionTemporal(self, value):
        energyReductionTemporal = value
    @property
    def EnergyReductionToZeroPermanent(self):
        return energyReductionToZeroPermanent
    @EnergyReductionToZeroPermanent.setter
    def EnergyReductionToZeroPermanent(self, value):
        energyReductionToZeroPermanent = value
    @property
    def EnergyReductionToZeroTemporal(self):
        return energyReductionToZeroTemporal
    @EnergyReductionToZeroTemporal.setter
    def EnergyReductionToZeroTemporal(self, value):
        energyReductionToZeroTemporal = value
    @property
    def AcEnergyBonus2(self):
        return acEnergyBonus2
    @AcEnergyBonus2.setter
    def AcEnergyBonus2(self, value):
        acEnergyBonus2 = value
    @property
    def AcEnergyBonus2Quantity(self):
        return acEnergyBonus2Quantity
    @AcEnergyBonus2Quantity.setter
    def AcEnergyBonus2Quantity(self, value):
        acEnergyBonus2Quantity = value
    @property
    def StealAuras(self):
        return stealAuras
    @StealAuras.setter
    def StealAuras(self, value):
        stealAuras = value
    @property
    def FlipSprite(self):
        return flipSprite
    @FlipSprite.setter
    def FlipSprite(self, value):
        flipSprite = value
    @property
    def SoundPreActionFemale(self):
        return soundPreActionFemale
    @SoundPreActionFemale.setter
    def SoundPreActionFemale(self, value):
        soundPreActionFemale = value
    @property
    def ReduceAuras(self):
        return reduceAuras
    @ReduceAuras.setter
    def ReduceAuras(self, value):
        reduceAuras = value
    @property
    def IncreaseCurses(self):
        return increaseCurses
    @IncreaseCurses.setter
    def IncreaseCurses(self, value):
        increaseCurses = value
    @property
    def IncreaseAuras(self):
        return increaseAuras
    @IncreaseAuras.setter
    def IncreaseAuras(self, value):
        increaseAuras = value
    @property
    def OnlyInWeekly(self):
        return onlyInWeekly
    @OnlyInWeekly.setter
    def OnlyInWeekly(self, value):
        onlyInWeekly = value
    def Init(self, newId):
        id = newId
    def InitClone(self, _internalId):
        id = _internalId
        internalId = _internalId
        if (energyCostOriginal == 0):
            energyCostOriginal = energyCost
        damageTypeOriginal = damageType
        damageType2Original = damageType2
        damagePreCalculated = damage
        damagePreCalculated2 = damage2
        damageSelfPreCalculated = damageSelf
        damageSidesPreCalculated = damageSides
        damageSidesPreCalculated2 = damageSides2
        damageSelfPreCalculated2 = damageSelf2
        effectRequired = effectRequired.ToLower()
        if (itemEnchantment != None):
            enchantDamagePreCalculated = itemEnchantment.DamageToTarget
        elif (item != None):
            enchantDamagePreCalculated = item.DamageToTarget
        healPreCalculated = heal
        healSelfPreCalculated = healSelf
        if innate:
            KeyNotes.Add(Globals.Instance.GetKeyNotesData("innate"))
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("innate"), id)
        if vanish:
            KeyNotes.Add(Globals.Instance.GetKeyNotesData("vanish"))
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("vanish"), id)
        if (energyRecharge > 0):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData("energy"))
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("energy"), id)
        if (aura != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(aura.Id))
        if (aura2 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(aura2.Id))
        if (aura3 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(aura3.Id))
        if (auraSelf != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(auraSelf.Id))
        if (auraSelf2 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(auraSelf2.Id))
        if (auraSelf3 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(auraSelf3.Id))
        if (curse != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(curse.Id))
        if (curse2 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(curse2.Id))
        if (curse3 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(curse3.Id))
        if (curseSelf != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(curseSelf.Id))
        if (curseSelf2 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(curseSelf2.Id))
        if (curseSelf3 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(curseSelf3.Id))
        if (healAuraCurseSelf != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(healAuraCurseSelf.Id))
        if (healAuraCurseName != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(healAuraCurseName.Id))
        if (healAuraCurseName2 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(healAuraCurseName2.Id))
        if (healAuraCurseName3 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(healAuraCurseName3.Id))
        if (healAuraCurseName4 != None):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(healAuraCurseName4.Id))
    def InitClone2(self):
        if (effectRequired != ""):
            KeyNotes.Add(Globals.Instance.GetKeyNotesData(effectRequired))
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText(effectRequired), id)
        SetDescriptionNew()
        SetTarget()
        SetRarity()
    def ModifyDamageType(self, dt = Enums.DamageType._None, ch = None):
        _ = damageType
        if (dt == Enums.DamageType._None):
            damageType = damageTypeOriginal
            damageType2 = damageType2Original
        else:
            damageType = dt
            damageType2 = dt
    def SetEnchantDamagePrecalculated(self, damage):
        enchantDamagePreCalculated = damage
    def SetDamagePrecalculated(self, damage):
        damagePreCalculated = damage
    def SetDamagePrecalculated2(self, damage):
        damagePreCalculated2 = damage
    def SetDamageSelfPrecalculated(self, damage):
        damageSelfPreCalculated = damage
    def SetDamageSelfPrecalculated2(self, damage):
        damageSelfPreCalculated2 = damage
    def SetDamageSidesPrecalculated(self, damage):
        damageSidesPreCalculated = damage
    def SetDamageSidesPrecalculated2(self, damage):
        damageSidesPreCalculated2 = damage
    def SetHealPrecalculated(self, heal):
        healPreCalculated = heal
    def SetHealSelfPrecalculated(self, heal):
        healSelfPreCalculated = heal
    def ColorTextArray(self, type, *text):
        stringBuilder = StringBuilder()
        stringBuilder.Append("<nobr>")
        if ((type == "damage")):
            stringBuilder.Append("<color=#B00A00>")
        elif ((type == "heal")):
            stringBuilder.Append("<color=#1E650F>")
        elif ((type == "aura")):
            stringBuilder.Append("<color=#263ABC>")
        elif ((type == "curse")):
            stringBuilder.Append("<color=#720070>")
        elif ((type == "system")):
            stringBuilder.Append("<color=#5E3016>")
        elif ((type == "")):
            pass
        else:
            stringBuilder.Append("<color=#5E3016")
            stringBuilder.Append(">")
        num = 0
        for value in text:
            if (num > 0):
                stringBuilder.Append(" ")
            stringBuilder.Append(value)
            num += 1
        if (type != ""):
            stringBuilder.Append("</color>")
        stringBuilder.Append("</nobr> ")
        return stringBuilder.ToString()
    def GetFinalAuraCharges(self, acId, charges, character = None):
        if (character == None):
            return charges
        return (charges + character.GetAuraCurseQuantityModification(acId, cardClass))
    def SpriteText(self, sprite):
        stringBuilder = StringBuilder()
        text = sprite.ToLower().Replace(" ", "")
        if (((text == "block")) or ((text == "card"))):
            stringBuilder.Append("<space=.2>")
        elif ((text == "piercing")):
            stringBuilder.Append("<space=.4>")
        elif ((text == "bleed")):
            stringBuilder.Append("<space=.1>")
        else:
            stringBuilder.Append("<space=.3>")
        stringBuilder.Append("<size=+.1><sprite name=")
        stringBuilder.Append(text)
        stringBuilder.Append("></size>")
        if ((text == "bleed")):
            stringBuilder.Append("<space=-.4>")
        elif ((text == "card")):
            stringBuilder.Append("<space=-.2>")
        elif (((text == "reinforce")) or ((text == "fire"))):
            pass
        else:
            stringBuilder.Append("<space=-.3>")
        return stringBuilder.ToString()
    def GetRequireText(self):
        text = ""
        if (effectRequired != ""):
            text = str.Format(Texts.Instance.GetText("requireSkill"), Globals.Instance.GetKeyNotesData(effectRequired).KeynoteName)
            if ((effectRequired.ToLower() == "stanzai") or (effectRequired.ToLower() == "stanzaii")):
                text += "+"
        return text
    def SetRarity(self):
        if (cardRarity == Enums.CardRarity.Common):
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("common"), id)
        elif (cardRarity == Enums.CardRarity.Uncommon):
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("uncommon"), id)
        elif (cardRarity == Enums.CardRarity.Rare):
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("rare"), id)
        elif (cardRarity == Enums.CardRarity.Epic):
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("epic"), id)
        elif (cardRarity == Enums.CardRarity.Mythic):
            Globals.Instance.IncludeInSearch(Texts.Instance.GetText("mythic"), id)
    def SetTarget(self):
        if autoplayDraw:
            target = Texts.Instance.GetText("onDraw")
        elif autoplayEndTurn:
            target = Texts.Instance.GetText("onEndTurn")
        elif ((targetType == Enums.CardTargetType.Global) and (targetSide == Enums.CardTargetSide.Anyone)):
            target = Texts.Instance.GetText("global")
        elif (targetSide == Enums.CardTargetSide.Self):
            target = Texts.Instance.GetText("self")
        elif ((targetSide == Enums.CardTargetSide.Anyone) and (targetPosition == Enums.CardTargetPosition.Random)):
            target = Texts.Instance.GetText("random")
        elif (((targetType == Enums.CardTargetType.Single) and (targetSide == Enums.CardTargetSide.Anyone)) and (targetPosition == Enums.CardTargetPosition.Anywhere)):
            target = Texts.Instance.GetText("anyone")
        elif (cardClass != Enums.CardClass.Monster):
            if (targetSide == Enums.CardTargetSide.Friend):
                if (targetType == Enums.CardTargetType.Global):
                    target = Texts.Instance.GetText("allHeroes")
                elif (targetPosition == Enums.CardTargetPosition.Random):
                    target = Texts.Instance.GetText("randomHero")
                elif (targetPosition == Enums.CardTargetPosition.Front):
                    target = Texts.Instance.GetText("frontHero")
                elif (targetPosition == Enums.CardTargetPosition.Back):
                    target = Texts.Instance.GetText("backHero")
                else:
                    target = Texts.Instance.GetText("hero")
            elif (targetSide == Enums.CardTargetSide.FriendNotSelf):
                target = Texts.Instance.GetText("otherHero")
            elif (targetSide == Enums.CardTargetSide.Enemy):
                if (targetType == Enums.CardTargetType.Global):
                    target = Texts.Instance.GetText("allMonsters")
                elif (targetPosition == Enums.CardTargetPosition.Random):
                    target = Texts.Instance.GetText("randomMonster")
                elif (targetPosition == Enums.CardTargetPosition.Front):
                    target = Texts.Instance.GetText("frontMonster")
                elif (targetPosition == Enums.CardTargetPosition.Back):
                    target = Texts.Instance.GetText("backMonster")
                else:
                    target = Texts.Instance.GetText("monster")
        elif (cardClass == Enums.CardClass.Monster):
            if (targetSide == Enums.CardTargetSide.Friend):
                if (targetType == Enums.CardTargetType.Global):
                    target = Texts.Instance.GetText("allMonsters")
                elif (targetPosition == Enums.CardTargetPosition.Random):
                    target = Texts.Instance.GetText("randomMonster")
                elif (targetPosition == Enums.CardTargetPosition.Front):
                    target = Texts.Instance.GetText("frontMonster")
                elif (targetPosition == Enums.CardTargetPosition.Back):
                    target = Texts.Instance.GetText("backMonster")
                elif (targetPosition == Enums.CardTargetPosition.Middle):
                    target = Texts.Instance.GetText("middleMonster")
                elif (targetPosition == Enums.CardTargetPosition.Slowest):
                    target = Texts.Instance.GetText("slowestMonster")
                elif (targetPosition == Enums.CardTargetPosition.Fastest):
                    target = Texts.Instance.GetText("fastestMonster")
                elif (targetPosition == Enums.CardTargetPosition.LeastHP):
                    target = Texts.Instance.GetText("leastHPMonster")
                elif (targetPosition == Enums.CardTargetPosition.MostHP):
                    target = Texts.Instance.GetText("mostHPMonster")
                else:
                    target = Texts.Instance.GetText("monster")
            elif (targetSide == Enums.CardTargetSide.FriendNotSelf):
                target = Texts.Instance.GetText("otherMonster")
            elif (targetSide == Enums.CardTargetSide.Enemy):
                if (targetType == Enums.CardTargetType.Global):
                    target = Texts.Instance.GetText("allHeroes")
                elif (targetPosition == Enums.CardTargetPosition.Random):
                    target = Texts.Instance.GetText("randomHero")
                elif (targetPosition == Enums.CardTargetPosition.Front):
                    target = Texts.Instance.GetText("frontHero")
                elif (targetPosition == Enums.CardTargetPosition.Back):
                    target = Texts.Instance.GetText("backHero")
                elif (targetPosition == Enums.CardTargetPosition.Middle):
                    target = Texts.Instance.GetText("middleHero")
                elif (targetPosition == Enums.CardTargetPosition.Slowest):
                    target = Texts.Instance.GetText("slowestHero")
                elif (targetPosition == Enums.CardTargetPosition.Fastest):
                    target = Texts.Instance.GetText("fastestHero")
                elif (targetPosition == Enums.CardTargetPosition.LeastHP):
                    target = Texts.Instance.GetText("leastHPHero")
                elif (targetPosition == Enums.CardTargetPosition.MostHP):
                    target = Texts.Instance.GetText("mostHPHero")
                else:
                    target = Texts.Instance.GetText("hero")
        Globals.Instance.IncludeInSearch(target, id)
    def SetDescriptionNew(self, forceDescription = False, character = None, includeInSearch = True):
        if (forceDescription or (not Globals.Instance.CardsDescriptionNormalized.ContainsKey(id))):
            stringBuilder = StringBuilder()
            stringBuilder2 = StringBuilder()
            value = "<line-height=15%><br></line-height>"
            value2 = "<color=#444><size=-.15>"
            value3 = "</size></color>"
            value4 = "<color=#5E3016><size=-.15>"
            num = 0
            if (descriptionId != ""):
                stringBuilder.Append(Functions.FormatStringCard(Texts.Instance.GetText(descriptionId)))
            elif ((item == None) and (itemEnchantment == None)):
                text = ""
                text2 = ""
                text3 = ""
                num2 = 0
                text4 = ""
                flag = False
                flag2 = False
                flag3 = True
                flag4 = False
                stringBuilder3 = StringBuilder()
                if ((((damage > 0) or (damage2 > 0)) or (damageSelf > 0)) or (DamageSelf2 > 0)):
                    flag3 = False
                if (drawCard != 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDraw"), ColorTextArray("", NumFormat(drawCard), SpriteText("card"))))
                    stringBuilder.Append("<br>")
                num = 0
                if ((summonUnit != None) and (summonUnitNum > 0)):
                    stringBuilder2.Append("\n<color=#5E3016>")
                    if (summonUnitNum > 1):
                        stringBuilder2.Append(summonUnitNum)
                        stringBuilder2.Append(" ")
                    if ((summonUnit != None) and (Globals.Instance.GetNPC(summonUnit.Id) != None)):
                        stringBuilder2.Append(Globals.Instance.GetNPC(summonUnit.Id).NPCName)
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSummon"), stringBuilder2.ToString()))
                    stringBuilder.Append("</color>\n")
                    stringBuilder2.Clear()
                num = 0
                if (((specialValueGlobal == Enums.CardSpecialValue._None) and (specialValue1 == Enums.CardSpecialValue._None)) and (specialValue2 == Enums.CardSpecialValue._None)):
                    stringBuilder4 = StringBuilder()
                    stringBuilder5 = StringBuilder()
                    if (healAuraCurseName != None):
                        if healAuraCurseName.IsAura:
                            stringBuilder4.Append(SpriteText(healAuraCurseName.ACName))
                        else:
                            stringBuilder5.Append(SpriteText(healAuraCurseName.ACName))
                    if (healAuraCurseName2 != None):
                        if healAuraCurseName2.IsAura:
                            stringBuilder4.Append(SpriteText(healAuraCurseName2.ACName))
                        else:
                            stringBuilder5.Append(SpriteText(healAuraCurseName2.ACName))
                    if (healAuraCurseName3 != None):
                        if healAuraCurseName3.IsAura:
                            stringBuilder4.Append(SpriteText(healAuraCurseName3.ACName))
                        else:
                            stringBuilder5.Append(SpriteText(healAuraCurseName3.ACName))
                    if (healAuraCurseName4 != None):
                        if healAuraCurseName4.IsAura:
                            stringBuilder4.Append(SpriteText(healAuraCurseName4.ACName))
                        else:
                            stringBuilder5.Append(SpriteText(healAuraCurseName4.ACName))
                    if (stringBuilder4.Length > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurge"), stringBuilder4.ToString()))
                        stringBuilder.Append("\n")
                    if (stringBuilder5.Length > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispel"), stringBuilder5.ToString()))
                        stringBuilder.Append("\n")
                    if (healCurses > 0):
                        if (targetSide == Enums.CardTargetSide.Enemy):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurge"), ColorTextArray("aura", NumFormatItem(healCurses))))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispel"), ColorTextArray("curse", NumFormatItem(healCurses))))
                        stringBuilder.Append("\n")
                    if (healCurses == -1):
                        if (targetSide == Enums.CardTargetSide.Enemy):
                            stringBuilder.Append(Texts.Instance.GetText("cardsPurgeAll"))
                        else:
                            stringBuilder.Append(Texts.Instance.GetText("cardsDispelAll"))
                        stringBuilder.Append("\n")
                    if (dispelAuras > 0):
                        if (targetSide == Enums.CardTargetSide.Enemy):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurge"), dispelAuras))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispel"), dispelAuras))
                        stringBuilder.Append("\n")
                    if (dispelAuras == -1):
                        if (targetSide == Enums.CardTargetSide.Enemy):
                            stringBuilder.Append(Texts.Instance.GetText("cardsDispelAll"))
                        else:
                            stringBuilder.Append(Texts.Instance.GetText("cardsPurgeAll"))
                        stringBuilder.Append("\n")
                    if (healAuraCurseSelf != None):
                        if healAuraCurseSelf.IsAura:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurgeYour"), SpriteText(healAuraCurseSelf.ACName)))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispelYour"), SpriteText(healAuraCurseSelf.ACName)))
                        stringBuilder.Append("\n")
                elif (healCurses > 0):
                    if (targetSide == Enums.CardTargetSide.Enemy):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurge"), healCurses))
                    else:
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispel"), healCurses))
                    stringBuilder.Append("\n")
                if (transferCurses > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTransferCurse"), transferCurses.ToString()))
                    stringBuilder.Append("\n")
                if (stealAuras > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsStealAuras"), stealAuras.ToString()))
                    stringBuilder.Append("\n")
                if (increaseAuras > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsIncreaseAura"), increaseAuras.ToString()))
                    stringBuilder.Append("\n")
                if (increaseCurses > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsIncreaseCurse"), increaseCurses.ToString()))
                    stringBuilder.Append("\n")
                if (reduceAuras > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsReduceAura"), reduceAuras.ToString()))
                    stringBuilder.Append("\n")
                if (reduceCurses > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsReduceCurse"), reduceCurses.ToString()))
                    stringBuilder.Append("\n")
                num = 0
                if ((((damage > 0) and (not damageSpecialValue1)) and (not damageSpecialValue2)) and (not damageSpecialValueGlobal)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("damage", NumFormat(damagePreCalculated), SpriteText(Enum.GetName(Enums.DamageType, damageType))))
                    if (((damage2 > 0) and (damageType == damageType2)) and (((damage2SpecialValue1 or damage2SpecialValue2) or damage2SpecialValueGlobal))):
                        stringBuilder2.Append("+")
                        stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType))))
                if ((((damage2 > 0) and (not damage2SpecialValue1)) and (not damage2SpecialValue2)) and (not damage2SpecialValueGlobal)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("damage", NumFormat(damagePreCalculated2), SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                if (num > 0):
                    if (flag4 and (num > 1)):
                        stringBuilder2.Insert(0, value)
                        stringBuilder2.Insert(0, "\n")
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDealDamage"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (healSelfPerDamageDonePercent > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsHealSelfPerDamage"), healSelfPerDamageDonePercent.ToString()))
                    stringBuilder.Append("\n")
                if ((selfHealthLoss != 0) and (not selfHealthLossSpecialGlobal)):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLoseHp"), ColorTextArray("damage", NumFormat(selfHealthLoss), "HP")))
                    stringBuilder.Append("\n")
                if ((((((targetSide == Enums.CardTargetSide.Friend) or (targetSide == Enums.CardTargetSide.FriendNotSelf))) and (SpecialValueGlobal == Enums.CardSpecialValue.AuraCurseYours)) and (SpecialAuraCurseNameGlobal != None)) and (SpecialValueModifierGlobal > 0)):
                    flag = True
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsShareYour"), SpriteText(SpecialAuraCurseNameGlobal.ACName)))
                    stringBuilder.Append("\n")
                if (((not Damage2SpecialValue1) and (not flag)) and ((((specialValueGlobal != 0) or (specialValue1 != 0)) or (specialValue2 != 0)))):
                    if (((not damageSpecialValueGlobal) and (not damageSpecialValue1)) and (not damageSpecialValue2)):
                        if ((targetSide == Enums.CardTargetSide.Self) and (((specialValueGlobal == Enums.CardSpecialValue.AuraCurseTarget) or (specialValueGlobal == Enums.CardSpecialValue.AuraCurseYours)))):
                            if (specialAuraCurseNameGlobal != None):
                                text = SpriteText(specialAuraCurseNameGlobal.ACName)
                            if auraChargesSpecialValueGlobal:
                                text2 = SpriteText(aura.ACName)
                                if ((aura2 != None) and auraCharges2SpecialValueGlobal):
                                    text3 = SpriteText(aura2.ACName)
                            elif curseChargesSpecialValueGlobal:
                                text2 = SpriteText(curse.ACName)
                                if ((curse2 != None) and curseCharges2SpecialValueGlobal):
                                    text3 = SpriteText(curse2.ACName)
                        elif (specialValue1 == Enums.CardSpecialValue.AuraCurseTarget):
                            if (specialAuraCurseName1 != None):
                                text = SpriteText(specialAuraCurseName1.ACName)
                            if auraChargesSpecialValue1:
                                text2 = SpriteText(aura.ACName)
                                if ((aura2 != None) and auraCharges2SpecialValue1):
                                    text3 = SpriteText(aura2.ACName)
                            elif curseChargesSpecialValue1:
                                text2 = SpriteText(curse.ACName)
                                if ((curse2 != None) and CurseCharges2SpecialValue1):
                                    text3 = SpriteText(curse2.ACName)
                        if ((text != "") and (text2 != "")):
                            flag2 = True
                            if (text == text2):
                                if (specialValueGlobal == Enums.CardSpecialValue.AuraCurseTarget):
                                    if (specialValueModifierGlobal == 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDoubleTarget"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifierGlobal == 200):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTripleTarget"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifierGlobal < 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLosePercentTarget"), (100 - specialValueModifierGlobal), text))
                                        stringBuilder.Append("\n")
                                elif (specialValueGlobal == Enums.CardSpecialValue.AuraCurseYours):
                                    if (specialValueModifierGlobal == 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDoubleYour"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifierGlobal == 200):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTripleYour"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifierGlobal < 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLosePercentYour"), (100 - specialValueModifierGlobal), text))
                                        stringBuilder.Append("\n")
                                elif (specialValue1 == Enums.CardSpecialValue.AuraCurseTarget):
                                    if (specialValueModifier1 == 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDoubleTarget"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifier1 == 200):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTripleTarget"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifier1 < 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLosePercentTarget"), (100 - specialValueModifier1), text))
                                        stringBuilder.Append("\n")
                                elif (specialValue1 == Enums.CardSpecialValue.AuraCurseYours):
                                    if (specialValueModifier1 == 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDoubleYour"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifier1 == 200):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTripleYour"), text))
                                        stringBuilder.Append("\n")
                                    elif (specialValueModifier1 < 100):
                                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLosePercentYour"), (100 - specialValueModifier1), text))
                                        stringBuilder.Append("\n")
                            else:
                                stringBuilder2.Append(text2)
                                if (specialValueModifier1 > 0):
                                    num2 = (specialValueModifier1 / 100)
                                if ((num2 > 0) and (num2 != 1)):
                                    text4 = ("x " + num2)
                                if (text4 != ""):
                                    stringBuilder2.Append(" <c>")
                                    stringBuilder2.Append(text4)
                                    stringBuilder2.Append("</c>")
                                if (text3 != ""):
                                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTransformIntoAnd"), text, stringBuilder2.ToString(), text3))
                                else:
                                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTransformInto"), text, stringBuilder2.ToString()))
                                stringBuilder.Append("\n")
                                stringBuilder2.Clear()
                                num2 = 0
                                text4 = ""
                    text = ""
                    text2 = ""
                    text3 = ""
                num = 0
                if ((damage > 0) and ((damageSpecialValue1 or damageSpecialValueGlobal))):
                    stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType))))
                    num += 1
                if ((damage2 > 0) and ((damageSpecialValue2 or damageSpecialValueGlobal))):
                    stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                    num += 1
                elif (((damage2 > 0) and damage2SpecialValueGlobal) and (damageType != damageType2)):
                    stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                    num += 1
                if (((damage2 > 0) and damage2SpecialValue1) and (damageType != damageType2)):
                    stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                    num += 1
                if (num > 0):
                    if (flag4 and (num > 1)):
                        stringBuilder2.Insert(0, value)
                        stringBuilder2.Insert(0, "\n")
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDealDamage"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                auraCurseData = None
                if ((not flag) and (not flag2)):
                    num = 0
                    if ((aura != None) and ((auraChargesSpecialValue1 or auraChargesSpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("aura", "X", SpriteText(aura.ACName)))
                        auraCurseData = aura
                    if ((aura2 != None) and ((auraCharges2SpecialValue1 or auraCharges2SpecialValueGlobal))):
                        num += 1
                        if ((aura != None) and (aura == aura2)):
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(aura.Id, auraCharges, character)), SpriteText(aura.ACName)))
                            stringBuilder2.Append("+")
                        stringBuilder2.Append(ColorTextArray("aura", "X", SpriteText(aura2.ACName)))
                        auraCurseData = aura2
                    if ((aura3 != None) and ((auraCharges3SpecialValue1 or auraCharges3SpecialValueGlobal))):
                        num += 1
                        if ((aura != None) and (aura == aura3)):
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(aura.Id, auraCharges, character)), SpriteText(aura.ACName)))
                            stringBuilder2.Append("+")
                        if ((aura2 != None) and (aura == aura3)):
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(aura2.Id, auraCharges2, character)), SpriteText(aura3.ACName)))
                            stringBuilder2.Append("+")
                        stringBuilder2.Append(ColorTextArray("aura", "X", SpriteText(aura3.ACName)))
                        auraCurseData = aura3
                    if (num > 0):
                        if (targetSide == Enums.CardTargetSide.Self):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGrant"), stringBuilder2.ToString()))
                        stringBuilder.Append("\n")
                        stringBuilder2.Clear()
                if ((not flag) and (not flag2)):
                    num = 0
                    if ((curse != None) and ((curseChargesSpecialValue1 or curseChargesSpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("curse", "X", SpriteText(curse.ACName)))
                    if ((curse2 != None) and ((curseCharges2SpecialValue1 or curseCharges2SpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("curse", "X", SpriteText(curse2.ACName)))
                    if ((curse3 != None) and ((curseCharges3SpecialValue1 or curseCharges3SpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("curse", "X", SpriteText(curse3.ACName)))
                    if (num > 0):
                        if (targetSide == Enums.CardTargetSide.Self):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsApply"), stringBuilder2.ToString()))
                        stringBuilder.Append("\n")
                        stringBuilder2.Clear()
                    num = 0
                    if ((curseSelf != None) and ((curseChargesSpecialValue1 or curseChargesSpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("curse", "X", SpriteText(curseSelf.ACName)))
                    if ((curseSelf2 != None) and ((curseCharges2SpecialValue1 or curseCharges2SpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("curse", "X", SpriteText(curseSelf2.ACName)))
                    if ((curseSelf3 != None) and ((curseCharges3SpecialValue1 or curseCharges3SpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("curse", "X", SpriteText(curseSelf3.ACName)))
                    if (num > 0):
                        if ((((targetSide == Enums.CardTargetSide.Self) or (curseSelf != None)) or (curseSelf2 != None)) or (curseSelf3 != None)):
                            if (targetSide == Enums.CardTargetSide.Self):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                                stringBuilder.Append("\n")
                            elif (not flag3):
                                stringBuilder3.Append(str.Format(Texts.Instance.GetText("cardsYouSuffer"), stringBuilder2.ToString()))
                                stringBuilder3.Append("\n")
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsYouSuffer"), stringBuilder2.ToString()))
                                stringBuilder.Append("\n")
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsApply"), stringBuilder2.ToString()))
                            stringBuilder.Append("\n")
                        stringBuilder2.Clear()
                num = 0
                if ((heal > 0) and ((healSpecialValue1 or healSpecialValueGlobal))):
                    stringBuilder2.Append(ColorTextArray("heal", "X", SpriteText("heal")))
                    num += 1
                if (stringBuilder2.Length > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsHeal"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                num = 0
                if ((healSelf > 0) and ((healSelfSpecialValue1 or healSelfSpecialValueGlobal))):
                    stringBuilder2.Append(ColorTextArray("heal", "X", SpriteText("heal")))
                    num += 1
                if (stringBuilder2.Length > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsHealSelf"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if ((not flag) and (not flag2)):
                    if (specialValueModifierGlobal > 0):
                        num2 = (specialValueModifierGlobal / 100)
                    elif (specialValueModifier1 > 0):
                        num2 = (specialValueModifier1 / 100)
                    if ((num2 > 0) and (num2 != 1)):
                        text4 = ("x" + num2)
                    if (specialValue1 == Enums.CardSpecialValue.AuraCurseYours):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYour"), SpriteText(SpecialAuraCurseName1.ACName), text4))
                    elif (specialValue1 == Enums.CardSpecialValue.AuraCurseTarget):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsTarget"), SpriteText(SpecialAuraCurseName1.ACName), text4))
                    elif (specialValueGlobal == Enums.CardSpecialValue.AuraCurseYours):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYour"), SpriteText(SpecialAuraCurseNameGlobal.ACName), text4))
                    elif (specialValueGlobal == Enums.CardSpecialValue.AuraCurseTarget):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsTarget"), SpriteText(SpecialAuraCurseNameGlobal.ACName), text4))
                    if (specialValueGlobal == Enums.CardSpecialValue.HealthYours):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYourHp"), text4))
                    elif (specialValue1 == Enums.CardSpecialValue.HealthYours):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYourHp"), text4))
                    elif (specialValue1 == Enums.CardSpecialValue.HealthTarget):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsTargetHp"), text4))
                    if (((specialValueGlobal == Enums.CardSpecialValue.CardsHand) or (specialValue1 == Enums.CardSpecialValue.CardsHand)) or (specialValue2 == Enums.CardSpecialValue.CardsHand)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYourHand"), SpriteText("card"), text4))
                    elif (((specialValueGlobal == Enums.CardSpecialValue.CardsDeck) or (specialValue1 == Enums.CardSpecialValue.CardsDeck)) or (specialValue2 == Enums.CardSpecialValue.CardsDeck)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYourDeck"), SpriteText("card"), text4))
                    elif (((specialValueGlobal == Enums.CardSpecialValue.CardsDiscard) or (specialValue1 == Enums.CardSpecialValue.CardsDiscard)) or (specialValue2 == Enums.CardSpecialValue.CardsDiscard)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYourDiscard"), SpriteText("card"), text4))
                    elif (((specialValueGlobal == Enums.CardSpecialValue.CardsVanish) or (specialValue1 == Enums.CardSpecialValue.CardsVanish)) or (specialValue2 == Enums.CardSpecialValue.CardsVanish)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsYourVanish"), SpriteText("card"), text4))
                    elif (((specialValueGlobal == Enums.CardSpecialValue.CardsDeckTarget) or (specialValue1 == Enums.CardSpecialValue.CardsDeckTarget)) or (specialValue2 == Enums.CardSpecialValue.CardsDeckTarget)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsTargetDeck"), SpriteText("card"), text4))
                    elif (((specialValueGlobal == Enums.CardSpecialValue.CardsDiscardTarget) or (specialValue1 == Enums.CardSpecialValue.CardsDiscardTarget)) or (specialValue2 == Enums.CardSpecialValue.CardsDiscardTarget)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsTargetDiscard"), SpriteText("card"), text4))
                    elif (((specialValueGlobal == Enums.CardSpecialValue.CardsVanishTarget) or (specialValue1 == Enums.CardSpecialValue.CardsVanishTarget)) or (specialValue2 == Enums.CardSpecialValue.CardsVanishTarget)):
                        stringBuilder2.Append(str.Format(Texts.Instance.GetText("cardsXEqualsTargetVanish"), SpriteText("card"), text4))
                    if (stringBuilder2.Length > 0):
                        stringBuilder.Append(value4)
                        stringBuilder.Append(stringBuilder2)
                        stringBuilder.Append(value3)
                        stringBuilder.Append("\n")
                        stringBuilder2.Clear()
                        if (healAuraCurseName != None):
                            if (targetSide == Enums.CardTargetSide.Self):
                                if healAuraCurseName.IsAura:
                                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurgeYour"), SpriteText(healAuraCurseName.ACName)))
                                else:
                                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispelYour"), SpriteText(healAuraCurseName.ACName)))
                            elif healAuraCurseName.IsAura:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurge"), SpriteText(healAuraCurseName.ACName)))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispel"), SpriteText(healAuraCurseName.ACName)))
                            stringBuilder.Append("\n")
                        if (healAuraCurseSelf != None):
                            if healAuraCurseSelf.IsAura:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPurgeYour"), SpriteText(healAuraCurseSelf.ACName)))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispelYour"), SpriteText(healAuraCurseSelf.ACName)))
                            stringBuilder.Append("\n")
                    num2 = 0
                    text4 = ""
                if ((selfHealthLoss > 0) and selfHealthLossSpecialGlobal):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsYouLose"), ColorTextArray("damage", "X", "HP")))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                num = 0
                if (damageSelf > 0):
                    num += 1
                    if ((damageSpecialValueGlobal or damageSpecialValue1) or damageSpecialValue2):
                        stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType))))
                    else:
                        stringBuilder2.Append(ColorTextArray("damage", NumFormat(damageSelfPreCalculated), SpriteText(Enum.GetName(Enums.DamageType, damageType))))
                if (damageSelf2 > 0):
                    num += 1
                    if ((damage2SpecialValueGlobal or damage2SpecialValue1) or damage2SpecialValue2):
                        stringBuilder2.Append(ColorTextArray("damage", "X", SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                    else:
                        stringBuilder2.Append(ColorTextArray("damage", NumFormat(damageSelfPreCalculated2), SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                if ((curseSelf != None) and (curseCharges > 0)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", NumFormat(GetFinalAuraCharges(curseSelf.Id, curseCharges, character)), SpriteText(curseSelf.ACName)))
                if ((curseSelf2 != None) and (curseCharges2 > 0)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", NumFormat(GetFinalAuraCharges(curseSelf2.Id, curseCharges2, character)), SpriteText(curseSelf2.ACName)))
                if ((curseSelf3 != None) and (curseCharges3 > 0)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", NumFormat(GetFinalAuraCharges(curseSelf3.Id, curseCharges3, character)), SpriteText(curseSelf3.ACName)))
                if (num > 0):
                    if (num > 2):
                        stringBuilder2.Insert(0, value)
                        stringBuilder2.Insert(0, "\n")
                    if (targetSide == Enums.CardTargetSide.Self):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                        stringBuilder.Append("\n")
                    else:
                        stringBuilder3.Append(str.Format(Texts.Instance.GetText("cardsYouSuffer"), stringBuilder2.ToString()))
                        stringBuilder3.Append("\n")
                    stringBuilder2.Clear()
                num = 0
                if (energyRecharge < 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLoseHp"), stringBuilder2.Append(ColorTextArray("system", NumFormat(Mathf.Abs(energyRecharge)), SpriteText("energy")))))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (energyRecharge > 0):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("system", NumFormat(energyRecharge), SpriteText("energy")))
                if (((aura != None) and (auraCharges > 0)) and (aura != auraCurseData)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(aura.Id, auraCharges, character)), SpriteText(aura.ACName)))
                if (((aura2 != None) and (auraCharges2 > 0)) and (aura2 != auraCurseData)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(aura2.Id, auraCharges2, character)), SpriteText(aura2.ACName)))
                if (((aura3 != None) and (auraCharges3 > 0)) and (aura3 != auraCurseData)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(aura3.Id, auraCharges3, character)), SpriteText(aura3.ACName)))
                if (num > 0):
                    if (num > 2):
                        stringBuilder2.Insert(0, value)
                        stringBuilder2.Insert(0, "\n")
                    if (targetSide == Enums.CardTargetSide.Self):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                    else:
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGrant"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                num = 0
                if ((auraSelf != None) and (auraCharges > 0)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(auraSelf.Id, auraCharges, character)), SpriteText(auraSelf.ACName)))
                if ((auraSelf2 != None) and (auraCharges2 > 0)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(auraSelf2.Id, auraCharges2, character)), SpriteText(auraSelf2.ACName)))
                if ((auraSelf3 != None) and (auraCharges3 > 0)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(auraSelf3.Id, auraCharges3, character)), SpriteText(auraSelf3.ACName)))
                if (not flag):
                    if ((auraSelf != None) and ((auraChargesSpecialValue1 or auraChargesSpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("aura", "X", SpriteText(auraSelf.ACName)))
                    if ((auraSelf2 != None) and ((auraCharges2SpecialValue1 or auraCharges2SpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("aura", "X", SpriteText(auraSelf2.ACName)))
                    if ((auraSelf3 != None) and ((auraCharges3SpecialValue1 or auraCharges3SpecialValueGlobal))):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("aura", "X", SpriteText(auraSelf3.ACName)))
                if (num > 0):
                    if (num > 2):
                        stringBuilder2.Insert(0, value)
                        stringBuilder2.Insert(0, "\n")
                    if (targetSide == Enums.CardTargetSide.Self):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                        stringBuilder.Append("\n")
                    else:
                        stringBuilder3.Append(str.Format(Texts.Instance.GetText("cardsYouGain"), stringBuilder2.ToString()))
                        stringBuilder3.Append("\n")
                    stringBuilder2.Clear()
                num = 0
                if ((curseCharges > 0) and (curse != None)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", NumFormat(GetFinalAuraCharges(curse.Id, curseCharges, character)), SpriteText(curse.ACName)))
                if ((curseCharges2 > 0) and (curse2 != None)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", NumFormat(GetFinalAuraCharges(curse2.Id, curseCharges2, character)), SpriteText(curse2.ACName)))
                if ((curseCharges3 > 0) and (curse3 != None)):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", NumFormat(GetFinalAuraCharges(curse3.Id, curseCharges3, character)), SpriteText(curse3.ACName)))
                if (num > 0):
                    if (num > 2):
                        stringBuilder2.Insert(0, value)
                        stringBuilder2.Insert(0, "\n")
                    if (targetSide == Enums.CardTargetSide.Self):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                    else:
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsApply"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (((heal > 0) and (not healSpecialValue1)) and (not healSpecialValueGlobal)):
                    stringBuilder2.Append(ColorTextArray("heal", NumFormat(healPreCalculated), SpriteText("heal")))
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsHeal"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (((healSelf > 0) and (not healSelfSpecialValue1)) and (not healSelfSpecialValueGlobal)):
                    stringBuilder2.Append(ColorTextArray("heal", NumFormat(healSelfPreCalculated), SpriteText("heal")))
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsHealSelf"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (damageSides > 0):
                    stringBuilder2.Append(ColorTextArray("damage", NumFormat(damageSidesPreCalculated), SpriteText(Enum.GetName(Enums.DamageType, damageType))))
                if (damageSides2 > 0):
                    stringBuilder2.Append(ColorTextArray("damage", NumFormat(damageSidesPreCalculated2), SpriteText(Enum.GetName(Enums.DamageType, damageType2))))
                if (stringBuilder2.Length > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTargetSides"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (addCard != 0):
                    text5 = ""
                    if (addCardId != ""):
                        stringBuilder2.Append(ColorTextArray("", NumFormat(addCard), SpriteText("card")))
                        cardData = Globals.Instance.GetCardData(addCardId, instantiate = False)
                        if (cardData != None):
                            stringBuilder2.Append(ColorFromCardDataRarity(cardData))
                            stringBuilder2.Append(cardData.CardName)
                            stringBuilder2.Append("</color>")
                        text5 = stringBuilder2.ToString()
                        stringBuilder2.Clear()
                    else:
                        if (addCardChoose > 0):
                            stringBuilder2.Append(ColorTextArray("", NumFormat(addCardChoose), SpriteText("card")))
                        else:
                            stringBuilder2.Append(ColorTextArray("", NumFormat(addCard), SpriteText("card")))
                        if (addCardType != 0):
                            stringBuilder2.Append("<color=#5E3016>")
                            stringBuilder2.Append(Texts.Instance.GetText(Enum.GetName(Enums.CardType, addCardType)))
                            stringBuilder2.Append("</color>")
                        text5 = stringBuilder2.ToString()
                        stringBuilder2.Clear()
                    text6 = ""
                    if (addCardReducedCost == -1):
                        text6 = ((((str.Format(Texts.Instance.GetText("cardsAddCostVanish"), 0) if ((not addCardCostTurn)) else str.Format(Texts.Instance.GetText("cardsAddCostVanish"), 0))) if addCardVanish else ((str.Format(Texts.Instance.GetText("cardsAddCost"), 0) if ((not addCardCostTurn)) else str.Format(Texts.Instance.GetText("cardsAddCostTurn"), 0)))))
                    elif (addCardReducedCost > 0):
                        text6 = ((((str.Format(Texts.Instance.GetText("cardsAddCostReducedVanish"), addCardReducedCost) if ((not addCardCostTurn)) else str.Format(Texts.Instance.GetText("cardsAddCostReducedVanishTurn"), addCardReducedCost))) if addCardVanish else ((str.Format(Texts.Instance.GetText("cardsAddCostReduced"), addCardReducedCost) if ((not addCardCostTurn)) else str.Format(Texts.Instance.GetText("cardsAddCostReducedTurn"), addCardReducedCost)))))
                    text7 = ""
                    if (addCardId != ""):
                        if (addCardPlace == Enums.CardPlace.RandomDeck):
                            text7 = (("cardsIDShuffleTargetDeck" if ((targetSide != Enums.CardTargetSide.Self)) else "cardsIDShuffleDeck"))
                        elif (addCardPlace == Enums.CardPlace.Hand):
                            text7 = "cardsIDPlaceHand"
                        elif (addCardPlace == Enums.CardPlace.TopDeck):
                            text7 = (("cardsIDPlaceTargetTopDeck" if ((targetSide != Enums.CardTargetSide.Self)) else "cardsIDPlaceTopDeck"))
                        elif (addCardPlace == Enums.CardPlace.Discard):
                            text7 = "cardsIDPlaceTargetDiscard"
                    elif (addCardFrom == Enums.CardFrom.Game):
                        if (addCardPlace == Enums.CardPlace.RandomDeck):
                            text7 = (("cardsDiscoverNumberToDeck" if ((addCardChoose != 0)) else "cardsDiscoverToDeck"))
                        elif (addCardPlace == Enums.CardPlace.Hand):
                            text7 = (("cardsDiscoverNumberToHand" if ((addCardChoose != 0)) else "cardsDiscoverToHand"))
                        elif ((addCardPlace == Enums.CardPlace.TopDeck) and (addCardChoose != 0)):
                            text7 = "cardsDiscoverNumberToTopDeck"
                    elif (addCardFrom == Enums.CardFrom.Deck):
                        if (addCardPlace == Enums.CardPlace.Hand):
                            text7 = (("cardsRevealNumberToHand" if ((addCardChoose > 0)) else (("cardsRevealItToHand" if ((addCard <= 1)) else "cardsRevealThemToHand"))))
                        elif (addCardPlace == Enums.CardPlace.TopDeck):
                            text7 = (("cardsRevealNumberToTopDeck" if ((addCardChoose > 0)) else (("cardsRevealItToTopDeck" if ((addCard <= 1)) else "cardsRevealThemToTopDeck"))))
                    elif (addCardFrom == Enums.CardFrom.Discard):
                        if (addCardPlace == Enums.CardPlace.TopDeck):
                            text7 = "cardsPickToTop"
                        elif (addCardPlace == Enums.CardPlace.Hand):
                            text7 = "cardsPickToHand"
                    elif (addCardFrom == Enums.CardFrom.Hand):
                        if (targetSide == Enums.CardTargetSide.Friend):
                            if (addCardPlace == Enums.CardPlace.TopDeck):
                                text7 = "cardsDuplicateToTargetTopDeck"
                            elif (addCardPlace == Enums.CardPlace.RandomDeck):
                                text7 = "cardsDuplicateToTargetRandomDeck"
                        elif (addCardPlace == Enums.CardPlace.Hand):
                            text7 = "cardsDuplicateToHand"
                    elif (addCardFrom == Enums.CardFrom.Vanish):
                        if (addCardPlace == Enums.CardPlace.TopDeck):
                            text7 = "cardsFromVanishToTop"
                        elif (addCardPlace == Enums.CardPlace.Hand):
                            text7 = "cardsFromVanishToHand"
                    stringBuilder.Append(str.Format(Texts.Instance.GetText(text7), text5, ColorTextArray("", NumFormat(addCard))))
                    if (text6 != ""):
                        stringBuilder.Append(" ")
                        stringBuilder.Append(value2)
                        stringBuilder.Append(text6)
                        stringBuilder.Append(value3)
                    stringBuilder.Append("\n")
                if (discardCard != 0):
                    if (discardCardType != 0):
                        stringBuilder2.Append("<color=#5E3016>")
                        stringBuilder2.Append(Texts.Instance.GetText(Enum.GetName(Enums.CardType, discardCardType)))
                        stringBuilder2.Append("</color>")
                    if (discardCardPlace == Enums.CardPlace.Discard):
                        if (not discardCardAutomatic):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDiscard"), ColorTextArray("", NumFormat(discardCard), SpriteText("card"))))
                            stringBuilder.Append(stringBuilder2)
                            stringBuilder.Append("\n")
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDiscard"), ColorTextArray("", NumFormat(discardCard), SpriteText("cardrandom"))))
                            stringBuilder.Append(stringBuilder2)
                            stringBuilder.Append("\n")
                    elif (discardCardPlace == Enums.CardPlace.TopDeck):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsPlaceToTop"), ColorTextArray("", NumFormat(discardCard), SpriteText("card"), stringBuilder2.ToString().Trim())))
                        stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (lookCards != 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsLook"), ColorTextArray("", NumFormat(lookCards), SpriteText("card"))))
                    stringBuilder.Append("\n")
                    if (lookCardsDiscardUpTo == -1):
                        stringBuilder.Append(Texts.Instance.GetText("cardsDiscardAny"))
                        stringBuilder.Append("\n")
                    elif (lookCardsDiscardUpTo > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDiscardUpTo"), ColorTextArray("", NumFormat(lookCardsDiscardUpTo))))
                        stringBuilder.Append("\n")
                    elif (lookCardsVanishUpTo > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsVanishUpTo"), ColorTextArray("", NumFormat(lookCardsVanishUpTo))))
                        stringBuilder.Append("\n")
                if (stringBuilder3.Length > 0):
                    stringBuilder.Append(stringBuilder3.ToString())
                if killPet:
                    stringBuilder.Append(Texts.Instance.GetText("killPet"))
                    stringBuilder.Append("\n")
                if (((damageEnergyBonus > 0) or (healEnergyBonus > 0)) or (acEnergyBonus != None)):
                    stringBuilder6 = StringBuilder()
                    stringBuilder6.Append("<line-height=40%><br></line-height>")
                    stringBuilder7 = StringBuilder()
                    stringBuilder7.Append(value2)
                    stringBuilder7.Append("[")
                    stringBuilder7.Append(Texts.Instance.GetText("overchargeAcronym"))
                    stringBuilder7.Append("]")
                    stringBuilder7.Append(value3)
                    stringBuilder7.Append("  ")
                    if (damageEnergyBonus > 0):
                        stringBuilder6.Append(stringBuilder7.ToString())
                        stringBuilder6.Append(str.Format(Texts.Instance.GetText("cardsDealDamage"), ColorTextArray("damage", NumFormat(damageEnergyBonus), SpriteText(Enum.GetName(Enums.DamageType, damageType)))))
                        stringBuilder6.Append("\n")
                    if (acEnergyBonus != None):
                        stringBuilder2.Append(ColorTextArray("aura", NumFormat(acEnergyBonusQuantity), SpriteText(acEnergyBonus.ACName)))
                        if (acEnergyBonus2 != None):
                            stringBuilder2.Append(" ")
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(acEnergyBonus2Quantity), SpriteText(acEnergyBonus2.ACName)))
                        if acEnergyBonus.IsAura:
                            if (targetSide == Enums.CardTargetSide.Self):
                                stringBuilder6.Append(stringBuilder7.ToString())
                                stringBuilder6.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                            else:
                                stringBuilder6.Append(stringBuilder7.ToString())
                                stringBuilder6.Append(str.Format(Texts.Instance.GetText("cardsGrant"), stringBuilder2.ToString()))
                        elif (not acEnergyBonus.IsAura):
                            if (targetSide == Enums.CardTargetSide.Self):
                                stringBuilder6.Append(stringBuilder7.ToString())
                                stringBuilder6.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                            else:
                                stringBuilder6.Append(stringBuilder7.ToString())
                                stringBuilder6.Append(str.Format(Texts.Instance.GetText("cardsApply"), stringBuilder2.ToString()))
                        stringBuilder6.Append("\n")
                    if (healEnergyBonus > 0):
                        stringBuilder6.Append(stringBuilder7.ToString())
                        stringBuilder6.Append(str.Format(Texts.Instance.GetText("cardsHeal"), ColorTextArray("heal", NumFormat(healEnergyBonus), SpriteText("heal"))))
                        stringBuilder6.Append("\n")
                    stringBuilder.Append(stringBuilder6.ToString())
                    stringBuilder2.Clear()
                    stringBuilder6.Clear()
                if ((effectRepeat > 1) or (effectRepeatMaxBonus > 0)):
                    stringBuilder.Append(value)
                    stringBuilder.Append(value2)
                    if (effectRepeatMaxBonus > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsRepeatUpTo"), effectRepeatMaxBonus))
                    elif (effectRepeatTarget == Enums.EffectRepeatTarget.Chain):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsRepeatChain"), (effectRepeat - 1)))
                    elif (effectRepeatTarget == Enums.EffectRepeatTarget.NoRepeat):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsRepeatJump"), (effectRepeat - 1)))
                    else:
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsRepeat"), (effectRepeat - 1)))
                    if ((effectRepeatModificator != 0) and (effectRepeatTarget != Enums.EffectRepeatTarget.Chain)):
                        stringBuilder.Append(" (")
                        if (effectRepeatModificator > 0):
                            stringBuilder.Append("+")
                        stringBuilder.Append(effectRepeatModificator)
                        stringBuilder.Append("%)")
                    stringBuilder.Append(value3)
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (ignoreBlock or ignoreBlock2):
                    stringBuilder.Append(value)
                    stringBuilder.Append(value2)
                    stringBuilder.Append(Texts.Instance.GetText("cardsIgnoreBlock"))
                    stringBuilder.Append(value3)
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                stringBuilder3 = None
            else:
                itemData = None
                itemData = ((itemEnchantment if ((not ((item != None)))) else item))
                if (itemData.MaxHealth != 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemMaxHp"), NumFormatItem(itemData.MaxHealth, plus = True)))
                    stringBuilder.Append("\n")
                if (itemData.ResistModified1 == Enums.DamageType.All):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemAllResistances"), NumFormatItem(itemData.ResistModifiedValue1, plus = True, percent = True)))
                    stringBuilder.Append("\n")
                num = 0
                num3 = 0
                if ((itemData.ResistModified1 != 0) and (itemData.ResistModified1 != Enums.DamageType.All)):
                    stringBuilder2.Append(SpriteText(Enum.GetName(Enums.DamageType, itemData.ResistModified1)))
                    num3 = itemData.ResistModifiedValue1
                    num += 1
                if ((itemData.ResistModified2 != 0) and (itemData.ResistModified2 != Enums.DamageType.All)):
                    stringBuilder2.Append(SpriteText(Enum.GetName(Enums.DamageType, itemData.ResistModified2)))
                    if (num3 == 0):
                        num3 = itemData.ResistModifiedValue2
                    num += 1
                if ((itemData.ResistModified3 != 0) and (itemData.ResistModified3 != Enums.DamageType.All)):
                    stringBuilder2.Append(SpriteText(Enum.GetName(Enums.DamageType, itemData.ResistModified3)))
                    if (num3 == 0):
                        num3 = itemData.ResistModifiedValue3
                    num += 1
                if (num > 0):
                    if (num > 1):
                        stringBuilder2.Append("\n")
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemXResistances"), stringBuilder2.ToString(), NumFormatItem(num3, plus = True, percent = True)))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (itemData.CharacterStatModified == Enums.CharacterStat.Speed):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemSpeed"), NumFormatItem(itemData.CharacterStatModifiedValue, plus = True)))
                    stringBuilder.Append("\n")
                if (itemData.CharacterStatModified == Enums.CharacterStat.EnergyTurn):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemEnergyRegeneration"), SpriteText("energy"), NumFormatItem(itemData.CharacterStatModifiedValue, plus = True)))
                    stringBuilder.Append("\n")
                if (itemData.CharacterStatModified2 == Enums.CharacterStat.Speed):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemSpeed"), NumFormatItem(itemData.CharacterStatModifiedValue2, plus = True)))
                    stringBuilder.Append("\n")
                if (itemData.CharacterStatModified2 == Enums.CharacterStat.EnergyTurn):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemEnergyRegeneration"), SpriteText("energy"), NumFormatItem(itemData.CharacterStatModifiedValue2, plus = True)))
                    stringBuilder.Append("\n")
                if (itemData.DamageFlatBonus == Enums.DamageType.All):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemAllDamages"), NumFormatItem(itemData.DamageFlatBonusValue, plus = True)))
                    stringBuilder.Append("\n")
                num = 0
                num4 = 0
                if ((itemData.DamageFlatBonus != 0) and (itemData.DamageFlatBonus != Enums.DamageType.All)):
                    stringBuilder2.Append(SpriteText(Enum.GetName(Enums.DamageType, itemData.DamageFlatBonus)))
                    num4 = itemData.DamageFlatBonusValue
                    num += 1
                if ((itemData.DamageFlatBonus2 != 0) and (itemData.DamageFlatBonus2 != Enums.DamageType.All)):
                    stringBuilder2.Append(SpriteText(Enum.GetName(Enums.DamageType, itemData.DamageFlatBonus2)))
                    num += 1
                if ((itemData.DamageFlatBonus3 != 0) and (itemData.DamageFlatBonus3 != Enums.DamageType.All)):
                    stringBuilder2.Append(SpriteText(Enum.GetName(Enums.DamageType, itemData.DamageFlatBonus3)))
                    num += 1
                if (itemData.DamagePercentBonus == Enums.DamageType.All):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemAllDamages"), NumFormatItem(Functions.FuncRoundToInt(itemData.DamagePercentBonusValue), plus = True, percent = True)))
                    stringBuilder.Append("\n")
                if (num > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemXDamages"), stringBuilder2.ToString(), NumFormatItem(num4, plus = True)))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (itemData.UseTheNextInsteadWhenYouPlay and (itemData.HealPercentBonus != 0)):
                    arg = ""
                    if (itemData.DestroyAfterUses > 1):
                        arg = (("(" + itemData.DestroyAfterUses) + ") ")
                    stringBuilder8 = StringBuilder()
                    stringBuilder8.Append("<size=-.15><color=#444>[")
                    stringBuilder8.Append(Texts.Instance.GetText("itemTheNext"))
                    stringBuilder8.Append("]</color></size><br>")
                    stringBuilder2.Append("<color=#5E3016>")
                    stringBuilder2.Append(Texts.Instance.GetText(Enum.GetName(Enums.CardType, itemData.CastedCardType)))
                    stringBuilder2.Append("</color>")
                    stringBuilder.Append(str.Format(stringBuilder8.ToString(), arg, stringBuilder2.ToString()))
                    stringBuilder2.Clear()
                    stringBuilder8.Clear()
                if (itemData.HealFlatBonus != 0):
                    stringBuilder.Append(SpriteText("heal"))
                    stringBuilder.Append(" ")
                    stringBuilder.Append(Functions.LowercaseFirst(Texts.Instance.GetText("healDone")))
                    stringBuilder.Append(NumFormatItem(itemData.HealFlatBonus, plus = True))
                    stringBuilder.Append("\n")
                if (itemData.HealPercentBonus != 0):
                    stringBuilder.Append(SpriteText("heal"))
                    stringBuilder.Append(" ")
                    stringBuilder.Append(Functions.LowercaseFirst(Texts.Instance.GetText("healDone")))
                    stringBuilder.Append(NumFormatItem(Functions.FuncRoundToInt(itemData.HealPercentBonus), plus = True, percent = True))
                    stringBuilder.Append("\n")
                if (itemData.HealReceivedFlatBonus != 0):
                    stringBuilder.Append(SpriteText("heal"))
                    stringBuilder.Append(" ")
                    stringBuilder.Append(Functions.LowercaseFirst(Texts.Instance.GetText("healTaken")))
                    stringBuilder.Append(NumFormatItem(Functions.FuncRoundToInt(itemData.HealReceivedFlatBonus), plus = True))
                    stringBuilder.Append("\n")
                if (itemData.HealReceivedPercentBonus != 0):
                    stringBuilder.Append(SpriteText("heal"))
                    stringBuilder.Append(" ")
                    stringBuilder.Append(Functions.LowercaseFirst(Texts.Instance.GetText("healTaken")))
                    stringBuilder.Append(NumFormatItem(Functions.FuncRoundToInt(itemData.HealReceivedPercentBonus), plus = True, percent = True))
                    stringBuilder.Append("\n")
                if (((((itemData.AuracurseBonus1 != None) and (itemData.AuracurseBonusValue1 > 0)) and (itemData.AuracurseBonus2 != None)) and (itemData.AuracurseBonusValue2 > 0)) and (itemData.AuracurseBonusValue1 == itemData.AuracurseBonusValue2)):
                    stringBuilder2.Append(SpriteText(itemData.AuracurseBonus1.ACName))
                    stringBuilder2.Append(SpriteText(itemData.AuracurseBonus2.ACName))
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemCharges"), stringBuilder2.ToString(), NumFormatItem(itemData.AuracurseBonusValue1, plus = True)))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                else:
                    if ((itemData.AuracurseBonus1 != None) and (itemData.AuracurseBonusValue1 > 0)):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemCharges"), SpriteText(itemData.AuracurseBonus1.ACName), NumFormatItem(itemData.AuracurseBonusValue1, plus = True)))
                        stringBuilder.Append("\n")
                    if ((itemData.AuracurseBonus2 != None) and (itemData.AuracurseBonusValue2 > 0)):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemCharges"), SpriteText(itemData.AuracurseBonus2.ACName), NumFormatItem(itemData.AuracurseBonusValue2, plus = True)))
                        stringBuilder.Append("\n")
                num = 0
                if (itemData.AuracurseImmune1 != None):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", SpriteText(itemData.AuracurseImmune1.Id)))
                if (itemData.AuracurseImmune2 != None):
                    num += 1
                    stringBuilder2.Append(ColorTextArray("curse", SpriteText(itemData.AuracurseImmune2.Id)))
                if (num > 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsImmuneTo"), stringBuilder2.ToString()))
                    stringBuilder.Append("\n")
                    stringBuilder2.Clear()
                if (itemData.PercentDiscountShop != 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemDiscount"), NumFormatItem(itemData.PercentDiscountShop, plus = True, percent = True)))
                    stringBuilder.Append("\n")
                if (itemData.PercentRetentionEndGame != 0):
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("itemDieRetain"), NumFormatItem(itemData.PercentRetentionEndGame, plus = True, percent = True)))
                    stringBuilder.Append("\n")
                if ((itemData.AuracurseCustomString != "") and (itemData.AuracurseCustomAC != None)):
                    stringBuilder9 = StringBuilder()
                    if ((((itemData.AuracurseCustomString == "itemCustomTextMaxChargesIncrasedOnEnemies") or (itemData.AuracurseCustomString == "itemCustomTextMaxChargesIncrasedOnHeroes"))) and (itemData.AuracurseCustomModValue1 > 0)):
                        stringBuilder9.Append("+")
                    stringBuilder9.Append(itemData.AuracurseCustomModValue1)
                    stringBuilder.Append(str.Format(Texts.Instance.GetText(itemData.AuracurseCustomString), ColorTextArray("aura", SpriteText(itemData.AuracurseCustomAC.Id)), stringBuilder9.ToString(), itemData.AuracurseCustomModValue2))
                    stringBuilder.Append("\n")
                    stringBuilder9 = None
                if (itemData.Id == "harleyrare"):
                    stringBuilder.Append(Texts.Instance.GetText("immortal"))
                    stringBuilder.Append("\n")
                if (itemData.ModifiedDamageType != 0):
                    stringBuilder.Append("<nobr>")
                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsTransformDamage"), SpriteText(Enum.GetName(Enums.DamageType, itemData.ModifiedDamageType))))
                    stringBuilder.Append("</nobr>")
                    stringBuilder.Append("\n")
                if (itemData.IsEnchantment and (((itemData.CastedCardType != 0) or ((((((itemData.Activation == Enums.EventActivation.PreFinishCast) or (itemData.Activation == Enums.EventActivation.FinishCast)) or (itemData.Activation == Enums.EventActivation.FinishFinishCast))) and (not itemData.EmptyHand)))))):
                    if (itemData.CastedCardType != 0):
                        stringBuilder2.Append("<color=#5E3016>")
                        stringBuilder2.Append(Texts.Instance.GetText(Enum.GetName(Enums.CardType, itemData.CastedCardType)))
                        stringBuilder2.Append("</color>")
                    else:
                        stringBuilder2.Append(" <sprite name=cards>")
                    if itemData.UseTheNextInsteadWhenYouPlay:
                        if (itemData.HealPercentBonus == 0):
                            arg2 = ""
                            if (itemData.DestroyAfterUses > 1):
                                arg2 = (("(" + itemData.DestroyAfterUses) + ") ")
                            stringBuilder10 = StringBuilder()
                            stringBuilder10.Append("<size=-.15><color=#444>[")
                            stringBuilder10.Append(Texts.Instance.GetText("itemTheNext"))
                            stringBuilder10.Append("]</color></size><br>")
                            stringBuilder.Append(str.Format(stringBuilder10.ToString(), arg2, stringBuilder2.ToString()))
                            stringBuilder10 = None
                    else:
                        stringBuilder.Append("<size=-.15>")
                        stringBuilder.Append("<color=#444>[")
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemWhenYouPlay"), stringBuilder2.ToString()))
                        stringBuilder.Append("]</color>")
                        stringBuilder.Append("</size><br>")
                    stringBuilder2.Clear()
                if ((itemData.Activation != 0) and (itemData.Activation != Enums.EventActivation.PreBeginCombat)):
                    if (stringBuilder.Length > 0):
                        stringBuilder.Append("<line-height=15%><br></line-height>")
                    stringBuilder11 = StringBuilder()
                    if (itemData.Activation == Enums.EventActivation.BeginCombat):
                        stringBuilder11.Append(Texts.Instance.GetText("itemCombatStart"))
                    elif (itemData.Activation == Enums.EventActivation.BeginCombatEnd):
                        stringBuilder11.Append(Texts.Instance.GetText("itemCombatEnd"))
                    elif ((itemData.Activation == Enums.EventActivation.BeginTurnAboutToDealCards) or (itemData.Activation == Enums.EventActivation.BeginTurnCardsDealt)):
                        if (itemData.RoundCycle > 1):
                            stringBuilder11.Append(str.Format(Texts.Instance.GetText("itemEveryNRounds"), itemData.RoundCycle.ToString()))
                        elif (itemData.ExactRound == 1):
                            stringBuilder11.Append(Texts.Instance.GetText("itemFirstTurn"))
                        else:
                            stringBuilder11.Append(Texts.Instance.GetText("itemEveryRound"))
                    elif (((itemData.Activation == Enums.EventActivation.PreFinishCast) or (itemData.Activation == Enums.EventActivation.FinishCast)) or (itemData.Activation == Enums.EventActivation.FinishFinishCast)):
                        if (itemData.TimesPerTurn == 1):
                            stringBuilder11.Append(Texts.Instance.GetText("itemOncePerTurn"))
                        elif (itemData.TimesPerTurn == 2):
                            stringBuilder11.Append(Texts.Instance.GetText("itemTwicePerTurn"))
                        elif (itemData.TimesPerTurn == 3):
                            stringBuilder11.Append(Texts.Instance.GetText("itemThricePerTurn"))
                    elif (itemData.Activation == Enums.EventActivation.Damage):
                        stringBuilder11.Append(Texts.Instance.GetText("itemDamageDone"))
                    elif (itemData.Activation == Enums.EventActivation.Damaged):
                        if (itemData.LowerOrEqualPercentHP < 100):
                            stringBuilder11.Append(str.Format(Texts.Instance.GetText("itemWhenDamagedBelow"), (itemData.LowerOrEqualPercentHP + "%")))
                        else:
                            stringBuilder11.Append(Texts.Instance.GetText("itemWhenDamaged"))
                    elif (itemData.Activation == Enums.EventActivation.Hitted):
                        stringBuilder11.Append(Texts.Instance.GetText("itemWhenHitted"))
                    elif (itemData.Activation == Enums.EventActivation.Block):
                        stringBuilder11.Append(Texts.Instance.GetText("itemWhenBlock"))
                    elif (itemData.Activation == Enums.EventActivation.Heal):
                        stringBuilder11.Append(Texts.Instance.GetText("itemHealDoneAction"))
                    elif (itemData.Activation == Enums.EventActivation.Healed):
                        stringBuilder11.Append(Texts.Instance.GetText("itemWhenHealed"))
                    elif (itemData.Activation == Enums.EventActivation.Evaded):
                        stringBuilder11.Append(Texts.Instance.GetText("itemWhenEvaded"))
                    elif (itemData.Activation == Enums.EventActivation.Evade):
                        stringBuilder11.Append(Texts.Instance.GetText("itemWhenEvade"))
                    elif (itemData.Activation == Enums.EventActivation.BeginTurn):
                        if (itemData.RoundCycle > 1):
                            stringBuilder11.Append(str.Format(Texts.Instance.GetText("itemEveryNRounds"), itemData.RoundCycle.ToString()))
                        else:
                            stringBuilder11.Append(Texts.Instance.GetText("itemEveryRound"))
                    elif (itemData.Activation == Enums.EventActivation.Killed):
                        stringBuilder11.Append(Texts.Instance.GetText("itemWhenKilled"))
                    elif ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent == 0)):
                        stringBuilder11.Append(str.Format(Texts.Instance.GetText("itemWhenYouApply"), ColorTextArray("curse", SpriteText(itemData.AuraCurseSetted.Id))))
                    if (stringBuilder11.Length > 0):
                        stringBuilder.Append("<size=-.15>")
                        stringBuilder.Append("<color=#444>[")
                        stringBuilder.Append(stringBuilder11.ToString())
                        stringBuilder.Append("]</color>")
                        stringBuilder.Append("</size><br>")
                    stringBuilder11 = None
                    if itemData.UsedEnergy:
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyForEnergyUsed"), ColorTextArray("system", SpriteText("energy"))))
                        stringBuilder.Append("\n")
                    if itemData.EmptyHand:
                        stringBuilder.Append(Texts.Instance.GetText("itemWhenHandEmpty"))
                        stringBuilder.Append(":<br>")
                    if ((itemData.ChanceToDispel > 0) and (itemData.ChanceToDispelNum > 0)):
                        if (itemData.ChanceToDispel < 100):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemChanceToDispel"), ColorTextArray("aura", NumFormatItem(itemData.ChanceToDispel, plus = False, percent = True)), ColorTextArray("curse", NumFormatItem(itemData.ChanceToDispelNum))))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDispel"), ColorTextArray("curse", NumFormatItem(itemData.ChanceToDispelNum))))
                        stringBuilder.Append("\n")
                    if ((not itemData.IsEnchantment) and (itemData.CastedCardType != 0)):
                        stringBuilder2.Append("<color=#5E3016>")
                        stringBuilder2.Append(Texts.Instance.GetText(Enum.GetName(Enums.CardType, itemData.CastedCardType)))
                        stringBuilder2.Append("</color>")
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemWhenYouPlay"), stringBuilder2.ToString()))
                        stringBuilder2.Clear()
                        stringBuilder.Append(":\n")
                    elif ((((not itemData.IsEnchantment) and (itemData.CastedCardType == Enums.CardType._None)) and ((((itemData.Activation == Enums.EventActivation.PreFinishCast) or (itemData.Activation == Enums.EventActivation.FinishCast)) or (itemData.Activation == Enums.EventActivation.FinishFinishCast)))) and (not itemData.EmptyHand)):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemWhenYouPlay"), "  <sprite name=cards>"))
                        stringBuilder.Append(":\n")
                    if (itemData.DrawCards > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDraw"), ColorTextArray("", NumFormat(itemData.DrawCards), SpriteText("card"))))
                        stringBuilder.Append("<br>")
                    if (itemData.HealQuantity > 0):
                        stringBuilder2.Append("<color=#111111>")
                        stringBuilder2.Append(NumFormatItem(itemData.HealQuantity, plus = True))
                        stringBuilder2.Append("</color>")
                        if (itemData.ItemTarget == Enums.ItemTarget.AllHero):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverHeroes"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.Self):
                            if (itemData.Activation == Enums.EventActivation.Killed):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemResurrectHP"), stringBuilder2.ToString()))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverSelf"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.AllEnemy):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverSelf"), stringBuilder2.ToString()))
                        stringBuilder.Append("<br>")
                        stringBuilder2.Clear()
                    if ((itemData.EnergyQuantity > 0) and (itemData.ItemTarget == Enums.ItemTarget.Self)):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), ColorTextArray("system", NumFormat(itemData.EnergyQuantity), SpriteText("energy"))))
                    if (itemData.HealPercentQuantity > 0):
                        stringBuilder2.Append("<color=#111111>")
                        stringBuilder2.Append(NumFormatItem(itemData.HealPercentQuantity, plus = True, percent = True))
                        stringBuilder2.Append("</color>")
                        if (itemData.ItemTarget == Enums.ItemTarget.AllHero):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverHeroes"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.Self):
                            if (itemData.Activation == Enums.EventActivation.Killed):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemResurrectHP"), stringBuilder2.ToString()))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverSelf"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.LowestFlatHpEnemy):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverLowestHPMonster"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.AllEnemy):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemRecoverSelf"), stringBuilder2.ToString()))
                        stringBuilder.Append("<br>")
                        stringBuilder2.Clear()
                    if (itemData.DamageToTarget > 0):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsDealDamage"), ColorTextArray("damage", NumFormat(enchantDamagePreCalculated), SpriteText(Enum.GetName(Enums.DamageType, itemData.DamageToTargetType)))))
                        stringBuilder.Append("\n")
                    num = 0
                    flag5 = True
                    if ((itemData.AuracurseGain1 != None) and (itemData.AuracurseGainValue1 > 0)):
                        num += 1
                        if itemData.NotShowCharacterBonus:
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(itemData.AuracurseGainValue1), SpriteText(itemData.AuracurseGain1.Id)))
                        else:
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(itemData.AuracurseGain1.Id, itemData.AuracurseGainValue1, character)), SpriteText(itemData.AuracurseGain1.Id)))
                        if (not itemData.AuracurseGain1.IsAura):
                            flag5 = False
                    if ((itemData.AuracurseGain2 != None) and (itemData.AuracurseGainValue2 > 0)):
                        num += 1
                        if itemData.NotShowCharacterBonus:
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(itemData.AuracurseGainValue2), SpriteText(itemData.AuracurseGain2.Id)))
                        else:
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(itemData.AuracurseGain2.Id, itemData.AuracurseGainValue2, character)), SpriteText(itemData.AuracurseGain2.Id)))
                    if ((itemData.AuracurseGain3 != None) and (itemData.AuracurseGainValue3 > 0)):
                        num += 1
                        if itemData.NotShowCharacterBonus:
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(itemData.AuracurseGainValue3), SpriteText(itemData.AuracurseGain3.Id)))
                        else:
                            stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(itemData.AuracurseGain3.Id, itemData.AuracurseGainValue3, character)), SpriteText(itemData.AuracurseGain3.Id)))
                    if (num > 0):
                        if (itemData.ItemTarget == Enums.ItemTarget.Self):
                            if (((itemData.HealQuantity > 0) or (itemData.EnergyQuantity > 0)) or (itemData.HealPercentQuantity > 0)):
                                stringBuilder12 = StringBuilder()
                                if flag5:
                                    stringBuilder12.Append(str.Format(Texts.Instance.GetText("cardsAnd"), stringBuilder.ToString(), str.Format(Functions.LowercaseFirst(Texts.Instance.GetText("cardsGain")), stringBuilder2.ToString())))
                                else:
                                    stringBuilder12.Append(str.Format(Texts.Instance.GetText("cardsAnd"), stringBuilder.ToString(), str.Format(Functions.LowercaseFirst(Texts.Instance.GetText("cardsSuffer")), stringBuilder2.ToString())))
                                stringBuilder.Clear()
                                stringBuilder.Append(stringBuilder12.ToString())
                            elif flag5:
                                text8 = stringBuilder.ToString()
                                if ((text8.Length > 8) and (text8.Substring((text8.Length - 9)) == "<c>, </c>")):
                                    stringBuilder.Append(str.Format(Functions.LowercaseFirst(Texts.Instance.GetText("cardsGain")), stringBuilder2.ToString()))
                                else:
                                    stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                            elif (stringBuilder.ToString().Substring((stringBuilder.ToString().Length - 9)) == "<c>, </c>"):
                                stringBuilder.Append(str.Format(Functions.LowercaseFirst(Texts.Instance.GetText("cardsSuffer")), stringBuilder2.ToString()))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.AllEnemy):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyEnemies"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.AllHero):
                            if (cardClass == Enums.CardClass.Monster):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyHeroesFromMonster"), stringBuilder2.ToString()))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyHeroes"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.RandomHero):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemForEveryCharge"), ColorTextArray("curse", SpriteText(itemData.AuraCurseSetted.Id))))
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyRandomHero"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.RandomEnemy):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemForEveryCharge"), ColorTextArray("curse", SpriteText(itemData.AuraCurseSetted.Id))))
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyRandomEnemy"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.HighestFlatHpEnemy):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemForEveryCharge"), ColorTextArray("curse", SpriteText(itemData.AuraCurseSetted.Id))))
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyHighestFlatHpEnemy"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.LowestFlatHpEnemy):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemForEveryCharge"), ColorTextArray("curse", (itemData.AuraCurseNumForOneEvent.ToString() if ((itemData.AuraCurseNumForOneEvent > 1)) else ""), SpriteText(itemData.AuraCurseSetted.Id))))
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyLowestFlatHpEnemy"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.HighestFlatHpHero):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemForEveryCharge"), ColorTextArray("curse", (itemData.AuraCurseNumForOneEvent.ToString() if ((itemData.AuraCurseNumForOneEvent > 1)) else ""), SpriteText(itemData.AuraCurseSetted.Id))))
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyHighestFlatHpHero"), stringBuilder2.ToString()))
                        elif (itemData.ItemTarget == Enums.ItemTarget.LowestFlatHpHero):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemForEveryCharge"), ColorTextArray("curse", (itemData.AuraCurseNumForOneEvent.ToString() if ((itemData.AuraCurseNumForOneEvent > 1)) else ""), SpriteText(itemData.AuraCurseSetted.Id))))
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyLowestFlatHpHero"), stringBuilder2.ToString()))
                        elif ((targetSide == Enums.CardTargetSide.Enemy) or (itemData.ItemTarget == Enums.ItemTarget.CurrentTarget)):
                            if ((itemData.AuraCurseSetted != None) and (itemData.AuraCurseNumForOneEvent > 0)):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyForEvery"), ColorTextArray("curse", (itemData.AuraCurseNumForOneEvent.ToString() if ((itemData.AuraCurseNumForOneEvent > 1)) else ""), SpriteText(itemData.AuraCurseSetted.Id)), stringBuilder2.ToString()))
                            elif (itemData.ItemTarget == Enums.ItemTarget.Random):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("itemApplyRandom"), stringBuilder2.ToString()))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsApply"), stringBuilder2.ToString()))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGrant"), stringBuilder2.ToString()))
                        stringBuilder.Append("\n")
                        stringBuilder2.Clear()
                    num = 0
                    flag5 = True
                    if ((itemData.AuracurseGainSelf1 != None) and (itemData.AuracurseGainSelfValue1 > 0)):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(itemData.AuracurseGainSelf1.Id, itemData.AuracurseGainSelfValue1, character)), SpriteText(itemData.AuracurseGainSelf1.Id)))
                        if (not itemData.AuracurseGainSelf1.IsAura):
                            flag5 = False
                    if ((itemData.AuracurseGainSelf2 != None) and (itemData.AuracurseGainSelfValue2 > 0)):
                        num += 1
                        stringBuilder2.Append(ColorTextArray("aura", NumFormat(GetFinalAuraCharges(itemData.AuracurseGainSelf2.Id, itemData.AuracurseGainSelfValue2, character)), SpriteText(itemData.AuracurseGainSelf2.Id)))
                    if (num > 0):
                        if (((itemData.HealQuantity > 0) or (itemData.EnergyQuantity > 0)) or (itemData.HealPercentQuantity > 0)):
                            stringBuilder13 = StringBuilder()
                            if flag5:
                                stringBuilder13.Append(str.Format(Texts.Instance.GetText("cardsAnd"), stringBuilder.ToString(), str.Format(Functions.LowercaseFirst(Texts.Instance.GetText("cardsGain")), stringBuilder2.ToString())))
                            else:
                                stringBuilder13.Append(str.Format(Texts.Instance.GetText("cardsAnd"), stringBuilder.ToString(), str.Format(Functions.LowercaseFirst(Texts.Instance.GetText("cardsSuffer")), stringBuilder2.ToString())))
                            stringBuilder.Clear()
                            stringBuilder.Append(stringBuilder13.ToString())
                            stringBuilder13 = None
                        elif flag5:
                            if (stringBuilder.ToString().Substring((stringBuilder.ToString().Length - 9)) == "<c>, </c>"):
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                            else:
                                stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsGain"), stringBuilder2.ToString()))
                        elif (stringBuilder.ToString().Substring((stringBuilder.ToString().Length - 9)) == "<c>, </c>"):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsSuffer"), stringBuilder2.ToString()))
                        stringBuilder.Append("\n")
                        stringBuilder2.Clear()
                    if (itemData.CardNum > 0):
                        if (not ((itemData.CardToGain != None))):
                            _ = itemData.CardToGainType
                        text9 = ""
                        if (itemData.CardToGain != None):
                            if (itemData.CardNum > 1):
                                stringBuilder2.Append(ColorTextArray("", NumFormat(itemData.CardNum), SpriteText("card")))
                            else:
                                stringBuilder2.Append(SpriteText("card"))
                            cardData2 = Globals.Instance.GetCardData(itemData.CardToGain.Id, instantiate = False)
                            if (cardData2 != None):
                                stringBuilder2.Append(ColorFromCardDataRarity(cardData2))
                                stringBuilder2.Append(cardData2.CardName)
                                stringBuilder2.Append("</color>")
                            text9 = stringBuilder2.ToString()
                            stringBuilder2.Clear()
                        else:
                            if (itemData.CardNum > 1):
                                stringBuilder2.Append(ColorTextArray("", NumFormat(itemData.CardNum), SpriteText("card")))
                            else:
                                stringBuilder2.Append(SpriteText("card"))
                            if (itemData.CardToGainType != 0):
                                stringBuilder2.Append("<color=#5E3016>")
                                stringBuilder2.Append(Texts.Instance.GetText(Enum.GetName(Enums.CardType, itemData.CardToGainType)))
                                stringBuilder2.Append("</color>")
                            text9 = stringBuilder2.ToString()
                            stringBuilder2.Clear()
                        text10 = ""
                        if itemData.Permanent:
                            if itemData.Vanish:
                                if itemData.CostZero:
                                    text10 = str.Format(Texts.Instance.GetText("cardsAddCostVanish"), 0)
                                elif (itemData.CostReduction > 0):
                                    text10 = str.Format(Texts.Instance.GetText("cardsAddCostReducedVanish"), NumFormatItem(itemData.CostReduction, plus = True))
                            elif itemData.CostZero:
                                text10 = str.Format(Texts.Instance.GetText("cardsAddCost"), 0)
                            elif (itemData.CostReduction > 0):
                                text10 = str.Format(Texts.Instance.GetText("cardsAddCostReduced"), NumFormatItem(itemData.CostReduction, plus = True))
                        elif itemData.Vanish:
                            if itemData.CostZero:
                                text10 = str.Format(Texts.Instance.GetText("cardsAddCostVanishTurn"), 0)
                            elif (itemData.CostReduction > 0):
                                text10 = str.Format(Texts.Instance.GetText("cardsAddCostReducedVanishTurn"), NumFormatItem(itemData.CostReduction, plus = True))
                        elif itemData.CostZero:
                            text10 = str.Format(Texts.Instance.GetText("cardsAddCostTurn"), 0)
                        elif (itemData.CostReduction > 0):
                            text10 = str.Format(Texts.Instance.GetText("cardsAddCostReducedTurn"), NumFormatItem(itemData.CostReduction, plus = True))
                        if itemData.DuplicateActive:
                            if (itemData.CardPlace == Enums.CardPlace.Hand):
                                stringBuilder.Append(Texts.Instance.GetText("cardsDuplicateHand"))
                        elif (itemData.CardPlace == Enums.CardPlace.RandomDeck):
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsIDShuffleDeck"), text9))
                        elif (itemData.CardPlace == Enums.CardPlace.Cast):
                            if (itemData.CardToGain != None):
                                cardData3 = Globals.Instance.GetCardData(itemData.CardToGain.Id, instantiate = False)
                                if (cardData3 != None):
                                    stringBuilder2.Append(ColorFromCardDataRarity(cardData3))
                                    stringBuilder2.Append(cardData3.CardName)
                                    stringBuilder2.Append("</color>")
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsCast"), stringBuilder2.ToString()))
                            stringBuilder2.Clear()
                        elif (itemData.CardPlace == Enums.CardPlace.Hand):
                            if (itemData.CardNum > 1):
                                stringBuilder2.Append(ColorTextArray("", NumFormat(itemData.CardNum), SpriteText("card")))
                            else:
                                stringBuilder2.Append(SpriteText("card"))
                            if (itemData.CardToGain != None):
                                cardData4 = Globals.Instance.GetCardData(itemData.CardToGain.Id, instantiate = False)
                                if (cardData4 != None):
                                    stringBuilder2.Append(ColorFromCardDataRarity(cardData4))
                                    stringBuilder2.Append(cardData4.CardName)
                                    stringBuilder2.Append("</color>")
                            stringBuilder2.Clear()
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("cardsIDPlaceHand"), text9))
                        if (text10 != ""):
                            stringBuilder.Append(" ")
                            stringBuilder.Append(value2)
                            stringBuilder.Append(text10)
                            stringBuilder.Append(value3)
                        stringBuilder.Append(" ")
                    if (itemData.CardsReduced > 0):
                        arg3 = (("<color=#5E3016>" + itemData.CardsReduced) + "</color>")
                        arg4 = (("<color=#5E3016>" + Texts.Instance.GetText(Enum.GetName(Enums.CardType, itemData.CardToReduceType))) + "</color>")
                        if (itemData.CardToReduceType == Enums.CardType._None):
                            arg4 = "  <sprite name=cards>"
                        arg5 = (("<color=#111111>" + itemData.CostReduceReduction) + "</color>")
                        if (itemData.CostReducePermanent and itemData.ReduceHighestCost):
                            stringBuilder.Append(str.Format(arg0 = (((("<color=#111111>(" + itemData.CardsReduced) + ")</color> ")) if ((itemData.CardsReduced != 1)) else ""), format = Texts.Instance.GetText("itemReduceHighestPermanent"), arg1 = arg4, arg2 = arg5))
                        elif itemData.CostReducePermanent:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemReduce"), arg3, arg4, arg5))
                        elif itemData.ReduceHighestCost:
                            stringBuilder.Append(str.Format(arg0 = (((("<color=#111111>(" + itemData.CardsReduced) + ")</color> ")) if ((itemData.CardsReduced != 1)) else ""), format = Texts.Instance.GetText("itemReduceHighestTurn"), arg1 = arg4, arg2 = arg5))
                        else:
                            stringBuilder.Append(str.Format(Texts.Instance.GetText("itemReduceTurn"), arg3, arg4, arg5))
                        stringBuilder.Append("\n")
                if (itemData.DestroyStartOfTurn or itemData.DestroyEndOfTurn):
                    stringBuilder.Append("<voffset=-.2><size=-.05><color=#1A505A>- ")
                    stringBuilder.Append(Texts.Instance.GetText("itemDestroyStartTurn"))
                    stringBuilder.Append(" -</color></size>")
                if ((itemData.DestroyAfterUses > 0) and (not itemData.UseTheNextInsteadWhenYouPlay)):
                    stringBuilder.Append("<nobr><voffset=-.1><size=-.05><color=#1A505A>- ")
                    if (itemData.DestroyAfterUses > 1):
                        stringBuilder.Append(str.Format(Texts.Instance.GetText("itemLastUses"), itemData.DestroyAfterUses))
                    else:
                        stringBuilder.Append(Texts.Instance.GetText("itemLastUse"))
                    stringBuilder.Append(" -</color></size></nobr>")
                if (itemData.TimesPerCombat == 1):
                    stringBuilder.Append("<nobr><voffset=-.1><size=-.05><color=#1A505A>- ")
                    stringBuilder.Append(Texts.Instance.GetText("itemOncePerCombat"))
                    stringBuilder.Append(" -</color></size></nobr>")
                if itemData.PassSingleAndCharacterRolls:
                    stringBuilder.Append(Texts.Instance.GetText("cardsPassEventRoll"))
                    stringBuilder.Append("\n")
            stringBuilder.Replace("<c>", "<color=#5E3016>")
            stringBuilder.Replace("</c>", "</color>")
            stringBuilder.Replace("<nb>", "<nobr>")
            stringBuilder.Replace("</nb>", "</nobr>")
            stringBuilder.Replace("<br1>", "<br><line-height=15%><br></line-height>")
            stringBuilder.Replace("<br2>", "<br><line-height=30%><br></line-height>")
            stringBuilder.Replace("<br3>", "<br><line-height=50%><br></line-height>")
            descriptionNormalized = stringBuilder.ToString()
            descriptionNormalized = Regex.Replace(descriptionNormalized, "[,][ ]*(<(.*?)>)*(.)", lambda m: m.ToString().ToLower())
            descriptionNormalized = Regex.Replace(descriptionNormalized, "<br>\\w", lambda m: m.ToString().ToUpper())
            Globals.Instance.CardsDescriptionNormalized[id] = stringBuilder.ToString()
            if includeInSearch:
                input = Regex.Replace(descriptionNormalized, "<sprite name=(.*?)>", lambda m: Texts.Instance.GetText(m.Groups[1].Value))
                input = Regex.Replace(input, "(<(.*?)>)*", "")
                Globals.Instance.IncludeInSearch(input, id, includeFullTerm = False)
            stringBuilder = None
            stringBuilder2 = None
        else:
            descriptionNormalized = Globals.Instance.CardsDescriptionNormalized[id]
    def NumFormatItem(self, num, plus = False, percent = False):
        stringBuilder = StringBuilder()
        stringBuilder.Append(" <nobr>")
        if (num > 0):
            stringBuilder.Append("<color=#263ABC><size=+.1>")
            if plus:
                stringBuilder.Append("+")
        else:
            stringBuilder.Append("<color=#720070><size=+.1>")
            if plus:
                stringBuilder.Append("-")
        stringBuilder.Append(Mathf.Abs(num))
        if percent:
            stringBuilder.Append("%")
        stringBuilder.Append("</color></size></nobr>")
        return stringBuilder.ToString()
    def NumFormat(self, num):
        if (num < 0):
            num = 0
        stringBuilder = StringBuilder()
        stringBuilder.Append("<size=+.1>")
        stringBuilder.Append(num)
        stringBuilder.Append("</size>")
        return stringBuilder.ToString()
    def GetCardTypes(self):
        if (cardTypeList == None):
            cardTypeList = List[Enums.CardType]()
            if (cardType != 0):
                cardTypeList.Add(cardType)
                i = 0
                while (i < cardTypeAux.Length):
                    if (cardTypeAux[i] != 0):
                        cardTypeList.Add(cardTypeAux[i])
                    i += 1
        return cardTypeList
    def HasCardType(self, type):
        if (cardType == type):
            return True
        i = 0
        while (i < cardTypeAux.Length):
            if (cardTypeAux[i] == type):
                return True
            i += 1
        return False
    def DoExhaust(self):
        if bool(MatchManager.Instance):
            heroHeroActive = MatchManager.Instance.GetHeroHeroActive()
            if (heroHeroActive != None):
                Debug.Log(((((("DoExhaust from " + exhaustCounter) + " char-> ") + heroHeroActive.GetAuraCharges("Exhaust")) + " to->") + ((exhaustCounter + heroHeroActive.GetAuraCharges("Exhaust")))))
                exhaustCounter += heroHeroActive.GetAuraCharges("Exhaust")
    def GetIgnoreBlock(self, _index = 0):
        if bool(MatchManager.Instance):
            heroHeroActive = MatchManager.Instance.GetHeroHeroActive()
            if ((((heroHeroActive != None) and (heroHeroActive.SubclassName == "archer")) and AtOManager.Instance.CharacterHaveTrait("archer", "perforatingshots")) and HasCardType(Enums.CardType.Ranged_Attack)):
                return True
        return _index
        0
        ignoreBlock
        1
        ignoreBlock2
        lambda _: False
def ResetExhaust():
    exhaustCounter = 0
def GetCardFinalCost():
    num = EnergyCostOriginal
    if bool(MatchManager.Instance):
        if (EnergyReductionToZeroPermanent or EnergyReductionToZeroTemporal):
            num = 0
        num = ((num - EnergyReductionPermanent) - EnergyReductionTemporal)
        num = ((((num + ExhaustCounter)) if (((((((CardClass != Enums.CardClass.Special) or Playable)) and (CardClass != Enums.CardClass.Boon)) and (CardClass != Enums.CardClass.Injury)) and (((CardClass != Enums.CardClass.Monster) or Playable)))) else 0))
        if (num < 0):
            num = 0
    return num
def ColorFromCardDataRarity(_cData):
    if (_cData != None):
        stringBuilder = StringBuilder()
        stringBuilder.Append("<color=#")
        if (_cData.cardUpgraded == Enums.CardUpgraded.A):
            stringBuilder.Append(colorUpgradeBlue)
        elif (_cData.cardUpgraded == Enums.CardUpgraded.B):
            stringBuilder.Append(colorUpgradeGold)
        elif (_cData.cardUpgraded == Enums.CardUpgraded.Rare):
            stringBuilder.Append(colorUpgradeRare)
        else:
            stringBuilder.Append(colorUpgradePlain)
        stringBuilder.Append(">")
        return stringBuilder.ToString()
    return "<color=#5E3016>"
