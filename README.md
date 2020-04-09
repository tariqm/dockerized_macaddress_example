# dockerized_macaddress_example

Makes an API call to https://macaddress.io/ to look up the company name for a MAC Address.

### Note
This is an example/test code for a project. Do NOT use it in production.

## Securing Your API Key
Before you can run this app, you must obtain your own API key from https://macaddress.io/.
Always supply the API key as an argument. If you must run it through some automation, you can store it as a secured variable, e.g. as a SecureString in AWS Systems Manager Parameter Store.

## Installation

This is a dockerized app. Create a docker image by running the following command from the root directory.

```bash
docker build --tag=macaddr .
```

## Usage
Once the Docker image has been created, run the following command.


```bash
docker run macaddr -k='<API_KEY>' -m='<MAC_ADDRESS'
```



## Example
Given the API_KEY of 'ABCDEFGH12345' and MAC Address of '44:38:39:ff:ef:57'
You will run the following Docker command:
```bash
docker run macaddr -k='ABCDEFGH12345' -m='44:38:39:ff:ef:57'
```
The above command will return the following output:
```bash
MAC Address: 44:38:39:ff:ef:57
Company Name: Cumulus Networks, Inc
```
