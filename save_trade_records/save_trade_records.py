import time

from .setting import conn_ctp_pro
from vnpy_ctp import CtpGateway
from vnpy.trader.engine import MainEngine
from vnpy.event import EventEngine
from vnpy.trader.database import get_database


def save_trading_records(trades, orders):
    database = get_database()
    database.save_trade_data(trades)
    database.save_order_data(orders)


def main():
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway)
    main_engine.connect(conn_ctp_pro, 'CTP')
    time.sleep(60)
    orders = main_engine.get_all_orders()
    trades = main_engine.get_all_trades()
    save_trading_records(trades, orders)
    print("save_trading_records done")


if __name__ == '__main__':
    main()