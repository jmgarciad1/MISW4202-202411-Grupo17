



class RelationalBdResource():
    id: int = 0

    def get_id(self) -> int:
        self.id = self.id+1
        return self.id