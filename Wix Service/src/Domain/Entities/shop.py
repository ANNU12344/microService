from datetime import datetime
from typing import List
class Categories:
    primary:str
    secondary:List[str]
    businessTermID:str
    def __init__(self, primary:str, secondary:List[str], businessTermID:str) -> None:
        self.primary = primary
        self.secondary = secondary
        self.businessTermID = businessTermID

class Local:
    languageCode:str
    country:str
    def __init__(self,languageCode:str,country:str)->None:
        self.languageCode=languageCode
        self.country=country

class Hint:
    text:str
    placement:str
    def __init__(self,text:str,placement:str)->None:
        self.text=text
        self.placement=placement


class Coordinator:
    latitude:int
    longitude:int
    def __init__(self,latitude:int,longitude:int)->None:
        self.latitude=latitude
        self.longitude=longitude


class Address:
    street:str
    city:str
    country:str
    state:str
    zip:str
    hint:Hint
    isPhysical:bool
    googleFormattedAddress:str
    streetNumber:str
    apartmentNumber:str
    coordinates:Coordinator
    def __init__(self,street:str,city:str,country:str,state:str,zip:str,hint:Hint,isPhysical:bool,googleFormattedAddress:str,streetNumber:str,apartmentNumber:str,coordinates:Coordinator)->None:
        self.street=street
        self.city=city
        self.country=country
        self.state=state
        self.zip=zip
        self.hint=hint
        self.isPhysical=isPhysical
        self.googleFormattedAddress=googleFormattedAddress
        self.streetNumber=streetNumber
        self.apartmentNumber=apartmentNumber
        self.coordinates=coordinates


class TimePeriod:
    openDay:str
    openTime:str
    closeDay:str
    closeTime:str
    def __init__(self, openDay: str, openTime: str, closeDay: str, closeTime: str):
        self.openDay = openDay
        self.openTime = openTime
        self.closeDay = closeDay
        self.closeTime = closeTime


class SpecialHourPeriod:
    startDate:str
    endDate:str
    isClosed:bool
    comment:str
    def __init__(self, startDate: str, endDate: str, isClosed: bool, comment: str):
        self.startDate = startDate
        self.endDate = endDate
        self.isClosed = isClosed
        self.comment = comment

class BusinessSchedule:
    periods:List[TimePeriod]
    specialHourPeriod:List[SpecialHourPeriod]
    def __init__(self, periods: List[TimePeriod], specialHourPeriod: List[SpecialHourPeriod]):
        self.periods = periods
        self.specialHourPeriod = specialHourPeriod

class Locale:
    languageCode:str
    country:str
    def __init__(self, languageCode: str, country: str):
        self.languageCode = languageCode
        self.country = country


class SupportedLanguage:
    langaugeCode:str
    locale:Locale
    isPrimary:bool
    countryCode:str
    resolutionMethod:str
    def __init__(self, langaugeCode: str, locale: Locale, isPrimary: bool, countryCode: str, resolutionMethod: str):
        self.langaugeCode = langaugeCode
        self.locale = locale
        self.isPrimary = isPrimary
        self.countryCode = countryCode
        self.resolutionMethod = resolutionMethod



class Multilingual:
    supportedLanguage:List[SupportedLanguage]
    autoRedirect:bool
    def __init__(self, supportedLanguage: List[SupportedLanguage], autoRedirect: bool):
        self.supportedLanguage = supportedLanguage
        self.autoRedirect = autoRedirect


class ConsentPolicy:
    essential:bool
    functional:bool
    analytics:bool
    advertising:bool
    dataToThirdParty:bool
    def __init__(self, essential: bool, functional: bool, analytics: bool, advertising: bool, dataToThirdParty: bool):
        self.essential = essential
        self.functional = functional
        self.analytics = analytics
        self.advertising = advertising
        self.dataToThirdParty = dataToThirdParty

class Properties:
    categories:Categories
    local:Local
    language: str
    paymentCurrency: str
    timeZone: str
    email: str
    phone: str
    fax: str
    address:Address
    siteDisplayName: str
    businessName: str
    logo: str
    description: str
    businessSchedule:BusinessSchedule
    multilingual:Multilingual
    consentPolicy:ConsentPolicy
    businessConfig: str
    externalSiteUrl: str
    trackClicksAnalytics: bool
    def __init__(
        self,
        categories: Categories,
        local: Local,
        language: str,
        paymentCurrency: str,
        timeZone: str,
        email: str,
        phone: str,
        fax: str,
        address: Address,
        siteDisplayName: str,
        businessName: str,
        logo: str,
        description: str,
        businessSchedule: BusinessSchedule,
        multilingual: Multilingual,
        consentPolicy: ConsentPolicy,
        businessConfig: str,
        externalSiteUrl: str,
        trackClicksAnalytics: bool
    ):
        self.categories = categories
        self.local = local
        self.language = language
        self.paymentCurrency = paymentCurrency
        self.timeZone = timeZone
        self.email = email
        self.phone = phone
        self.fax = fax
        self.address = address
        self.siteDisplayName = siteDisplayName
        self.businessName = businessName
        self.logo = logo
        self.description = description
        self.businessSchedule = businessSchedule
        self.multilingual = multilingual
        self.consentPolicy = consentPolicy
        self.businessConfig = businessConfig
        self.externalSiteUrl = externalSiteUrl
        self.trackClicksAnalytics = trackClicksAnalytics

    

class Site:
    properties:Properties
    def __init__(self, properties: Properties):
        self.properties = properties

    
    def to_dict(self) -> dict:
        return {
            "siteDisplayName": self.properties.siteDisplayName,
            "businessName": self.properties.businessName,
            "description": self.properties.description,
            "logo": self.properties.logo
            }
            