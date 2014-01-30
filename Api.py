# API
import urllib2
import json
import Item
class Api:
    base_api = "http://services.runescape.com/m=itemdb_rs/api/catalogue/"
    item_api = "detail.json?item={i}"
    catalog_api="items.json?category={cid}&alpha={a}&page={p}"

    def __init__(self, ):
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent',
                                   'GenExcPriceUpdater /1.0 klokeman3@gmail.com')]

    def _getItemJson(self, id_):
        try:
            response = self.opener.open(Api.base_api+Api.item_api.format(i=id_))
            response_json = json.loads(response.read())
            return response_json
        except urllib2.HTTPError:
            raise IOError
            
    def _strToInt(self, string):
        if (string[-1] == 'k'):
            num = int(float(string[:-1])*10**3)
        elif (string[-1] == 'm'):
            num = int(float(string[:-1])*10**6)        
        else:
            num = int(string)
        return num
    
    def getItem(self,id_):
        try:
            response_json = self._getItemJson(id_)
        except:
            return "DNE"
        item = response_json['item']
        item_id = item['id']
        item_name = item['name']
        new_item = Item.Item(int(item_id),item_name)
        return new_item
        
    def getItemPrice(self, id_):
        try:
            response_json = self._getItemJson(id_)
        except:
            return "DNE"
        item = response_json['item']
        item_price  = item['current']['price']
        return self._strToInt(item_price)
    
    def getCatalog(self,cid, alpha, page):
        response = self.opener.open(Api.base_api+Api.catalog_api.format(cid=cid,
                                                                        a=alpha,
                                                                        p=page))
        items = []
        response_json = json.loads(response.read())
        items_json = response_json["items"]
        for item_json in items_json:
            item_id = item_json['id']
            item_name = item_json['name']
            new_item = Item.Item(int(item_id),item_name)
            items.append(new_item)
        return items

    def getAlchemy(self, id_):
        pass

if __name__ == "__main__":
    api = Api()
    print(api.getItem(11284))
    print(api.getItem(1))
    print("Catalog")
    print(api.getCatalog(1,'b',1))
    print(api.getItemPrice(11284))
