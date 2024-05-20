from typing import List
from typing import Dict
class WeightRange:
    minValue:int
    maxValue:int
    def __init(self,minValue:int,maxValue:int):
        self.minValue=minValue
        self.maxValue=maxValue
class ProductInventory:
    trackInventory:bool
    quantity: int
    inStock:bool
    inventoryStatus:str
    def __init(self,trackInventory:bool,quantity: int,inStock:bool,inventoryStatus:str):
        self.trackInventory=trackInventory
        self.quantity=quantity
        self.inStock=inStock
        self.inventoryStatus=inventoryStatus

class Formatted:
    price:int
    discountedPrice:str
    pricePerUnit:str
    def __init__(self, price:int,discountedPrice:str,pricePerUnit:str):
        self.price=price
        self.discountedPrice=discountedPrice
        self.pricePerUnit=pricePerUnit

class Price:
    currency:str
    price:int
    discountedPrice:int
    formatted:Formatted
    pricePerUnit:int
    def __init__(self,currency:str,price:int,discountedPrice:int,formatted:Formatted,pricePerUnit:int):
        self.currency=currency
        self.price=price
        self.discountedPrice=discountedPrice
        self.formatted=formatted
        self.pricePerUnit=pricePerUnit

class PriceData:
    currency:str
    price:int
    discountedPrice:int
    formatted:Formatted
    pricePerUnit:int
    def __init__(self,currency:str,price:int,discountedPrice:int,formatted:Formatted,pricePerUnit:int):
        self.currency=currency
        self.price=price
        self.discountedPrice=discountedPrice
        self.formatted=formatted
        self.pricePerUnit=pricePerUnit
class ConvertedPriceData:
    currency:str
    price:int
    discountedPrice:int
    formatted:Formatted
    pricePerUnit:int
    def __init(self,currency:str,price:int,discountedPrice:int,formatted:Formatted,pricePerUnit:int):
        self.currency=currency
        self.price=price
        self.discountedPrice=discountedPrice
        self.formatted=formatted
        self.pricePerUnit=pricePerUnit

class AdditionalInfoSection:
    title:str
    description:str
    def __init(self,title:str,description:str):
        self.title=title
        self.description=description

class PricePerUnitData:
    totalQuantity:int
    totalMeasurementUnit:str
    baseQuantity:int
    baseMeasurementUnit:str
    def __init__(self,totalQuantity:int,totalMeasurementUnit:str,baseQuantity:int,baseMeasurementUnit:str):
        self.totalQuantity=totalQuantity
        self.totalMeasurementUnit
        self.baseQuantity=baseQuantity
        self.baseMeasurementUnit=baseMeasurementUnit

class CostRange:
    minValue:int
    maxValue:int
    def __init__(self,minValue:int,maxValue:int):
        self.minValue=minValue
        self.maxValue=maxValue

class PriceRange:
    minValue:int
    maxValue:int
    def __init__(self,minValue:int,maxValue:int):
        self.minValue=minValue
        self.maxValue=maxValue

class CostAndProfitData:
    itemCost:int
    formattedItemCost:str
    profit:int
    formattedProfit:str
    profitMargin:int
    def __init__(self,itemCost:int,formattedItemCost:str,profit:int,formattedProfit:str,profitMargin:int):
        self.itemCost=itemCost
        self.formattedItemCost=formattedItemCost
        self.profit=profit
        self.formattedProfit=formattedProfit
        self.profitMargin=profitMargin

class Thumbnail:
    url:str
    width:int
    height:int
    format:str
    altText:str
    def __init__(self,url:str,width:int,height:int,format:str,altText:str):
        self.url:url
        self.width=width
        self.height=height
        self.format=format
        self.altText=altText
class Image:
    url:str
    width:int
    height: str
    format: str
    altText:str
    def __init__(self,url:str,width:int,height: str,format: str,altText:str):
        self.url=url
        self.width=width
        self.height=height
        self.format=format
        self.altText=altText

class MediaItemUrlAndSize:
    url:str
    width:int
    height:int
    format:str
    altText:str
    def __init__(self,url:str,width:int,height:int,format:str,altText:str):
        self.url=url
        self.width=width
        self.height=height
        self.format=format
        self.altText=altText

