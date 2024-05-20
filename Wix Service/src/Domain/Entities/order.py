from typing import List

class BuyerInfo:
    def __init__(self, info):
        self.id = info['id']
        self.type = info['type']
        self.identityType = info['identityType']
        self.firstName = info['firstName']
        self.lastName = info['lastName']
        self.phone = info['phone']
        self.email = info['email']

class Totals:
    def __init__(self, totals):
        self.subtotal = totals['subtotal']
        self.shipping = totals['shipping']
        self.tax = totals['tax']
        self.discount = totals['discount']
        self.total = totals['total']
        self.weight = totals['weight']
        self.quantity = totals['quantity']
        self.refund= totals['refund']
        self.giftCard=totals['giftCard']

class FullName:
    def __init__(self, name):
        self.firstName = name['firstName']
        self.lastName = name['lastName']

class VatId:
    def __init__(self,vat):
        self.number=vat['number']
        self.type=vat['type']

class Address:
    def __init__(self, address):
        self.fullName = FullName(address['fullName'])
        self.country = address['country']
        self.subdivision = address['subdivision']
        self.city = address['city']
        self.zipCode = address['zipCode']
        self.phone = address['phone']
        self.company=address['company']
        self.email = address['email']
        self.addressLine2 = address['addressLine2']
        self.vatId=VatId(address['vatId'])
        self.addressLine1= address['addressLine1']

class BillingInfo:
    def __init__(self, info):
        self.paymentMethod = info['paymentMethod']
        self.paymentProviderTransactionId=info['paymentProviderTransactionId']
        self.paymentGatewayTransactionId = info['paymentGatewayTransactionId']
        self.address = Address(info['address'])
        self.paidDate=info['paidDate']
        self.refundableByPaymentProvider = info['refundableByPaymentProvider']

class TrackingInfo:
    def __init__(self, info):
        self.trackingNumber = info['trackingNumber']
        self.shippingProvider = info['shippingProvider']
        self.trackingLink = info['trackingLink']

class PriceData:
    def __init__(self, data):
        self.taxIncludedInPrice = data['taxIncludedInPrice']
        self.price = data['price']
        self.totalPrice=data['totalPrice']
        

class ShipmentDetails:
    def __init__(self, details):
        self.address = Address(details['address'])
        self.trackingInfo = TrackingInfo(details['trackingInfo'])
        self.discount = details['discount']
        self.tax = details['tax']
        self.priceData = PriceData(details['priceData'])

class ShippingInfo:
    def __init__(self, info):
        self.deliveryOption = info['deliveryOption']
        self.estimatedDeliveryTime=info['estimatedDeliveryTime']
        self.shippingRegion = info['shippingRegion']
        self.code = info['code']
        self.shipmentDetails = ShipmentDetails(info['shipmentDetails'])

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
        self.externalImageUrl=media['externalImageUrl']
        self.altText=media['altText']

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
        self.weight=item['weight']
        self.mediaItem = MediaItem(item['mediaItem'])
        self.sku = item['sku']
        self.notes=item['notes']
        self.variantId = item['variantId']
        self.fulfillerId=item['fulfillerId']
        self.discount = item['discount']
        self.tax = item['tax']
        self.taxIncludedInPrice = item['taxIncludedInPrice']
        self.taxGroupId=item['taxGroupId']
        self.priceData = PriceData(item['priceData'])
        



class Activities:
    def __init__(self, activity):
        self.type = activity['type']
        self.author=activity['author']
        self.message=activity['message']
        self.timestamp = activity['timestamp']

class InvoiceInfo:
    def __init__(self,invoice):
        self.id=invoice['id']
        self.source=invoice['source']

class FulfillmentLineItem:
    def __init__(self,item):
        self.index=item['index']
        self.quantity=item['quantity']

class Fulfillments:
    def __init__(self, fulfillment):
        self.id = fulfillment['id']
        self.dateCreated = fulfillment['dateCreated']
        self.lineItems = [FulfillmentLineItem(item) for item in fulfillment['lineItems']]
        self.trackingLink=TrackingInfo(fulfillment['trackingLink'])

class AppliedCoupon:
    def __init__(self,coupon):
        self.couponId=coupon['couponId']
        self.name=coupon['name']
        self.code=coupon['code']

class Discount:
    def __init__(self, discount):
        self.value = discount['value']
        self.appliedCoupon = AppliedCoupon(discount['appliedCoupon'])

class CustomField:
    def __init__(self,field):
        self.value=field['value']
        self.title=field['title']
        self.translatedTitle=field['translatedTitle']

class ChannelInfo:
    def __init__(self, info):
        self.type=info['type']
        self.externalOrderId = info['externalOrderId']
        self.externalOrderUrl= info['externalOrderUrl']

class EnteredBy:
    def __init__(self, by):
        self.id = by['id']
        self.identityType = by['identityType']

class SubscriptionSettings:
    def __init__(self,setting):
        self.frequency=setting['frequency']
        self.autoRenewal=setting['autoRenewal']
        self.billingCycles=setting['billingCycles']

class SubscriptionOptionInfo:
    def __init_(self,info):
        self.title=info['title']
        self.description=info['description']

class SubscriptionInfo:
    def __init__(self,subscription):
        self.id=subscription['id']
        self.cycleNumer=subscription['cycleNumber']
        self.subscriptionSettings=SubscriptionSettings(subscription['subscriptionSettings'])
        self.subscriptionOptionInfo=SubscriptionOptionInfo(subscription['subscriptionOptionInfo'])

class Refunds:
    def __init__(self,refund):
        self.dateCreated=refund['dateCreated']
        self.amount=refund['amount']
        self.reason=refund['reason']
        self.paymentProvidefTransactionId=refund['paymentProvidefTransactionId']
        self.id=refund['id']
        self.externalRefund=refund['paymentProvidefTransactionId']

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
        self.activities = [Activities(act) for act in order_dict['activities']]
        self.invoiceInfo=InvoiceInfo(order_dict['invoiceInfo'])
        self.fulfillments = [Fulfillments(ful) for ful in order_dict['fulfillments']]
        self.discount = Discount(order_dict['discount'])
        self.customField=CustomField(order_dict['customField'])
        self.cartId = order_dict['cartId']
        self.buyerLanguage = order_dict['buyerLanguage']
        self.channelInfo = ChannelInfo(order_dict['channelInfo'])
        self.enteredBy = EnteredBy(order_dict['enteredBy'])
        self.lastUpdated = order_dict['lastUpdated']
        self.subscriptionInfo= SubscriptionInfo(order_dict['subscriptionInfo'])
        self.numericId = order_dict['numericId']
        self.refunds = order_dict['refunds']
        

