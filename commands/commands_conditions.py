from discord.ext import commands


class commands_conditions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="comandos")
    async def send_message(self, ctx):
        name = ctx.author.name

        response = '''
            **Condições:**
    *!agarrado - !grappled
    !amedrontado - !frightened
    !atordoado - !stunned
    !caido - !prone
    !cego - !blinded
    !enfeitiçado  - !charmed
    !envenenado - !poisoned
    !exaustao - !exhaustion
    !impedido  - !restrained
    !incapacitado - !incapacitated
    !inconsciente - !unconscious
    !invisivel - !invisible
    !paralisado - !paralyzed
    !petrificado - !petrified
    !surdo - deafened*
    '''
        await ctx.send(response)


def setup(bot):
    bot.add_cog(commands_conditions(bot))
