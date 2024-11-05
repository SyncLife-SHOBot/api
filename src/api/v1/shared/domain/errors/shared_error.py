class SharedError(Exception):
    def __init__(self, error_message: str):
        super().__init__(f"Error de Shared: {error_message}")
