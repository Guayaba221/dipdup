import demo_tezos_dex.models as models
from demo_tezos_dex.types.quipu_fa2.tezos_storage import QuipuFa2Storage
from dipdup.context import HandlerContext
from dipdup.models.tezos import TezosOrigination


async def on_fa2_origination(
    ctx: HandlerContext,
    quipu_fa2_origination: TezosOrigination[QuipuFa2Storage],
) -> None:
    symbol = ctx.template_values['symbol']

    for address, value in quipu_fa2_origination.storage.storage.ledger.items():
        shares_qty = value.balance
        await models.Position(trader=address, symbol=symbol, shares_qty=shares_qty).save()
