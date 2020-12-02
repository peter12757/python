

class OrderForm():
    """
    订单
    """
    orderNo:str = "" #采购单
    caigouNo:str = ""#采购编号
    time = "" # 下单时间
    person = "" # 采购人员
    company = "" # 供应商名称
    chromeHandle = None #chrome tab页的句柄

    def __init__(self,orderNo,caigouNo,time,person,company) -> None:
        self.orderNo = orderNo
        self.caigouNo = caigouNo
        self.time = time
        self.person = person
        self.company = company


    pass