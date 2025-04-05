import azure.functions as func
import logging
from datetime import datetime
 
 
app = func.FunctionApp()
 
 
@app.function_name(name="HttpTrigger")
@app.route(route="hello", methods=["GET", "POST", "OPTIONS"])
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Handle CORS preflight requests
        if req.method == "OPTIONS":
            headers = {
                "Access-Control-Allow-Origin": "https://portal.azure.com",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",
                "Access-Control-Max-Age": "86400"
            }
            return func.HttpResponse(
                status_code=204,
                headers=headers
            )
 
        logging.info('Python HTTP trigger function processed a request.')
        
        # Log request details
        logging.info(f'Request method: {req.method}')
        logging.info(f'Request URL: {req.url}')
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response_message = f"Hello, Priya! How is it going? Current time: {current_time}"
        
        logging.info(f'Sending response: {response_message}')
        
        # Add CORS headers to the response
        headers = {
            "Access-Control-Allow-Origin": "https://portal.azure.com",
            "Content-Type": "text/plain"
        }
        
        return func.HttpResponse(
            response_message,
            status_code=200,
            headers=headers
        )
    except Exception as e:
        error_message = f"Error in function execution: {str(e)}"
        logging.error(error_message)
        return func.HttpResponse(
            error_message,
            status_code=500,
            mimetype="text/plain"
        )
 