# API
import urllib2
class Api:
    base_api = "http://services.runescape.com/m=itemdb_rs/api/catalogue/"
    item_api = "detail.json?item={i}"
    catalog_api="items.json?category={cid}&alpha={a}&page={p}"

    def __init__(self, ):
        self.opener = urllib2.build_opener()
        opener.addheaders = [('User-agent',
                              'GenExcPriceUpdater /1.0 klokeman3@gmail.com')]

    def getItem(id_):
        response = self.opener(Api.base_api+Api.item_api.format(i=id_))

    def getCatalog(cid, alpha, page):
        response = self.opener(Api.base_api+Api.item_api.format(cid=cid,
                                                                a=alpha,
                                                                p=page))
        

    def _json_to_item(raw_json):
        pass

if __name__ == "__main__":
    api = Api()
    
    

    
