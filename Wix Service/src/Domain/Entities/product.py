from enum import Enum
from typing import List, Any, Optional
from uuid import UUID
from datetime import datetime
class AdditionalInfoSection:
    title: str
    description: str

    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description


class Currency(Enum):
    USD = "USD"


class DiscountedPrice(Enum):
    THE_3000 = "$30.00"
    THE_6000 = "$60.00"
    THE_6500 = "$65.00"


class Price(Enum):
    THE_3500 = "$35.00"
    THE_6500 = "$65.00"
    THE_7000 = "$70.00"


class PricePerUnit(Enum):
    THE_012 = "$0.12"
    THE_024 = "$0.24"
    THE_026 = "$0.26"


class Formatted:
    price: Price
    discountedPrice: DiscountedPrice
    pricePerUnit: PricePerUnit

    def __init__(self, price: Price, discountedPrice: DiscountedPrice, pricePerUnit: PricePerUnit) -> None:
        self.price = price
        self.discountedPrice = discountedPrice
        self.pricePerUnit = pricePerUnit


class ConvertedPriceData:
    currency: Currency
    price: int
    discountedPrice: int
    formatted: Formatted
    pricePerUnit: float

    def __init__(self, currency: Currency, price: int, discountedPrice: int, formatted: Formatted, pricePerUnit: float) -> None:
        self.currency = currency
        self.price = price
        self.discountedPrice = discountedPrice
        self.formatted = formatted
        self.pricePerUnit = pricePerUnit


class Range:
    minValue: float
    maxValue: int

    def __init__(self, minValue: float, maxValue: int) -> None:
        self.minValue = minValue
        self.maxValue = maxValue


class CustomTextField:
    title: str
    maxLength: int
    mandatory: bool

    def __init__(self, title: str, maxLength: int, mandatory: bool) -> None:
        self.title = title
        self.maxLength = maxLength
        self.mandatory = mandatory


class Discount:
    type: str
    value: int

    def __init__(self, type: str, value: int) -> None:
        self.type = type
        self.value = value


class Image:
    url: str
    width: int
    height: int

    def __init__(self, url: str, width: int, height: int) -> None:
        self.url = url
        self.width = width
        self.height = height


class MainMedia:
    thumbnail: Image
    mediaType: str
    title: str
    image: Image
    id: str

    def __init__(self, thumbnail: Image, mediaType: str, title: str, image: Image, id: str) -> None:
        self.thumbnail = thumbnail
        self.mediaType = mediaType
        self.title = title
        self.image = image
        self.id = id


class ProductMedia:
    mainMedia: MainMedia
    items: List[MainMedia]

    def __init__(self, mediaMedia: MainMedia, items: List[MainMedia]) -> None:
        self.mediaMedia = mediaMedia
        self.items = items


class PricePerUnitData:
    totalQuantity: int
    totalMeasurementUnit: str
    baseQuantity: int
    baseMeasurementUnit: str

    def __init__(self, totalQuantity: int, totalMeasurementUnit: str, baseQuantity: int, baseMeasurementUnit: str) -> None:
        self.totalQuantity = totalQuantity
        self.totalMeasurementUnit = totalMeasurementUnit
        self.baseQuantity = baseQuantity
        self.baseMeasurementUnit = baseMeasurementUnit


class ChoiceMedia:
    items: List[Any]

    def __init__(self, items: List[Any]) -> None:
        self.items = items


class Choice:
    value: str
    description: str
    media: Optional[ChoiceMedia]
    inStock: bool
    visible: bool

    def __init__(self, value: str, description: str, media: Optional[ChoiceMedia], inStock: bool, visible: bool) -> None:
        self.value = value
        self.description = description
        self.media = media
        self.inStock = inStock
        self.visible = visible


class ProductOption:
    optionType: str
    name: str
    choices: List[Choice]

    def __init__(self, optionType: str, name: str, choices: List[Choice]) -> None:
        self.optionType = optionType
        self.name = name
        self.choices = choices


class ProductPageURL:
    base: str
    path: str

    def __init__(self, base: str, path: str) -> None:
        self.base = base
        self.path = path


class Ribbon:
    text: str

    def __init__(self, text: str) -> None:
        self.text = text


class Props:
    name: str
    content: str

    def __init__(self, name: str, content: str) -> None:
        self.name = name
        self.content = content


class Tag:
    type: str
    children: str
    custom: bool
    disabled: bool
    props: Optional[Props]

    def __init__(self, type: str, children: str, custom: bool, disabled: bool, props: Optional[Props]) -> None:
        self.type = type
        self.children = children
        self.custom = custom
        self.disabled = disabled
        self.props = props


