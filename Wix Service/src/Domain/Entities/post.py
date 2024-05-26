from uuid import UUID
from datetime import datetime
from typing import List


class URL:
    base: str
    path: str

    def __init__(self, base: str, path: str) -> None:
        self.base = base
        self.path = path


class Post:
    id: UUID
    title: str
    slug: str
    url: URL
    firstPublishedDate: datetime
    lastPublishedDate: datetime
    featured: bool
    pinned: bool
    categoryIds: List[str]
    memberId: str
    hashtags: List[str]
    commentingEnabled: bool
    minutesToRead: int
    tagIds: List[str]
    pricingPlanIds: List[str]
    relatedPostIds: List[UUID]
    language: str
    translationId: UUID

    def __init__(self, id: UUID, title: str, slug: str, url: URL, firstPublishedDate: datetime, lastPublishedDate: datetime, featured: bool, pinned: bool, categoryIds: List[str], memberId: str, hashtags: List[str], commentingEnabled: bool, minutesToRead: int, tagIds: List[str], pricingPlanIds: List[str], relatedPostIds: List[UUID], language: str, translationId: UUID) -> None:
        self.id = id
        self.title = title
        self.slug = slug
        self.url = url
        self.firstPublishedDate = firstPublishedDate
        self.lastPublishedDate = lastPublishedDate
        self.featured = featured
        self.pinned = pinned
        self.categoryIds = categoryIds
        self.memberId = memberId
        self.hashtags = hashtags
        self.commentingEnabled = commentingEnabled
        self.minutesToRead = minutesToRead
        self.tagIds = tagIds
        self.pricingPlanIds = pricingPlanIds
        self.relatedPostIds = relatedPostIds
        self.language = language
        self.translationId = translationId

