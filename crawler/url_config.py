"""
    作者：wanghuamin
    日期：20200308
    功能：tools 163，sin 配置
    版本：1.0
"""
class http_config():


    def get_config(self, name):
        config = {
            '163_current': 'http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA%3BEXCHANGE%3ACNSESH&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=1595&type=query',
            '163_html': 'http://quotes.money.163.com/trade/lsjysj_{stockCode}.html#01b07',
            '163_download': 'http://quotes.money.163.com/service/chddata.html?code=0{stockCode}&start={date_start}&end={date_end}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP',
            'sina':'http://hq.sinajs.cn/list=sh{stockCode}'
        }
        return config[name]