# encoding: utf-8

from sqlalchemy.sql.expression import false, null, true
import ckan.plugins.toolkit as toolkit


class Helper():

    def get_groups_list():
        groups = toolkit.get_action('group_list')({}, {'all_fields':true})
        group_list = []
        temp = {}
        temp['value'] = '0'
        temp['text'] = 'No group'
        group_list.append(temp)
        for group in groups:
            if not Helper.check_access_edit_group(group['id']):
                continue
            temp = {}
            temp['value'] = group['id']
            temp['text'] = group['name']
            group_list.append(temp)
        
        return group_list
    
    def get_organizations_list():
        orgs = toolkit.get_action('organization_list')({}, {'all_fields':true})
        org_list = []
        temp = {}
        temp['value'] = '0'
        temp['text'] = 'No organization'
        org_list.append(temp)
        for org in orgs:
            if not Helper.check_access_add_dataset_to_org(org['id']):
                continue
            temp = {}
            temp['value'] = org['id']
            temp['text'] = org['name']
            org_list.append(temp)
        
        return org_list
    

    def check_plugin_enabled(plugin_name):
        plugins = toolkit.config.get("ckan.plugins")
        if plugin_name in plugins:
            return True
        return False
    

    def check_access_edit_group(group_id):
        context = {'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        data_dict = {'id':group_id}
        try:
            toolkit.check_access('group_update', context, data_dict)
            return True

        except toolkit.NotAuthorized:
            return False


    def check_access_add_dataset_to_org(org_id):
        context = {'user': toolkit.g.user, 'auth_user_obj': toolkit.g.userobj}
        data_dict = {'id':org_id}
        try:
            toolkit.check_access('organization_update', context, data_dict)
            return True

        except toolkit.NotAuthorized:
            return False



