class Client:
    def __init__(self, db):
        self.client = db
        
    def create_all(self):
        self.client.create_all()
    
    def add_all(self, items):
        self.client.session.add_all(items)
        self.client.session.commit()
    
    def drop_all(self):
        self.client.drop_all()
    
    def get_item_by_id(self, table_name, item_id):
        table = getattr(self.client.Model.metadata.tables, table_name)
        item = table.query.get(item_id)
        return item
    
    def get_all_items(self, table_name):
        table = getattr(self.client.Model.metadata.tables, table_name)
        items = table.query.all()
        return items
    
    def add(self, table_name, data):
        table = getattr(self.client.Model.metadata.tables, table_name)
        item = table(**data)
        self.client.session.add(item)
        self.client.session.commit()
    
    def update_item_by_id(self, table_name, item_id, field, value):
        table = getattr(self.client.Model.metadata.tables, table_name)
        item = table.query.get(item_id)
        setattr(item, field, value)
        self.client.session.commit()

    def delete_item_by_id(self, table_name, item_id):
        table = getattr(self.client.Model.metadata.tables, table_name)
        item = table.query.get(item_id)
        self.client.session.delete(item)
        self.client.session.commit()

    def is_table_empty(self, table_name):
        table = getattr(self.client.Model.metadata.tables, table_name)
        return table.query.count() == 0

