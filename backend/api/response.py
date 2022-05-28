from backend.api.strings import PROCESS_FAILED


class ApiResponse:

    def __init__(self, action=False, result=None, message=PROCESS_FAILED, status=500) -> None:
        self.action = action
        self.result = result
        self.message = message
        self.status = status

    def to_dict(self):
        return {
            'action': self.action,
            'messsage': self.message,
            'result': self.result,
            'status': self.status
        }