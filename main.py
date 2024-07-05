items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


class BaseError(KeyError):
    message = "Нет итема с таким индексом"

    def __str__(self) -> str:
        return self.message


class TreeStore:
    def __init__(self, items: list[dict]):
        self.tree = {}
        for item in items:
            id = item['id']
            parent = item['parent']
            self.tree[id] = {'parent': item['parent'],
                             'children': list()}
            if 'type' in item.keys():
                self.tree[id]['type'] = item['type']
            if parent in self.tree:
                self.tree[parent]['children'].append(item)

    def getAll(self):
        return self.tree

    def getItem(self, id: int):
        try:
            item = self.tree[id]
            return {'id': id, 'parent': item.get('parent', None), 'type': item.get('type', None)}
        except KeyError:
            raise BaseError()

    def getChildren(self, parent_id: int):
        try:
            return self.tree[parent_id]['children']
        except KeyError:
            raise BaseError()

    def getAllParents(self, id: int):
        try:
            parent_id = self.getItem(id)['parent']
            parents = []
            while isinstance(parent_id, int):
                parent = self.getItem(parent_id)
                parents.append(parent)
                parent_id = parent["parent"]
                return parents
        except KeyError:
            raise BaseError()


ts = TreeStore(items)

print(ts.getItem(15))
