from typing import List
from uuid import UUID


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
    media_type: str
    title: str
    image: Image
    id: str

    def __init__(self, thumbnail: Image, media_type: str, title: str, image: Image, id: str) -> None:
        self.thumbnail = thumbnail
        self.media_type = media_type
        self.title = title
        self.image = image
        self.id = id


class Media:
    main_media: MainMedia
    items: List[MainMedia]

    def __init__(self, main_media: MainMedia, items: List[MainMedia]) -> None:
        self.main_media = main_media
        self.items = items


class Collection:
    id: UUID
    name: str
    slug: str
    visible: bool
    description: str
    media: Media
    numberOfProducts: int

    def __init__(self, id: UUID, name: str, slug: str, visible: bool, description: str, media: Media, numberOfProducts: int) -> None:
        self.id = id
        self.name = name
        self.slug = slug
        self.visible = visible
        self.description = description
        self.media = media
        self.numberOfProducts = numberOfProducts
    
    

