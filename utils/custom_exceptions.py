class InvalidDobError(Exception):
    """Exception raised for when user enters an invalid date of birth format"""
    def __init__(self,message = "[ERROR]: Invalid date format. Use YYYY-MM-DD"):
        super().__init__(message)










