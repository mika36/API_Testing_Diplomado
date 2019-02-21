import yaml

global info_dict
generic_data = yaml.load(open('config/config.yml'))


def before_all(context):
        context.host=generic_data['api']['host']
        context.method = generic_data['api']['method']
        context.code = generic_data['api']['code']