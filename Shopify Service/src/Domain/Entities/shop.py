
from datetime import datetime
from typing import List


class Shop:
    id: int
    name: str
    email: str
    domain: str
    province: str
    country: str
    address1: str
    zip: int
    city: str
    source: None
    phone: int
    latitude: float
    longitude: float
    primary_locale: str
    address2: str
    created_at: datetime
    updated_at: datetime
    country_code: str
    country_name: str
    currency: str
    customer_email: str
    timezone: str
    iana_timezone: str
    shop_owner: str
    money_format: str
    money_with_currency_format: str
    weight_unit: str
    province_code: str
    taxes_included: None
    auto_configure_tax_inclusivity: None
    tax_shipping: None
    county_taxes: bool
    plan_display_name: str
    plan_name: str
    has_discounts: bool
    has_gift_cards: bool
    myshopify_domain: str
    google_apps_domain: None
    google_apps_login_enabled: None
    money_in_emails_format: str
    money_with_currency_in_emails_format: str
    eligible_for_payments: bool
    requires_extra_payments_agreement: bool
    password_enabled: bool
    has_storefront: bool
    finances: bool
    primary_location_id: int
    checkout_api_supported: bool
    multi_location_enabled: bool
    setup_required: bool
    pre_launch_enabled: bool
    enabled_presentment_currencies: List[str]
    transactional_sms_disabled: bool
    marketing_sms_consent_enabled_at_checkout: bool

    def __init__(self, id: int, name: str, email: str, domain: str, province: str, country: str, address1: str, zip: int, city: str, source: None, phone: int, latitude: float, longitude: float, primary_locale: str, address2: str, created_at: datetime, updated_at: datetime, country_code: str, country_name: str, currency: str, customer_email: str, timezone: str, iana_timezone: str, shop_owner: str, money_format: str, money_with_currency_format: str, weight_unit: str, province_code: str, taxes_included: None, auto_configure_tax_inclusivity: None, tax_shipping: None, county_taxes: bool, plan_display_name: str, plan_name: str, has_discounts: bool, has_gift_cards: bool, myshopify_domain: str, google_apps_domain: None, google_apps_login_enabled: None, money_in_emails_format: str, money_with_currency_in_emails_format: str, eligible_for_payments: bool, requires_extra_payments_agreement: bool, password_enabled: bool, has_storefront: bool, finances: bool, primary_location_id: int, checkout_api_supported: bool, multi_location_enabled: bool, setup_required: bool, pre_launch_enabled: bool, enabled_presentment_currencies: List[str], transactional_sms_disabled: bool, marketing_sms_consent_enabled_at_checkout: bool) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.domain = domain
        self.province = province
        self.country = country
        self.address1 = address1
        self.zip = zip
        self.city = city
        self.source = source
        self.phone = phone
        self.latitude = latitude
        self.longitude = longitude
        self.primary_locale = primary_locale
        self.address2 = address2
        self.created_at = created_at
        self.updated_at = updated_at
        self.country_code = country_code
        self.country_name = country_name
        self.currency = currency
        self.customer_email = customer_email
        self.timezone = timezone
        self.iana_timezone = iana_timezone
        self.shop_owner = shop_owner
        self.money_format = money_format
        self.money_with_currency_format = money_with_currency_format
        self.weight_unit = weight_unit
        self.province_code = province_code
        self.taxes_included = taxes_included
        self.auto_configure_tax_inclusivity = auto_configure_tax_inclusivity
        self.tax_shipping = tax_shipping
        self.county_taxes = county_taxes
        self.plan_display_name = plan_display_name
        self.plan_name = plan_name
        self.has_discounts = has_discounts
        self.has_gift_cards = has_gift_cards
        self.myshopify_domain = myshopify_domain
        self.google_apps_domain = google_apps_domain
        self.google_apps_login_enabled = google_apps_login_enabled
        self.money_in_emails_format = money_in_emails_format
        self.money_with_currency_in_emails_format = money_with_currency_in_emails_format
        self.eligible_for_payments = eligible_for_payments
        self.requires_extra_payments_agreement = requires_extra_payments_agreement
        self.password_enabled = password_enabled
        self.has_storefront = has_storefront
        self.finances = finances
        self.primary_location_id = primary_location_id
        self.checkout_api_supported = checkout_api_supported
        self.multi_location_enabled = multi_location_enabled
        self.setup_required = setup_required
        self.pre_launch_enabled = pre_launch_enabled
        self.enabled_presentment_currencies = enabled_presentment_currencies
        self.transactional_sms_disabled = transactional_sms_disabled
        self.marketing_sms_consent_enabled_at_checkout = marketing_sms_consent_enabled_at_checkout

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "domain": self.domain
            }