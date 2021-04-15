# Python-CI-CD-Azure-Pipelines

## Demonstrate Continuous Integration & Continuous Deployment using GitHub and Azure Services

### Repository consists of 3 Projects
1) [x] Project 1 - located in folder **/Hello_Python_App** demonstrates CI using GitHub Actions
2) [ ] Project 2 - located in folder **/Flask_ML_Python_App** demonstrates CI and CD using Azure Pipelines
3) [x] Project 3 - located in folder **/Flask_ML_Pyhton_App-GitHub_Actions** demonstrates CI and CD using GitHub Actions

### Architectural Diagram
[![Architectural Diagram using Visual Studio Code, GitHub and Azure]](./architecture/images/project2_architectural_diagram.jpg)

### Project Plan
[Yearly, Quarterly Project Plan for CI-CD Project](./project_plan/Q1-2021.xlsx)

### Trello Board
[Project's Trello Board](https://trello.com/b/KuYAsEet/project-2)

## Project 1
Demonstrate Continuous Integration with a Python App in folder **/Hello_Python_App**

### Clone the repository using GitBash
[Cloned Respository for /Hello_Python_App](/images/01-git_repository_cloned_in_gitbash_to_local_repository.jpg)

### Execute make all on local computer
[Output for **make all** command on local computer](/images/02-make_all_output.jpg)

### GitHub Action Workflow for Project 1
[Output for **GitHub Action** executes make all on GitHub](/images/03-github_action_build.jpg)

[![Python application CI test with Github actions](https://github.com/npworkcode/Python-CI-CD-Azure-Pipelines/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/npworkcode/Python-CI-CD-Azure-Pipelines/actions/workflows/pythonapp.yml)

## Project 2

### Deploy the Python App to Azure App Service from Powershell
### Project located in folder **/Flask_ML_Python_App**
[Successful Deployment of Python App](/images/05-successful_deployment_of_python_app_to_azure_from_command_line.jpg)

### Unable to perform CI - CD with Azure Pipelines
- Waiting for approval from Microsoft for my Azure DevOps organisation to use Service agent for Azure Pipeline
> - https://devblogs.microsoft.com/devops/change-in-azure-pipelines-grant-for-private-projects/
> - https://devblogs.microsoft.com/devops/change-in-azure-pipelines-grant-for-public-projects/

## Project 3

### Located in folder **/Flask_ML_Python_App-GitHub_Actions

### Successful deploy of Flask ML Python App to Azure App Service
[Successful deployment to Azure](/images/09-succesful_deploy_of_python_app_using_github_actions.jpg)

[Make prediction using Flask ML Python App] (/06-make_prediction_fun_against_azure_website_with_deployed_app.jpg)

## Load Test Deployed App with Locust

### Setup Locust to run load test

### Move to directory with locust files **/locust**
```PowerShell
py -3 -m venv ~/.avenv
source ~/.avenv/scripts/activate
pip install locust
locust -f locusApp.py
```
### Open a Web browser to http://localhost:8089
[Locust start page](/images/08-locust_start_new_load_test.jpg)

1) The number of users to simulate
2) The spawn rate (number of users created per second)
3) Enter the URL of the app https://python04152021-ml-project2.azurewebsites.net

[Locust load testing the python app](/images/07-locust_load_testing_of_app_on_azure_websites.jpg)

[Locust load testing report](./locust/images/report_1618320165.2787147.html)

## Demo
[Youtube link to demo of project]

## Future Enhancements
1) Deploy the app in a Docker Container and Automatically deploy to a Kubernetes Pod
2) Use different programming language to create the app






[![Python application CI test with Github actions](https://github.com/npworkcode/Python-CI-CD-Azure-Pipelines/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/npworkcode/Python-CI-CD-Azure-Pipelines/actions/workflows/pythonapp.yml)
