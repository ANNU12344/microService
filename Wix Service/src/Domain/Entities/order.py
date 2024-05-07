class Order:
    def __init__(self, order_dict):
        self.id = order_dict['id']
        self.number = order_dict['number']
        self.dateCreated = order_dict['dateCreated']
        self.buyerInfo = BuyerInfo(order_dict['buyerInfo'])
        self.currency = order_dict['currency']
        self.weightUnit = order_dict['weightUnit']
        self.totals = Totals(order_dict['totals'])
        self.billingInfo = BillingInfo(order_dict['billingInfo'])
        self.shippingInfo = ShippingInfo(order_dict['shippingInfo'])
        self.buyerNote = order_dict['buyerNote']
        self.read = order_dict['read']
        self.archived = order_dict['archived']
        self.paymentStatus = order_dict['paymentStatus']
        self.fulfillmentStatus = order_dict['fulfillmentStatus']
        self.lineItems = [LineItem(item) for item in order_dict['lineItems']]
        self.activities = [Activity(act) for act in order_dict['activities']]
        self.fulfillments = [Fulfillment(ful) for ful in order_dict['fulfillments']]
        self.discount = Discount(order_dict['discount'])
        self.cartId = order_dict['cartId']
        self.buyerLanguage = order_dict['buyerLanguage']
        self.channelInfo = ChannelInfo(order_dict['channelInfo'])
        self.enteredBy = EnteredBy(order_dict['enteredBy'])
        self.lastUpdated = order_dict['lastUpdated']
        self.numericId = order_dict['numericId']
        self.refunds = order_dict['refunds']
        self.checkoutId = order_dict['checkoutId']
        self.isInternalOrderCreate = order_dict['isInternalOrderCreate']

class BuyerInfo:
    def __init__(self, info):
        self.id = info['id']
        self.type = info['type']
        self.identityType = info['identityType']
        self.firstName = info['firstName']
        self.lastName = info['lastName']
        self.phone = info['phone']
        self.email = info['email']
        self.contactId = info['contactId']

class Totals:
    def __init__(self, totals):
        self.subtotal = totals['subtotal']
        self.shipping = totals['shipping']
        self.tax = totals['tax']
        self.discount = totals['discount']
        self.total = totals['total']
        self.weight = totals['weight']
        self.quantity = totals['quantity']

class BillingInfo:
    def __init__(self, info):
        self.paymentMethod = info['paymentMethod']
        self.paymentGatewayTransactionId = info['paymentGatewayTransactionId']
        self.address = Address(info['address'])
        self.refundableByPaymentProvider = info['refundableByPaymentProvider']

class ShippingInfo:
    def __init__(self, info):
        self.deliveryOption = info['deliveryOption']
        self.shippingRegion = info['shippingRegion']
        self.code = info['code']
        self.shipmentDetails = ShipmentDetails(info['shipmentDetails'])

class Address:
    def __init__(self, address):
        self.fullName = FullName(address['fullName'])
        self.country = address['country']
        self.subdivision = address['subdivision']
        self.city = address['city']
        self.zipCode = address['zipCode']
        self.phone = address['phone']
        self.email = address['email']
        self.addressLine1 = address['addressLine1']

class FullName:
    def __init__(self, name):
        self.firstName = name['firstName']
        self.lastName = name['lastName']

class ShipmentDetails:
    def __init__(self, details):
        self.address = Address(details['address'])
        self.trackingInfo = TrackingInfo(details['trackingInfo'])
        self.discount = details['discount']
        self.tax = details['tax']
        self.priceData = PriceData(details['priceData'])

class TrackingInfo:
    def __init__(self, info):
        self.trackingNumber = info['trackingNumber']
        self.shippingProvider = info['shippingProvider']
        self.trackingLink = info['trackingLink']

class PriceData:
    def __init__(self, data):
        self.taxIncludedInPrice = data['taxIncludedInPrice']
        self.price = data['price']

class LineItem:
    def __init__(self, item):
        self.index = item['index']
        self.quantity = item['quantity']
        self.price = item['price']
        self.name = item['name']
        self.translatedName = item['translatedName']
        self.productId = item['productId']
        self.totalPrice = item['totalPrice']
        self.lineItemType = item['lineItemType']
        self.options = [Option(opt) for opt in item.get('options', [])]
        self.customTextFields = item['customTextFields']
        self.mediaItem = MediaItem(item['mediaItem'])
        self.sku = item['sku']
        self.variantId = item['variantId']
        self.discount = item['discount']
        self.tax = item['tax']
        self.taxIncludedInPrice = item['taxIncludedInPrice']
        self.priceData = PriceData(item['priceData'])
        self.refundedQuantity = item['refundedQuantity']

class Option:
    def __init__(self, option):
        self.option = option['option']
        self.selection = option['selection']

class MediaItem:
    def __init__(self, media):
        self.mediaType = media['mediaType']
        self.url = media['url']
        self.width = media['width']
        self.height = media['height']
        self.mediaId = media['mediaId']
        self.id = media['id']

class Activity:
    def __init__(self, activity):
        self.type = activity['type']
        self.timestamp = activity['timestamp']

class Fulfillment:
    def __init__(self, fulfillment):
        self.id = fulfillment['id']
        self.dateCreated = fulfillment['dateCreated']
        self.lineItems = [LineItem(item) for item in fulfillment['lineItems']]

class Discount:
    def __init__(self, discount):
        self.type = discount['type']
        self.value = discount['value']
        self.appliedTo = discount['appliedTo']

class ChannelInfo:
    def __init__(self, info):
        self.channelType = info['channelType']
        self.channelId = info['channelId']

class EnteredBy:
    def __init__(self, by):
        self.id = by['id']
        self.type = by['type']