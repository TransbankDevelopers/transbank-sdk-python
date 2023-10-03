responses = {
    'create_response': {
        'token': '01ab69087c923abf08331e7bc42b4af10140f2d3f2e54e53d7ae01aebe6ddc52',
        'url': 'https://webpay3gint.transbank.cl/webpayserver/initTransaction'
    },
    'create_error': {
        'error_message': 'Not Authorized',
        'code': 401
    },
    'commit_status_response': {
            'vci': 'TSY',
            'amount': 150000,
            'status': 'AUTHORIZED',
            'buy_order': 'buy_order_mock_123456789',
            'session_id': 'session_ide_mock_123456789',
            'card_detail': {
                'card_number': '6623'
            },
            'accounting_date': '0624',
            'transaction_date': '2020-06-24T12:26:21.463Z',
            'authorization_code': '1213',
            'payment_type_code': 'VN',
            'response_code': 0,
            'installments_number': 0
    },
    'reversed_response': {
        'type': 'REVERSED'
    },
    'nullified_response': {
            'type': 'NULLIFIED',
            'balance': 16886,
            'authorization_code': '594213',
            'response_code': 0,
            'authorization_date': '2023-10-01T04:16:06.565Z',
            'nullified_amount': 300000
    },
    'error_api_mismatch': {
        'error_message': 'Api mismatch error, required version is 1.3'
    },
    'error_commit': {
        'message': 'Invalid status 0 for transaction while authorizing. Commerce will be notified by webpay to'
                   ' authorize',
        'code': 422
    },
    'general_error': {
        'description': 'Internal server error',
        'code': 500
    },
    'expired_token': {
        'error_message': 'The transactions date has passed max time (7 days) to recover the status',
        'code': 422
    },
    'invalid_parameter': {
        'error_message': 'Invalid value for parameter: amount',
        'code': 422
    },
    'required_parameter': {
        'error_message': 'amount is required!',
        'code': 422
    },
}
