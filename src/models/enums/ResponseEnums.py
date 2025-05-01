from enum import Enum
import pydantic

class ResponseSignal(Enum):
    
    FILE_VALIDATED_SUCESS = "file_validated_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXEEDED = "file_size_exceded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    