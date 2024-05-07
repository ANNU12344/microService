from typing import Optional, List, Any
from enum import Enum
from datetime import datetime


class Address:
    first_name: Optional[str]
    address1: str
    phone: str
    city: str
    zip: int
    province: str
    country: str
    last_name: Optional[str]
    address2: str
    company: None
    latitude: Optional[float]
    longitude: Optional[float]
    name: str
    country_code: str
    province_code: str
    id: Optional[int]
    customer_id: Optional[int]
    country_name: Optional[str]
    default: Optional[bool]

    def __init__(self, first_name: Optional[str], address1: str, phone: str, city: str, zip: int, province: str, country: str, last_name: Optional[str], address2: str, company: None, latitude: Optional[float], longitude: Optional[float], name: str, country_code: str, province_code: str, id: Optional[int], customer_id: Optional[int], country_name: Optional[str], default: Optional[bool]) -> None:
        self.first_name = first_name
        self.address1 = address1
        self.phone = phone
        self.city = city
        self.zip = zip
        self.province = province
        self.country = country
        self.last_name = last_name
        self.address2 = address2
        self.company = company
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.country_code = country_code
        self.province_code = province_code
        self.id = id
        self.customer_id = customer_id
        self.country_name = country_name
        self.default = default


class ClientDetails:
    accept_language: None
    browser_height: None
    browser_ip: str
    browser_width: None
    session_hash: None
    user_agent: None

    def __init__(self, accept_language: None, browser_height: None, browser_ip: str, browser_width: None, session_hash: None, user_agent: None) -> None:
        self.accept_language = accept_language
        self.browser_height = browser_height
        self.browser_ip = browser_ip
        self.browser_width = browser_width
        self.session_hash = session_hash
        self.user_agent = user_agent


class Currency(Enum):
    USD = "USD"


class Money:
    amount: str
    currency_code: Currency

    def __init__(self, amount: str, currency_code: Currency) -> None:
        self.amount = amount
        self.currency_code = currency_code


class Set:
    shop_money: Money
    presentment_money: Money

    def __init__(self, shop_money: Money, presentment_money: Money) -> None:
        self.shop_money = shop_money
        self.presentment_money = presentment_money


class MarketingConsent:
    state: str
    opt_in_level: Optional[str]
    consent_updated_at: datetime
    consent_collected_from: Optional[str]

    def __init__(self, state: str, opt_in_level: Optional[str], consent_updated_at: datetime, consent_collected_from: Optional[str]) -> None:
        self.state = state
        self.opt_in_level = opt_in_level
        self.consent_updated_at = consent_updated_at
        self.consent_collected_from = consent_collected_from


class Customer:
    id: int
    email: str
    accepts_marketing: bool
    created_at: datetime
    updated_at: datetime
    first_name: str
    last_name: str
    state: str
    note: None
    verified_email: bool
    multipass_identifier: None
    tax_exempt: bool
    phone: str
    email_marketing_consent: MarketingConsent
    sms_marketing_consent: MarketingConsent
    tags: str
    currency: Currency
    accepts_marketing_updated_at: datetime
    marketing_opt_in_level: None
    tax_exemptions: List[Any]
    admin_graphql_api_id: str
    default_address: Address

    def __init__(self, id: int, email: str, accepts_marketing: bool, created_at: datetime, updated_at: datetime, first_name: str, last_name: str, state: str, note: None, verified_email: bool, multipass_identifier: None, tax_exempt: bool, phone: str, email_marketing_consent: MarketingConsent, sms_marketing_consent: MarketingConsent, tags: str, currency: Currency, accepts_marketing_updated_at: datetime, marketing_opt_in_level: None, tax_exemptions: List[Any], admin_graphql_api_id: str, default_address: Address) -> None:
        self.id = id
        self.email = email
        self.accepts_marketing = accepts_marketing
        self.created_at = created_at
        self.updated_at = updated_at
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.note = note
        self.verified_email = verified_email
        self.multipass_identifier = multipass_identifier
        self.tax_exempt = tax_exempt
        self.phone = phone
        self.email_marketing_consent = email_marketing_consent
        self.sms_marketing_consent = sms_marketing_consent
        self.tags = tags
        self.currency = currency
        self.accepts_marketing_updated_at = accepts_marketing_updated_at
        self.marketing_opt_in_level = marketing_opt_in_level
        self.tax_exemptions = tax_exemptions
        self.admin_graphql_api_id = admin_graphql_api_id
        self.default_address = default_address