class Video:
    files:List[MediaItemUrlAndSize]
    stillFrameMediaId:str
    def __init__(self,files:List[MediaItemUrlAndSize],stillFrameMediaId:str):
        self.files=files
        self.stillFrameMediaId=stillFrameMediaId

class MainMedia:
    thumbnail:Thumbnail
    mediaType:str
    title:str
    id:str
    image:Image
    video:Video #one of select krna hai
    def __init__(self,thumbnail:Thumbnail,mediaType:str,title:str,id:str,image:Image):
        self.thumbnail=thumbnail
        self.mediaType=mediaType
        self.title=title
        self.id=id
        self.image:Image

class MediaItem:
    thumbnail:Thumbnail
    mediaType:str
    title:str
    id:str
    image:Image
    def __init__(self,thumbnail:Thumbnail,mediaType:str,title:str,id:str,image:Image):
        self.thumbnail=thumbnail
        self.mediaType=mediaType
        self.title=title
        self.id=id
        self.image=image
class Media:
    mainMedia:MainMedia
    items:List[MediaItem]

class CustomTextFields:
    title:str
    maxLength:int
    mandatory:bool
    def __init__(self,title:str,maxLength:int,mandatory:bool):
        self.title=title
        self.maxLength=maxLength
        self.mandatory=mandatory
class Ribbons:
    text:str
    def __init__(self,text:str):
        self.text=text
class Choices:
    value:str
    description:str
    media:Media
    inStock:bool
    visible:bool
    def __init__(self,value:str,description:str,media:Media,inStock:bool,visible:bool):
        self.value=value
        self.description=description
        self.media=media
        self.inStock=inStock
        self.visible:visible

class ProductOptions:
    optionType:str
    name:str
    choices:Choices
    def __init__(self,optionType:str,name:str,choices:Choices):
        self.optionType=optionType
        self.name=name
        self.choices=choices
        
class ProductPageUrl:
    base:str
    path:str
    def __init__(self,base:str,path:str):
        self.base=base
        self.path=path
class Discount:
    type:str
    value:int
    def __init__(self,type:str,value:int):
        self.type=type
        self.value=value
class Keywords:
    term:str
    isMain:bool
    def __init__(self,term:str,isMain:bool):
        self.term=term
        self.isMain=isMain
class Props:
    def __init__(self, name=None, content=None, rel=None, href=None):
        self.name = name
        self.content = content
        self.rel = rel
        self.href = href
class Meta:
    def __init__(self, height=None, width=None):
        self.height = height
        self.width = width

class Tags:
    type:str
    props:Props
    meta:Meta
    children:str
    custom:bool
    disabled:bool
    def __init__(self, type: str, props: Props, meta: Meta, children: str, custom: bool, disabled: bool):
        self.type = type
        self.props = props
        self.meta = meta
        self.children = children
        self.custom = custom
        self.disabled = disabled

class Settings:
    preventAutoRedirect:bool
    keywords:List[Keywords]
    def __init__(self,preventAutoRedirect:bool, keywords:List[Keywords]):
        self.preventAutoRedirect=preventAutoRedirect
        self.keywords=keywords
class SeoData:
    tags:Tags
    settings:Settings
    def __init__(self,tags:Tags,settings:Settings):
        self.tags:tags
        self.settings:settings

class Stock:
    trackQuantity:bool
    quantity:int
    inStock:bool
    def __init__(self,trackQuantity:bool,quantity:int,inStock:bool):
        self.trackQuantity:trackQuantity
        self.quantity:quantity
        self.inStock:inStock
class Variant:
    priceData:PriceData
    convertedPriceData:ConvertedPriceData
    costAndProfitData:CostAndProfitData
    weight:int
    sku:str
    visible:bool
    def __init__(self,priceData:PriceData,convertedPriceData:ConvertedPriceData,costAndProfitData:CostAndProfitData,weight:int,sku:str,visible:bool):
        self.priceData:priceData
        self.convertedPriceData=convertedPriceData
        self.costAndProfitData=costAndProfitData
        self.weight=weight
        self.sku=sku
        self.visible=visible

