import ckan.plugins as p
from ckan.plugins.toolkit import add_template_directory

from ckanext.repeating import validators



class MDfromowlPlugin(p.SingletonPlugin):
    p.implements(p.IValidators)
    p.implements(p.IConfigurer)

    def get_helpers(self):
    	data=[]
	data.append({'aa':'11'})
	data.append({'bb':'22'})
	return { 'dataowl': data,}

    def update_config(self, config):
        """
        templates
        """
        add_template_directory(config, 'templates')

    def get_validators(self):
        return {
            'repeating_text': validators.repeating_text,
            'repeating_text_output':
                validators.repeating_text_output,
            }



