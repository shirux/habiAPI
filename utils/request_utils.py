import re

class RequestUtils:

    @staticmethod
    def process_params(request, params):
        """Process all query params on request

        Args:
            request (HttpRequest): Request
            params (dict): params to process
        """
        for key in params.items():
            if request.GET.get(key[0]):
                # Normalize params
                value = request.GET[key[0]].strip()
                value = re.sub(" +", " ", value)

                # If key is year, convert to integer
                if key[0] == 'min_year' or key[0] == 'max_year':
                    try:
                        value = int(value)
                    except ValueError:
                        value = 0
                
                # Update value if exists
                params[key[0]] = value