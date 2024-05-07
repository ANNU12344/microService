import json
from google.protobuf.json_format import MessageToDict, Parse

class ApiVerifier:
    def __init__(self):
        pass

    @staticmethod
    def verify_input_format(request_data, expected_fields):
        """
        Verify the input format against expected fields.

        Args:
            request_data (dict): The input data received in the request.
            expected_fields (list): List of expected fields in the input.

        Returns:
            bool: True if the input format is valid, False otherwise.
            str: Error message if the input format is invalid.
        """
        if not all(field in request_data for field in expected_fields):
            error_msg = f"Missing one or more required fields: {expected_fields}"
            return False, error_msg
        return True, None

    @staticmethod
    def verify_output_format(response_data, expected_fields):
        """
        Verify the output format against expected fields.

        Args:
            response_data (dict): The output data to be sent in the response.
            expected_fields (list): List of expected fields in the output.

        Returns:
            bool: True if the output format is valid, False otherwise.
            str: Error message if the output format is invalid.
        """
        if not all(field in response_data for field in expected_fields):
            error_msg = f"Missing one or more required fields: {expected_fields}"
            return False, error_msg
        return True, None

    @staticmethod
    def verify_grpc_request(request, expected_message_type):
        """
        Verify the gRPC request format.

        Args:
            request: gRPC request object.
            expected_message_type: The expected message type for the request.

        Returns:
            bool: True if the request format is valid, False otherwise.
            str: Error message if the request format is invalid.
        """
        try:
            Parse(request, expected_message_type)
            return True, None
        except Exception as e:
            error_msg = f"Error parsing gRPC request: {str(e)}"
            return False, error_msg

    @staticmethod
    def verify_grpc_response(response, expected_message_type):
        """
        Verify the gRPC response format.

        Args:
            response: gRPC response object.
            expected_message_type: The expected message type for the response.

        Returns:
            bool: True if the response format is valid, False otherwise.
            str: Error message if the response format is invalid.
        """
        try:
            MessageToDict(response, including_default_value_fields=True)
            return True, None
        except Exception as e:
            error_msg = f"Error converting gRPC response to dictionary: {str(e)}"
            return False, error_msg
