responses = {
    'create_response': {
        'token': '01ab69087c923abf08331e7bc42b4af10140f2d3f2e54e53d7ae01aebe6ddc52',
        'url': 'https://webpay3gint.transbank.cl/webpayserver/initTransaction'
    },
    'create_error': {
        'error_message': 'Not Authorized'
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
    'commit_error': {
        'error_message': 'Invalid status 0 for transaction while authorizing. Commerce will be notified by webpay to'
                         ' authorize'
    },
    'general_error': {
        'description': 'Internal server error'
    },
    'expired_token': {
        'error_message': 'The transactions date has passed max time (7 days) to recover the status'
    },
    'invalid_parameter': {
        'error_message': 'Invalid value for parameter: amount'
    },
    'required_parameter': {
        'error_message': 'amount is required!'
    },
    'commit_deferred': {
        'vci': 'TSY',
        'amount': 1209,
        'status': 'AUTHORIZED',
        'buy_order': 'O-74351',
        'session_id': 'S-72021',
        'card_detail': {
         'card_number': '6623'
        },
        'accounting_date': '1004',
        'transaction_date': '2023-10-04T12:48:34.770Z',
        'authorization_code': '123456',
        'payment_type_code': 'VN',
        'response_code': 0,
        'installments_number': 0,
        'capture_expiration_date': '2023-11-03T12:49:26.709Z'
    },
    'increase_amount_response': {
        'authorization_code': '123456',
        'authorization_date': '2023-10-04T12:51:36Z',
        'total_amount': 2209,
        'expiration_date': '2023-11-03T12:49:26.709Z',
        'response_code': 0
    },
    'increase_autho_date_response':
    {
        'authorization_code': '123456',
        'authorization_date': '2023-10-04T12:52:51Z',
        'total_amount': 2209,
        'expiration_date': '2023-11-03T12:52:51.108Z',
        'response_code': 0
    },
    'capture_history_response': [
         {
              'type': 'Preauthorization',
              'amount': 1209,
              'authorization_code': '123456',
              'authorization_date': '2023-10-04T12:49:26.709Z',
              'total_amount': 1209,
              'expiration_date': '2023-11-03T12:49:26.709Z',
              'response_code': 0
         },
         {
              'type': 'Amount adjustment',
              'amount': 1000,
              'authorization_code': '123456',
              'authorization_date': '2023-10-04T12:51:36.577Z',
              'total_amount': 2209,
              'expiration_date': '2023-11-03T12:49:26.709Z',
              'response_code': 0
         },
         {
              'type': 'Expiration date adjustment',
              'amount': 0,
              'authorization_code': '123456',
              'authorization_date': '2023-10-04T12:52:51.108Z',
              'total_amount': 2209,
              'expiration_date': '2023-11-03T12:52:51.108Z',
              'response_code': 0
         }
    ],
    'capture_response': {
        'authorization_code': '123456',
        'authorization_date': '2023-10-04T12:55:49Z',
        'captured_amount': 2209,
        'response_code': 0
    },
    'reverse_preauthorized_amount': {
         'authorization_code': '123456',
         'authorization_date': '2023-10-04T13:01:04Z',
         'total_amount': 1126,
         'expiration_date': '2023-11-03T13:00:44.751Z',
         'response_code': 0
    },
}
