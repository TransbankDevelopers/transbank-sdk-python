from transbank.common.api_constants import ApiConstants
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.common.validation_util import ValidationUtil
from transbank.common.api_constants import ApiConstants
from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.error.transbank_error import TransbankError
from transbank.error.mall_bin_info_query_error import MallBinInfoQueryError
from transbank.webpay.oneclick.request import MallBinInfoQueryRequest
from transbank.webpay.oneclick.schema import MallBinInfoQueryRequestSchema

class MallBinInfo(WebpayTransaction):
    INFO_ENDPOINT = ApiConstants.ONECLICK_ENDPOINT + '/bin_info'

    def __init__(self, options: WebpayOptions):
        super().__init__(options)
    
    def query_bin(self, tbk_user: str):
        """
        Queries the BIN information for a given `tbk_user`.

        Args:
            tbk_user (str): The `tbk_user` for which to query the BIN information.
        Returns:
            dict: The BIN information for the specified `tbk_user`.
        Raises:
            MallBinInfoQueryError: If there is an error querying the BIN information.
            TransbankError: If `tbk_user` exceeds the max length
        """
        ValidationUtil.has_text_with_max_length(tbk_user, ApiConstants.TBK_USER_LENGTH, "tbk_user")
        try:
            endpoint = MallBinInfo.INFO_ENDPOINT
            request = MallBinInfoQueryRequest(tbk_user)
            return RequestService.post(endpoint, MallBinInfoQueryRequestSchema().dumps(request), self.options)
        except TransbankError as e:
            raise MallBinInfoQueryError(e.message, e.code)
