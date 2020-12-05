

class HttpOrderForm():
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




class XmlOrderForm():
    """
    docstring
    """
    caiGouNo:str = ""    # 采购编号
    wuLiaoNo:str = ""   # 物料编号
    gongZhuoLingNo:str = ""   # 工作令
    xingHao:str = ""  # 规格/型号
    num:str = ""    # 报交数
    price:str = ""  # 单价

    def __init__(self,caigoubianhao:str,wuliaobianhao:str,gongzhuoling:str,xinghao:str,num:str,price:str):
        super().__init__()
        self.caiGouNo = caigoubianhao
        self.wuLiaoNo = wuliaobianhao
        self.gongZhuoLingNo = gongzhuoling
        self.xingHao = xinghao
        self.num = num
        self.price = price
        

    pass