class TagError(Exception):
    def __init__(self, error_message: str):
        super().__init__(f"Error de Tags: {error_message}")