class DiscountApplication:
    target_type: str
    type: str
    value: str
    value_type: str
    allocation_method: str
    target_selection: str
    code: str

    def __init__(self, target_type: str, type: str, value: str, value_type: str, allocation_method: str, target_selection: str, code: str) -> None:
        self.target_type = target_type
        self.type = type
        self.value = value
        self.value_type = value_type
        self.allocation_method = allocation_method
        self.target_selection = target_selection
        self.code = code


class DiscountCode:
    code: str
    amount: str
    type: str

    def __init__(self, code: str, amount: str, type: str) -> None:
        self.code = code
        self.amount = amount
        self.type = type


class DiscountAllocation:
    amount: str
    amount_set: Set
    discount_application_index: int

    def __init__(self, amount: str, amount_set: Set, discount_application_index: int) -> None:
        self.amount = amount
        self.amount_set = amount_set
        self.discount_application_index = discount_application_index


class NoteAttribute:
    name: str
    value: str

    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value


class TaxLine:
    channel_liable: None
    price: str
    price_set: Set
    rate: float
    title: str

    def __init__(self, channel_liable: None, price: str, price_set: Set, rate: float, title: str) -> None:
        self.channel_liable = channel_liable
        self.price = price
        self.price_set = price_set
        self.rate = rate
        self.title = title


class LineItem:
    id: int
    admin_graphql_api_id: str
    fulfillable_quantity: int
    fulfillment_service: str
    fulfillment_status: None
    gift_card: bool
    grams: int
    name: str
    price: str
    price_set: Set
    product_exists: bool
    product_id: int
    properties: List[NoteAttribute]
    quantity: int
    requires_shipping: bool
    sku: str
    taxable: bool
    title: str
    total_discount: str
    total_discount_set: Set
    variant_id: int
    variant_inventory_management: str
    variant_title: str
    vendor: None
    tax_lines: List[TaxLine]
    duties: List[Any]
    discount_allocations: List[DiscountAllocation]

    def __init__(self, id: int, admin_graphql_api_id: str, fulfillable_quantity: int, fulfillment_service: str, fulfillment_status: None, gift_card: bool, grams: int, name: str, price: str, price_set: Set, product_exists: bool, product_id: int, properties: List[NoteAttribute], quantity: int, requires_shipping: bool, sku: str, taxable: bool, title: str, total_discount: str, total_discount_set: Set, variant_id: int, variant_inventory_management: str, variant_title: str, vendor: None, tax_lines: List[TaxLine], duties: List[Any], discount_allocations: List[DiscountAllocation]) -> None:
        self.id = id
        self.admin_graphql_api_id = admin_graphql_api_id
        self.fulfillable_quantity = fulfillable_quantity
        self.fulfillment_service = fulfillment_service
        self.fulfillment_status = fulfillment_status
        self.gift_card = gift_card
        self.grams = grams
        self.name = name
        self.price = price
        self.price_set = price_set
        self.product_exists = product_exists
        self.product_id = product_id
        self.properties = properties
        self.quantity = quantity
        self.requires_shipping = requires_shipping
        self.sku = sku
        self.taxable = taxable
        self.title = title
        self.total_discount = total_discount
        self.total_discount_set = total_discount_set
        self.variant_id = variant_id
        self.variant_inventory_management = variant_inventory_management
        self.variant_title = variant_title
        self.vendor = vendor
        self.tax_lines = tax_lines
        self.duties = duties
        self.discount_allocations = discount_allocations


class OriginAddress:
    pass

    def __init__(self, ) -> None:
        pass


class Receipt:
    testcase: bool
    authorization: int

    def __init__(self, testcase: bool, authorization: int) -> None:
        self.testcase = testcase
        self.authorization = authorization


