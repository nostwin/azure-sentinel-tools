import json
import os

TEMPLATE_DIR_PATH: str = 'templates'
MASTER_TEMPLATE_PATH: str = 'test.json'
TEMPLATES_TO_ADD_PATH: list[str] = []
MODE: str = 'create'  # modes: add, create

arm_base_template = {
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "workspaceName": {
            "type": "string",
            "metadata": {
                "description": "Workspace"
            }
        },
        "watchlistdescription": {
            "type": "string",
            "defaultValue": "Watchlist"
        }
    },
    "resources": []
}


def get_template_files(template_dir: str) -> list[str]:
    files = []
    for file in os.listdir(template_dir):
        if file.endswith('.json'):
            files.append(os.path.join(template_dir, file))
    return files


def get_template_resources(template_files: list) -> list[dict]:
    resource_list = []
    for file in template_files:
        with open(file, 'r') as f:
            content = json.loads(f.read())
            resource_list.append(content.get('resources')[0])
    return resource_list


def build_master_template(master_template_path: str) -> str:
    template_file_list = get_template_files(TEMPLATE_DIR_PATH)
    resources = get_template_resources(template_file_list)
    arm_base_template['resources'] = resources
    with open(master_template_path, 'w') as w:
        json.dump(arm_base_template, w, indent=4)
    return 'Ok'


def add_templates_to_master(master_template_path: str, templates_to_add_path: list[str]) -> str:
    if len(templates_to_add_path) <= 0:
        return 'TEMPLATES_TO_ADD_PATH cannot be empty'

    resources = get_template_resources(templates_to_add_path)
    with open(master_template_path, 'r') as file:
        content = json.loads(file.read())
    for resource in resources:
        content.get('resources').append(resource)
    with open(master_template_path, 'w') as file:
        json.dump(content, file, indent=4)
    return 'Ok'


if __name__ == '__main__':
    match MODE:
        case 'create':
            print(build_master_template(MASTER_TEMPLATE_PATH))
        case 'add':
            print(add_templates_to_master(MASTER_TEMPLATE_PATH, TEMPLATES_TO_ADD_PATH))
        case _:
            print('Define one of the following modes: create, add.')
