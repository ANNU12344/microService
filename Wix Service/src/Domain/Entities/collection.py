from typing import Optional, List
class Image:
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
class Thumbnail:
    url:str
    width:int
    height:int
    format:str
    altText:str
    def __init__(self,url:str,width:int,height:int, format:str,altText:str):
        self.url=url
        self.width=width
        self.height=height
        self.format=format
        self.altText=altText
class MainMedia:
    thumbnail:Thumbnail
    mediaType:str
    title:str
    id:str
    image:Image
    def __init__(self,thumbnail:Thumbnail,mediaType:str,title:str,id:str, image:Image):
        self.thumbnail=thumbnail
        self.mediaType=mediaType
        self.title=title
        self.id=id
        self.image=image


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
    def __init__(self,mainMedia:MainMedia,items:List[MediaItem]):
        self.mainMedia=mainMedia
        self.items=items
class Collection:
    id:str
    name:str
    media:Optional[Media]
    numberOfPrducts:int
    decription:str
    slug:str
    visible:bool
    def __init__(self,id:str,name:str,media:Media,numberOfPrducts:int,decription:str,slug:str,visible:bool):
        self.id=id
        self.name=name
        self.media=media
        self:numberOfPrducts
        self.decription=decription
        self.slug=slug
        self.visible=visible
        