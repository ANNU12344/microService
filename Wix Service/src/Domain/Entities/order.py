from datetime import datetime
from uuid import UUID
from typing import List, Any


class Activity:
    type: str
    timestamp: datetime

    def __init__(self, type: str, timestamp: datetime) -> None:
        self.type = type
        self.timestamp = timestamp


class FullName:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Address:
    full_name: FullName
    country: str
    subdivision: str
    city: str
    zip_code: int
    phone: str
    email: str
    address_line1: str

    def __init__(self, full_name: FullName, country: str, subdivision: str, city: str, zip_code: int, phone: str, email: str, address_line1: str) -> None:
        self.full_name = full_name
        self.country = country
        self.subdivision = subdivision
        self.city = city
        self.zip_code = zip_code
        self.phone = phone
        self.email = email
        self.address_line1 = address_line1


class BillingInfo:
    payment_method: str
    payment_gateway_transaction_id: UUID
    address: Address
    refundable_by_payment_provider: bool

    def __init__(self, payment_method: str, payment_gateway_transaction_id: UUID, address: Address, refundable_by_payment_provider: bool) -> None:
        self.payment_method = payment_method
        self.payment_gateway_transaction_id = payment_gateway_transaction_id
        self.address = address
        self.refundable_by_payment_provider = refundable_by_payment_provider


class BuyerInfo:
    id: UUID
    type: str
    identity_type: str
    first_name: str
    last_name: str
    phone: str
    email: str
    contact_id: UUID

    def __init__(self, id: UUID, type: str, identity_type: str, first_name: str, last_name: str, phone: str, email: str, contact_id: UUID) -> None:
        self.id = id
        self.type = type
        self.identity_type = identity_type
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.contact_id = contact_id


class ChannelInfo:
    type: str

    def __init__(self, type: str) -> None:
        self.type = type


class AppliedCoupon:
    coupon_id: UUID
    name: str
    code: str

    def __init__(self, coupon_id: UUID, name: str, code: str) -> None:
        self.coupon_id = coupon_id
        self.name = name
        self.code = code


class Discount:
    value: str
    applied_coupon: AppliedCoupon

    def __init__(self, value: str, applied_coupon: AppliedCoupon) -> None:
        self.value = value
        self.applied_coupon = applied_coupon


class EnteredBy:
    id: UUID
    identity_type: str

    def __init__(self, id: UUID, identity_type: str) -> None:
        self.id = id
        self.identity_type = identity_type


class FulfillmentLineItem:
    index: int
    quantity: int

    def __init__(self, index: int, quantity: int) -> None:
        self.index = index
        self.quantity = quantity


class TrackingInfo:
    tracking_number: int
    shipping_provider: str
    tracking_link: str

    def __init__(self, tracking_number: int, shipping_provider: str, tracking_link: str) -> None:
        self.tracking_number = tracking_number
        self.shipping_provider = shipping_provider
        self.tracking_link = tracking_link


class Fulfillment:
    id: UUID
    dateCreated: datetime
    lineItems: List[FulfillmentLineItem]
    tracking_info: TrackingInfo

    def __init__(self, id: UUID, dateCreated: datetime, lineItems: List[FulfillmentLineItem], tracking_info: TrackingInfo) -> None:
        self.id = id
        self.dateCreated = dateCreated
        self.lineItems = lineItems
        self.tracking_info = tracking_info


class MediaItem:
    media_type: str
    url: str
    width: int
    height: int
    media_id: str
    id: str

    def __init__(self, media_type: str, url: str, width: int, height: int, media_id: str, id: str) -> None:
        self.media_type = media_type
        self.url = url
        self.width = width
        self.height = height
        self.media_id = media_id
        self.id = id


class Option:
    option: str
    selection: str

    def __init__(self, option: str, selection: str) -> None:
        self.option = option
        self.selection = selection


class LineItemPriceData:
    tax_included_in_price: bool
    price: str
    total_price: str

    def __init__(self, tax_included_in_price: bool, price: str, total_price: str) -> None:
        self.tax_included_in_price = tax_included_in_price
        self.price = price
        self.total_price = total_price


