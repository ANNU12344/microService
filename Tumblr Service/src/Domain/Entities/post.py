from typing import Optional, List
class Post:
    def __init__(self, post_type: str, state: Optional[str] = "published", tags: Optional[str] = None,
                 tweet: Optional[str] = None, date: Optional[str] = None, format: Optional[str] = "html"):
        self.type = post_type
        self.state = state
        self.tags = tags
        self.tweet = tweet
        self.date = date
        self.format = format

class TextPost(Post):
    def __init__(self, title: Optional[str] = None, body: str = "", **kwargs):
        super().__init__("text", **kwargs)
        self.title = title
        self.body = body

class PhotoPost(Post):
    def __init__(self, caption: Optional[str] = None, link: Optional[str] = None, source: str = "",
                 data: Optional[List[str]] = None, data64: Optional[str] = None, **kwargs):
        super().__init__("photo", **kwargs)
        self.caption = caption
        self.link = link
        self.source = source
        self.data = data
        self.data64 = data64

class QuotePost(Post):
    def __init__(self, quote: str = "", source: Optional[str] = None, **kwargs):
        super().__init__("quote", **kwargs)
        self.quote = quote
        self.source = source

class LinkPost(Post):
    def __init__(self, title: Optional[str] = None, url: str = "", description: Optional[str] = None,
                 thumbnail: Optional[str] = None, excerpt: Optional[str] = None, author: Optional[str] = None, **kwargs):
        super().__init__("link", **kwargs)
        self.title = title
        self.url = url
        self.description = description
        self.thumbnail = thumbnail
        self.excerpt = excerpt
        self.author = author

class ChatPost(Post):
    def __init__(self, title: Optional[str] = None, conversation: str = "", **kwargs):
        super().__init__("chat", **kwargs)
        self.title = title
        self.conversation = conversation

class AudioPost(Post):
    def __init__(self, caption: Optional[str] = None, external_url: Optional[str] = None,
                 data: Optional[str] = None, **kwargs):
        super().__init__("audio", **kwargs)
        self.caption = caption
        self.external_url = external_url
        self.data = data

class VideoPost(Post):
    def __init__(self, caption: Optional[str] = None, embed: Optional[str] = None,
                 data: Optional[str] = None, **kwargs):
        super().__init__("video", **kwargs)
        self.caption = caption
        self.embed = embed
        self.data = data

