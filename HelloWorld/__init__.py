import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="HelloWorld", auth_level=func.AuthLevel.FUNCTION)
def hello_world(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Hey Priya! How DevOps is going?",
             status_code=200
        )

def main(req: func.HttpRequest) -> func.HttpResponse:
    return hello_world(req)