class OrderLineItem:
    index: int
    quantity: int
    price: str
    name: str
    translated_name: str
    product_id: UUID
    total_price: str
    line_item_type: str
    options: List[Option]
    custom_text_fields: List[Any]
    media_item: MediaItem
    sku: str
    variant_id: UUID
    discount: str
    tax: str
    tax_included_in_price: bool
    price_data: LineItemPriceData
    refunded_quantity: int

    def __init__(self, index: int, quantity: int, price: str, name: str, translated_name: str, product_id: UUID, total_price: str, line_item_type: str, options: List[Option], custom_text_fields: List[Any], media_item: MediaItem, sku: str, variant_id: UUID, discount: str, tax: str, tax_included_in_price: bool, price_data: LineItemPriceData, refunded_quantity: int) -> None:
        self.index = index
        self.quantity = quantity
        self.price = price
        self.name = name
        self.translated_name = translated_name
        self.product_id = product_id
        self.total_price = total_price
        self.line_item_type = line_item_type
        self.options = options
        self.custom_text_fields = custom_text_fields
        self.media_item = media_item
        self.sku = sku
        self.variant_id = variant_id
        self.discount = discount
        self.tax = tax
        self.tax_included_in_price = tax_included_in_price
        self.price_data = price_data
        self.refunded_quantity = refunded_quantity


class ShipmentDetailsPriceData:
    tax_included_in_price: bool
    price: int

    def __init__(self, tax_included_in_price: bool, price: int) -> None:
        self.tax_included_in_price = tax_included_in_price
        self.price = price


class ShipmentDetails:
    address: Address
    tracking_info: TrackingInfo
    discount: int
    tax: str
    price_data: ShipmentDetailsPriceData

    def __init__(self, address: Address, tracking_info: TrackingInfo, discount: int, tax: str, price_data: ShipmentDetailsPriceData) -> None:
        self.address = address
        self.tracking_info = tracking_info
        self.discount = discount
        self.tax = tax
        self.price_data = price_data


class ShippingInfo:
    delivery_option: str
    shipping_region: str
    code: UUID
    shipment_details: ShipmentDetails

    def __init__(self, delivery_option: str, shipping_region: str, code: UUID, shipment_details: ShipmentDetails) -> None:
        self.delivery_option = delivery_option
        self.shipping_region = shipping_region
        self.code = code
        self.shipment_details = shipment_details


class Totals:
    subtotal: str
    shipping: str
    tax: str
    discount: str
    total: str
    weight: int
    quantity: int

    def __init__(self, subtotal: str, shipping: str, tax: str, discount: str, total: str, weight: int, quantity: int) -> None:
        self.subtotal = subtotal
        self.shipping = shipping
        self.tax = tax
        self.discount = discount
        self.total = total
        self.weight = weight
        self.quantity = quantity


class Order:
    id: UUID
    number: int
    dateCreated: datetime
    buyerInfo: BuyerInfo
    currency: str
    weightUnit: str
    totals: Totals
    billingInfo: BillingInfo
    shippingInfo: ShippingInfo
    buyerNote: str
    read: bool
    archived: bool
    paymentStatus: str
    fulfillmentStatus: str
    lineItems: List[OrderLineItem]
    activities: List[Activity]
    fulfillments: List[Fulfillment]
    discount: Discount
    cartId: UUID
    buyerLanguage: str
    channelInfo: ChannelInfo
    enteredBy: EnteredBy
    lastUpdated: datetime
    numericId: int
    refunds: List[Any]
    checkoutId: UUID
    isInternalOrderCreate: bool

    def __init__(self, id: UUID, number: int, dateCreated: datetime, buyerInfo: BuyerInfo, currency: str, weightUnit: str, totals: Totals, billingInfo: BillingInfo, shippingInfo: ShippingInfo, buyerNote: str, read: bool, archived: bool, paymentStatus: str, fulfillmentStatus: str, lineItems: List[OrderLineItem], activities: List[Activity], fulfillments: List[Fulfillment], discount: Discount, cartId: UUID, buyerLanguage: str, channelInfo: ChannelInfo, enteredBy: EnteredBy, lastUpdated: datetime, numericId: int, refunds: List[Any], checkoutId: UUID, isInternalOrderCreate: bool) -> None:
        self.id = id
        self.number = number
        self.dateCreated = dateCreated
        self.buyerInfo = buyerInfo
        self.currency = currency
        self.weightUnit = weightUnit
        self.totals = totals
        self.billingInfo = billingInfo
        self.shippingInfo = shippingInfo
        self.buyerNote = buyerNote
        self.read = read
        self.archived = archived
        self.paymentStatus = paymentStatus
        self.fulfillmentStatus = fulfillmentStatus
        self.lineItems = lineItems
        self.activities = activities
        self.fulfillments = fulfillments
        self.discount = discount
        self.cartId = cartId
        self.buyerLanguage = buyerLanguage
        self.channelInfo = channelInfo
        self.enteredBy = enteredBy
        self.lastUpdated = lastUpdated
        self.numericId = numericId
        self.refunds = refunds
        self.checkout_id = checkoutId
        self.isInternalOrderCreate = isInternalOrderCreate



