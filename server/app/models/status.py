import enum

class StatusType(enum.Enum):
    PENDING = 'pending',
    CONFIRMED = 'confirmed',
    CANCELLED = 'cancelled',
    DELIVERED = 'delivered',
    RETURNED = 'returned',
    COMPLETED = 'completed'