class Fulfillment:
    id: int
    admin_graphql_api_id: str
    created_at: datetime
    location_id: int
    name: str
    order_id: int
    origin_address: OriginAddress
    receipt: Receipt
    service: str
    shipment_status: None
    status: str
    tracking_company: str
    tracking_number: str
    tracking_numbers: List[str]
    tracking_url: str
    tracking_urls: List[str]
    updated_at: datetime
    line_items: List[LineItem]

    def __init__(self, id: int, admin_graphql_api_id: str, created_at: datetime, location_id: int, name: str, order_id: int, origin_address: OriginAddress, receipt: Receipt, service: str, shipment_status: None, status: str, tracking_company: str, tracking_number: str, tracking_numbers: List[str], tracking_url: str, tracking_urls: List[str], updated_at: datetime, line_items: List[LineItem]) -> None:
        self.id = id
        self.admin_graphql_api_id = admin_graphql_api_id
        self.created_at = created_at
        self.location_id = location_id
        self.name = name
        self.order_id = order_id
        self.origin_address = origin_address
        self.receipt = receipt
        self.service = service
        self.shipment_status = shipment_status
        self.status = status
        self.tracking_company = tracking_company
        self.tracking_number = tracking_number
        self.tracking_numbers = tracking_numbers
        self.tracking_url = tracking_url
        self.tracking_urls = tracking_urls
        self.updated_at = updated_at
        self.line_items = line_items


class RefundLineItem:
    id: int
    line_item_id: int
    location_id: int
    quantity: int
    restock_type: str
    subtotal: float
    subtotal_set: Set
    total_tax: float
    total_tax_set: Set
    line_item: LineItem

    def __init__(self, id: int, line_item_id: int, location_id: int, quantity: int, restock_type: str, subtotal: float, subtotal_set: Set, total_tax: float, total_tax_set: Set, line_item: LineItem) -> None:
        self.id = id
        self.line_item_id = line_item_id
        self.location_id = location_id
        self.quantity = quantity
        self.restock_type = restock_type
        self.subtotal = subtotal
        self.subtotal_set = subtotal_set
        self.total_tax = total_tax
        self.total_tax_set = total_tax_set
        self.line_item = line_item


class Transaction:
    id: int
    admin_graphql_api_id: str
    amount: str
    authorization: str
    created_at: datetime
    currency: Currency
    device_id: None
    error_code: None
    gateway: str
    kind: str
    location_id: None
    message: None
    order_id: int
    parent_id: int
    payment_id: str
    processed_at: datetime
    receipt: OriginAddress
    source_name: str
    status: str
    test: bool
    user_id: None

    def __init__(self, id: int, admin_graphql_api_id: str, amount: str, authorization: str, created_at: datetime, currency: Currency, device_id: None, error_code: None, gateway: str, kind: str, location_id: None, message: None, order_id: int, parent_id: int, payment_id: str, processed_at: datetime, receipt: OriginAddress, source_name: str, status: str, test: bool, user_id: None) -> None:
        self.id = id
        self.admin_graphql_api_id = admin_graphql_api_id
        self.amount = amount
        self.authorization = authorization
        self.created_at = created_at
        self.currency = currency
        self.device_id = device_id
        self.error_code = error_code
        self.gateway = gateway
        self.kind = kind
        self.location_id = location_id
        self.message = message
        self.order_id = order_id
        self.parent_id = parent_id
        self.payment_id = payment_id
        self.processed_at = processed_at
        self.receipt = receipt
        self.source_name = source_name
        self.status = status
        self.test = test
        self.user_id = user_id


class Refund:
    id: int
    admin_graphql_api_id: str
    created_at: datetime
    note: str
    order_id: int
    processed_at: datetime
    restock: bool
    total_additional_fees_set: Set
    total_duties_set: Set
    user_id: int
    order_adjustments: List[Any]
    transactions: List[Transaction]
    refund_line_items: List[RefundLineItem]
    duties: List[Any]
    additional_fees: List[Any]

    def __init__(self, id: int, admin_graphql_api_id: str, created_at: datetime, note: str, order_id: int, processed_at: datetime, restock: bool, total_additional_fees_set: Set, total_duties_set: Set, user_id: int, order_adjustments: List[Any], transactions: List[Transaction], refund_line_items: List[RefundLineItem], duties: List[Any], additional_fees: List[Any]) -> None:
        self.id = id
        self.admin_graphql_api_id = admin_graphql_api_id
        self.created_at = created_at
        self.note = note
        self.order_id = order_id
        self.processed_at = processed_at
        self.restock = restock
        self.total_additional_fees_set = total_additional_fees_set
        self.total_duties_set = total_duties_set
        self.user_id = user_id
        self.order_adjustments = order_adjustments
        self.transactions = transactions
        self.refund_line_items = refund_line_items
        self.duties = duties
        self.additional_fees = additional_fees