class Variants:
    id:str
    choices: Dict[str, str]
    variant:Variant
    stock:Stock
    def __init__(self,id:str,choices:int,variant:Variant,stock:Stock):
        self.id=id
        self.choices=choices
        self.variant=variant
        self.stock=stock
class Product:
    id: str
    name: str
    slug: str
    visible : bool
    productType : str
    description: str
    sku : str
    weight : int
    weightRange:WeightRange
    stock:ProductInventory
    price:Price
    priceData=PriceData
    convertedPriceData:ConvertedPriceData
    priceRange:PriceRange
    costAndProfitData:CostAndProfitData
    costRange:CostRange
    pricePerUnitData:PricePerUnitData
    additionalInfoSections:List[AdditionalInfoSection]
    ribbons:List[Ribbons]
    media:Media
    customTextFields:CustomTextFields
    manageVariants:bool
    productPageUrl:ProductPageUrl
    numericId:int
    inventoryItemId:str
    discount:Discount #kuch kuch change krna hai
    collectionIds:List[str]
    variants:List[Variants]
    lastUpdated:str
    createdDate=str
    seoData:SeoData
    ribbon:str
    brand:str

    def __init__(
        self,
        id: str,
        name: str,
        slug: str,
        visible: bool,
        productType: str,
        description: str,
        sku: str,
        weight: int,
        weightRange: WeightRange,
        stock: ProductInventory,
        price: Price,
        priceData: PriceData,
        convertedPriceData: ConvertedPriceData,
        priceRange: PriceRange,
        costAndProfitData: CostAndProfitData,
        costRange: CostRange,
        pricePerUnitData: PricePerUnitData,
        additionalInfoSections: List[AdditionalInfoSection],
        ribbons: List[Ribbons],
        media: Media,
        customTextFields: CustomTextFields,
        manageVariants: bool,
        productPageUrl: ProductPageUrl,
        numericId: int,
        inventoryItemId: str,
        discount: Discount,
        collectionIds: List[str],
        variants: List[Variants],
        lastUpdated: str,
        createdDate: str,
        seoData: SeoData,
        ribbon: str,
        brand: str
    ):
        self.id = id
        self.name = name
        self.slug = slug
        self.visible = visible
        self.productType = productType
        self.description = description
        self.sku = sku
        self.weight = weight
        self.weightRange = weightRange
        self.stock = stock
        self.price = price
        self.priceData = priceData
        self.convertedPriceData = convertedPriceData
        self.priceRange = priceRange
        self.costAndProfitData = costAndProfitData
        self.costRange = costRange
        self.pricePerUnitData = pricePerUnitData
        self.additionalInfoSections = additionalInfoSections
        self.ribbons = ribbons
        self.media = media
        self.customTextFields = customTextFields
        self.manageVariants = manageVariants
        self.productPageUrl = productPageUrl
        self.numericId = numericId
        self.inventoryItemId = inventoryItemId
        self.discount = discount
        self.collectionIds = collectionIds
        self.variants = variants
        self.lastUpdated = lastUpdated
        self.createdDate = createdDate
        self.seoData = seoData
        self.ribbon = ribbon
        self.brand = brand

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "visible": self.visible,
            "productType": self.productType,
            "description": self.description,
            "sku": self.sku,
            "weight": self.weight,
            "weightRange": self.weightRange,
            "stock": self.stock,
            "price": self.price,
            "priceData": self.priceData,
            "convertedPriceData": self.convertedPriceData,
            "priceRange": self.priceRange,
            "costAndProfitData": self.costAndProfitData,
            "costRange": self.costRange,
            "pricePerUnitData": self.pricePerUnitData,
            "additionalInfoSections": self.additionalInfoSections,
            "ribbons": self.ribbons,
            "media": self.media,
            "customTextFields": self.customTextFields,
            "manageVariants": self.manageVariants,
            "productPageUrl": self.productPageUrl,
            "numericId": self.numericId,
            "inventoryItemId": self.inventoryItemId,
            "discount": self.discount,
            "collectionIds": self.collectionIds,
            "variants": self.variants,
            "lastUpdated": self.lastUpdated,
            "createdDate": self.createdDate,
            "seoData": self.seoData,
            "ribbon": self.ribbon,
            "brand": self.brand
        }
