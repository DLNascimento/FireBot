from discord.ext import commands
import discord


class messages_ptbr(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="agarrado")
    async def agarrado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    O Deslocamento de uma criatura agarrada se torna 0, e ela não pode se beneficiar de qualquer bônus em seu deslocamento.
    A condição encerra caso a criatura que agarrou fique incapacitada(Veja a condição).
    A condição se encerra se um efeito, como o causado pela magia "Onda Trovejante", remover a criatura agarrada do alcance
    da criatura que a agarrou ou do efeito que causa a condição."""

        await ctx.send(response)

    @commands.command(name="amedrontado")
    async def amedrontado(self, ctx):
        name = ctx.author.name
        response = f"""{name}
    Uma criatura amedrontada sofre desvantagem em testes de habilidade e jogadas de ataque enquanto a fonte do seu medo estiver em sua linha de visão.
    A criatura não pode se mover voluntariamente para uma posição que a faça terminar o turno mais próxima da sua fonte de medo do que sua posição inicial."""

        await ctx.send(response)

    @commands.command(name='atordoado')
    async def atordoado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura atordoada está incapacitada (veja a condição). Ela não pode se mover e somente pode falar hesitantemente.
    A criatura falha automaticamente em testes de resistência de Força ou Destreza.
    Jogadas de ataque contra a criatura possuem vantagem"""

        await ctx.send(response)

    @commands.command(name="caido")
    async def caido(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    A única opção de movimento que uma criatura caída tem é rastejar, a menos que ela se levante, encerrando assim a condição. A criatura sofre desvantagem nas jogadas de ataque.
    Uma jogada de ataque contra a criatura possui vantagem se o atacante estiver a 1,5 metro dela. De qualquer outra forma a jogada sofre desvantagem."""

        await ctx.send(response)

    @commands.command(name="cego")
    async def cego(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura cega falha automaticamente em qualquer teste de habilidade que requeira o uso da visão.
    Jogadas de ataque contra a criatura possuem vantagem, e os ataques da criatura sofrem desvantagem"""

        await ctx.send(response)

    @commands.command(name='enfeitiçado')
    async def enfeitiçado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura enfeitiçada não pode atacar quem a enfeitiçou ou tê-lo como alvo de habilidades ou efeitos mágicos nocivos.
    Quem a enfeitiçou possui vantagem em testes de habilidade feitos para interagir socialmente com a criatura"""

        await ctx.send(response)

    @commands.command(name='envenenado')
    async def envenenado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura envenenada sofre desvantagem em jogadas de ataque e testes de habilidade"""

        await ctx.send(response)

    @commands.command(name='exaustao')
    async def exaustao(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Algumas habilidades especiais e perigos ambientais, como fome e exposição prolongada a temperaturas congelantes ou escaldantes, podem impor uma condição especial chamada exaustão. 
    A exaustão é medida em seis níveis. Um efeito pode fazer com que uma criatura sofra um ou mais níveis de exaustão, como especificado na descrição do efeito.
    Nível Efeito
    1 - Desvantagem em testes de habilidade
    2 - Deslocamento reduzido à metade
    3 - Desvantagem nas jogadas de ataque e testes de resistência
    4 - Máximo de pontos de vida reduzido à metade
    5 - Deslocamento reduzido à 0
    6 - Morte
    Se uma criatura que já possui um nível de exaustão sofrer outro efeito que também causa exaustão, o nível atual de exaustão da criatura aumenta em uma quantidade especificada pela descrição do efeito que a causou.
    Conforme o nível de exaustão de uma criatura aumenta, os efeitos pioram. A criatura não sofre apenas o efeito do seu nível atual de exaustão, mas de todos os níveis anteriores, sendo assim uma criatura sofrendo 
    o nível 2 de exaustão tem seu deslocamento reduzido pela metade além de sofrer desvantagem em testes de habilidade.
    Um efeito que remova exaustão reduz seu nível, com todos os efeitos de exaustão desaparecendo se esse nível for reduzido abaixo de 1.
    Terminar um descanso longo reduz a exaustão de uma criatura em 1 nível, contanto que ela também tenha ingerido um pouco de água e comida.
    """

        await ctx.send(response)

    @commands.command(name="impedido")
    async def impedido(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    O deslocamento de uma criatura impedida se torna 0, e ela não pode se beneficiar de qualquer bônus em seu deslocamento.
    Jogadas de ataque contra a criatura possuem vantagem, e os ataques da criatura sofrem desvantagem.
    A criatura sofre desvantagem em testes de resistência de Destreza.
    """

        await ctx.send(response)

    @commands.command(name='incapacitado')
    async def incapacitado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura incapacitada não pode realizar ações ou reações"""

        await ctx.send(response)

    @commands.command(name='inconsciente')
    async def incosciente(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura inconsciente está incapacitada (veja a condição). 
    Ela não pode se mover ou falar e não tem ciência de seus arredores.
    A criatura larga tudo que estiver segurando e fica caída. 
    A criatura falha automaticamente em testes de resistência de Força ou Destreza.
    Jogadas de ataque contra a criatura possuem vantagem.
    Qualquer ataque que atinja a criatura é um acerto crítico, se o atacante estiver a 1,5 metro dela"""

        await ctx.send(response)

    @commands.command(name='invisivel')
    async def invisivel(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura invisível é impossível de ser vista sem a ajuda de magia ou sentidos especiais. Para o propósito de se esconder, a criatura é considerada em área de escuridão densa. 
    A localização da criatura pode ser detectada por qualquer barulho que ela faça ou rastros que ela deixe.
    Jogadas de ataque contra a criatura sofrem desvantagem, e os ataques da criatura possuem vantagem.
    """

        await ctx.send(response)

    @commands.command(name="paralisado")
    async def paralisado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura paralisada está incapacitada (veja a condição). Ela não pode se mover ou falar. 
    A criatura falha automaticamente em teste de resistência de Força e Destreza.
    Jogadas de ataque contra a criatura possuem  vantagem.
    Qualquer ataque que atinja a criatura é um acerto crítico, se o atacante estiver a 1,5 metro dela"""

        await ctx.send(response)

    @commands.command(name="petrificado")
    async def petrificado(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura petrificada está transformada, juntamente com todos os objetos não-mágicos que estiver vestindo ou carregando, em uma substância sólida e 
    inanimada(geralmente pedra). 
    Seu peso é multiplicado por dez, e ela para de envelhecer.
    A criatura está incapacitada (veja a condição), não pode se mover ou falar, e não tem ciência de seus arredores.
    Jogadas de ataque contra a criatura possuem vantagem.
    A criatura falha automaticamente em testes de resistência de Força e Destreza.
    A criatura tem resistência a todos os tipos de dano.
    A criatura é imune a veneno e doenças, embora um veneno ou doença previamente presente em seu sistema seja apenas suspenso, não neutralizado"""

        await ctx.send(response)

    @commands.command(name="surdo")
    async def surdo(self, ctx):
        name = ctx.author.name

        response = f"""{name}
    Uma criatura surda falha automaticamente emqualquer teste de habilidade que requeira o uso da audição"""

        await ctx.send(response)


def setup(bot):
    bot.add_cog(messages_ptbr(bot))
