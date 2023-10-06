APIM configurations : <br>
1) import swagger from https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#completions for ex, https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2023-03-15-preview/inference.json then. Ref: https://github.com/Azure-Samples/openai-python-enterprise-logging <br>

2) enable subscription and change header as api-key <br>

3) add named values i) backend-url-1 2) backend-url-2 3) OpenAI-KEY 4) TENANT-ID and for 1 & 2 it would be in the form of https://aoaipoclb1.openai.azure.com/openai <br>

4) Custom domain (optional) - for TLS as part of any enterprise implementation standard <br>

On AOAI instances <br>
5) - i) provision them ii) deploy completion/embedding etc. models iii) disable network access and enable private endpoint <br>

6) Provision VNet, subnets (different for PEs, APIM etc.) with configurations as per the ones given in the docs folder <br>

7) Provision PIP

8) (Optional) Create AOAI instance, Vnet, in another region, deployed models, enabled private endpoint and finally peered VNet between regions <br>

Further Reading:

Reference for the above - <br>
https://journeyofthegeek.com/2023/04/02/authentication-in-azure-openai-service/ <br>
https://journeyofthegeek.com/2023/04/27/apim-and-azure-openai-service-azure-ad/ <br>
https://journeyofthegeek.com/2023/05/18/granular-chargebacks-in-azure-openai-service/ <br>
https://journeyofthegeek.com/2023/05/31/load-balancing-in-azure-openai-service/ <br>
https://github.com/anevjes/apimLoadBalancing  <br>
https://journeyofthegeek.com/2023/03/19/infra-security-stuff-in-the-azure-openai-service/  <br>
https://learn.microsoft.com/en-us/azure/api-management/api-management-using-with-vnet?tabs=stv2  <br>
https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-api-inspector  <br>
https://techcommunity.microsoft.com/t5/apps-on-azure-blog/build-an-enterprise-ready-azure-openai-solution-with-azure-api/ba-p/3907562  <br>
https://github.com/Azure-Samples/openai-python-enterprise-logging  <br>
https://github.com/mattfeltonma/azure-openai-apim/tree/main/apim-policies  <br>
https://journeyofthegeek.com/2023/04/06/authorization-in-azure-openai-service/  <br>
https://journeyofthegeek.com/2023/07/01/blocking-api-key-access-in-azure-openai-service/  <br>
https://learn.microsoft.com/en-us/azure/api-management/configure-custom-domain?tabs=custom  <br>

cURL to test end to end out <br>

``curl -d '{"model":"gpt-35-turbo","messages":[{"role":"user","content":"Hello!"}]}' -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X POST <APIM endpoint>/chat/completions?api-version=2023-03-15-preview``
