## Argo pipelines

## To run:
To run the pipeline you could use argo commandline tool, e.g.: <br>
`argo submit --watch YAML_FILE --namespace=argo` <br>
make sure that you have the kubectl correctly configured. To export config: <br>
`export KUBECONFIG=PATH_TO_THE_CONFIG_FILE`
## To see logs:
`argo logs -w WORKFLOW_ID --namespace=argo`

## Running argo pipelines using Grace API:
See tutorial:
https://docs.google.com/document/d/13zm4YxcZT4Q1pK1oSGrzJPwQXgy67FHeVUNPsJz_nfc/edit?usp=sharing
