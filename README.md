# debug-functions

A collection of super simple functions that can be used to debug or verify the behaior inside an OpenFaaS cluster.

1. `echovars` - responds with the environment variables that the function is able to see.

    Deploy using

    ```sh
    TEST=foo faas-cli up  --token=$CLOUD_TOKEN -f echovars.yml
    ```
