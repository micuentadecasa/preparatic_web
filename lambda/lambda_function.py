def lambda_handler(event, context):
    """
    Lambda function to calculate Fibonacci number for a given input.
    
    Args:
        event: Dictionary containing 'n' key with the input number
        context: AWS Lambda context (not used in this function)
    
    Returns:
        Dictionary with the Fibonacci number or error message
    """
    try:
        n = int(event.get('n', 0))
        if n < 0:
            return {
                'statusCode': 400,
                'body': {'error': 'Input must be non-negative'}
            }
        
        if n == 0:
            return {'statusCode': 200, 'body': 0}
        elif n == 1:
            return {'statusCode': 200, 'body': 1}
        
        # Calculate Fibonacci using iterative approach
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return {'statusCode': 200, 'body': b}
        
    except ValueError:
        return {
            'statusCode': 400,
            'body': {'error': 'Invalid input: must be an integer'}
        }

    # Import necessary modules for AWS Lambda compatibility
    import json
    import logging

    # Set up logging (recommended for AWS Lambda)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
