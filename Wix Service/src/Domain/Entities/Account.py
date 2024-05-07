class Account:
    def __init__(self, id, contactId, memberId, points, latestTransaction, rewardAvailable, createdDate, updatedDate, revision):
        self.id = id
        self.contactId = contactId
        self.memberId = memberId
        self.points = points
        self.latestTransaction = latestTransaction
        self.rewardAvailable = rewardAvailable
        self.createdDate = createdDate
        self.updatedDate = updatedDate
        self.revision = revision

class Points:
    def __init__(self, balance, earned, redeemed, adjusted):
        self.balance = balance
        self.earned = earned
        self.redeemed = redeemed
        self.adjusted = adjusted

class LatestTransaction:
    def __init__(self, id, amount, type, description, createdDate, rewardId, appId, idempotencyKey):
        self.id = id
        self.amount = amount
        self.type = type
        self.description = description
        self.createdDate = createdDate
        self.rewardId = rewardId
        self.appId = appId
        self.idempotencyKey = idempotencyKey