class SEOData:
    tags: List[Tag]

    def __init__(self, tags: List[Tag]) -> None:
        self.tags = tags


class Stock:
    trackInventory: bool
    inStock: bool
    inventoryStatus: str

    def __init__(self, trackInventory: bool, inStock: bool, inventoryStatus: str) -> None:
        self.trackInventory = trackInventory
        self.inStock = inStock
        self.inventoryStatus = inventoryStatus


class Choices:
    weight: str
    groundFor: str

    def __init__(self, weight: str, groundFor: str) -> None:
        self.weight = weight
        self.groundFor = groundFor


class CostAndProfitData:
    itemCost: int
    formatted_itemCost: str
    profit: int
    formattedProfit: str
    profitMargin: float

    def __init__(self, itemCost: int, formatted_itemCost: str, profit: int, formattedProfit: str, profitMargin: float) -> None:
        self.itemCost = itemCost
        self.formatted_itemCost = formatted_itemCost
        self.profit = profit
        self.formattedProfit = formattedProfit
        self.profitMargin = profitMargin


class VariantVariant:
    priceData: ConvertedPriceData
    convertedPriceData: ConvertedPriceData
    costAndProfitData: CostAndProfitData
    weight: float
    sku: int
    visible: bool

    def __init__(self, priceData: ConvertedPriceData, convertedPriceData: ConvertedPriceData, costAndProfitData: CostAndProfitData, weight: float, sku: int, visible: bool) -> None:
        self.priceData = priceData
        self.convertedPriceData = convertedPriceData
        self.costAndProfitData = costAndProfitData
        self.weight = weight
        self.sku = sku
        self.visible = visible


class VariantElement:
    id: UUID
    choices: Choices
    variant: VariantVariant

    def __init__(self, id: UUID, choices: Choices, variant: VariantVariant) -> None:
        self.id = id
        self.choices = choices
        self.variant = variant


class Product:
    id: UUID
    name: str
    slug: str
    visible: bool
    productType: str
    description: str
    stock: Stock
    weightRange: Range
    price: ConvertedPriceData
    priceData: ConvertedPriceData
    convertedPriceData: ConvertedPriceData
    priceRange: Range
    costRange: Range
    # pricePerUnitData: PricePerUnitData
    additionalInfoSections: List[AdditionalInfoSection]
    ribbons: List[Ribbon]
    media: ProductMedia
    customTextFields: List[CustomTextField]
    manageVariants: bool
    productOptions: List[ProductOption]
    productPageUrl: ProductPageURL
    numericId: str
    inventoryItemId: UUID
    discount: Discount
    collectionIds: List[str]
    variants: List[VariantElement]
    lastUpdated: datetime
    createdDate: datetime
    # seoData: SEOData
    ribbon: str
    # brand: str

    def __init__(self, id: UUID, name: str, slug: str, visible: bool, productType: str, description: str, stock: Stock, weightRange: Range, price: ConvertedPriceData, priceData: ConvertedPriceData, convertedPriceData: ConvertedPriceData, priceRange: Range, costRange: Range, additionalInfoSections: List[AdditionalInfoSection], ribbons: List[Ribbon], media: ProductMedia, customTextFields: List[CustomTextField], manageVariants: bool, productOptions: List[ProductOption], productPageUrl: ProductPageURL, numericId: str, inventoryItemId: UUID, discount: Discount, collectionIds: List[str], variants: List[VariantElement], lastUpdated: datetime, createdDate: datetime, ribbon: str) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.visible = visible
        self.product_type = productType
        self.description = description
        self.stock = stock
        self.weight_range = weightRange
        self.price = price
        self.priceData = priceData
        self.convertedPriceData = convertedPriceData
        self.priceRange = priceRange
        self.costRange= costRange
        # self.pricePerUnitData = pricePerUnitData
        self.additionalInfoSections = additionalInfoSections
        self.ribbons = ribbons
        self.media = media
        self.customTextFields= customTextFields
        self.manageVariants = manageVariants
        self.productOptions = productOptions
        self.productPageUrl = productPageUrl
        self.numericId = numericId
        self.inventoryItemId = inventoryItemId
        self.discount = discount
        self.collectionIds = collectionIds
        self.variants = variants
        self.lastUpdated = lastUpdated
        self.createdDate = createdDate
        # self.seoData = seoData
        self.ribbon = ribbon
        # self.brand = brand


