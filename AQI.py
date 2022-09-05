import requests
r = requests.get(
    'https://data.epa.gov.tw/api/v1/aqx_p_488?format=json&offset=0&limit=5&api_key=bade005d-8815-4448-946a-c3346ca316da')
print(r.text)
