import enum

class RoleType(enum.Enum):
    ADMIN = 'admin'
    MARTISAN = 'martisan'
    DEALER = 'dealer'

class StatusType(enum.Enum):
    PENDING = 'pending',
    CONFIRMED = 'confirmed',
    CANCELLED = 'cancelled',
    DELIVERED = 'delivered',
    RETURNED = 'returned',
    COMPLETED = 'completed'

class CategoryType(enum.Enum):
    HARD = "Hardwood"
    SPC = "SPC"
    ENG = "Engineered"

class ShippingType(enum.Enum):
    PICKUP = 'pickup'
    DELIVERY = 'delivery'