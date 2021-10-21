import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint
from ckanext.organization_group.controllers import GroupOwnershipController



class OrganizationGroupPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public/statics')
        toolkit.add_resource('public/statics', 'ckanext-organization-group')

    def get_blueprint(self):

        blueprint = Blueprint(self.name, self.__module__)        
        blueprint.add_url_rule(
            u'/upgrade_dataset/add_ownership_view/<id>',
            u'add_ownership_view',
            GroupOwnershipController.add_ownership_view,
            methods=['GET']
            )
        
        blueprint.add_url_rule(
            u'/upgrade_dataset/save_ownership',
            u'save_ownership',
            GroupOwnershipController.save_ownership,
            methods=['POST']
            )

        return blueprint
    
    #ITemplateHelpers

    def get_helpers(self):
        return {'cancel_dataset_is_enabled': GroupOwnershipController.cancel_dataset_plugin_is_enabled,
            'mediawiki_is_enabled': GroupOwnershipController.mediawiki_plugin_is_enabled,
            'get_user_org': GroupOwnershipController.get_user_org,
            'get_user_group': GroupOwnershipController.get_user_group
        }