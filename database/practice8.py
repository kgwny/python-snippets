# 自己結合
# 自己結合を行う場合、aliasで別名のオブジェクトを作成しておき、それを利用する
    fromBusStop = BusStopOrder.alias()
    toBusStop = BusStopOrder.alias()
    query = (fromBusStop
        .select(fromBusStop, toBusStop, BusStop)
        .join(
            toBusStop,
            on=((toBusStop.route == fromBusStop.route) & (toBusStop.stopOrder > fromBusStop.stopOrder))
            .alias('toBusStopOrder')
        )
        .switch(toBusStop)
        .join(BusStop, on=(toBusStop.busStop==BusStop.id))
        .where((fromBusStop.busStop==from_bus_stop))
    )
    for r in query:
        print (r.toBusStopOrder.busStop.id)