class ShippingLine:
    id: int
    carrier_identifier: None
    code: str
    discounted_price: str
    discounted_price_set: Set
    phone: None
    price: str
    price_set: Set
    requested_fulfillment_service_id: None
    source: str
    title: str
    tax_lines: List[Any]
    discount_allocations: List[Any]

    def __init__(self, id: int, carrier_identifier: None, code: str, discounted_price: str, discounted_price_set: Set, phone: None, price: str, price_set: Set, requested_fulfillment_service_id: None, source: str, title: str, tax_lines: List[Any], discount_allocations: List[Any]) -> None:
        self.id = id
        self.carrier_identifier = carrier_identifier
        self.code = code
        self.discounted_price = discounted_price
        self.discounted_price_set = discounted_price_set
        self.phone = phone
        self.price = price
        self.price_set = price_set
        self.requested_fulfillment_service_id = requested_fulfillment_service_id
        self.source = source
        self.title = title
        self.tax_lines = tax_lines
        self.discount_allocations = discount_allocations


class Order:
    id: int
    admin_graphql_api_id: str
    app_id: None
    browser_ip: str
    buyer_accepts_marketing: bool
    cancel_reason: None
    cancelled_at: None
    cart_token: str
    checkout_id: int
    checkout_token: str
    client_details: ClientDetails
    closed_at: None
    confirmation_number: None
    confirmed: bool
    contact_email: str
    created_at: datetime
    currency: Currency
    current_subtotal_price: str
    current_subtotal_price_set: Set
    current_total_additional_fees_set: None
    current_total_discounts: str
    current_total_discounts_set: Set
    current_total_duties_set: None
    current_total_price: str
    current_total_price_set: Set
    current_total_tax: str
    current_total_tax_set: Set
    customer_locale: None
    device_id: None
    discount_codes: List[DiscountCode]
    email: str
    estimated_taxes: bool
    financial_status: str
    fulfillment_status: None
    landing_site: str
    landing_site_ref: str
    location_id: None
    merchant_of_record_app_id: None
    name: str
    note: None
    note_attributes: List[NoteAttribute]
    number: int
    order_number: int
    order_status_url: str
    original_total_additional_fees_set: None
    original_total_duties_set: None
    payment_gateway_names: List[str]
    phone: str
    po_number: str
    presentment_currency: Currency
    processed_at: datetime
    reference: str
    referring_site: str
    source_identifier: str
    source_name: str
    source_url: None
    subtotal_price: str
    subtotal_price_set: Set
    tags: str
    tax_exempt: bool
    tax_lines: List[TaxLine]
    taxes_included: bool
    test: bool
    token: str
    total_discounts: str
    total_discounts_set: Set
    total_line_items_price: str
    total_line_items_price_set: Set
    total_outstanding: str
    total_price: str
    total_price_set: Set
    total_shipping_price_set: Set
    total_tax: str
    total_tax_set: Set
    total_tip_received: str
    total_weight: int
    updated_at: datetime
    user_id: None
    billing_address: Address
    customer: Customer
    discount_applications: List[DiscountApplication]
    fulfillments: List[Fulfillment]
    line_items: List[LineItem]
    payment_terms: None
    refunds: List[Refund]
    shipping_address: Address
    shipping_lines: List[ShippingLine]

    def __init__(self, id: int, admin_graphql_api_id: str, app_id: None, browser_ip: str, buyer_accepts_marketing: bool, cancel_reason: None, cancelled_at: None, cart_token: str, checkout_id: int, checkout_token: str, client_details: ClientDetails, closed_at: None, confirmation_number: None, confirmed: bool, contact_email: str, created_at: datetime, currency: Currency, current_subtotal_price: str, current_subtotal_price_set: Set, current_total_additional_fees_set: None, current_total_discounts: str, current_total_discounts_set: Set, current_total_duties_set: None, current_total_price: str, current_total_price_set: Set, current_total_tax: str, current_total_tax_set: Set, customer_locale: None, device_id: None, discount_codes: List[DiscountCode], email: str, estimated_taxes: bool, financial_status: str, fulfillment_status: None, landing_site: str, landing_site_ref: str, location_id: None, merchant_of_record_app_id: None, name: str, note: None, note_attributes: List[NoteAttribute], number: int, order_number: int, order_status_url: str, original_total_additional_fees_set: None, original_total_duties_set: None, payment_gateway_names: List[str], phone: str, po_number: str, presentment_currency: Currency, processed_at: datetime, reference: str, referring_site: str, source_identifier: str, source_name: str, source_url: None, subtotal_price: str, subtotal_price_set: Set, tags: str, tax_exempt: bool, tax_lines: List[TaxLine], taxes_included: bool, test: bool, token: str, total_discounts: str, total_discounts_set: Set, total_line_items_price: str, total_line_items_price_set: Set, total_outstanding: str, total_price: str, total_price_set: Set, total_shipping_price_set: Set, total_tax: str, total_tax_set: Set, total_tip_received: str, total_weight: int, updated_at: datetime, user_id: None, billing_address: Address, customer: Customer, discount_applications: List[DiscountApplication], fulfillments: List[Fulfillment], line_items: List[LineItem], payment_terms: None, refunds: List[Refund], shipping_address: Address, shipping_lines: List[ShippingLine]) -> None:
        self.id = id
        self.admin_graphql_api_id = admin_graphql_api_id
        self.app_id = app_id
        self.browser_ip = browser_ip
        self.buyer_accepts_marketing = buyer_accepts_marketing
        self.cancel_reason = cancel_reason
        self.cancelled_at = cancelled_at
        self.cart_token = cart_token
        self.checkout_id = checkout_id
        self.checkout_token = checkout_token
        self.client_details = client_details
        self.closed_at = closed_at
        self.confirmation_number = confirmation_number
        self.confirmed = confirmed
        self.contact_email = contact_email
        self.created_at = created_at
        self.currency = currency
        self.current_subtotal_price = current_subtotal_price
        self.current_subtotal_price_set = current_subtotal_price_set
        self.current_total_additional_fees_set = current_total_additional_fees_set
        self.current_total_discounts = current_total_discounts
        self.current_total_discounts_set = current_total_discounts_set
        self.current_total_duties_set = current_total_duties_set
        self.current_total_price = current_total_price
        self.current_total_price_set = current_total_price_set
        self.current_total_tax = current_total_tax
        self.current_total_tax_set = current_total_tax_set
        self.customer_locale = customer_locale
        self.device_id = device_id
        self.discount_codes = discount_codes
        self.email = email
        self.estimated_taxes = estimated_taxes
        self.financial_status = financial_status
        self.fulfillment_status = fulfillment_status
        self.landing_site = landing_site
        self.landing_site_ref = landing_site_ref
        self.location_id = location_id
        self.merchant_of_record_app_id = merchant_of_record_app_id
        self.name = name
        self.note = note
        self.note_attributes = note_attributes
        self.number = number
        self.order_number = order_number
        self.order_status_url = order_status_url
        self.original_total_additional_fees_set = original_total_additional_fees_set
        self.original_total_duties_set = original_total_duties_set
        self.payment_gateway_names = payment_gateway_names
        self.phone = phone
        self.po_number = po_number
        self.presentment_currency = presentment_currency
        self.processed_at = processed_at
        self.reference = reference
        self.referring_site = referring_site
        self.source_identifier = source_identifier
        self.source_name = source_name
        self.source_url = source_url
        self.subtotal_price = subtotal_price
        self.subtotal_price_set = subtotal_price_set
        self.tags = tags
        self.tax_exempt = tax_exempt
        self.tax_lines = tax_lines
        self.taxes_included = taxes_included
        self.test = test
        self.token = token
        self.total_discounts = total_discounts
        self.total_discounts_set = total_discounts_set
        self.total_line_items_price = total_line_items_price
        self.total_line_items_price_set = total_line_items_price_set
        self.total_outstanding = total_outstanding
        self.total_price = total_price
        self.total_price_set = total_price_set
        self.total_shipping_price_set = total_shipping_price_set
        self.total_tax = total_tax
        self.total_tax_set = total_tax_set
        self.total_tip_received = total_tip_received
        self.total_weight = total_weight
        self.updated_at = updated_at
        self.user_id = user_id
        self.billing_address = billing_address
        self.customer = customer
        self.discount_applications = discount_applications
        self.fulfillments = fulfillments
        self.line_items = line_items
        self.payment_terms = payment_terms
        self.refunds = refunds
        self.shipping_address = shipping_address
        self.shipping_lines = shipping_lines
