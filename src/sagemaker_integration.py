import boto3

def carregar_modelo_sagemaker(model_name):
    client = boto3.client('sagemaker-runtime')
    response = client.invoke_endpoint(
        EndpointName=model_name,
        Body='some input data',  # Aqui você passaria os dados do Google Sheets, por exemplo
        ContentType='application/json'
    )
    
    result = response['Body'].read().decode()
    return result
