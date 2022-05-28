from discord.ext import commands


class messages_eng(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='grappled')
    async def grappled(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A grappled creature's speed becom es 0, and it can't benefit from any bonus to its speed.
    The condition ends if the grappler is incapacitated (see the condition).
    The condition also ends if an effect rem oves the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell."""

        await ctx.send(response)

    @commands.command(name='frightened')
    async def frightened(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line o f sight.
    The creature can't willingly move closer to the source of its fear."""

        await ctx.send(response)

    @commands.command(name='blinded')
    async def blinded(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A blinded creature can’t see and automatically fails any ability check that requires sight.
    Attack rolls against the creature have advantage, and the creature’s attack rolls have disadvantage."""

        await ctx.send(response)

    @commands.command(name='charmed')
    async def charmed(self, ctx):
        name = ctx.author.name

        response = f'''{name}
    A charm ed creature can't attack the charm er or target the charm er with harmful abilities or m agical effects.
    The charm er has advantage on any ability check to interact socially with the creature'''

        await ctx.send(response)

    @commands.command(name='deafened')
    async def deafened(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A deafened creature can't hear and automatically fails any ability check that requires hearing."""

        await ctx.send(response)

    @commands.command(name='incapacitated')
    async def incapacitated(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    An incapacitated creature can't take actions or reactions"""

        await ctx.send(response)

    @commands.command(name='invisible')
    async def invisible(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    An invisible creature is im possible to see without the aid o f m agic or a special sense. For the purpose of hiding, the creature is heavily obscured. 
    The creature's location can be detected by any noise it makes or any tracks it leaves.
    Attack rolls against the creature have disadvantage, and the creature's attack rolls have advantage"""

        await ctx.send(response)

    @commands.command(name='paralyzed')
    async def paralyzed(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A paralyzed creature is incapacitated (see the condition) and can't move or speak.The creature automatically fails Strength and Dexterity saving throws.
    Attack rolls against the creature have advantage.
    Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature"""

        await ctx.send(response)

    @commands.command(name='exhaustion')
    async def exhaustion(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. 
    Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description.
    Level Effect
    1 Disadvantage on ability checks
    2 Speed halved
    3 Disadvantage on attack rolls and saving throws
    4 Hit point maximum halved
    5 Speed reduced to 0
    6 Death
    If an already exhausted creature suffers another effect that causes exhaustion, its current level of exhaustion increases by the amount specified in the effect's description.
    A creature suffers the effect of its current level of exhaustion as well as all lower levels. For example, a creature suffering level 2 exhaustion has its speed halved and has disadvantage on ability checks.
    An effect that removes exhaustion reduces its level as specified in the effect's description, with all exhaustion 
    effects ending if a creature's exhaustion level is reduced below 1.
    Finishing a long rest reduces a creature's exhaustion level by 1, provided that the creature has also ingested some food and drink"""

        await ctx.send(response)

    @commands.command(name='petrified')
    async def petrified(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A petrified creature is transformed, along with any nonm agical object it is w earing or carrying, into a solid inanimate substance (usually stone). Its weight 
    increases by a factor of ten, and it ceases aging.
    The creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings.
    Attack rolls against the creature have advantage.
    The creature automatically fails Strength and Dexterity saving throws.
    The creature has resistance to all damage.
    The creature is im mune to poison and disease, although a poison or disease already in its system is suspended, not neutralized.
    """

        await ctx.send(response)

    @commands.command(name='poisoned')
    async def poisoned(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A poisoned creature has disadvantage on attack rolls and ability checks"""

        await ctx.send(response)

    @commands.command(name='prone')
    async def prone(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A prone creature’s only movement option is to crawl, unless it stands up and thereby ends the condition.
    The creature has disadvantage on attack rolls.
    An attack roll against the creature has advantage if the attacker is within 5 feet of the creature. 
    Otherwise, the attack roll has disadvantage"""

        await ctx.send(response)

    @commands.command(name='restrained')
    async def restrained(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A restrained creature’s speed becom es 0, and it can't benefit from any bonus to its speed.
    Attack rolls against the creature have advantage, and the creature's attack rolls have disadvantage.
    The creature has disadvantage on Dexterity saving throws"""

        await ctx.send(response)

    @commands.command(name='stunned')
    async def stunned(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A stunned creature is incapacitated (see the condition), can’t move, and can speak only falteringly.
    The creature automatically fails Strength and Dexterity saving throws.
    Attack rolls against the creature have advantage"""

        await ctx.send(response)

    @commands.command(name='unconscious')
    async def unconscious(self, ctx):
        name = ctx.author.name

        response = f"""
                    {name}
    An unconscious creature is incapacitated (seethe condition), can't move or speak, and is unaware of its surroundings
    The creature drops whatever it’s holding and falls prone.
    The creature automatically fails Strength and Dexterity saving throws.
    Attack rolls against the creature have advantage.
    Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.
    """

        await ctx.send(response)


def setup(bot):
    bot.add_cog(messages_eng(bot))
